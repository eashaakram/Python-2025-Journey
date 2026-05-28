import streamlit as st
import graphviz

from my_pages.utils import home_button

st.markdown("---")
# =========================================
# COLORS (same modern theme as BST)
# =========================================
BG = "#121826"
NODE = "#1F2A44"
NODE_BORDER = "#00BFFF"

LEFT = "#00E676"
RIGHT = "#FFB74D"

TEXT = "#E6EDF3"


# =========================================
# NODE CLASS (AVL = HEIGHT INCLUDED)
# =========================================
class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None
        self.height = 1


# =========================================
# HEIGHT + BALANCE FACTOR
# =========================================
def height(node):
    if not node:
        return 0
    return node.height


def balance_factor(node):
    if not node:
        return 0
    return height(node.left) - height(node.right)


# =========================================
# ROTATIONS
# =========================================
def right_rotate(y):
    x = y.left
    T2 = x.right

    x.right = y
    y.left = T2

    y.height = 1 + max(height(y.left), height(y.right))
    x.height = 1 + max(height(x.left), height(x.right))

    return x


def left_rotate(x):
    y = x.right
    T2 = y.left

    y.left = x
    x.right = T2

    x.height = 1 + max(height(x.left), height(x.right))
    y.height = 1 + max(height(y.left), height(y.right))

    return y


# =========================================
# AVL INSERT
# =========================================
def insert(root, val):

    if not root:
        return Node(val)

    if val < root.val:
        root.left = insert(root.left, val)
    else:
        root.right = insert(root.right, val)

    # update height
    root.height = 1 + max(height(root.left), height(root.right))

    bf = balance_factor(root)

    # LL
    if bf > 1 and val < root.left.val:
        return right_rotate(root)

    # RR
    if bf < -1 and val > root.right.val:
        return left_rotate(root)

    # LR
    if bf > 1 and val > root.left.val:
        root.left = left_rotate(root.left)
        return right_rotate(root)

    # RL
    if bf < -1 and val < root.right.val:
        root.right = right_rotate(root.right)
        return left_rotate(root)

    return root


# =========================================
# GET MIN NODE
# =========================================
def get_min(node):
    while node.left:
        node = node.left
    return node


# =========================================
# AVL DELETE
# =========================================
def delete(root, val):

    if not root:
        return root

    if val < root.val:
        root.left = delete(root.left, val)

    elif val > root.val:
        root.right = delete(root.right, val)

    else:

        # 0 or 1 child
        if not root.left:
            return root.right
        elif not root.right:
            return root.left

        # 2 children
        temp = get_min(root.right)
        root.val = temp.val
        root.right = delete(root.right, temp.val)

    # update height
    root.height = 1 + max(height(root.left), height(root.right))

    bf = balance_factor(root)

    # LL
    if bf > 1 and balance_factor(root.left) >= 0:
        return right_rotate(root)

    # LR
    if bf > 1 and balance_factor(root.left) < 0:
        root.left = left_rotate(root.left)
        return right_rotate(root)

    # RR
    if bf < -1 and balance_factor(root.right) <= 0:
        return left_rotate(root)

    # RL
    if bf < -1 and balance_factor(root.right) > 0:
        root.right = right_rotate(root.right)
        return left_rotate(root)

    return root


# =========================================
# TRAVERSALS
# =========================================
def inorder(root, res):
    if root:
        inorder(root.left, res)
        res.append(root.val)
        inorder(root.right, res)


def preorder(root, res):
    if root:
        res.append(root.val)
        preorder(root.left, res)
        preorder(root.right, res)


def postorder(root, res):
    if root:
        postorder(root.left, res)
        postorder(root.right, res)
        res.append(root.val)


# =========================================
# DRAW AVL TREE (GRAPHVIZ)
# =========================================
def draw_tree(node, graph=None):

    if graph is None:
        graph = graphviz.Digraph()

        graph.attr(
            rankdir='TB',
            bgcolor=BG,
            splines='ortho',
            nodesep='0.6',
            ranksep='0.9'
        )

        graph.attr('node',
            shape='circle',
            style='filled',
            fillcolor=NODE,
            color=NODE_BORDER,
            fontcolor=TEXT,
            fontsize='14',
            width='0.6',
            height='0.6'
        )

    if node:

        node_id = str(id(node))

        graph.node(
            node_id,
            f"{node.val}\nBF:{balance_factor(node)}\nH:{node.height}"
        )

        if node.left:
            left_id = str(id(node.left))
            graph.edge(node_id, left_id, color=LEFT, penwidth='2')
            draw_tree(node.left, graph)

        if node.right:
            right_id = str(id(node.right))
            graph.edge(node_id, right_id, color=RIGHT, penwidth='2')
            draw_tree(node.right, graph)

    return graph


# =========================================
# MAIN STREAMLIT UI
# =========================================
def show_avl():
    home_button()
    st.title("AVL Tree ⚖️ Visualizer")

    if "avl_root" not in st.session_state:
        st.session_state.avl_root = None

    value = st.number_input("Enter Value", step=1)

    col1, col2, col3 = st.columns(3)

    # INSERT
    with col1:
        if st.button("Insert 🌱"):
            st.session_state.avl_root = insert(st.session_state.avl_root, value)
            st.rerun()

    # DELETE
    with col2:
        if st.button("Delete ❌"):
            st.session_state.avl_root = delete(st.session_state.avl_root, value)
            st.rerun()

    # RESET
    with col3:
        if st.button("Reset 🔄"):
            st.session_state.avl_root = None
            st.rerun()

    st.markdown("---")

    # TREE VISUALIZATION
    st.subheader("AVL Tree Visualization")

    if st.session_state.avl_root:
        graph = draw_tree(st.session_state.avl_root)
        st.graphviz_chart(graph)
    else:
        st.info("Tree is empty")

    st.markdown("---")

    # TRAVERSAL
    st.subheader("Traversal Output")

    traversal = st.selectbox(
        "Select Traversal",
        [
            "Inorder (Sorted)",
            "Preorder",
            "Postorder"
        ]
    )

    if st.button("Run Traversal ▶"):

        result = []

        if "Inorder" in traversal:
            inorder(st.session_state.avl_root, result)

        elif "Preorder" in traversal:
            preorder(st.session_state.avl_root, result)

        else:
            postorder(st.session_state.avl_root, result)

        st.success(" → ".join(map(str, result)))

    st.markdown("---")

    # COMPLEXITY
    st.subheader("Time Complexity")

    st.table({
        "Operation": ["Insert", "Delete", "Search", "Traversal"],
        "Complexity": ["O(log n)", "O(log n)", "O(log n)", "O(n)"]
    })

    st.markdown("---")

    # EXPLANATION
    with st.expander("Explanation 📘"):

        st.write("""
AVL Tree is a self-balancing BST.

✔ Balance Factor = Height(Left) - Height(Right)

Allowed range: -1, 0, +1

If imbalance happens:
→ Rotations fix the tree automatically

Cases:
1. LL → Right Rotation
2. RR → Left Rotation
3. LR → Left + Right
4. RL → Right + Left
        """)

    # C++ CODE
    with st.expander("C++ Code 💻"):

        st.code("""
struct Node {
    int data;
    Node* left;
    Node* right;
    int height;
};
        """, language="cpp")