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

    messages = []
    user_input = ""

    while True:
        user_input = st.text_input("User:", value=user_input, key="user_input")
        if st.button("Send"):
            if user_input:
                messages.append({"role": "user", "content": user_input})
                response = send_request(messages)
                messages.append({"role": "EconGPT", "content": response})
                user_input = ""

        st.text_area("Conversation", value="\n".join(
            [f"{msg['role']}: {msg['content']}" for msg in messages]
        ))

        if st.button("Clear Conversation"):
            messages = []
            user_input = ""


if __name__ == "__main__":
    main()
