import streamlit as st
from chatbot import get_response

# Page configuration
st.set_page_config(
    page_title="Multilingual Chatbot",
    page_icon="🤖"
)

st.title("🤖 Multilingual Chatbot")
st.write("Ask me anything in English, Hindi, Telugu, or german!")

# Initialize chat history
if "messages" not in st.session_state:
    st.session_state.messages = []

# Display previous messages
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# User input
user_input = st.chat_input("Type your message...")

if user_input:

    # Show user message
    st.session_state.messages.append(
        {"role": "user", "content": user_input}
    )

    with st.chat_message("user"):
        st.markdown(user_input)

    # Get chatbot response
    bot_response = get_response(user_input)

    # Show bot response
    with st.chat_message("assistant"):
        st.markdown(bot_response)

    st.session_state.messages.append(
        {"role": "assistant", "content": bot_response}
    )