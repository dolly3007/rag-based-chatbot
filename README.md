# EdTech Multimodal Tutor Chatbot

This project is a multimodal Retrieval-Augmented Generation (RAG) chatbot designed for the **EdTech domain**, specifically for solving **physics questions**. It supports both **text** and **image-based inputs** using OCR and responds using a physics textbook as its knowledge base.

Hosted on **Streamlit Cloud**

---

## 🚀 Features

- **RAG-based Question Answering** using a physics textbook
- **OCR-powered Image Input** (JPG, PNG) using Tesseract
- **Natural Language Understanding** with Groq’s LLM
- **Optional Tool Calling Support**
- **Generative UI** built with Streamlit
- **Deployed on Streamlit Cloud**

---

## Project Structure

rag-based-chatbot/
├── llm_response/
│ └── generate_response.py # Runs RAG using vector DB + Groq
├── rag_engine1/
│ ├── build_vector_store.py # Builds FAISS vector DB from textbook
│ └── query_rag_with_groq.py # Embedding + Groq integration
├── multimodal_input/
│ └── image_to_text.py # OCR using pytesseract or OCR API
├── faiss_index/ # Vector DB stored locally
├── streamlit_app.py # Main Streamlit frontend
├── requirements.txt
└── README.md

---

## Setup Instructions

1. **Clone the repository**
   ```bash
   git clone https://github.com/your-username/rag-based-chatbot.git
   cd rag-based-chatbot
   
2. **Create and activate virtual environment**
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate

3. **Install dependencies**
   pip install -r requirements.txt

4. **Add your secrets**
   On Streamlit Cloud, go to App Settings → Secrets, and add:
   GROQ_API_KEY = "your_groq_api_key"
   OCR_API_KEY = "your_ocr_api_key"  # Optional if using online OCR

## Demonstration Guide

1. **Upload a physics question as text or image**
2. The chatbot processes the input using OCR (if image)
3. A relevant context is retrieved from the vector store
4. Groq LLM generates a physics-grounded answer
5. The response is shown on the screen!







