import requests
import streamlit as st


def ocr_image_to_text(image_path):
    API_KEY = st.secrets["OCR_API_KEY"]  # Make sure this exists in your .streamlit/secrets.toml

    with open(image_path, 'rb') as image_file:
        response = requests.post(
            'https://api.ocr.space/parse/image',
            files={'filename': image_file},
            data={
                'apikey': API_KEY,
                'language': 'eng',
                'isOverlayRequired': False,
            },
        )

    result = response.json()

    if result.get("IsErroredOnProcessing"):
        st.error("OCR failed. Reason: " + result.get("ErrorMessage", ["Unknown error"])[0])
        return "OCR failed"

    parsed_results = result.get("ParsedResults")
    if not parsed_results:
        st.error("No parsed text found in OCR result.")
        return "OCR failed"

    return parsed_results[0].get("ParsedText", "OCR found no text.")
