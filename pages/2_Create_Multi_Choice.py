import streamlit as st 
import Libs as glib 
from PyPDF2 import PdfReader
import Libs as glib 

st.set_page_config(page_title="Create question for a Lecture/Paper")

st.markdown("Upload your lecture to create multiple choice questions!") 
uploaded_file = st.file_uploader("Upload Lecture/Paper in PDF")
docs = []

if uploaded_file is not None:
    reader = PdfReader(uploaded_file)
    for page in reader.pages:
        docs.append(page.extract_text())

    response = glib.create_questions(docs)
    st.write_stream(response)
   