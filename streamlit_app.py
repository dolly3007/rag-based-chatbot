import streamlit as st
import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '')))
from multimodal_input.image_to_text import ocr_image_to_text
from llm_response.generate_response import generate_answer

st.title("EdTech Multimodal Tutor")
image = st.file_uploader("Upload a physics question", type=["jpg", "jpeg", "png"])

if image:
    with open("temp_image.png", "wb") as f:
        f.write(image.read())
    question = ocr_image_to_text("temp_image.png")
    st.subheader("Recognized Text")
    st.write(question)
    st.subheader("Answer")
    answer = generate_answer(question)
    st.write(answer)

st.subheader("Or type your question:")
typed_question = st.text_input("Your question")

if typed_question:
    st.subheader("Answer")
    answer = generate_answer(typed_question)
    st.write(answer)