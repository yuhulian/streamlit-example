import streamlit as st
import requests

API_ENDPOINT = "http://192.170.12.80:5002/econservice"


def send_request(messages):
    response = requests.post(API_ENDPOINT, json=messages)
    if response.status_code == 200:
        data = response.json()
        return data["response"]
    else:
        return "Error: Failed to fetch response"


def main():
    st.title("EconGPT Chat")

    # Create columns for conversation and user input
    col1, col2 = st.beta_columns([4, 1])

    # Create empty container for chat messages
    messages_container = col1.empty()

    # Initialize messages list
    messages = []

    # Get user input
    user_input = col2.text_input("User Input")

    if col2.button("Send"):
        if user_input:
            messages.append({"role": "user", "content": user_input})
            response = send_request(messages)
            messages.append({"role": "EconGPT", "content": response})
            user_input = ""

    # Display chat messages
    for msg in messages:
        if msg["role"] == "user":
            messages_container.text(f"User: {msg['content']}")
        elif msg["role"] == "EconGPT":
            messages_container.text(f"EconGPT: {msg['content']}")

    # Add button to clear conversation
    if st.button("Clear Conversation"):
        messages = []


if __name__ == "__main__":
    main()
