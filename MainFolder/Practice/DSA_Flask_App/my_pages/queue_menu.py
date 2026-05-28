import streamlit as st

from my_pages.utils import home_button

st.markdown("---")

def show_queue_menu():
    home_button()
    st.title("Queue Visualizer 🚶")

    st.write("Choose Queue Type")

    col1, col2 = st.columns(2)

    # SIMPLE QUEUE
    with col1:
        if st.button("Simple Queue", use_container_width=True):
            st.session_state.page = "simple_queue"

    # CIRCULAR QUEUE
    with col2:
        if st.button("Circular Queue", use_container_width=True):
            st.session_state.page = "circular_queue"
        