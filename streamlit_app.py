import ollama
import streamlit as st

st.title("Local Chatbot (Llama3)")

# Initialize chat history
if "messages" not in st.session_state:
    st.session_state.messages = []

# Display chat history
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# User input
prompt = st.chat_input("Ask something...")

if prompt:
    # Show user message
    with st.chat_message("user"):
        st.markdown(prompt)

    st.session_state.messages.append({"role": "user", "content": prompt})

    # Generate response using OLLAMA (LOCAL)
    with st.chat_message("assistant"):
        message_placeholder = st.empty()
        full_response = ""

        stream = ollama.chat(
            model="llama3",
            messages=st.session_state.messages,
            stream=True
        )

        for chunk in stream:
            full_response += chunk["message"]["content"]
            message_placeholder.markdown(full_response + "▌")

        message_placeholder.markdown(full_response)

    st.session_state.messages.append({"role": "assistant", "content": full_response})