import streamlit as st
from components.render import render_user_message, render_assistant_message
from components.styles import load_chat_styles
from models.chat_settings import ChatSettings
from services.backend_client import BackendClient
from components.chat_settings_panel import render_chat_settings_panel

PAGE_KEY = "chat"
PAGE_NAME = "Aktueller Chat"
PAGE_PATH = "/views/chat.py"
PAGE_ICON = "💬"

# Hauptfunktion, die die Seite rendert
def render_chat():

    load_chat_styles()
    init_session_state()

    # Legt einen Container fest, der Chat-Header, Chat-Verlauf und Chat_Input enthält
    with st.container(key="chat_page_container"):
        render_chat_header()

        with st.container(key="chat_conversation_container"):
            render_conversation()
    
        with st.container(key="chat_input_container"):
            handle_user_input()
        

# Initialisiert den Session State für die aktuelle Konversation (nicht persistente Speicherung im frontend)
def init_session_state():

    if "messages" not in st.session_state:
        st.session_state.messages = []
    
    if "chat_settings" not in st.session_state:
        st.session_state.chat_settings = ChatSettings()
    

# Rendert den Chat-Header mit dem Titel und einem Button, der die Chat-Einstellungen öffnet
def render_chat_header():

    header = st.container(key="chat_header_container")

    with header:
        title_col, button_col = st.columns([8, 1])

        with title_col:
            st.subheader("Aktueller Chat")

        with button_col:
            with st.popover("⚙️"):
                render_chat_settings_panel()




# Rendert die aktuelle Konversation, indem sie durch die gespeicherten Nachrichten im Session State iteriert und sie entsprechend darstellt
def render_conversation():

    for message in st.session_state.messages:
            
            if message["role"] == "user":
                render_user_message(message["content"])

            elif message["role"] == "assistant":
                render_assistant_message(message["content"])

                if "chunks" in message:

                    for chunk in message["chunks"]:

                        render_assistant_message(
                            f"""
                📄 {chunk['file_name']}

                👤 {chunk['author']}

                ⭐ Confidence Score: {chunk['confidence_score']}

                {chunk['content']}
                """
                            )


# Handhabt die Benutzereingabe, indem sie die Nachricht des Benutzers zum Session State hinzufügt, eine KI-Antwort generiert 
# (hier als Platzhalter) und diese ebenfalls zum Session State hinzufügt, bevor die Seite neu geladen wird, um die aktualisierte Konversation anzuzeigen
def handle_user_input():

    user_input = st.chat_input("Type your message here...")

    if user_input:

        #User-Nachricht zum Session State hinzufügen
        st.session_state.messages.append({
            "role": "user",
            "content": user_input
        })

        # Anfrage an FastAPI senden
        backend_client = BackendClient()
        response = backend_client.send_chat_message(
            user_input,
            st.session_state.chat_settings
        )

        ai_response = response.get("response")
        chunks = response.get("chunks", [])

        st.session_state.messages.append({
            "role": "assistant",
            "content": ai_response,
            "chunks": chunks
        })

        st.rerun()
