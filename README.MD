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
* ⚡ I
