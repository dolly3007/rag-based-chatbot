import streamlit as st
api_key = st.secrets["GROQ_API_KEY"]
from langchain_community.vectorstores import FAISS
from langchain_community.embeddings import HuggingFaceEmbeddings
from langchain_groq import ChatGroq
from langchain.chains import RetrievalQA

embedding = HuggingFaceEmbeddings(model_name="sentence-transformers/all-MiniLM-L6-v2")

def run_rag_with_groq(question: str) -> str:
    db = FAISS.load_local("faiss_index", embedding, allow_dangerous_deserialization=True)
    retriever = db.as_retriever()

    groq_client = ChatGroq(api_key=st.secrets["GROQ_API_KEY"], model="llama3-70b-8192")
    qa_chain = RetrievalQA.from_chain_type(llm=groq_client, retriever=retriever)

    return qa_chain.run(question)