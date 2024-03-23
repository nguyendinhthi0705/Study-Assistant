import streamlit as st 
import Libs as glib 
import json

st.set_page_config(page_title="Home")


st.markdown("Ask me anything as below samples:") 
st.markdown("Top 10 interview questions for OOP in Java") 
st.markdown("Write a recursive function.") 
st.markdown("Phân biệt giữa classifcation and object detection trong computer vision.") 
st.markdown("Thuật toán nào được dùng để xây dựng hệ thống recommendation.") 

input_text = st.text_input("Input your question") 
if input_text: 
    with st.chat_message("user"): 
        st.markdown(input_text) 
    response = glib.call_claude_sonet_stream(input_text)
    st.write_stream(response)

    



    
   