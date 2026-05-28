import streamlit as st

from my_pages.utils import home_button

st.markdown("---")

def tree_menu():
    home_button()
    st.title("🌳 Tree Visualizer Hub")

    st.write("Choose which tree you want to explore")

    col1, col2 = st.columns(2)

    with col1:
        if st.button("BST Tree 🌳", use_container_width=True):
            st.session_state.page = "bst"
            st.rerun()

    with col2:
        if st.button("AVL Tree ⚖️", use_container_width=True):
            st.session_state.page = "avl"
            st.rerun()

    st.markdown("---")

    st.info("""
BST → Simple Binary Search Tree  
AVL → Self Balancing Tree (Rotations + Balance Factor)
""")