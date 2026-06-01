import streamlit as st

from my_pages.utils import home_button

st.markdown("---")

# -----------------------------
# DRAW QUEUE (IMPROVED)
# -----------------------------
def draw_queue(queue):

    st.subheader("Queue Visualization (Front → Rear)")

    if not queue or len(queue) == 0:
        st.warning("Queue is empty")
        return

    cols = st.columns(len(queue))

    for i, value in enumerate(queue):

        with cols[i]:

            # FRONT label
            if i == 0:
                st.markdown("⬅ FRONT")

            # REAR label
            if i == len(queue) - 1:
                st.markdown("REAR ➡")

            # BOX DESIGN
            st.markdown(
                f"""
                <div style="
                    border:2px solid #00FFFF;
                    padding:18px;
                    text-align:center;
                    border-radius:12px;
                    background-color:{'#00FF99' if i == 0 else '#1E1E1E'};
                    color:white;
                    font-size:22px;
                    font-weight:bold;
                ">
                    {value}
                </div>
                """,
                unsafe_allow_html=True
            )

            st.caption(f"Index {i}")


# -----------------------------
# MAIN PAGE
# -----------------------------
def show_simple_queue():
    home_button()
    st.title("Queue Data Structure Visualizer")

    # INIT
    if "queue" not in st.session_state:
        st.session_state.queue = []

    # DISPLAY QUEUE
    draw_queue(st.session_state.queue)

    st.markdown("---")

    # ---------------- ENQUEUE ----------------
    st.subheader("Insert (Enqueue)")

    value = st.number_input("Enter Value", step=1, key="enqueue_value")

    if st.button("Enqueue"):
        st.session_state.queue.append(value)
        st.rerun()

    # ---------------- DEQUEUE ----------------
    st.subheader("Delete (Dequeue)")

    if st.button("Dequeue"):
        if len(st.session_state.queue) > 0:
            st.session_state.queue.pop(0)
            st.rerun()
        else:
            st.warning("Queue is already empty")

    st.markdown("---")

    # ---------------- COMPLEXITY ----------------
    st.subheader("Time Complexity")

    st.table({
        "Operation": ["Enqueue", "Dequeue", "Peek"],
        "Complexity": ["O(1)", "O(n)", "O(1)"]
    })

    st.markdown("---")

    # ---------------- CODE VIEW ----------------
    with st.expander("View C++ Code (Simple Queue)"):

      st.code("""
#include<iostream>
using namespace std;

class Queue{

    int arr[5];
    int front;
    int rear;

public:

    Queue(){
        front = -1;
        rear = -1;
    }

    void enqueue(int value){

        if(rear == 4){
            cout << "Queue Overflow";
            return;
        }

        if(front == -1){
            front = 0;
        }

        rear++;
        arr[rear] = value;
    }

    void dequeue(){

        if(front == -1 || front > rear){
            cout << "Queue Underflow";
            return;
        }

        cout << arr[front] << " removed" << endl;
        front++;
    }

    void display(){

        if(front == -1 || front > rear){
            cout << "Queue Empty";
            return;
        }

        for(int i=front; i<=rear; i++){
            cout << arr[i] << " ";
        }

        cout << endl;
    }
};

int main(){

    Queue q;

    q.enqueue(10);
    q.enqueue(20);
    q.enqueue(30);

    q.display();

    q.dequeue();

    q.display();
}
    """, language="cpp")