import streamlit as st

from my_pages.utils import home_button

st.markdown("---")

# -----------------------------
# COLORS
# -----------------------------
BOX = "#2C3E50"
FRONT = "#27AE60"
REAR = "#E67E22"


# -----------------------------
# DRAW QUEUE
# -----------------------------
def draw_circular_queue(queue, front, rear):

    st.subheader("Circular Queue Visualization")

    cols = st.columns(len(queue))

    for i, val in enumerate(queue):

        color = BOX

        # FRONT POINTER
        if i == front:
            color = FRONT

        # REAR POINTER
        elif i == rear:
            color = REAR

        with cols[i]:

            # FRONT LABEL
            if i == front:
                st.markdown("### FRONT")

            # REAR LABEL
            if i == rear:
                st.markdown("### REAR")

            st.markdown(
                f"""
                <div style="
                    height:80px;
                    display:flex;
                    align-items:center;
                    justify-content:center;
                    background-color:{color};
                    color:white;
                    border-radius:12px;
                    font-size:22px;
                    font-weight:bold;
                    box-shadow:0px 4px 10px rgba(0,0,0,0.3);
                ">
                    {val if val is not None else ""}
                </div>
                """,
                unsafe_allow_html=True
            )

            st.caption(f"Index {i}")


# -----------------------------
# MAIN FUNCTION
# -----------------------------
def show_circular_queue():
    home_button()
    st.title("Circular Queue 🔄")

    # -----------------------------
    # CREATE QUEUE FIRST
    # -----------------------------
    if "cq_created" not in st.session_state:
        st.session_state.cq_created = False

    # -----------------------------
    # SIZE INPUT
    # -----------------------------
    if not st.session_state.cq_created:

        size = st.number_input(
            "Enter Queue Size",
            min_value=3,
            max_value=20,
            step=1
        )

        if st.button("Create Circular Queue"):

            st.session_state.cq_size = size
            st.session_state.cq = [None] * size
            st.session_state.front = -1
            st.session_state.rear = -1
            st.session_state.cq_created = True

            st.rerun()

        return

    # -----------------------------
    # LOAD VALUES
    # -----------------------------
    size = st.session_state.cq_size
    queue = st.session_state.cq
    front = st.session_state.front
    rear = st.session_state.rear

    # -----------------------------
    # SHOW SIZE
    # -----------------------------
    st.info(f"Fixed Queue Size: {size}")

    # -----------------------------
    # VISUALIZATION
    # -----------------------------
    draw_circular_queue(queue, front, rear)

    st.markdown("---")

    # -----------------------------
    # INPUT
    # -----------------------------
    value = st.number_input(
        "Enter Value",
        step=1,
        key="cq_input"
    )

    col1, col2, col3 = st.columns(3)

    # -----------------------------
    # ENQUEUE
    # -----------------------------
    with col1:

        if st.button("Enqueue"):

            # OVERFLOW
            if (rear + 1) % size == front:

                st.error("Queue Overflow ❌")

            else:

                # FIRST ELEMENT
                if front == -1:
                    front = 0
                    rear = 0

                else:
                    rear = (rear + 1) % size

                queue[rear] = value

                st.session_state.front = front
                st.session_state.rear = rear
                st.session_state.cq = queue

                st.success(f"{value} inserted")

                st.rerun()

    # -----------------------------
    # DEQUEUE
    # -----------------------------
    with col2:

        if st.button("Dequeue"):

            # UNDERFLOW
            if front == -1:

                st.error("Queue Underflow ❌")

            else:

                removed = queue[front]

                queue[front] = None

                # LAST ELEMENT
                if front == rear:

                    front = -1
                    rear = -1

                else:

                    front = (front + 1) % size

                st.session_state.front = front
                st.session_state.rear = rear
                st.session_state.cq = queue

                st.success(f"{removed} removed")

                st.rerun()

    # -----------------------------
    # RESET
    # -----------------------------
    with col3:

        if st.button("Reset Queue"):

            st.session_state.cq_created = False

            del st.session_state.cq
            del st.session_state.front
            del st.session_state.rear
            del st.session_state.cq_size

            st.rerun()

    st.markdown("---")

    # -----------------------------
    # COMPLEXITY
    # -----------------------------
    st.subheader("Time Complexity")

    st.table({
        "Operation": ["Enqueue", "Dequeue", "Peek"],
        "Complexity": ["O(1)", "O(1)", "O(1)"]
    })

    st.markdown("---")

    # -----------------------------
    # THEORY
    # -----------------------------
    with st.expander("Circular Queue Theory"):

        st.write("""
### Circular Queue

A Circular Queue connects the last position back to the first position.

It avoids memory wastage that happens in a normal queue.

Operations:
- Enqueue → Insert element
- Dequeue → Remove element

Pointers:
- Front
- Rear

Formula:
(rear + 1) % size
        """)

    # -----------------------------
    # C++ CODE
    # -----------------------------
    with st.expander("View C++ Code"):

        st.code("""
#include<iostream>
using namespace std;

class CircularQueue {

    int* arr;
    int front;
    int rear;
    int size;

public:

    CircularQueue(int s) {

        size = s;
        arr = new int[size];

        front = -1;
        rear = -1;
    }

    void enqueue(int value) {

        // Overflow
        if((rear + 1) % size == front) {

            cout << "Queue Overflow" << endl;
            return;
        }

        // First element
        if(front == -1) {

            front = 0;
            rear = 0;
        }

        else {

            rear = (rear + 1) % size;
        }

        arr[rear] = value;

        cout << value << " inserted" << endl;
    }

    void dequeue() {

        // Underflow
        if(front == -1) {

            cout << "Queue Underflow" << endl;
            return;
        }

        cout << arr[front] << " removed" << endl;

        // Last element
        if(front == rear) {

            front = -1;
            rear = -1;
        }

        else {

            front = (front + 1) % size;
        }
    }

    void display() {

        if(front == -1) {

            cout << "Queue Empty" << endl;
            return;
        }

        int i = front;

        while(true) {

            cout << arr[i] << " ";

            if(i == rear)
                break;

            i = (i + 1) % size;
        }

        cout << endl;
    }
};

int main() {

    int size;

    cout << "Enter Queue Size: ";
    cin >> size;

    CircularQueue q(size);

    q.enqueue(10);
    q.enqueue(20);
    q.enqueue(30);

    q.display();

    q.dequeue();

    q.display();

    return 0;
}
        """, language="cpp")