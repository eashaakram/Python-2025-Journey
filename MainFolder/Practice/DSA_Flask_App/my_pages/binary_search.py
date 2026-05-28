import streamlit as st
import time

from my_pages.utils import home_button

st.markdown("---")
# -----------------------------
# COLORS
# -----------------------------
NORMAL = "#2C3E50"
MID = "#F39C12"
FOUND = "#27AE60"
RANGE = "#3498DB"


# -----------------------------
# DRAW ARRAY
# -----------------------------
def draw_array(arr, low=None, mid=None, high=None, found=None):

    cols = st.columns(len(arr))

    for i, val in enumerate(arr):

        color = NORMAL

        if found is not None and i == found:
            color = FOUND

        elif i == mid:
            color = MID

        elif low is not None and high is not None and low <= i <= high:
            color = RANGE

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
                    font-size:20px;
                    font-weight:bold;
                ">
                    {val}
                </div>
                """,
                unsafe_allow_html=True
            )

            st.caption(f"Index {i}")


# -----------------------------
# MAIN
# -----------------------------
def show_binary_search():
    home_button()
    st.title("Binary Search Visualizer 🔍⚡")

    # ---------------- USER INPUT ARRAY ----------------
    user_input = st.text_input(
        "Enter sorted array (comma separated)",
        "5,10,15,20,25,30,40"
    )

    arr = [int(x.strip()) for x in user_input.split(",") if x.strip().isdigit()]

    if len(arr) == 0:
        st.warning("Enter valid array")
        return

    # AUTO SORT (important safety feature)
    arr.sort()

    st.info("Binary Search requires sorted array → auto sorted applied")

    draw_array(arr)

    st.markdown("---")

    # ---------------- TARGET ----------------
    target = st.number_input("Enter Target Value", step=1)

    speed = st.slider("Speed Control", 0.1, 1.5, 0.5)

    col1, col2 = st.columns(2)

    # ---------------- SEARCH ----------------
    with col1:

        if st.button("Start Search"):

            low = 0
            high = len(arr) - 1
            comparisons = 0
            found = None

            placeholder = st.empty()

            while low <= high:

                mid = (low + high) // 2
                comparisons += 1

                with placeholder.container():

                    draw_array(arr, low, mid, high)

                    st.write(f"Low={low}, Mid={mid}, High={high}")
                    st.info(f"Comparing {arr[mid]} with {target}")
                    st.write(f"Comparisons: {comparisons}")

                    # 🔥 EXPLANATION PANEL (IMPORTANT IMPROVEMENT)
                    if arr[mid] > target:
                        st.warning("Target is smaller → moving LEFT half")
                    elif arr[mid] < target:
                        st.warning("Target is larger → moving RIGHT half")
                    else:
                        st.success("Match found!")

                time.sleep(speed)

                if arr[mid] == target:
                    found = mid

                    with placeholder.container():
                        draw_array(arr, low, mid, high, found)
                        st.success(f"Found at index {mid}")
                        st.write(f"Total comparisons: {comparisons}")

                    break

                elif arr[mid] < target:
                    low = mid + 1
                else:
                    high = mid - 1

            if found is None:
                with placeholder.container():
                    st.error("Not Found ❌")
                    st.write(f"Comparisons: {comparisons}")

    # ---------------- RESET ----------------
    with col2:
        if st.button("Reset"):
            st.rerun()

    # ---------------- COMPLEXITY ----------------
    st.subheader("Time Complexity")
    st.table({
        "Case": ["Best", "Worst", "Average"],
        "Complexity": ["O(1)", "O(log n)", "O(log n)"]
    })

    # -----------------------------
    # EXPLANATION
    # -----------------------------
    with st.expander("Explanation"):

        st.write("""
Binary Search works by repeatedly dividing the search range in half.

Steps:
1. Find middle element
2. Compare with target
3. Eliminate half array
4. Repeat

Only works on sorted arrays.
        """)

    # -----------------------------
    # C++ CODE
    # -----------------------------
    with st.expander("View C++ Code"):

        st.code("""
#include<iostream>
using namespace std;

void binarySearch(int arr[], int n, int target) {

    int low = 0;
    int high = n - 1;
    int comparisons = 0;

    while(low <= high) {

        int mid = (low + high) / 2;
        comparisons++;

        if(arr[mid] == target) {

            cout << "Found at index: " << mid << endl;
            cout << "Comparisons: " << comparisons << endl;
            return;
        }

        else if(arr[mid] < target) {
            low = mid + 1;
        }

        else {
            high = mid - 1;
        }
    }

    cout << "Element not found" << endl;
    cout << "Comparisons: " << comparisons << endl;
}

int main() {

    int arr[] = {5, 10, 15, 20, 25, 30, 40};
    int n = 7;
    int target;

    cout << "Enter target: ";
    cin >> target;

    binarySearch(arr, n, target);

    return 0;
}
        """, language="cpp")