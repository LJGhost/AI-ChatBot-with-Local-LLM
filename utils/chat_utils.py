from transformers import pipeline
from langchain.llms import HuggingFacePipeline
from langchain.chains import RetrievalQA
from langchain_community.embeddings import HuggingFaceEmbeddings
from langchain.vectorstores import FAISS

import torch

def load_local_model():
    qa_pipeline = pipeline(
        "text2text-generation",
        model="google/flan-t5-base",
        device=0 if torch.cuda.is_available() else -1,
        max_length=512
    )

    return HuggingFacePipeline(pipeline=qa_pipeline)

def load_embeddings():
    return HuggingFaceEmbeddings(model_name="all-MiniLM-L6-v2")

def prepare_qa_chain(text):
    llm = load_local_model()
    embeddings = load_embeddings()

    texts = text.split("\n")
    retriever = FAISS.from_texts(texts, embedding=embeddings).as_retriever()

    return RetrievalQA.from_chain_type(llm=llm, retriever=retriever)
