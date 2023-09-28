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

    # Create conversation window
    st.markdown(
        """
        <div style="width: 80%; height: 400px; overflow-y: scroll; border: 1px solid gray; padding: 10px;">
            <div id="conversation"></div>
        </div>
        """,
        unsafe_allow_html=True
    )

    # Create user input section
    user_input = st.text_input("User Input")

    # Create send button
    send_button_col, _ = st.beta_columns([1, 9])
    if send_button_col.button("Send"):
        if user_input:
            messages.append({"role": "user", "content": user_input})
            response = send_request(messages)
            messages.append({"role": "EconGPT", "content": response})
            user_input = ""

    # Display chat messages
    for msg in messages:
        if msg["role"] == "user":
            st.markdown(f"<p style='color: blue;'>User: {msg['content']}</p>", unsafe_allow_html=True)
        elif msg["role"] == "EconGPT":
            st.markdown(f"<p style='color: red;'>EconGPT: {msg['content']}</p>", unsafe_allow_html=True)

    # Add button to clear conversation
    if st.button("Clear Conversation"):
        messages = []


if __name__ == "__main__":
    main()
