import streamlit as st
import time

from my_pages.utils import home_button

st.markdown("---")

# -----------------------------
# PROFESSIONAL COLORS
# -----------------------------
BG = "#1E1E2F"
BOX = "#2C3E50"
HIGHLIGHT = "#F39C12"
SWAP = "#E74C3C"


# -----------------------------
# DRAW ARRAY
# -----------------------------
def draw_bars(arr, i=None, j=None):

    cols = st.columns(len(arr))

    for index, val in enumerate(arr):

        color = BOX

        if index == i or index == j:
            color = HIGHLIGHT

        with cols[index]:
            st.markdown(
                f"""
                <div style="
                    height:80px;
                    display:flex;
                    align-items:center;
                    justify-content:center;
                    background-color:{color};
                    color:white;
                    border-radius:10px;
                    font-size:18px;
                    font-weight:600;
                    box-shadow:0px 4px 10px rgba(0,0,0,0.3);
                ">
                    {val}
                </div>
                """,
                unsafe_allow_html=True
            )


# -----------------------------
# MAIN VISUALIZER
# -----------------------------
def show_sorting_bubble():
    home_button()
    st.title("Bubble Sort Visualizer 🔥")

    # ---------------- INIT ARRAY ----------------
    if "arr" not in st.session_state:
        st.session_state.arr = [50, 20, 40, 10, 30]

    if "i" not in st.session_state:
        st.session_state.i = 0

    if "j" not in st.session_state:
        st.session_state.j = 0

    if "running" not in st.session_state:
        st.session_state.running = False

    # ---------------- USER INPUT ----------------
    st.subheader("Custom Array Input")

    user_input = st.text_input("Enter numbers separated by comma (e.g. 10,20,30)")

    colA, colB = st.columns(2)

    with colA:
        if st.button("Set Custom Array"):
            try:
                arr = list(map(int, user_input.split(",")))
                st.session_state.arr = arr
                st.session_state.i = 0
                st.session_state.j = 0
            except:
                st.warning("Invalid input format")

    with colB:
        if st.button("Reset Default"):
            st.session_state.arr = [50, 20, 40, 10, 30]
            st.session_state.i = 0
            st.session_state.j = 0
            st.session_state.running = False

    arr = st.session_state.arr
    n = len(arr)

    st.markdown("---")

    # ---------------- SPEED CONTROL ----------------
    speed = st.slider("Speed Control (seconds)", 0.1, 1.5, 0.5)

    # ---------------- VISUAL ----------------
    draw_bars(arr, st.session_state.i, st.session_state.j)

    st.markdown("---")

    # ---------------- CONTROLS ----------------
    c1, c2, c3 = st.columns(3)

    with c1:
        if st.button("▶ Play / Pause"):
            st.session_state.running = not st.session_state.running

    with c2:
        if st.button("Step-by-Step"):
            bubble_step(arr)
            st.rerun()

    with c3:
        if st.button("🔄 Reset"):
            st.session_state.arr = [50, 20, 40, 10, 30]
            st.session_state.i = 0
            st.session_state.j = 0
            st.session_state.running = False
            st.rerun()

    st.markdown("---")

    # ---------------- AUTOPLAY ----------------
    if st.session_state.running:

        bubble_step(arr)
        time.sleep(speed)
        st.rerun()

# -----------------------------
# LOGIC ENGINE
# -----------------------------
def bubble_step(arr):

    i = st.session_state.i
    j = st.session_state.j
    n = len(arr)

    if i < n:

        if j < n - i - 1:

            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]

            st.session_state.j += 1

        else:
            st.session_state.i += 1
            st.session_state.j = 0

    st.session_state.arr = arr
    
    
    # CODE
    with st.expander("View C++ Code"):
        st.code("""
#include<iostream>
using namespace std;
void display(int arr[], int sz){
	for (int i=0; i<sz; i++){
		cout<<arr[i]<<" ";
	}
	cout<<endl;
}
void bubblesort(int arr[], int sz){
	int swap=0;
	for(int i=0; i<sz-1; i++){
		for(int j=0; j<sz-i-1; j++){
			if(arr[j]>arr[j+1]){
				int temp=arr[j];
				arr[j]=arr[j+1];
				arr[j+1]=temp;
				swap++;
			}
		}
		cout<<"After iteration"<<i<<": ";
		display(arr,sz );
	}
			cout<<"Total swapping "<<swap<<endl;
}
int main(){
	int size=6;
	int arr[size]={9,3,1,6,2,4};
	cout<<"Before Sort: ";
	display(arr,size);
	bubblesort(arr,size);
	cout<<"After Sort: ";
	display(arr,size);
}
        """)