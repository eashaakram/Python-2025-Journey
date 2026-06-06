import streamlit as st
import graphviz

from my_pages.utils import home_button

st.markdown("---")
# =========================================
# COLORS
# =========================================
BG = "#121826"        # dark aur modern background
NODE = "#1F2A44"      # dark blue-gray node (clean look)
NODE_BORDER = "#00BFFF"  # cyan border highlight

LEFT = "#00E676"      # soft green (left child)
RIGHT = "#FFB74D"     # soft orange (right child)

TEXT = "#E6EDF3"      # soft white text (easy on eyes)
SHADOW = "rgba(0,0,0,0.4)"

# =========================================
# NODE CLASS
# =========================================
class Node:

    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None


# =========================================
# INSERT
# =========================================
def insert(root, val):

    if root is None:
        return Node(val)

    if val < root.val:
        root.left = insert(root.left, val)

    elif val > root.val:
        root.right = insert(root.right, val)

    return root


# =========================================
# FIND MIN
# =========================================
def find_min(node):

    while node.left:
        node = node.left

    return node


# =========================================
# DELETE
# =========================================
def delete(root, val):

    if root is None:
        return root

    if val < root.val:
        root.left = delete(root.left, val)

    elif val > root.val:
        root.right = delete(root.right, val)

    else:

        # CASE 1: NO CHILD
        if root.left is None and root.right is None:
            return None

        # CASE 2: ONE CHILD
        if root.left is None:
            return root.right

        if root.right is None:
            return root.left

        # CASE 3: TWO CHILDREN
        temp = find_min(root.right)

        root.val = temp.val

        root.right = delete(root.right, temp.val)

    return root


# =========================================
# TRAVERSALS
# =========================================
def inorder(root, result):

    if root:

        inorder(root.left, result)

        result.append(root.val)

        inorder(root.right, result)


def preorder(root, result):

    if root:

        result.append(root.val)

        preorder(root.left, result)

        preorder(root.right, result)


def postorder(root, result):

    if root:

        postorder(root.left, result)

        postorder(root.right, result)

        result.append(root.val)


# =========================================
# DRAW TREE
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
            fontname='Arial Bold',
            fontsize='14',
            width='0.6',
            height='0.6'
        )

    if node:

        node_id = str(id(node))   # unique ID

        graph.node(node_id, str(node.val))

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
# MAIN BST UI
# =========================================
def show_bst():
    home_button()
    st.title("BST Visualizer 🌳")

    st.write("Binary Search Tree Operations & Visualization")

    st.markdown("---")

    # =========================================
    # SESSION STATE
    # =========================================
    if "root" not in st.session_state:
        st.session_state.root = None

    root = st.session_state.root

    # =========================================
    # INPUT
    # =========================================
    value = st.number_input(
        "Enter Value",
        step=1
    )

    col1, col2, col3 = st.columns(3)

    # =========================================
    # INSERT
    # =========================================
    with col1:

        if st.button("Insert 🌱", use_container_width=True):

            st.session_state.root = insert(root, value)

            st.success(f"{value} inserted")

            st.rerun()

    # =========================================
    # DELETE
    # =========================================
    with col2:

        if st.button("Delete ❌", use_container_width=True):

            st.session_state.root = delete(root, value)

            st.success(f"{value} deleted")

            st.rerun()

    # =========================================
    # RESET
    # =========================================
    with col3:

        if st.button("Reset 🔄", use_container_width=True):

            st.session_state.root = None

            st.rerun()

    st.markdown("---")

    # =========================================
    # TREE VISUALIZATION
    # =========================================
    st.subheader("Tree Visualization 🌳")

    if st.session_state.root:

        graph = draw_tree(st.session_state.root)

        st.graphviz_chart(graph)

    else:

        st.info("Tree is empty")

    st.markdown("---")

    # =========================================
    # TRAVERSALS
    # =========================================
    st.subheader("Traversal Output")

    traversal = st.selectbox(
        "Select Traversal Type",
        [
    "Inorder (Left → Root → Right)",
    "Preorder (Root → Left → Right)",
    "Postorder (Left → Right → Root)"
        ]
    )

    if st.button("Run Traversal ▶"):

        result = []

        if "Inorder" in traversal:
            inorder(st.session_state.root, result)

        elif "Preorder" in traversal:
            preorder(st.session_state.root, result)

        elif traversal == "Postorder":
            postorder(st.session_state.root, result)

        st.success(" → ".join(map(str, result)))

    st.markdown("---")

    # =========================================
    # COMPLEXITY
    # =========================================
    st.subheader("Time Complexity")

    st.table({
        "Operation": [
            "Insert",
            "Delete",
            "Search",
            "Traversal"
        ],

        "Complexity": [
            "O(log n)",
            "O(log n)",
            "O(log n)",
            "O(n)"
        ]
    })

    st.markdown("---")

    # =========================================
    # EXPLANATION
    # =========================================
    st.subheader("Explanation 📘")

    st.write("""
### Binary Search Tree (BST)

BST is a special binary tree where:

✔ Left child is smaller than Root  
✔ Right child is greater than Root

This rule helps searching become very fast.

---

### Insert Operation 🌱

1. Compare value with root
2. Smaller → move left
3. Greater → move right
4. Insert at empty position

---

### Delete Operation ❌

Deletion has 3 cases:

1️⃣ Leaf Node  
Simply remove node

2️⃣ One Child  
Replace node with child

3️⃣ Two Children  
Replace with inorder successor

---

### Traversals 🔄

✔ Inorder  
Left → Root → Right  
(Gives sorted output in BST)

✔ Preorder  
Root → Left → Right  
(Used to copy tree)

✔ Postorder  
Left → Right → Root  
(Used to delete tree)
""")

    st.markdown("---")

    # =========================================
    # C++ CODE
    # =========================================
    with st.expander("View C++ Code 💻"):

        st.code("""
#include<iostream>
using namespace std;

struct Node{

    int data;
    Node* left;
    Node* right;

    Node(int val){

        data = val;
        left = NULL;
        right = NULL;
    }
};

Node* insert(Node* root, int val){

    if(root == NULL)
        return new Node(val);

    if(val < root->data)
        root->left = insert(root->left, val);

    else if(val > root->data)
        root->right = insert(root->right, val);

    return root;
}
""", language="cpp")