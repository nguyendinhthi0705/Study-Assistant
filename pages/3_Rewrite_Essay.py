import streamlit as st 
import Libs as glib 

st.set_page_config(page_title="Rewrite a Essay")


input_text = st.text_area("Input your whole or apart of your essay") 
if input_text: 
    response = glib.rewrite_document(input_text) 
    st.write_stream(response)
    
