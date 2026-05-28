import streamlit as st

def show_welcome():
    # Hide unwanted lines
    st.html("<style>hr { display: none !important; } button p { font-weight: bold; }</style>")

    # 1. Title
    st.markdown("<h1 style='text-align:center; font-size:50px; color:#00BFFF; font-weight:800; margin-bottom:0;'>DSA Visualizer 🚀</h1>", unsafe_allow_html=True)
    st.markdown("<p style='text-align:center; color:#CCCCCC; font-size:18px; margin-top:5px; margin-bottom:30px;'>Learn Data Structures & Algorithms visually step-by-step.</p>", unsafe_allow_html=True)
    
    # 2. Short About Section
    intro_html = """
    <div style="background-color:#1E1E1E; padding:15px 20px; border-radius:10px; border: 1px solid #2d2d2d; max-width:800px; margin:0 auto 30px auto; text-align:center;">
        <p style="color:#FFFFFF; font-size:15px; margin:0; line-height:1.5;">
            <b>What is this website?</b><br>
            This platform animates dry code into real-time visuals. Watch how data structures move, change, and sort instantly.
        </p>
    </div>
    """
    st.markdown(intro_html, unsafe_allow_html=True)

    # 3. Short 3-Column Features Grid
    col_feat1, col_feat2, col_feat3 = st.columns(3)
    
    with col_feat1:
        st.markdown(
            """
            <div style="background-color:#161616; padding:15px; border-radius:8px; height:120px; text-align:center; border: 1px solid #2d2d2d; border-top: 4px solid #FF4B4B;">
                <h5 style="color:#FF4B4B; margin:0 0 5px 0; font-size:15px;">Sorting & Searching</h5>
                <p style="color:#AAAAAA; font-size:12.5px; margin:0;">Animate Bubble Sort, Merge Sort, and Binary Search live.</p>
            </div>
            """, unsafe_allow_html=True
        )

    with col_feat2:
        st.markdown(
            """
            <div style="background-color:#161616; padding:15px; border-radius:8px; height:120px; text-align:center; border: 1px solid #2d2d2d; border-top: 4px solid #00D2C4;">
                <h5 style="color:#00D2C4; margin:0 0 5px 0; font-size:15px;">Data Structures</h5>
                <p style="color:#AAAAAA; font-size:12.5px; margin:0;">See Linked Lists, Stacks, and Queues add or remove elements.</p>
            </div>
            """, unsafe_allow_html=True
        )

    with col_feat3:
        st.markdown(
            """
            <div style="background-color:#161616; padding:15px; border-radius:8px; height:120px; text-align:center; border: 1px solid #2d2d2d; border-top: 4px solid #FFD700;">
                <h5 style="color:#FFD700; margin:0 0 5px 0; font-size:15px;">Advanced Trees</h5>
                <p style="color:#AAAAAA; font-size:12.5px; margin:0;">Visualize Binary Search Trees (BST) and self-balancing AVL Trees.</p>
            </div>
            """, unsafe_allow_html=True
        )

    st.markdown("<div style='margin-bottom: 30px;'></div>", unsafe_allow_html=True)

   # 4. Action Button (UPDATED)
    col1, col2, col3 = st.columns([1.3, 1.4, 1.3])
    with col2:
        if st.button("Let's Start Learning 🔥", use_container_width=True):
            # Page state ko 'auth' par set karein taaki app.py routing active ho jaye
            st.session_state.page = "auth"
            
            # Pehla page hamesha Login dikhayein
            st.session_state.auth_page = "login"
            
            # Screen refresh karein
            st.rerun()