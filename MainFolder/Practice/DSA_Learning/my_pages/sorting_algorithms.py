import streamlit as st

from my_pages.utils import home_button

st.markdown("---")

def go(page):
    st.session_state.page = page


def show_sorting_algorithms():
    home_button()
    st.title("Sorting Algorithms Visualizer 🔢")

    st.write("Choose a Sorting Algorithm")

    col1, col2, col3 = st.columns(3)

    with col1:
        if st.button("Bubble Sort 🔵"):
            go("bubble")

    with col2:
        if st.button("Insertion Sort 🟢"):
            go("insertion")

    with col3:
        if st.button("Selection Sort 🟡"):
            go("selection")