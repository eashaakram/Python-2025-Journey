import streamlit as st

def home_button():
    # Sirf isi specific button ko solid blue block banani ki minimal CSS
    st.markdown("""
        <style>
        div.stButton > button:first-child {
            background-color: #0055ff !important; /* Aapka pasandeda perfect solid blue */
            color: white !important; /* Solid text color */
            font-size: 18px !important;
            font-weight: bold !important;
            padding: 12px 30px !important;
            border-radius: 12px !important; /* Perfect rounded button edges */
            border: none !important;
            box-shadow: 0 0 15px rgba(0, 85, 255, 0.6) !important; /* Blue light glow effect */
            transition: all 0.2s ease;
            width: auto;
        }
        /* Hover karne par halka sa effect */
        div.stButton > button:first-child:hover {
            background-color: #0044cc !important;
            box-shadow: 0 0 25px rgba(0, 85, 255, 0.9) !important;
        }
        </style>
    """, unsafe_allow_html=True)

    # Simple clean structure
    if st.button("⬅ Back To Menu"):
        st.session_state.page = "home"
        st.rerun()