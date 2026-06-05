import streamlit as st
import time
from my_pages.utils import home_button

# -----------------------------
# COLORS (Consistent)
# -----------------------------
BOX = "#2C3E50"      
HIGHLIGHT = "#F39C12" 
RANGE = "#3498DB"     
FOUND = "#27AE60"     

def draw_array(arr, low=None, mid=None, high=None, found=None):
    cols = st.columns(len(arr))
    for i, val in enumerate(arr):
        if i == found: color = FOUND
        elif i == mid: color = HIGHLIGHT
        elif low is not None and high is not None and low <= i <= high: color = RANGE
        else: color = BOX
        
        with cols[i]:
            st.markdown(f"""
            <div style="height:70px; display:flex; align-items:center; justify-content:center; 
                        background-color:{color}; color:white; border-radius:10px; 
                        font-size:18px; font-weight:600; box-shadow:0px 4px 8px rgba(0,0,0,0.3);">
                {val}
            </div>""", unsafe_allow_html=True)
            st.caption(f"[{i}]")

def show_binary_search():
    home_button()
    st.title("Binary Search Visualizer ⚡")

    # ---------------- CUSTOM INPUT ----------------
    st.subheader("Custom Array & Target")
    
    # NOTE ADDED: Binary Search Requirement
    st.info("ℹ️ **Note:** Binary Search only works on a **sorted array**. If you enter an unsorted array, it will be automatically sorted.")
    
    user_input = st.text_input("Enter array (comma separated)", "5,10,15,20,25,30,40")
    target = st.number_input("Enter Target Value", step=1, value=25)
    
    arr = sorted([int(x.strip()) for x in user_input.split(",") if x.strip().isdigit()])
    
    # ---------------- LAYOUT ----------------
    col_code, col_vis = st.columns([1, 1.2])

    with col_code:
        st.subheader("Algorithm Code")
        st.code("""
void binarySearch(int arr[], int n, int target) {
    int low = 0, high = n - 1;
    while(low <= high) {
        int mid = low + (high - low) / 2;
        if(arr[mid] == target) return mid;
        if(arr[mid] < target) low = mid + 1;
        else high = mid - 1;
    }
    return -1;
}""", language="cpp")

    with col_vis:
        st.subheader("Visualizer")
        speed = st.slider("Speed", 0.1, 1.5, 0.5)
        placeholder = st.empty()
        
        if st.button("Start Search"):
            low, high = 0, len(arr) - 1
            found = None
            while low <= high:
                mid = (low + high) // 2
                with placeholder.container():
                    draw_array(arr, low, mid, high)
                    st.info(f"Checking index {mid} (Value: {arr[mid]})")
                time.sleep(speed)
                
                if arr[mid] == target:
                    found = mid
                    with placeholder.container():
                        draw_array(arr, found=mid)
                        st.success(f"Found at index {mid}")
                    break
                elif arr[mid] < target:
                    low = mid + 1
                else:
                    high = mid - 1
            if found is None:
                with placeholder.container():
                    draw_array(arr)
                    st.error("Not Found ❌")
        else:
            with placeholder.container():
                draw_array(arr)

    # ---------------- EXPLANATION ----------------
    st.markdown("---")
    st.subheader("How Binary Search Works")
    st.write("Binary Search is an efficient algorithm that finds the position of a target value within a **sorted array** by repeatedly halving the search interval.")
    
    st.markdown("### Complexity Analysis")
    st.table({"Case": ["Best", "Average", "Worst"], "Complexity": ["O(1)", "O(log n)", "O(log n)"]})