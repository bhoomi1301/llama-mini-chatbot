import streamlit as st
from gtts import gTTS
import tempfile
from chatbot import chat_with_llama

# --- Direct Chat Page (Login removed) ---

st.title("💬 LLaMA Conversational Chatbot (Groq API)")
st.write("Chat with me! I remember our conversation.")

# Initialize chat history with system prompt if not already
if "chat_history" not in st.session_state:
    st.session_state.chat_history = [
        {"role": "system", "content": "You are a helpful, conversational assistant."}
    ]

# Add "Clear Chat" Button
if st.button("Clear Chat"):
    st.session_state.chat_history = [
        {"role": "system", "content": "You are a helpful, conversational assistant."}
    ]
    st.success("Chat has been cleared!")

# Use a form to clear input after submission automatically
with st.form(key="chat_form", clear_on_submit=True):
    user_input = st.text_input("You:", key="user_input")
    submit_button = st.form_submit_button("Send")

    if submit_button:
        if user_input.strip() != "":
            with st.spinner("LLaMA is typing..."):
                # Add user message to chat history
                st.session_state.chat_history.append({"role": "user", "content": user_input})

                # Get response from LLaMA
                bot_reply = chat_with_llama(st.session_state.chat_history)

                # Add bot response to chat history
                st.session_state.chat_history.append({"role": "assistant", "content": bot_reply})

                # Text-to-speech output for the bot's response
                tts = gTTS(bot_reply)
                with tempfile.NamedTemporaryFile(delete=False) as fp:
                    tts.save(fp.name)
                    st.audio(fp.name)

# Show conversation history (skip system prompt)
for message in reversed(st.session_state.chat_history[1:]):
    sender = "You" if message["role"] == "user" else "LLaMA"
    if message["role"] == "user":
        st.markdown(
            f"<div style='background-color:#D4EDDA;padding:10px;border-radius:10px;margin:5px;max-width:70%;color:#155724;'>"
            f"{sender}: {message['content']}</div>", unsafe_allow_html=True)
    else:
        st.markdown(
            f"<div style='background-color:#F8D7DA;padding:10px;border-radius:10px;margin:5px;max-width:70%;color:#721C24;'>"
            f"{sender}: {message['content']}</div>", unsafe_allow_html=True)
