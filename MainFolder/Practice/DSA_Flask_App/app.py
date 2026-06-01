import streamlit as st

# -----------------------------
# IMPORT PAGES
# -----------------------------
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


# -----------------------------
# PAGE CONFIG
# -----------------------------
st.set_page_config(
    page_title="DSA Learning", 
    layout="wide"
)

# Hide default streamlit sidebar 
st.markdown("""
<style>
[data-testid="stSidebar"] { display: none; }
[data-testid="collapsedControl"] { display: none; }

/* Custom Styling for Top Header Section - Background changed to match image */
.main-header {
    text-align: center;
    padding: 20px 0 10px 0;
    background-color: #22252a; /* Border se upar wale part ka dark background color */
    margin: -60px -50px 20px -50px; /* Puray top area ko cover karne ke liye padding offset */
    padding-top: 40px;
    padding-bottom: 20px;
}
.main-header h1 {
    font-size: 42px;
    font-weight: 700;
    margin-bottom: 5px;
}
.main-header p {
    font-size: 16px;
    color: #b0b0b0;
    margin-bottom: 20px;
}

/* Welcome Student Tag */
.student-badge {
    background-color: #33393f;
    color: white;
    padding: 8px 16px;
    border-radius: 8px;
    font-weight: 500;
    display: inline-block;
    text-align: center;
    width: 100%;
}

/* TARGET LOGOUT BUTTON: Styling it vibrant blue just like the welcome page */
div.stButton > button[key="btn_logout"] {
    background-color: #5d78ff !important;
    color: white !important;
    border-radius: 8px !important;
    border: none !important;
    font-weight: 600 !important;
}
div.stButton > button[key="btn_logout"]:hover {
    background-color: #4962e6 !important;
    color: white !important;
}

/* Content Hero Section */
.hero-section {
    text-align: center;
    padding: 40px 0 20px 0;
}
.hero-section h2 {
    font-size: 38px;
    font-weight: 700;
    margin-bottom: 10px;
}
.hero-section p {
    font-size: 18px;
    color: #9ca3af;
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
    # 1. TOP HEADER (Brand Name & Subtitle)
    st.markdown("""
    <div class="main-header">
        <h1>&lt;/&gt; DSA Learning</h1>
        <p>Master Data Structures & Algorithms</p>
    </div>
    """, unsafe_allow_html=True)

   
    # 2. USER INFO & LOGOUT ROW
    st.write("") # Spacer
    user_cols = st.columns([2, 2, 1.5, 2, 2])
    with user_cols[1]:
        st.markdown('<div class="student-badge">Welcome, Demo Student</div>', unsafe_allow_html=True)
    with user_cols[3]:
        if st.button("↪️ Logout", key="btn_logout", use_container_width=True):
            st.session_state.page = "auth"
            st.session_state.auth_page = "login"
            st.rerun()

    # Full Width Dark Background Section Divider Like image_6a9445.png
    st.markdown("<hr style='border: 1px solid #262730; margin: 30px 0;'>", unsafe_allow_html=True)

    # 4. HERO SECTION (Learn Data Structures & Algorithms)
    st.markdown("""
    <div class="hero-section">
        <h2>Learn Data Structures & Algorithms</h2>
        <p>Explore sorting and searching algorithms and understand how they work</p>
    </div>
    """, unsafe_allow_html=True)

    # Note: Search Bar is skipped as requested!

    # 5. ALGORITHMS HEADER 
    st.write("")
    algo_header_cols = st.columns([4, 1])
    with algo_header_cols[0]:
        st.markdown("### ↕️ Algorithms")
   

    # 6. CARDS / BUTTONS GRID FOR DSA TOPICS
    menu = [
        ("Sorting Algorithms", "sorting", "O(n log n) / O(n²)"),
        ("Searching Algorithms", "searching", "O(n) / O(log n)"),
        ("Queue", "queue_menu", "O(1) enqueue/dequeue"),
        ("Linked List", "linkedlist", "O(n) traversal"),
        ("Tree Visualizer", "tree_menu", "O(log n) - balanced")
    ]

    cols = st.columns(2)
    for i, (label, page, complexity) in enumerate(menu):
        with cols[i % 2]:
            st.write("")
            if st.button(f"**{label}**\n\n{complexity}", key=page, use_container_width=True):
                go(page)


# -----------------------------
# ROUTING SYSTEM
# -----------------------------
if st.session_state.page == "welcome":
    show_welcome()
    
elif st.session_state.page == "auth":
    if st.session_state.auth_page == "login":
        show_login()
    elif st.session_state.auth_page == "signup":
        show_signup()

elif st.session_state.page == "home":
    home()

# -------- LINKED LIST --------

elif st.session_state.page == "linkedlist":
    show_linked_list()


# -------- QUEUE MENU --------
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
    st.rerun()