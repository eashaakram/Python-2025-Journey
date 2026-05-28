import streamlit as st

from my_pages.utils import home_button

st.markdown("---")

# -----------------------------
# DRAW STACK
# -----------------------------
def draw_stack(stack):

    st.subheader("Stack (Top → Bottom)")

    if len(stack) == 0:
        st.warning("Stack is empty")
        return

    # reverse for visual (top on top)
    for i in range(len(stack)-1, -1, -1):

        value = stack[i]

        if i == len(stack) - 1:
            st.markdown("👉 TOP")

        st.markdown(
            f"""
            <div style="
                border:2px solid #00FFFF;
                padding:15px;
                margin:5px;
                text-align:center;
                border-radius:10px;
                background-color:#1E1E1E;
                color:white;
                font-size:22px;
            ">
                {value}
            </div>
            """,
            unsafe_allow_html=True
        )


# -----------------------------
# MAIN STACK PAGE
# -----------------------------
def show_stack():
    home_button()
    st.title("Stack Visualization 📚")

    # initialize stack
    if "stack" not in st.session_state:
        st.session_state.stack = []

    draw_stack(st.session_state.stack)

    st.markdown("---")

    # ---------------- PUSH ----------------
    value = st.number_input("Enter Value", step=1, key="stack_push")

    if st.button("Push"):
        st.session_state.stack.append(value)
        st.rerun()

    # ---------------- POP ----------------
    if st.button("Pop"):
        if len(st.session_state.stack) > 0:
            st.session_state.stack.pop()
            st.rerun()
        else:
            st.warning("Stack already empty")

    st.markdown("---")

    # ---------------- COMPLEXITY ----------------
    st.subheader("Time Complexity")

    st.table({
        "Operation": ["Push", "Pop", "Peek"],
        "Complexity": ["O(1)", "O(1)", "O(1)"]
    })

    st.markdown("---")

    # ---------------- CODE VIEW ----------------
    with st.expander("View C++ Code"):
        st.code("""
#include <iostream>
using namespace std;

class Stack {
    int top, maxsize;
    int* stack;

public:
    Stack(int size) {
        top = -1;
        maxsize = size;
        stack = new int[maxsize];
    }

    bool isEmpty() { return top == -1; }
    bool isFull() { return top == maxsize - 1; }

    void push(int x) {
        if (isFull()) cout << "Overflow\n";
        else stack[++top] = x;
    }

    void pop() {
        if (isEmpty()) cout << "Underflow\n";
        else top--;
    }

    void peek() {
        if (!isEmpty()) cout << "Top: " << stack[top] << endl;
    }

    void display() {
        for (int i = top; i >= 0; i--)
            cout << stack[i] << " ";
        cout << endl;
    }

    ~Stack() { delete[] stack; }
};

int main() {
    Stack s(5);

    s.push(10);
    s.push(20);
    s.push(30);

    s.display();
    s.peek();

    s.pop();
    s.display();

    return 0;
}
        """)