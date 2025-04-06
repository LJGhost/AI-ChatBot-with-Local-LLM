import streamlit as st
from utils.pdf_utils import extract_text_from_pdf
from utils.chat_utils import prepare_qa_chain

st.set_page_config(page_title="📄 PDF Chatbot", layout="wide")

st.title("🤖 PDF Q&A Chatbot")

uploaded_file = st.file_uploader("📎 Upload a PDF file", type="pdf")

if uploaded_file:
    st.write("📄 Extracting text from PDF...")
    text = extract_text_from_pdf(uploaded_file)

    st.write("🧠 Preparing QA model...")
    qa_chain = prepare_qa_chain(text)

    question = st.text_input("❓ Ask a question based on the PDF")
    if question:
        with st.spinner("💬 Thinking..."):
            answer = qa_chain.run(question)
            st.success(f"📝 Answer: {answer}")
