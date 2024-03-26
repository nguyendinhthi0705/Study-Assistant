import streamlit as st 
import Libs as glib 

st.set_page_config(page_title="Search Knowledge base")
st.markdown("Một số bệnh phổ biến của trẻ em là gì?") 
st.markdown("Tóm tắt  tài chính apple?") 
input_text = st.text_input("Search Knowledge base") 
if input_text: 
    response = glib.search(input_text) 
    st.write(response["result"])
    st.write(response)
    
