import streamlit as st 
import Libs as glib 

st.set_page_config(page_title="Improve writing an essay")


input_text = st.text_area("Input your whole or apart of your essay") 
if input_text: 
    response = glib.suggest_writing_document(input_text) 
    st.write_stream(response)
    
