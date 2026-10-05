import streamlit as st
import requests


st.set_page_config(
    page_title="Sales AI Agent",
    page_icon="📊",
    layout="wide"
)


st.title("📊 Sales AI Agent")
st.caption("AI-powered sales and product analysis")


question = st.chat_input("Ask about your sales...")


if question:

    with st.chat_message("user"):
        st.write(question)

    try:

        response = requests.post(
            "http://127.0.0.1:8000/ask",
            params={
                "question": question
            },
            headers={
                "api-key": "company123"
            }
        )

        response.raise_for_status()

        data = response.json()

        answer = data["answer"]

    except Exception as e:
        answer = f"Error: {e}"

    with st.chat_message("assistant"):
        st.write(answer)