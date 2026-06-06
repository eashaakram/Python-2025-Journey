import streamlit as st
import time
from my_pages.utils import home_button

# -----------------------------
# COLORS (Consistent with other pages)
# -----------------------------
BOX = "#2C3E50"      # Base Color
HIGHLIGHT = "#F39C12" # Active Element
FOUND = "#27AE60"     # Found Element

def draw_array(arr, current=None, found=None):
    cols = st.columns(len(arr))
    for i, val in enumerate(arr):
        color = BOX
        if i == found: color = FOUND
        elif i == current: color = HIGHLIGHT
        
        with cols[i]:
            st.markdown(f"""
            <div style="height:70px; display:flex; align-items:center; justify-content:center; 
                        background-color:{color}; color:white; border-radius:10px; 
                        font-size:18px; font-weight:600; box-shadow:0px 4px 8px rgba(0,0,0,0.3);">
                {val}
            </div>""", unsafe_allow_html=True)
            st.caption(f"[{i}]")

def show_linear_search():
    home_button()
    st.title("Linear Search Visualizer 🔍")

    # ---------------- INPUT ----------------
    st.subheader("Custom Array & Target")
    user_input = st.text_input("Enter array (comma separated)", "10,25,7,18,30,45")
    target = st.number_input("Enter Target Value", step=1, value=30)
    arr = [int(x.strip()) for x in user_input.split(",") if x.strip().isdigit()]

    # ---------------- LAYOUT ----------------
    col_code, col_vis = st.columns([1, 1.2])

    with col_code:
        st.subheader("Algorithm Code")
        st.code("""
void linearSearch(int arr[], int n, int target) {
    for(int i = 0; i < n; i++) {
        if(arr[i] == target) {
            return i; // Found
        }
    }
    return -1; // Not found
}""", language="cpp")

    with col_vis:
        st.subheader("Visualizer")
        speed = st.slider("Speed", 0.1, 1.5, 0.5)
        
        placeholder = st.empty()
        with placeholder.container():
            draw_array(arr)

        if st.button("Start Search"):
            found = None
            comparisons = 0
            for i in range(len(arr)):
                comparisons += 1
                with placeholder.container():
                    draw_array(arr, current=i)
                    st.info(f"Comparing {arr[i]} with {target}")
                time.sleep(speed)
                
                if arr[i] == target:
                    found = i
                    with placeholder.container():
                        draw_array(arr, found=i)
                        st.success(f"Found at index {i}")
                    break
            
            if found is None:
                with placeholder.container():
                    draw_array(arr)
                    st.error("Not Found ❌")

    # ---------------- EXPLANATION ----------------
    st.markdown("---")
    st.subheader("How Linear Search Works")
    st.write("Linear search sequentially checks each element of the list until a match is found or the whole list has been searched.")
    
    st.markdown("### Complexity Analysis")
    st.table({"Case": ["Best", "Average", "Worst"], "Complexity": ["O(1)", "O(n)", "O(n)"]})