import streamlit as st
import time

from my_pages.utils import home_button

st.markdown("---")

# -----------------------------
# COLORS (PROFESSIONAL)
# -----------------------------
BOX = "#2C3E50"
MIN_COLOR = "#F39C12"
COMPARE = "#5DADE2"
SORTED = "#27AE60"


# -----------------------------
# DRAW ARRAY
# -----------------------------
def draw_bars(arr, min_idx=None, compare_idx=None, sorted_upto=0):

    cols = st.columns(len(arr))

    for i, val in enumerate(arr):

        color = BOX

        if i < sorted_upto:
            color = SORTED

        if i == min_idx:
            color = MIN_COLOR

        if i == compare_idx:
            color = COMPARE

        with cols[i]:
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
                    box-shadow:0px 4px 8px rgba(0,0,0,0.3);
                ">
                    {val}
                </div>
                """,
                unsafe_allow_html=True
            )


# -----------------------------
# MAIN FUNCTION
# -----------------------------
def show_sorting_selection():
    home_button()
    st.title("Selection Sort Visualizer 🎯")

    # INIT
    if "arr" not in st.session_state:
        st.session_state.arr = [42, 17, 33, 8, 29]

    if "i" not in st.session_state:
        st.session_state.i = 0

    if "j" not in st.session_state:
        st.session_state.j = 1

    if "min_idx" not in st.session_state:
        st.session_state.min_idx = 0

    if "running" not in st.session_state:
        st.session_state.running = False

    arr = st.session_state.arr
    n = len(arr)

    # ---------------- UI ----------------
    draw_bars(
        arr,
        st.session_state.min_idx,
        st.session_state.j,
        st.session_state.i
    )

    st.markdown("---")

    speed = st.slider("Speed Control", 0.1, 1.5, 0.5)

    col1, col2, col3 = st.columns(3)

    # PLAY / PAUSE
    with col1:
        if st.button("▶ Play / Pause"):
            st.session_state.running = not st.session_state.running

    # STEP
    with col2:
        if st.button("Step-by-Step"):
            selection_step()
            st.rerun()

    # RESET
    with col3:
        if st.button("🔄 Reset"):
            st.session_state.arr = [42, 17, 33, 8, 29]
            st.session_state.i = 0
            st.session_state.j = 1
            st.session_state.min_idx = 0
            st.session_state.running = False
            st.rerun()

    st.markdown("---")

    # AUTO PLAY
    if st.session_state.running:
        selection_step()
        time.sleep(speed)
        st.rerun()

    # CODE VIEW
    with st.expander("View Code (C++)"):
        st.code("""
#include<iostream>
using namespace std;
void display(int arr[], int sz){
	for (int i=0; i<sz; i++){
		cout<<arr[i]<<" ";
	}
	cout<<endl;
}
void selectionsort(int arr[],int sz){
	int swapping=0;
	for(int i=0; i<sz-1; i++){
		int minIndex=i;
		for(int j=i+1; j<sz; j++){
			if(arr[j]<arr[minIndex]){
				minIndex=j;
			}
		}
		if(minIndex!=i){
			int temp=arr[i];
			arr[i]=arr[minIndex];
			arr[minIndex]=temp;
			swapping++;
		}
	}

	cout<<"Total Swap: "<<swapping<<endl;
}
int main(){
	int size=6;
	int arr[size]={9,3,1,6,2,4};
	cout<<"Before Sort: ";
	display(arr,size);
	selectionsort(arr,size);
		cout<<"After Sort: ";
	display(arr,size);
}
        """, language="cpp")


# -----------------------------
# LOGIC ENGINE
# -----------------------------
def selection_step():

    arr = st.session_state.arr
    i = st.session_state.i
    j = st.session_state.j
    min_idx = st.session_state.min_idx

    n = len(arr)

    if i < n:

        if j < n:

            if arr[j] < arr[min_idx]:
                st.session_state.min_idx = j

            st.session_state.j += 1

        else:
            # swap minimum with current i
            arr[i], arr[min_idx] = arr[min_idx], arr[i]

            st.session_state.i += 1
            st.session_state.j = st.session_state.i + 1
            st.session_state.min_idx = st.session_state.i

    st.session_state.arr = arr