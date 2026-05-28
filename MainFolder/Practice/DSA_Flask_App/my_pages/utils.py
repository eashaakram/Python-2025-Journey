import streamlit as st

def home_button():

    if st.button("⬅ Back To Menu"):

        st.session_state.page = "home"
        st.rerun()