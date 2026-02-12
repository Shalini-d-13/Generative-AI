import os
from groq import Groq
import streamlit as st
client= Groq()
st.title("LLM Chatbot")
if "messages" not in st.session.state:
    st.session.state.messages=[]
    user_input= st.chat_input("Ask me anything!")
if user_input:
    st.session_state.messages.append({"role":"user","content":user_input})
    response= client.chat(st.session_state.messages)
    reply=response.choices[0].message.content
    st.session_state.messages.append({"role":"assistant","content":reply})
for message in st.session_state.messages:
    st.chat_message(message["role"]).write(message["content"])
