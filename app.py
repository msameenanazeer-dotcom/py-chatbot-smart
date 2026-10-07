```python
import streamlit as st

st.set_page_config(
    page_title="Python Chatbot",
    page_icon="🤖",
    layout="centered"
)

st.title("🤖 Python Chatbot")
st.write("Welcome! Ask me a question.")

# Store chat history
if "messages" not in st.session_state:
    st.session_state.messages = []

# Display previous messages
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.write(message["content"])


def chatbot_response(user_input):

    text = user_input.lower()

    if "hello" in text or "hi" in text or "hey" in text:
        return "Hello! 👋 How can I help you?"

    elif "name" in text:
        return "I am a Python chatbot 🤖."

    elif "python" in text:
        return "Python is a popular programming language used for AI, ML, data science and web development. 🐍"

    elif "ai" in text or "artificial intelligence" in text:
        return "AI means Artificial Intelligence. It enables computers to perform tasks that normally require human intelligence."

    elif "machine learning" in text:
        return "Machine Learning is a branch of AI where computers learn patterns from data."

    elif "github" in text:
        return "GitHub is a platform for storing, managing and sharing code."

    elif "thank" in text:
        return "You're welcome! 😊"

    elif "bye" in text:
        return "Goodbye! 👋"

    else:
        return "Sorry, I don't understand that yet. Please try another question."


# Chat input
user_input = st.chat_input("Type your message here...")

if user_input:

    # Display user message
    st.session_state.messages.append({
        "role": "user",
        "content": user_input
    })

    with st.chat_message("user"):
        st.write(user_input)

    # Generate response
    response = chatbot_response(user_input)

    # Display bot response
    with st.chat_message("assistant"):
        st.write(response)

    # Save response
    st.session_state.messages.append({
        "role": "assistant",
        "content": response
    })
```
