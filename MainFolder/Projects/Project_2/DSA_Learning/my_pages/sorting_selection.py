import streamlit as st
import time
from my_pages.utils import home_button

# -----------------------------
# COLORS (Bubble Sort jaisa same)
# -----------------------------
BOX = "#2C3E50"      # Base Color
HIGHLIGHT = "#F39C12" # Active Element / Min
SORTED = "#27AE60"    # Sorted Portion

def draw_bars(arr, min_idx=None, compare_idx=None, sorted_upto=0):
    cols = st.columns(len(arr))
    for i, val in enumerate(arr):
        # Color Logic
        if i < sorted_upto: color = SORTED
        elif i == min_idx or i == compare_idx: color = HIGHLIGHT
        else: color = BOX
        
        with cols[i]:
            st.markdown(f"""
            <div style="height:70px; display:flex; align-items:center; justify-content:center; 
                        background-color:{color}; color:white; border-radius:10px; 
                        font-size:18px; font-weight:600; box-shadow:0px 4px 8px rgba(0,0,0,0.3);">
                {val}
            </div>""", unsafe_allow_html=True)
            st.caption(f"[{i}]")

def show_sorting_selection():
    home_button()
    st.title("Selection Sort Visualizer 🎯")

    # State Init
    if "arr" not in st.session_state: st.session_state.arr = [42, 17, 33, 8, 29]
    if "i" not in st.session_state: st.session_state.i = 0
    if "j" not in st.session_state: st.session_state.j = 1
    if "min_idx" not in st.session_state: st.session_state.min_idx = 0
    if "swaps" not in st.session_state: st.session_state.swaps = 0
    if "running" not in st.session_state: st.session_state.running = False

    # ---------------- CUSTOM INPUT ----------------
    st.subheader("Custom Array Input")
    user_input = st.text_input("Enter numbers (comma separated)", "42,17,33,8,29")
    colA, colB = st.columns([1, 4])
    if colA.button("Apply"):
        st.session_state.arr = list(map(int, user_input.split(",")))
        st.session_state.i, st.session_state.j, st.session_state.min_idx, st.session_state.swaps = 0, 1, 0, 0
        st.rerun()
    if colB.button("Reset"):
        st.session_state.arr = [42, 17, 33, 8, 29]
        st.session_state.i, st.session_state.j, st.session_state.min_idx, st.session_state.swaps = 0, 1, 0, 0
        st.rerun()

    st.markdown("---")

    col_code, col_vis = st.columns([1, 1.2])

    with col_code:
        st.subheader("Algorithm Code")
        st.code("""
void selectionSort(int arr[], int n) {
    for(int i = 0; i < n - 1; i++) {
        int minIdx = i;
        for(int j = i + 1; j < n; j++) {
            if(arr[j] < arr[minIdx]) minIdx = j;
        }
        // Swapping logic
        swap(arr[i], arr[minIdx]);
    }
}""", language="cpp")

    with col_vis:
        st.subheader("Visualizer")
        speed = st.slider("Speed", 0.1, 1.5, 0.5)
        st.markdown(f"**Total Swaps:** {st.session_state.swaps}")
        
        c1, c2, c3 = st.columns(3)
        if c1.button("▶ Play"): st.session_state.running = True
        if c2.button("⏸ Pause"): st.session_state.running = False
        if c3.button("Step"): selection_step(); st.rerun()

        draw_bars(st.session_state.arr, st.session_state.min_idx, st.session_state.j, st.session_state.i)

    if st.session_state.running:
        selection_step()
        time.sleep(speed)
        st.rerun()

# ---------------- EXPLANATION ----------------
    st.markdown("---")
    st.subheader("Understanding Selection Sort")
    st.write("Selection Sort divides the list into a sorted and an unsorted part. It repeatedly selects the smallest element from the unsorted part and swaps it with the leftmost unsorted element.")
    
    st.markdown("### Complexity Analysis")
    st.table({"Case": ["Best", "Average", "Worst"], "Complexity": ["O(n²)", "O(n²)", "O(n²)"]})
    
def selection_step():
    arr = st.session_state.arr
    n = len(arr)
    if st.session_state.i < n - 1:
        if st.session_state.j < n:
            if arr[st.session_state.j] < arr[st.session_state.min_idx]:
                st.session_state.min_idx = st.session_state.j
            st.session_state.j += 1
        else:
            # Perform the SWAP
            if st.session_state.min_idx != st.session_state.i:
                arr[st.session_state.i], arr[st.session_state.min_idx] = arr[st.session_state.min_idx], arr[st.session_state.i]
                st.session_state.swaps += 1
            
            st.session_state.i += 1
            st.session_state.min_idx = st.session_state.i
            st.session_state.j = st.session_state.i + 1
    else:
        st.session_state.running = False
    st.session_state.arr = arr