import streamlit as st

def show_login():
    # Hide unwanted lines and customize button styles
    st.html("<style>hr { display: none !important; } button p { font-weight: bold; }</style>")
    
    st.markdown("<h2 style='text-align:center; color:#00BFFF;'>Welcome Back 🔐</h2>", unsafe_allow_html=True)
    st.markdown("<p style='text-align:center; color:#CCCCCC;'>Enter your credentials to access the visualizer</p>", unsafe_allow_html=True)
    
    login_identity = st.text_input("Email or Username")
    login_password = st.text_input("Password", type="password")
    
    st.write("")
    if st.button("Log In 🚀", use_container_width=True):
        if not (login_identity and login_password):
            st.error("Please enter both your Email/Username and Password!")
        else:
            st.success("Login Successful!")
            st.session_state.page = "home"  # Redirect to main dashboard (home in app.py)
            st.rerun()
            
    st.write("")
    if st.button("Don't have an account? Create an Account", use_container_width=True):
        # UPDATED: Routing state secure ki hai taaki direct signup file open ho
        st.session_state.page = "auth"
        st.session_state.auth_page = "signup"
        st.rerun()