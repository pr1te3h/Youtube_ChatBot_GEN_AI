# 📺 YouTube RAG Chatbot

A Python-based Generative AI application that allows users to **interact with YouTube videos through natural language**. The application retrieves the video's transcript, divides it into smaller sections, creates vector embeddings, and uses Retrieval-Augmented Generation (RAG) to provide answers based on the video content.

---

## 🗂️ Table of Contents

* [📺 YouTube RAG Chatbot](#-youtube-rag-chatbot)
* [🎯 Project Overview](#-project-overview)
* [🔧 Technologies Used](#-technologies-used)
* [🚀 Key Features](#-key-features)
* [🔄 How It Works](#-how-it-works)
* [💻 Setup](#-setup)
* [▶️ Running the Application](#️-running-the-application)
* [🖼️ Screenshots](#️-screenshots)
* [🛣️ Future Improvements](#️-future-improvements)
* [📜 License](#-license)

---

## 🎯 Project Overview

Finding a specific piece of information inside a long YouTube video can be time-consuming. This project provides a conversational interface that allows users to interact directly with the video's content.

The application follows these steps:

* Retrieves the transcript from a YouTube video
* Splits the transcript into smaller, meaningful chunks
* Converts the chunks into vector embeddings
* Stores the embeddings in a vector database
* Searches for relevant content based on the user's question
* Passes the retrieved context to an LLM to generate a response

This approach combines **semantic search and Generative AI** to make long-form video content easier to explore.

---

## 🔧 Technologies Used

| Category                  | Technology                                 |
| ------------------------- | ------------------------------------------ |
| **Programming Language**  | Python                                     |
| **Transcript Extraction** | `youtube-transcript-api`                   |
| **AI Framework**          | LangChain                                  |
| **Embeddings**            | ChatGroq / OpenAI / HuggingFace Embeddings |
| **Vector Database**       | FAISS / Chroma                             |
| **LLM Provider**          | OpenAI GPT / Groq / Local LLM              |
| **User Interface**        | Streamlit                                  |
| **Environment Variables** | `python-dotenv`                            |

> **Note:** Update the table according to the exact libraries and models used in your implementation.

---

## 🚀 Key Features

* 🔗 Accept a YouTube video URL or ID
* 📄 Automatically retrieve the available transcript
* ✂️ Split transcripts into smaller text chunks
* 🧠 Generate embeddings for semantic search
* 🔍 Retrieve relevant content using similarity search
* 💬 Ask natural-language questions about the video
* 🎯 Generate responses using retrieved video context
* ⚡ Interactive Streamlit-based interface

---

## 🔄 How It Works

The application follows a Retrieval-Augmented Generation pipeline:

```text
YouTube Video
      ↓
Transcript Extraction
      ↓
Text Processing & Chunking
      ↓
Embedding Generation
      ↓
Vector Database
      ↓
User Query
      ↓
Similarity Search
      ↓
Relevant Context
      ↓
Large Language Model
      ↓
Final Response
```

The transcript is first converted into searchable vector representations. When a user asks a question, the system retrieves the most relevant sections of the transcript and provides them as context to the language model.

---

## 💻 Setup

### 1. Clone the Repository

```bash
git clone https://github.com/Aman-coder2004/RAG_Based_Youtube_ChatBot_Python_Gen_AI
cd Rag_Based_Youtube_Chatbot
```

### 2. Create a Virtual Environment

#### Windows

```bash
python -m venv venv
venv\Scripts\activate
```

#### Linux / macOS

```bash
python -m venv venv
source venv/bin/activate
```

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

### 4. Configure API Keys

Create a `.env` file in the root directory and add the API key required by your implementation.

Example:

```env
OPENAI_API_KEY=your_api_key_here
```

> 🔐 Never commit your `.env` file or expose your API keys on GitHub.

---

## ▶️ Running the Application

Launch the Streamlit application using:

```bash
streamlit run app.py
```

### Usage

1. Enter a YouTube video URL or ID.
2. Wait for the transcript to be processed.
3. The transcript is split and converted into embeddings.
4. Ask a question about the video.
5. The system retrieves relevant transcript sections.
6. The LLM generates an answer using the retrieved context.

---

## 🖼️ Screenshots

Add your application screenshots below:

| Application Interface       | Chat Interface       |
| --------------------------- | -------------------- |
| ![Application](photo_1.png) | ![Chat](photo_2.png) |

---

## 🛣️ Future Improvements

* [ ] 📚 Support multiple videos and playlists
* [ ] 🎙️ Add voice input and voice responses
* [ ] 📝 Use Whisper for videos without available captions
* [ ] 🌐 Add multilingual transcript and query support
* [ ] 💾 Implement persistent chat history
* [ ] ☁️ Deploy the application using Streamlit Cloud or Hugging Face Spaces
* [ ] ⏱️ Add timestamps linking answers to relevant parts of the video
* [ ] 📊 Improve retrieval using advanced RAG techniques


⭐ If you find this project useful, consider giving the repository a star!
