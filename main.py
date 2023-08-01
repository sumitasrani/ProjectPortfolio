import streamlit as st

st.set_page_config(layout="wide")

col1, col2 = st.columns(2)

with col1:
    st.image("images/Sumit Asrani.png")

with col2:
    st.title("Sumit Asrani")
    content = """
                Hi, I am Sumit Asrani! I am a Python programmer.\n
                I am transitioning from Content (Marketing) to Coding.\n
                This project is to showcase various python projects
                I have built on my journey to learn Python.
            """
    st.info(content)

content1 = """ Below are the Python Projects. Feel free to connect with me."""

st.info(content1)