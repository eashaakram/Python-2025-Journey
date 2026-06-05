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

# Global CSS Injector (Edge-to-Edge Layout Fix)
st.markdown("""
<style>
[data-testid="stSidebar"] { display: none !important; }
[data-testid="collapsedControl"] { display: none !important; }
[data-testid="stHeader"] { display: none !important; }

/* Content Padding Reset for Perfect Headers */
.main .block-container { 
    padding-top: 0rem !important; 
    padding-bottom: 3rem !important;
    padding-left: 0rem !important;
    padding-right: 0rem !important;
    max-width: 100% !important;
}
[data-testid="stMainBlockContainer"] { padding-top: 0rem !important; }

html, body, [class*="css"], .stMarkdown p, h1, h2, h3, h4, span, a {
    font-family: 'Inter', -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, sans-serif !important;
}

/* NAVBAR DESIGN */
.custom-navbar {
    display: flex;
    justify-content: space-between;
    align-items: center;
    background-color: #1a1c1e;
    padding: 16px 40px; 
    margin: 0px 0px 40px 0px;
    border-bottom: 1px solid #2d3139;
    width: 100%;
    box-sizing: border-box;
}
.brand-wrapper { display: flex; flex-direction: column; }
.brand-main-logo { font-size: 23px; font-weight: 800; color: #ffffff; margin: 0; letter-spacing: -0.5px; }
.brand-tagline { font-size: 13px; color: #8a929b; margin-top: 1px; font-weight: 500; }
.middle-nav-links { display: flex; gap: 28px; align-items: center; }
.middle-nav-item { color: #ffffff; text-decoration: none; font-size: 15px; font-weight: 600; cursor: pointer; display: flex; align-items: center; gap: 8px; opacity: 0.9; }
.middle-nav-item:hover { color: #0055ff; opacity: 1; }
.right-nav-wrapper { display: flex; align-items: center; gap: 16px; }
.student-badge-pill { background-color: #262930; color: #e2e8f0; padding: 8px 16px; border-radius: 6px; font-size: 14px; font-weight: 600; border: 1px solid #343a40; }

/* BLUE GLOW LOGOUT BUTTON */
.glowing-logout-action {
    background-color: #0055ff !important;
    color: white !important;
    border-radius: 8px !important;
    font-weight: 700 !important;
    padding: 8px 20px !important;
    font-size: 14px !important;
    text-decoration: none !important;
    display: inline-flex !important;
    align-items: center !important;
    gap: 8px !important;
    box-shadow: 0 0 15px rgba(0, 85, 255, 0.6) !important; 
    transition: all 0.2s ease-in-out !important;
}
.glowing-logout-action:hover {
    background-color: #0044cc !important;
    box-shadow: 0 0 25px rgba(0, 85, 255, 0.9) !important; 
    color: white !important;
}

.inner-app-layout { padding: 0px 40px; }
.dashboard-hero { text-align: center; padding: 20px 0 30px 0; }
.dashboard-hero h2 { font-size: 40px; font-weight: 800; color: #ffffff; }
.dashboard-hero p { font-size: 17px; color: #9ca3af; }
.content-section-title { display: flex; align-items: center; gap: 10px; color: #ffffff; font-size: 24px; font-weight: 700; margin-bottom: 25px; }

/* BLUE TOP BORDER CARDS */
.dsa-interactive-card {
    background-color: #161616;
    padding: 24px;
    border-radius: 10px;
    border: 1px solid #2d2d2d;
    border-top: 4px solid #0055ff;
    margin-bottom: 20px;
}
.dsa-interactive-card h4 { color: #ffffff; margin: 0 0 8px 0; font-size: 18px; font-weight: 700; }
.dsa-interactive-card p { color: #a0aec0; font-size: 14px; margin: 0 0 16px 0; line-height: 1.5; }
.complexity-badge { display: inline-block; background-color: #242424; color: #00BFFF; padding: 4px 10px; border-radius: 4px; font-size: 12px; font-weight: 600; border: 1px solid #333; }
</style>
""", unsafe_allow_html=True)

# -----------------------------
# STEP 1: SESSION STATE INIT
# -----------------------------
if "page" not in st.session_state:
    st.session_state.page = "welcome"

if "auth_page" not in st.session_state:
    st.session_state.auth_page = "login"

# -----------------------------
# STEP 2: ALL FUNCTIONS DEFINED FIRST
# -----------------------------
def go(page):
    st.session_state.page = page
    st.rerun()

def render_navbar_header():
    if "action_logout" in st.query_params:
        st.query_params.clear()
        st.session_state.page = "auth"
        st.session_state.auth_page = "login"
        st.rerun()

    st.markdown("""
    <div class="custom-navbar">
        <div class="brand-wrapper">
            <div class="brand-main-logo">&lt;/&gt; DSA Learning</div>
            <div class="brand-tagline">Master Data Structures & Algorithms</div>
        </div>
        <div class="middle-nav-links">
            <span class="middle-nav-item" onclick="window.location.reload();">
                <svg width="18" height="18" viewBox="0 0 24 24" fill="currentColor"><path d="M10 20v-6h4v6h5v-8h3L12 3 2 12h3v8z"/></svg> Home
            </span>
            <span class="middle-nav-item">
                <svg width="18" height="18" viewBox="0 0 24 24" fill="currentColor"><path d="M16 17.01V10h-2v7.01h-3L15 21l4-3.99h-3zM9 3L5 6.99h3V14h2V6.99h3L9 3z"/></svg> Algorithms
            </span>
            <span class="middle-nav-item">
                <svg width="18" height="18" viewBox="0 0 24 24" fill="currentColor"><path d="M22 11V3h-7v3H9V3H2v8h7V8h2v10H9v-3H2v8h7v-3h2v3h7v-8h-7v3h-2V8h2v3h7z"/></svg> Data Structures
            </span>
        </div>
        <div class="right-nav-wrapper">
            <div class="student-badge-pill">Welcome, Demo Student</div>
            <a href="?action_logout=true" target="_self" class="glowing-logout-action">
                <svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5" stroke-linecap="round" stroke-linejoin="round"><path d="M9 21H5a2 2 0 0 1-2-2V5a2 2 0 0 1 2-2h4"></path><polyline points="16 17 21 12 16 7"></polyline><line x1="21" y1="12" x2="9" y2="12"></line></svg>
                Logout
            </a>
        </div>
    </div>
    """, unsafe_allow_html=True)

def render_footer():
    st.markdown("""
    <style>
    .footer {
        position: relative;
        left: 0;
        bottom: 0;
        width: 100%;
        background-color: #1a1c1e;
        color: #8a929b;
        text-align: center;
        padding: 20px;
        margin-top: 50px;
        border-top: 1px solid #2d3139;
        font-size: 14px;
        font-weight: 500;
    }
    </style>
    <div class="footer">
        Developed by Easha Akram | © 2026 DSA Learning Platform
    </div>
    """, unsafe_allow_html=True)

def home():
    st.markdown('<div class="inner-app-layout">', unsafe_allow_html=True)
    
    st.markdown("""
    <div class="dashboard-hero">
        <h2>Learn Data Structures & Algorithms</h2>
        <p>Explore sorting and searching algorithms and understand how they work</p>
    </div>
    """, unsafe_allow_html=True)

    st.markdown("""
    <div class="content-section-title">
        <svg width="22" height="22" viewBox="0 0 24 24" fill="#ffffff" style="vertical-align: middle;"><path d="M16 17.01V10h-2v7.01h-3L15 21l4-3.99h-3zM9 3L5 6.99h3V14h2V6.99h3L9 3z"/></svg>
        <span>Algorithms & Topics</span>
    </div>
    """, unsafe_allow_html=True)
   
    menu_items = [
        ("Sorting Algorithms", "sorting", "In-place comparisons including Bubble, Insertion, and Selection rules.", "O(n log n) / O(n²)"),
        ("Searching Algorithms", "searching", "Scan sequential setups or instantly divide items on ordered maps.", "O(n) / O(log n)"),
        ("Queue System", "queue_menu", "Linear structures tracking strict First-In-First-Out access sequences.", "O(1) operation"),
        ("Linked List", "linkedlist", "Dynamic sequences linked seamlessly via pointers across standard nodes.", "O(n) traversal"),
        ("Tree Visualizer", "tree_menu", "Hierarchical data tracking balanced splits across search branches.", "O(log n) balanced")
    ]

    cols = st.columns(2)
    for i, (label, page, desc, complexity) in enumerate(menu_items):
        with cols[i % 2]:
            st.markdown(f"""
            <div class="dsa-interactive-card">
                <h4>{label}</h4>
                <p>{desc}</p>
                <span class="complexity-badge">{complexity}</span>
            </div>
            """, unsafe_allow_html=True)
            if st.button(f"Open {label} Visualizer 🚀", key=f"btn_{page}", use_container_width=True):
                go(page)
                
    st.markdown('</div>', unsafe_allow_html=True)

# -----------------------------
# STEP 3: RUNTIME ROUTING LOGIC (Executed at last)
# -----------------------------

# Welcome aur Auth pages ke ilawa baki sab par auto header show hoga
if st.session_state.page not in ["welcome", "auth"]:
    render_navbar_header()

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
    st.markdown('<div class="inner-app-layout">', unsafe_allow_html=True)
    show_linked_list()
    st.markdown('</div>', unsafe_allow_html=True)

elif st.session_state.page == "queue_menu":
    st.markdown('<div class="inner-app-layout">', unsafe_allow_html=True)
    st.markdown("<h2>Queue Visualizer 📊</h2>", unsafe_allow_html=True)
    col1, col2 = st.columns(2)
    with col1:
        if st.button("Simple Queue", use_container_width=True): go("simple_queue")
    with col2:
        if st.button("Circular Queue", use_container_width=True): go("circular_queue")
    st.markdown('</div>', unsafe_allow_html=True)

elif st.session_state.page == "simple_queue": show_simple_queue()
elif st.session_state.page == "circular_queue": show_circular_queue()
elif st.session_state.page == "sorting": show_sorting_algorithms()
elif st.session_state.page == "bubble": show_sorting_bubble()
elif st.session_state.page == "insertion": show_sorting_insertion()
elif st.session_state.page == "selection": show_sorting_selection()
elif st.session_state.page == "searching": show_searching_algorithms()
elif st.session_state.page == "linear": show_linear_search()
elif st.session_state.page == "binary": show_binary_search()
elif st.session_state.page == "tree_menu": tree_menu()
elif st.session_state.page == "bst": show_bst()
elif st.session_state.page == "avl": show_avl()
else:
    st.session_state.page = "home"
    st.rerun()

# Only show footer on pages that have the navbar
if st.session_state.page not in ["welcome", "auth"]:
    render_footer()