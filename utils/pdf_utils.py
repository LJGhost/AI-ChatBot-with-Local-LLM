import fitz  # PyMuPDF
import streamlit as st

def extract_text_from_pdf(pdf_file):
    doc = fitz.open(stream=pdf_file.read(), filetype="pdf")
    text = ""
    for page_num in range(len(doc)):
        page_text = doc[page_num].get_text()
        st.write(f"✅ Page {page_num + 1} extracted: {len(page_text)} characters")
        text += page_text
    return text
