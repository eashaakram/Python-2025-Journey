import streamlit as st

from my_pages.layout import (
    BORDER,
    TEXT_MUTED,
    inject_global_styles,
    render_site_footer,
    render_site_header,
)
from my_pages.login import show_login
from my_pages.signup import show_signup
from my_pages.welcome import show_welcome
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


st.set_page_config(page_title="DSA Visualizer", layout="wide")


if "page" not in st.session_state:
    st.session_state.page = "welcome"

if "auth_page" not in st.session_state:
    st.session_state.auth_page = "login"

if "logged_in" not in st.session_state:
    st.session_state.logged_in = False

if "user_name" not in st.session_state:
    st.session_state.user_name = "Demo Student"


AUTH_PAGES = {"welcome", "auth"}
layout_mode = "auth" if st.session_state.page in AUTH_PAGES else "app"
inject_global_styles(layout_mode)
render_site_header()


def go(page):
    st.session_state.page = page
    st.rerun()


def home():
    display_name = st.session_state.get("user_name", "Demo Student")

    st.markdown(
        f"""
        <div style="text-align:center; padding: 8px 0 16px 0;">
            <h2 style="font-size:1.6rem; font-weight:700; color:#ffffff; margin-bottom:6px;">
                Learn Data Structures &amp; Algorithms
            </h2>
            <p style="font-size:0.95rem; color:{TEXT_MUTED}; margin:0;">
                Explore sorting and searching algorithms and understand how they work
            </p>
        </div>
        """,
        unsafe_allow_html=True,
    )

    user_cols = st.columns([2, 2, 1.5, 2, 2])
    with user_cols[1]:
        st.markdown(
            f"""
            <div style="background-color:#252a33; color:white; padding:8px 16px;
                        border-radius:8px; font-weight:500; text-align:center;
                        border:1px solid {BORDER};">
                Welcome, {display_name}
            </div>
            """,
            unsafe_allow_html=True,
        )
    with user_cols[3]:
        if st.button("↪ Logout", key="btn_logout", use_container_width=True):
            st.session_state.logged_in = False
            st.session_state.user_name = "Demo Student"
            st.session_state.page = "auth"
            st.session_state.auth_page = "login"
            st.rerun()

    st.markdown(
        f"<hr style='border:1px solid {BORDER}; margin:24px 0;'>",
        unsafe_allow_html=True,
    )

    st.markdown("### ↕️ Algorithms")

    menu = [
        ("Sorting Algorithms", "sorting", "O(n log n) / O(n²)"),
        ("Searching Algorithms", "searching", "O(n) / O(log n)"),
        ("Queue", "queue_menu", "O(1) enqueue/dequeue"),
        ("Linked List", "linkedlist", "O(n) traversal"),
        ("Tree Visualizer", "tree_menu", "O(log n) - balanced"),
    ]

    cols = st.columns(2)
    for i, (label, page, complexity) in enumerate(menu):
        with cols[i % 2]:
            st.write("")
            if st.button(f"**{label}**\n\n{complexity}", key=page, use_container_width=True):
                go(page)


if st.session_state.page == "welcome":
    show_welcome()

elif st.session_state.page == "auth":
    if st.session_state.auth_page == "login":
        show_login()
    elif st.session_state.auth_page == "signup":
        show_signup()

elif st.session_state.page == "home":
    home()

elif st.session_state.page == "linkedlist":
    show_linked_list()

elif st.session_state.page == "queue_menu":
    st.title("Queue Visualizer 📊")
    col1, col2 = st.columns(2)
    with col1:
        if st.button("Simple Queue", use_container_width=True):
            go("simple_queue")
    with col2:
        if st.button("Circular Queue", use_container_width=True):
            go("circular_queue")

elif st.session_state.page == "simple_queue":
    show_simple_queue()

elif st.session_state.page == "circular_queue":
    show_circular_queue()

elif st.session_state.page == "sorting":
    show_sorting_algorithms()

elif st.session_state.page == "bubble":
    show_sorting_bubble()

elif st.session_state.page == "insertion":
    show_sorting_insertion()

elif st.session_state.page == "selection":
    show_sorting_selection()

elif st.session_state.page == "searching":
    show_searching_algorithms()

elif st.session_state.page == "linear":
    show_linear_search()

elif st.session_state.page == "binary":
    show_binary_search()

elif st.session_state.page == "tree_menu":
    tree_menu()

elif st.session_state.page == "bst":
    show_bst()

elif st.session_state.page == "avl":
    show_avl()

else:
    st.error("Page not found ❌")
    st.session_state.page = "home"
    st.rerun()

render_site_footer()
