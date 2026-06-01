import streamlit as st
import time

from my_pages.utils import home_button

st.markdown("---")

# -----------------------------
# COLORS
# -----------------------------
NORMAL = "#2C3E50"
ACTIVE = "#F39C12"
FOUND = "#27AE60"


# -----------------------------
# DRAW ARRAY
# -----------------------------
def draw_array(arr, current=None, found=None):

    cols = st.columns(len(arr))

    for i, val in enumerate(arr):

        color = NORMAL

        if found is not None and i == found:
            color = FOUND
        elif current is not None and i == current:
            color = ACTIVE

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
# MAIN FUNCTION
# -----------------------------
def show_linear_search():
    home_button()
    st.title("Linear Search Visualizer 🔍")

    # ---------------- USER INPUT ARRAY ----------------
    user_input = st.text_input(
        "Enter array (comma separated)",
        "10,25,7,18,30,45"
    )

    arr = [int(x.strip()) for x in user_input.split(",") if x.strip().isdigit()]

    if len(arr) == 0:
        st.warning("Please enter valid array")
        return

    draw_array(arr)

    st.markdown("---")

    # ---------------- TARGET ----------------
    target = st.number_input("Enter Target Value", step=1)

    speed = st.slider("Speed Control", 0.1, 1.5, 0.5)

    col1, col2 = st.columns(2)

    # ---------------- SEARCH ----------------
    with col1:

        if st.button("Start Search"):

            placeholder = st.empty()
            comparisons = 0
            found = None

            for i in range(len(arr)):

                comparisons += 1

                with placeholder.container():
                    draw_array(arr, current=i)
                    st.info(f"Comparing {arr[i]} with {target}")
                    st.write(f"Comparisons: {comparisons}")

                time.sleep(speed)

                if arr[i] == target:
                    found = i

                    with placeholder.container():
                        draw_array(arr, found=i)
                        st.success(f"Found at index {i}")
                        st.write(f"Total comparisons: {comparisons}")

                    break

            if found is None:
                with placeholder.container():
                    st.error("Not Found ❌")
                    st.write(f"Total comparisons: {comparisons}")

    # ---------------- RESET ----------------
    with col2:
        if st.button("Reset"):
            st.rerun()

    # ---------------- COMPLEXITY ----------------
    st.subheader("Time Complexity")
    st.table({
        "Case": ["Best", "Worst", "Average"],
        "Complexity": ["O(1)", "O(n)", "O(n)"]
    })

    # ---------------- C++ CODE ----------------
    with st.expander("View C++ Code"):

        st.code("""
#include<iostream>
using namespace std;

void linearSearch(int arr[], int n, int target) {

    for(int i = 0; i < n; i++) {

        if(arr[i] == target) {
            cout << "Found at index: " << i;
            return;
        }
    }

    cout << "Not found";
}

int main() {

    int arr[] = {10, 25, 7, 18, 30, 45};
    int n = 6;

    linearSearch(arr, n, 30);

    return 0;
}
        """, language="cpp")