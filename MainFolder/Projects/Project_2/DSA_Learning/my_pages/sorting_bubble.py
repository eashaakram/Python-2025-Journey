import streamlit as st
import time
from my_pages.utils import home_button

# -----------------------------
# CONSTANTS & STYLES
# -----------------------------
BOX = "#2C3E50"
HIGHLIGHT = "#F39C12"

def draw_bars(arr, i=None, j=None):
    cols = st.columns(len(arr))
    for index, val in enumerate(arr):
        color = HIGHLIGHT if index == i or index == j else BOX
        with cols[index]:
            st.markdown(f"""
            <div style="height:70px; display:flex; align-items:center; justify-content:center; 
                        background-color:{color}; color:white; border-radius:10px; 
                        font-size:18px; font-weight:600; box-shadow:0px 4px 10px rgba(0,0,0,0.3);">
                {val}
            </div>""", unsafe_allow_html=True)
            st.caption(f"[{index}]")

def show_sorting_bubble():
    home_button()
    st.title("Bubble Sort Visualizer 🔥")
    
    # ---------------- INIT STATE ----------------
    if "arr" not in st.session_state: st.session_state.arr = [83, 63, 8, 21, 21]
    if "i" not in st.session_state: st.session_state.i = 0
    if "j" not in st.session_state: st.session_state.j = 0
    if "running" not in st.session_state: st.session_state.running = False
    if "swaps" not in st.session_state: st.session_state.swaps = 0

    # ---------------- CUSTOM INPUT (Directly Visible) ----------------
    st.subheader("Custom Array Input")
    user_input = st.text_input("Enter numbers (comma separated)", "83,63,8,21,21")
    colA, colB = st.columns([1, 4])
    
    if colA.button("Apply"):
        st.session_state.arr = list(map(int, user_input.split(",")))
        st.session_state.i = st.session_state.j = st.session_state.swaps = 0
        st.rerun()
    if colB.button("Reset to Default"):
        st.session_state.arr = [83, 63, 8, 21, 21]
        st.session_state.i = st.session_state.j = st.session_state.swaps = 0
        st.rerun()

    st.markdown("---")

    # ---------------- LAYOUT: CODE LEFT, VIS RIGHT ----------------
    col_code, col_vis = st.columns([1, 1.2])

    with col_code:
        st.subheader("Algorithm Code")
        st.code("""
void bubbleSort(int arr[], int n) {
    for (int i = 0; i < n - 1; i++) {
        for (int j = 0; j < n - i - 1; j++) {
            if (arr[j] > arr[j + 1]) {
                swap(arr[j], arr[j+1]);
            }
        }
    }
}""", language="cpp")

    with col_vis:
        st.subheader("Visualizer")
        speed = st.slider("Speed", 0.1, 1.0, 0.5)
        
        c1, c2, c3 = st.columns(3)
        if c1.button("▶ Play"): st.session_state.running = True
        if c2.button("⏸ Pause"): st.session_state.running = False
        if c3.button("Step"): bubble_step(st.session_state.arr); st.rerun()

        st.markdown(f"**Swaps:** {st.session_state.swaps}")
        draw_bars(st.session_state.arr, st.session_state.i, st.session_state.j)

    # ---------------- LOGIC ----------------
    if st.session_state.running:
        bubble_step(st.session_state.arr)
        time.sleep(speed)
        st.rerun()

    # ---------------- EXPLANATION ----------------
    st.markdown("---")
    st.subheader("Understanding Bubble Sort")
    st.write("""
    Bubble Sort works by repeatedly swapping adjacent elements if they are in the wrong order. 
    It is called "Bubble" sort because with each iteration, the largest element 'bubbles' 
    up to its correct position at the end of the array.
    """)
    
    st.markdown("### Complexity Analysis")
    st.table({"Case": ["Best", "Average", "Worst"], "Complexity": ["O(n)", "O(n²)", "O(n²)"]})

def bubble_step(arr):
    n = len(arr)
    if st.session_state.i < n - 1:
        if st.session_state.j < n - st.session_state.i - 1:
            if arr[st.session_state.j] > arr[st.session_state.j + 1]:
                arr[st.session_state.j], arr[st.session_state.j + 1] = arr[st.session_state.j + 1], arr[st.session_state.j]
                st.session_state.swaps += 1
            st.session_state.j += 1
        else:
            st.session_state.i += 1
            st.session_state.j = 0
    else:
        st.session_state.running = False
    st.session_state.arr = arr