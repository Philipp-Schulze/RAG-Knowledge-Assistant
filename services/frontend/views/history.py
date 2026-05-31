import streamlit as st

PAGE_KEY = "history"
PAGE_NAME = "Chat History"
PAGE_PATH = "/views/chat_history.py"
PAGE_ICON = "⏳"

def render_history():
    st.title("Chat History")
    st.write("This is where the chat history will be displayed.")