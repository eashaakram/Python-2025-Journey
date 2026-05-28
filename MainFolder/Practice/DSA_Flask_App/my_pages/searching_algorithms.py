import streamlit as st

from my_pages.utils import home_button

st.markdown("---")

def go(page):
    st.session_state.page = page


def show_searching_algorithms():
    home_button()
    st.title("Searching Algorithms 🔍")

    st.write("Choose Any Searching Algorithm")

    col1, col2 = st.columns(2)

    with col1:

        if st.button(
            "Linear Search",
            use_container_width=True
        ):

            go("linear")

    with col2:

        if st.button(
            "Binary Search",
            use_container_width=True
        ):

            go("binary")