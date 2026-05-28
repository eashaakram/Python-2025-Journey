import streamlit as st

# -----------------------------
# IMPORT PAGES
# -----------------------------
from my_pages.login import show_login
from my_pages.signup import show_signup
from my_pages.welcome import show_welcome
from my_pages.home import show_home
from my_pages.stack import show_stack
from my_pages.linkedlist import show_linked_list

from my_pages.queue_menu import show_queue_menu
from my_pages.simple_queue import show_simple_queue
from my_pages.circular_queue import show_circular_queue

from my_pages.sorting_algorithms import show_sorting_algorithms
from my_pages.sorting_bubble import show_sorting_bubble
from my_pages.sorting_insertion import show_sorting_insertion
from my_pages.sorting_selection import show_sorting_selection

from my_pages.searching_algorithms import show_searching_algorithms
from my_pages.linear_search import show_linear_search
from my_pages.binary_search import show_binary_search

from my_pages.tree_menu import tree_menu
from my_pages.bst import show_bst
from my_pages.avl import show_avl


# -----------------------------
# PAGE CONFIG
# -----------------------------
st.set_page_config(
    page_title="DSA Visualizer",
    layout="wide"
)

# Hide sidebar 
st.markdown("""
<style>
[data-testid="stSidebar"] {
    display: none;
}

[data-testid="collapsedControl"] {
    display: none;
}
</style>
""", unsafe_allow_html=True)


# -----------------------------
# SESSION STATE INIT
# -----------------------------
if "page" not in st.session_state:
    st.session_state.page = "welcome"

if "auth_page" not in st.session_state:
    st.session_state.auth_page = "login"

def go(page):
    st.session_state.page = page
    st.rerun()


# -----------------------------
# HOME PAGE
# -----------------------------
def home():

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
                go(page)


# -----------------------------
# ROUTING SYSTEM
# -----------------------------
if st.session_state.page == "welcome":
    show_welcome()
    
elif st.session_state.page == "auth":
    # Switch between login.py and signup.py files dynamically
    if st.session_state.auth_page == "login":
        show_login()
    elif st.session_state.auth_page == "signup":
        show_signup()

elif st.session_state.page == "home":
    home()

# -------- STACK / LINKED LIST --------
elif st.session_state.page == "stack":
    show_stack()

elif st.session_state.page == "linkedlist":
    show_linked_list()


# -------- QUEUE MENU --------
elif st.session_state.page == "queue_menu":

    st.title("Queue Visualizer ")

    col1, col2 = st.columns(2)

    with col1:
        if st.button("Simple Queue"):
            go("simple_queue")

    with col2:
        if st.button("Circular Queue"):
            go("circular_queue")


elif st.session_state.page == "simple_queue":
    show_simple_queue()

elif st.session_state.page == "circular_queue":
    show_circular_queue()


# -------- SORTING --------
elif st.session_state.page == "sorting":
    show_sorting_algorithms()

elif st.session_state.page == "bubble":
    show_sorting_bubble()

elif st.session_state.page == "insertion":
    show_sorting_insertion()

elif st.session_state.page == "selection":
    show_sorting_selection()


# -------- SEARCHING --------
elif st.session_state.page == "searching":
    show_searching_algorithms()

elif st.session_state.page == "linear":
    show_linear_search()

elif st.session_state.page == "binary":
    show_binary_search()

# -------- TREE --------
elif st.session_state.page == "tree_menu":
    tree_menu()

elif st.session_state.page == "bst":
    show_bst()

elif st.session_state.page == "avl":
    show_avl()


# -------- FALLBACK --------
else:
    st.error("Page not found ❌")
    st.session_state.page = "home"