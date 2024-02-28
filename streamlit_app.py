import streamlit as st
from groq import Groq
import os

from dotenv import load_dotenv
load_dotenv()

def fetch_response(user_input):
    client = Groq(api_key=os.environ['GROQ_API_KEY'])
    chat_completion = client.chat.completions.create(
        messages=[
            {"role": "system", "content": "You are a helpful assistant."},
            {"role": "user", "content": user_input},
        ],
        model="mixtral-8x7b-32768",
        temperature=0.5,
        max_tokens=1024,
        top_p=1,
        stop=None,
        stream=False,
    )
    return chat_completion.choices[0].message.content

def main():
    st.title("Groq Chatbot")
    st.sidebar.header("Input")
    user_input = st.sidebar.text_input("Enter your message here:")
    if st.sidebar.button("Send"):
        response = fetch_response(user_input)
        st.subheader("Output")
        st.text_area("", value=response, height=999, max_chars=None, key=None)

if __name__ == "__main__":
    main()
