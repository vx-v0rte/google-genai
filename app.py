import streamlit as st
from google import genai

# Configure your API key (replace with yours or use env var)
API_KEY = "AIzaSyB2HGvZ0r7LC_5VheTq3nnXrIT7fwYNV58"
client = genai.Client(api_key=API_KEY)

MODEL_NAME = "gemini-2.0-flash-001"

# Session state to keep chat
if "chat" not in st.session_state:
    st.session_state.chat = client.chats.create(model=MODEL_NAME)
    st.session_state.history = []

st.set_page_config(page_title="Gemini Chatbot", page_icon="🤖")

st.title("🤖 Gemini Chatbot")
st.write("Chat with your Gemini-powered assistant!")

# Show history
for role, msg in st.session_state.history:
    if role == "user":
        st.chat_message("user").markdown(msg)
    else:
        st.chat_message("assistant").markdown(msg)

# User input box
if prompt := st.chat_input("Type your message..."):
    st.session_state.history.append(("user", prompt))
    st.chat_message("user").markdown(prompt)

    response = st.session_state.chat.send_message(prompt)
    reply = response.text

    st.session_state.history.append(("assistant", reply))
    st.chat_message("assistant").markdown(reply)


