import streamlit as st

def show_welcome():
    # Hide unwanted lines and customize button with your specific solid blue and glow
    st.html("""
    <style>
    hr { display: none !important; } 
    button p { font-weight: bold; }
    
    /* Target only the main welcome action button using its text selector */
    div.stButton > button {
        background-color: #0055ff !important; /* Aapka perfect solid blue */
        color: white !important; /* Solid white text */
        font-size: 18px !important;
        font-weight: bold !important;
        padding: 12px 30px !important;
        border-radius: 12px !important; /* Perfectly rounded edges */
        border: none !important;
        box-shadow: 0 0 15px rgba(0, 85, 255, 0.6) !important; /* Blue glow effect */
        transition: all 0.2s ease-in-out;
    }
    
    /* Hover state for the blue glowing button */
    div.stButton > button:hover {
        background-color: #0044cc !important;
        box-shadow: 0 0 25px rgba(0, 85, 255, 0.9) !important;
    }
    </style>
    """)

    # 1. Title 
    st.markdown("<h1 style='text-align:center; font-size:50px; color:#00BFFF; font-weight:800; margin-bottom:0;'>DSA Visualizer</h1>", unsafe_allow_html=True)
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

    # 3. Short 3-Column Features Grid (All top borders unified to #00BFFF)
    col_feat1, col_feat2, col_feat3 = st.columns(3)
    
    with col_feat1:
        st.markdown(
            """
            <div style="background-color:#161616; padding:15px; border-radius:8px; height:120px; text-align:center; border: 1px solid #2d2d2d; border-top: 4px solid #00BFFF;">
                <h5 style="color:#00BFFF; margin:0 0 5px 0; font-size:15px;">Sorting & Searching</h5>
                <p style="color:#AAAAAA; font-size:12.5px; margin:0;">Animate Bubble Sort, Merge Sort, and Binary Search live.</p>
            </div>
            """, unsafe_allow_html=True
        )

    with col_feat2:
        st.markdown(
            """
            <div style="background-color:#161616; padding:15px; border-radius:8px; height:120px; text-align:center; border: 1px solid #2d2d2d; border-top: 4px solid #00BFFF;">
                <h5 style="color:#00BFFF; margin:0 0 5px 0; font-size:15px;">Data Structures</h5>
                <p style="color:#AAAAAA; font-size:12.5px; margin:0;">See Linked Lists, and Queues add or remove elements.</p>
            </div>
            """, unsafe_allow_html=True
        )

    with col_feat3:
        st.markdown(
            """
            <div style="background-color:#161616; padding:15px; border-radius:8px; height:120px; text-align:center; border: 1px solid #2d2d2d; border-top: 4px solid #00BFFF;">
                <h5 style="color:#00BFFF; margin:0 0 5px 0; font-size:15px;">Advanced Trees</h5>
                <p style="color:#AAAAAA; font-size:12.5px; margin:0;">Visualize Binary Search Trees (BST) and self-balancing AVL Trees.</p>
            </div>
            """, unsafe_allow_html=True
        )

    st.markdown("<div style='margin-bottom: 30px;'></div>", unsafe_allow_html=True)

    # 4. Action Button 
    col1, col2, col3 = st.columns([1.3, 1.4, 1.3])
    with col2:
        if st.button("Let's Start Learning 🔥", use_container_width=True):
            # Page state ko auth par set kia ha taaki app.py routing active ho jaye
            st.session_state.page = "auth"
            
            # first login pg will appear 
            st.session_state.auth_page = "login"
            
            # Refresh screen 
            st.rerun()