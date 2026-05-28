import streamlit as st

def show_home():

    st.title("DSA Visualizer 🚀")
    st.write("Choose Any Topic")

    menu = [
        ("Sorting Algorithms", "sorting"),
        ("Searching Algorithms", "searching"),
        ("Stack", "stack"),
        ("Queue", "queue_menu"),
        ("Linked List", "linkedlist"),
        ("Tree Visualizer", "tree_menu")
    ]

    cols = st.columns(3)

    for i, (label, page) in enumerate(menu):

        with cols[i % 3]:

            if st.button(label, use_container_width=True):

                st.session_state.page = page
                st.rerun()