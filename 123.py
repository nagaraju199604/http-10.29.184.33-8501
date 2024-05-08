


import streamlit as st
from PyPDF2 import PdfReader
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain.embeddings.openai import OpenAIEmbeddings
from langchain.vectorstores import FAISS
OPENAI_API_KEY ="sk-proj-aHhz1tv0D9lU1EZpWMxlT3BlbkFJfi8i4BQnrE1GXo3NK0oI"


st.header("My first Chatbot")

with  st.sidebar:
    st.title("Your Documents")
    file = st.file_uploader(" Upload a PDf file and start asking questions", type="pdf")


#Extract the text
if file is not None:
    pdf_reader = PdfReader(file)
    text = ""
    for page in pdf_reader.pages:
        text += page.extract_text()
        #print(st.write(text))
    text_splitter = RecursiveCharacterTextSplitter(
        separators="\n",
        chunk_size=1000,
        chunk_overlap=150,
        length_function=len
    )
    chunks=text_splitter.split_text(text)
    #print(st.write(chunks))
    embeddings = OpenAIEmbeddings(openai_api_key=OPENAI_API_KEY)
    #vector_store = FAISS.from_texts(chunks, embeddings)
    user_question = st.text_input("Type Your question here")

