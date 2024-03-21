import streamlit as st 
import Libs as glib 
import json

st.set_page_config(page_title="Home")

if 'chat_history' not in st.session_state: 
    st.session_state.chat_history = [] 

for message in st.session_state.chat_history: 
    with st.chat_message(message["role"]): 
        st.markdown(message["text"]) 

st.markdown("Ask me anything as below samples:") 
st.markdown("Top 10 questions for SQL.") 
st.markdown("Write a recursive function.") 

input_text = st.text_input("Input your question") 
if input_text: 
    with st.chat_message("user"): 
        st.markdown(input_text) 
    st.session_state.chat_history.append({"role":"user", "text":input_text}) 
    response = glib.call_claude_sonet_stream(input_text)
    st.write_stream(response)

    



    
   