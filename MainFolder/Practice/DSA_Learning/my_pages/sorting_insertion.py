import streamlit as st
import time
from my_pages.utils import home_button

# -----------------------------
# SAME PROFESSIONAL COLORS AS BUBBLE SORT
# -----------------------------
BOX = "#2C3E50"      # Base Color
HIGHLIGHT = "#F39C12" # Active Element Color

def draw_bars(arr, key_idx=None, j_idx=None):
    cols = st.columns(len(arr))
    for index, val in enumerate(arr):
        # Bubble sort ki tarah color logic
        color = HIGHLIGHT if index == key_idx or index == j_idx else BOX
        
        with cols[index]:
            st.markdown(f"""
            <div style="height:70px; display:flex; align-items:center; justify-content:center; 
                        background-color:{color}; color:white; border-radius:10px; 
                        font-size:18px; font-weight:600; box-shadow:0px 4px 10px rgba(0,0,0,0.3);">
                {val}
            </div>""", unsafe_allow_html=True)
            st.caption(f"[{index}]")

def show_sorting_insertion():
    home_button()
    st.title("Insertion Sort Visualizer 🧠")

    # State Initialization
    if "arr" not in st.session_state: st.session_state.arr = [50, 20, 40, 10, 30]
    if "i" not in st.session_state: st.session_state.i = 1
    if "j" not in st.session_state: st.session_state.j = -1
    if "swaps" not in st.session_state: st.session_state.swaps = 0
    if "running" not in st.session_state: st.session_state.running = False

    # Input Controls
    st.subheader("Custom Array Input")
    user_input = st.text_input("Enter numbers (comma separated)", "50,20,40,10,30")
    colA, colB = st.columns([1, 4])
    
    if colA.button("Apply"):
        st.session_state.arr = list(map(int, user_input.split(",")))
        st.session_state.i, st.session_state.j, st.session_state.swaps, st.session_state.running = 1, -1, 0, False
        st.rerun()
    if colB.button("Reset"):
        st.session_state.arr = [50, 20, 40, 10, 30]
        st.session_state.i, st.session_state.j, st.session_state.swaps, st.session_state.running = 1, -1, 0, False
        st.rerun()

    st.markdown("---")

    # Layout: Code Left, Visualizer Right
    col_code, col_vis = st.columns([1, 1.2])

    with col_code:
        st.subheader("Algorithm Code")
        st.code("""
void insertionSort(int arr[], int n) {
    for(int i = 1; i < n; i++) {
        int key = arr[i];
        int j = i - 1;
        while(j >= 0 && arr[j] > arr[j+1]) {
            swap(arr[j], arr[j+1]);
            j--;
        }
    }
}""", language="cpp")

    with col_vis:
        st.subheader("Visualizer")
        speed = st.slider("Speed", 0.1, 1.0, 0.5)
        st.markdown(f"**Swaps:** {st.session_state.swaps}")
        
        c1, c2, c3 = st.columns(3)
        if c1.button("▶ Play"): st.session_state.running = True
        if c2.button("⏸ Pause"): st.session_state.running = False
        if c3.button("Step"): insertion_step(); st.rerun()

        draw_bars(st.session_state.arr, st.session_state.i, st.session_state.j)

    if st.session_state.running:
        insertion_step()
        time.sleep(speed)
        st.rerun()

def insertion_step():
    arr = st.session_state.arr
    n = len(arr)
    if st.session_state.i < n:
        if st.session_state.j == -1: st.session_state.j = st.session_state.i - 1
        
        if st.session_state.j >= 0 and arr[st.session_state.j] > arr[st.session_state.j + 1]:
            arr[st.session_state.j], arr[st.session_state.j + 1] = arr[st.session_state.j + 1], arr[st.session_state.j]
            st.session_state.swaps += 1
            st.session_state.j -= 1
        else:
            st.session_state.i += 1
            st.session_state.j = -1
    else:
        st.session_state.running = False
    st.session_state.arr = arr