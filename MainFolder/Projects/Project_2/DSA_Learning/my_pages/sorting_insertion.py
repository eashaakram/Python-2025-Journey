import streamlit as st
import time

from my_pages.utils import home_button

st.markdown("---")

# -----------------------------
# COLORS
# -----------------------------
BOX = "#2C3E50"
KEY = "#F39C12"
SHIFT = "#3498DB"
SORTED = "#27AE60"


# -----------------------------
# DRAW
# -----------------------------
def draw_bars(arr, key_idx=None, j_idx=None, sorted_upto=0):

    cols = st.columns(len(arr))

    for i, val in enumerate(arr):

        color = BOX

        if i < sorted_upto:
            color = SORTED

        if i == key_idx:
            color = KEY

        if i == j_idx:
            color = SHIFT

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
# MAIN
# -----------------------------
def show_sorting_insertion():
    home_button()
    st.title("Insertion Sort Visualizer 🧠")

    if "arr" not in st.session_state:
        st.session_state.arr = [50, 20, 40, 10, 30]

    if "i" not in st.session_state:
        st.session_state.i = 1

    if "j" not in st.session_state:
        st.session_state.j = 0

    if "key" not in st.session_state:
        st.session_state.key = None

    if "running" not in st.session_state:
        st.session_state.running = False

    arr = st.session_state.arr
    n = len(arr)

    draw_bars(arr, st.session_state.i, st.session_state.j, st.session_state.i)

    st.markdown("---")

    speed = st.slider("Speed", 0.1, 1.5, 0.5)

    col1, col2, col3 = st.columns(3)

    with col1:
        if st.button("▶ Play / Pause"):
            st.session_state.running = not st.session_state.running

    with col2:
        if st.button("Step-by-Step"):
            insertion_step()
            st.rerun()

    with col3:
        if st.button("🔄 Reset"):
            st.session_state.arr = [50, 20, 40, 10, 30]
            st.session_state.i = 1
            st.session_state.j = 0
            st.session_state.running = False
            st.rerun()

    st.markdown("---")

    if st.session_state.running:
        insertion_step()
        time.sleep(speed)
        st.rerun()

    # CODE SECTION (FIXED INDENTATION)
    with st.expander("View C++ Code"):
     st.code("""
#include<iostream>
using namespace std;

void display(int arr[], int n){
    for(int i=0; i<n; i++){
        cout << arr[i] << " ";
    }
    cout << endl;
}

void insertionSort(int arr[], int n){
    int shift = 0;

    for(int i=1; i<n; i++){
        int key = arr[i];
        int j = i-1;

        while(j >= 0 && arr[j] > key){
            arr[j+1] = arr[j];
            j--;
            shift++;
        }

        arr[j+1] = key;

        cout << "After iteration " << i << ": ";
        display(arr, n);
    }

    cout << "Total shifts: " << shift << endl;
}

int main(){
    int arr[5] = {42,17,33,8,29};
    int size = 5;

    cout << "Before Array: ";
    display(arr, size);

    insertionSort(arr, size);

    cout << "After Array: ";
    display(arr, size);

    return 0;
}
    """, language="cpp")


# -----------------------------
# LOGIC
# -----------------------------
def insertion_step():

    arr = st.session_state.arr
    i = st.session_state.i
    j = st.session_state.j

    n = len(arr)

    if i < n:

        key = arr[i]
        j = i - 1

        while j >= 0 and arr[j] > key:
            arr[j + 1] = arr[j]
            j -= 1
            break

        arr[j + 1] = key

        st.session_state.i += 1
        st.session_state.arr = arr