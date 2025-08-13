import streamlit as st
import requests

st.title("HR Resource Chatbot")

query = st.text_input("Enter your query")

if st.button("Search") and query.strip():
    try:
        res = requests.post("http://localhost:8000/chat", json={"query": query})
        if res.status_code == 200:
            st.markdown(res.json()["response"])
        else:
            st.error("Error: " + res.text)
    except Exception as e:
        st.error(f"Could not connect to backend: {e}")
