import streamlit as st
import time

st.set_page_config(page_title="DSA Learning (Python Version)", layout="centered")

st.title("DSA Learning Platform (Python Conversion)")

menu = st.sidebar.selectbox(
    "Choose Module",
    ["Home", "Bubble Sort", "Selection Sort", "Insertion Sort"]
)

# ---------------- HOME ----------------
if menu == "Home":
    st.header("Welcome to DSA Learning Platform")
    st.write("Converted version in Python (Streamlit)")
    st.write("Select an algorithm from sidebar")

# ---------------- BUBBLE SORT ----------------
elif menu == "Bubble Sort":
    st.header("Bubble Sort Visualization")

    inp = st.text_input("Enter numbers (comma separated)", "5,3,8,1,2")

    if st.button("Start Bubble Sort"):
        arr = list(map(int, inp.split(",")))
        st.write("Initial Array:", arr)

        n = len(arr)

        for i in range(n):
            for j in range(n - i - 1):
                st.write(f"Comparing {arr[j]} and {arr[j+1]}")
                time.sleep(0.5)

                if arr[j] > arr[j + 1]:
                    arr[j], arr[j + 1] = arr[j + 1], arr[j]
                    st.write("Swapped →", arr)
                    time.sleep(0.5)

        st.success("Sorted Array")
        st.write(arr)

# ---------------- SELECTION SORT ----------------
elif menu == "Selection Sort":
    st.header("Selection Sort Visualization")

    inp = st.text_input("Enter numbers (comma separated)", "64,25,12,22,11")

    if st.button("Start Selection Sort"):
        arr = list(map(int, inp.split(",")))
        st.write("Initial Array:", arr)

        n = len(arr)

        for i in range(n):
            min_idx = i

            for j in range(i + 1, n):
                st.write(f"Comparing {arr[j]} and {arr[min_idx]}")
                time.sleep(0.5)

                if arr[j] < arr[min_idx]:
                    min_idx = j

            arr[i], arr[min_idx] = arr[min_idx], arr[i]
            st.write("Swapped →", arr)
            time.sleep(0.5)

        st.success("Sorted Array")
        st.write(arr)

# ---------------- INSERTION SORT ----------------
elif menu == "Insertion Sort":
    st.header("Insertion Sort Visualization")

    inp = st.text_input("Enter numbers (comma separated)", "9,5,1,4,3")

    if st.button("Start Insertion Sort"):
        arr = list(map(int, inp.split(",")))
        st.write("Initial Array:", arr)

        for i in range(1, len(arr)):
            key = arr[i]
            j = i - 1

            st.write(f"Key = {key}")

            while j >= 0 and arr[j] > key:
                st.write(f"Shifting {arr[j]} → right")
                arr[j + 1] = arr[j]
                j -= 1
                time.sleep(0.5)

            arr[j + 1] = key
            st.write("Inserted →", arr)
            time.sleep(0.5)

        st.success("Sorted Array")
        st.write(arr)