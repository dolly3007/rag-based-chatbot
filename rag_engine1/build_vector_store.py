from langchain_community.vectorstores import FAISS
from langchain_community.embeddings import HuggingFaceEmbeddings
from langchain_community.document_loaders import PyPDFLoader
import streamlit as st
api_key = st.secrets["GROQ_API_KEY"]

def build_vector_db(pdf_path):
    print("Loading PDF...")
    loader = PyPDFLoader(pdf_path)
    docs = loader.load_and_split()

    print("Creating vector store...")
    embeddings = HuggingFaceEmbeddings(model_name="sentence-transformers/all-MiniLM-L6-v2")
    db = FAISS.from_documents(docs, embeddings)
    db.save_local("faiss_index")


if __name__ == "__main__":
    build_vector_db("knowledge_base/textbook_chapters.pdf")

