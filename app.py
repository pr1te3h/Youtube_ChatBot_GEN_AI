import os
import re

import streamlit as st
from dotenv import load_dotenv

from youtube_transcript_api import YouTubeTranscriptApi
from youtube_transcript_api._errors import TranscriptsDisabled, NoTranscriptFound
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_community.vectorstores import FAISS
from langchain_huggingface import HuggingFaceEmbeddings
from langchain_core.prompts import PromptTemplate
from langchain_groq import ChatGroq

load_dotenv()

st.set_page_config(page_title="YouTube RAG Chatbot", page_icon="🎬", layout="wide")

# ----------------------------------------------------------------------------
# Same pipeline as the notebook, just organized into functions.
# ----------------------------------------------------------------------------

PROMPT = PromptTemplate(
    template="""you are a helpfull assistant please answer my question according to the context provided
             from the given transcript.
             if context is not sufficient just say you don't know
             {context}
             Question:{question}
             """,
    input_variables=["context", "question"],
)


def extract_video_id(url_or_id: str) -> str:
    """Accepts a raw video ID or a full YouTube URL and returns the video ID."""
    patterns = [
        r"(?:v=|/)([0-9A-Za-z_-]{11}).*",
        r"youtu\.be/([0-9A-Za-z_-]{11})",
    ]
    for p in patterns:
        m = re.search(p, url_or_id)
        if m:
            return m.group(1)
    return url_or_id.strip()  # assume it's already a plain video ID


@st.cache_resource(show_spinner=False)
def get_embeddings():
    # same model as the notebook
    return HuggingFaceEmbeddings(model_name="sentence-transformers/all-MiniLM-L6-v2")


def fetch_transcript(video_id: str, languages: list[str]) -> str:
    api = YouTubeTranscriptApi()
    fetched = api.fetch(video_id, languages=languages)
    return " ".join([item.text for item in fetched])


def build_vector_store(transcript: str):
    # same chunk_size / chunk_overlap as the notebook
    splitter = RecursiveCharacterTextSplitter(chunk_size=1000, chunk_overlap=150)
    chunks = splitter.create_documents([transcript])
    embeddings = get_embeddings()
    vector_store = FAISS.from_documents(chunks, embeddings)
    return vector_store, len(chunks)


def answer_question(retriever, llm, question: str) -> str:
    docs = retriever.invoke(question)
    context = "\n\n".join(doc.page_content for doc in docs)
    final_prompt = PROMPT.invoke({"context": context, "question": question})
    result = llm.invoke(final_prompt)
    return result.content


# ----------------------------------------------------------------------------
# Session state
# ----------------------------------------------------------------------------
for key, default in {
    "vector_store": None,
    "video_id": None,
    "messages": [],
    "chunk_count": 0,
}.items():
    st.session_state.setdefault(key, default)

# ----------------------------------------------------------------------------
# Sidebar — setup
# ----------------------------------------------------------------------------
with st.sidebar:
    st.title("🎬 YouTube RAG Chatbot")
    st.caption("Ask questions about any YouTube video's transcript.")

    groq_api_key = st.text_input(
        "Groq API Key",
        value=os.getenv("GROQ_API_KEY", ""),
        type="password",
        help="Get one at https://console.groq.com/keys",
    )

    video_input = st.text_input("YouTube video URL or ID", placeholder="e.g. ZAqIoDhornk or full URL")
    languages_input = st.text_input("Preferred language codes (comma-separated)", value="en")

    load_clicked = st.button("Load video", type="primary", use_container_width=True)

    if load_clicked:
        if not groq_api_key:
            st.error("Please enter your Groq API key.")
        elif not video_input:
            st.error("Please enter a video URL or ID.")
        else:
            vid = extract_video_id(video_input)
            langs = [l.strip() for l in languages_input.split(",") if l.strip()]
            transcript = None
            with st.spinner("Fetching transcript..."):
                try:
                    transcript = fetch_transcript(vid, langs)
                except TranscriptsDisabled:
                    st.error("Transcripts are disabled for this video.")
                except NoTranscriptFound:
                    st.error(f"No transcript found in language(s): {langs}")
                except Exception as e:
                    st.error(f"Could not fetch transcript: {e}")

            if transcript:
                with st.spinner("Building vector store..."):
                    vector_store, chunk_count = build_vector_store(transcript)
                st.session_state.vector_store = vector_store
                st.session_state.video_id = vid
                st.session_state.chunk_count = chunk_count
                st.session_state.messages = []
                st.success(f"Loaded! Transcript split into {chunk_count} chunks.")

    if st.session_state.video_id:
        st.divider()
        st.caption(f"Loaded video: `{st.session_state.video_id}` "
                   f"({st.session_state.chunk_count} chunks)")
        if st.button("Clear / load a different video", use_container_width=True):
            st.session_state.vector_store = None
            st.session_state.video_id = None
            st.session_state.messages = []
            st.rerun()

# ----------------------------------------------------------------------------
# Main area — video + chat
# ----------------------------------------------------------------------------
if st.session_state.video_id:
    col1, col2 = st.columns([1, 1.4])

    with col1:
        st.video(f"https://www.youtube.com/watch?v={st.session_state.video_id}")

    with col2:
        st.subheader("Chat with the video")

        for msg in st.session_state.messages:
            with st.chat_message(msg["role"]):
                st.markdown(msg["content"])

        question = st.chat_input("Ask something about the video...")
        if question:
            st.session_state.messages.append({"role": "user", "content": question})
            with st.chat_message("user"):
                st.markdown(question)

            if not groq_api_key:
                answer = "Please enter your Groq API key in the sidebar first."
            else:
                retriever = st.session_state.vector_store.as_retriever(
                    search_type="similarity", search_kwargs={"k": 4}
                )
                llm = ChatGroq(
                    model="openai/gpt-oss-20b",  # same model as the notebook
                    temperature=0,
                    api_key=groq_api_key,
                )
                with st.spinner("Thinking..."):
                    try:
                        answer = answer_question(retriever, llm, question)
                    except Exception as e:
                        answer = f"Error while generating answer: {e}"

            st.session_state.messages.append({"role": "assistant", "content": answer})
            with st.chat_message("assistant"):
                st.markdown(answer)
else:
    st.title("🎬 YouTube RAG Chatbot")
    st.write(
        "Enter your Groq API key and a YouTube video URL or ID in the sidebar, "
        "then click **Load video** to build a transcript-based knowledge base "
        "you can chat with."
    )
