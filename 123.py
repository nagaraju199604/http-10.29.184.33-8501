#!/usr/bin/env python
# coding: utf-8

# In[1]:





# In[2]:


import streamlit as st
from PyPDF2 import PdfReader


OPENAI_API_KEY ="sk-proj-aHhz1tv0D9lU1EZpWMxlT3BlbkFJfi8i4BQnrE1GXo3NK0oI"

# In[3]:





# In[4]:


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
        st.write(text)



   
    
        

