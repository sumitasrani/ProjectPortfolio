import streamlit as st
from send_email import send_mail

st.header("Contact Me")

with st.form(key="Contact_form"):
    user_email = st.text_input("Your email address")
    user_message = st.text_area("Your message")
    message = f"""\
Subject: New email from {user_email}

From: {user_email}
{user_message}
"""
    submit_btn = st.form_submit_button("Submit")
    if submit_btn:
        send_mail(message)
        st.info("Email was sent successfully")