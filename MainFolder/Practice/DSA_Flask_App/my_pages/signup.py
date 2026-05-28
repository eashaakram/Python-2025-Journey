import streamlit as st
from datetime import date

def show_signup():
    st.html("<style>hr { display: none !important; } button p { font-weight: bold; }</style>")
    
    st.markdown("<h2 style='text-align:center; color:#00BFFF;'>Create An Account 👤</h2>", unsafe_allow_html=True)
    st.markdown("<p style='text-align:center; color:#CCCCCC;'>Please fill in your details to register</p>", unsafe_allow_html=True)
    
    # Pure inputs ko ek Form ke andar wrap kar diya taaki data miss na ho
    with st.form("signup_form", clear_on_submit=False):
        full_name = st.text_input("Full Name")
        username = st.text_input("Username")
        email = st.text_input("Email Address")
        phone = st.text_input("Phone Number (e.g., 03XXXXXXXXX)", max_chars=11)
        cnic = st.text_input("CNIC Number (13 digits without dashes)", max_chars=13)
        dob = st.date_input("Date of Birth", min_value=date(1950, 1, 1), max_value=date.today())
        password = st.text_input("Password", type="password")
        
        st.write("")
        # Form ka apna submission button
        submit_button = st.form_submit_button("Sign Up 🔥", use_container_width=True)

    # Validation logic checks inside form submission
    if submit_button:
        # Strip whitespace to ensure empty spaces aren't counted as filled fields
        if not (full_name.strip() and username.strip() and email.strip() and phone.strip() and cnic.strip() and password.strip()):
            st.error("Please fill out all the fields before submitting!")
        
        elif not (phone.startswith("03") and len(phone) == 11 and phone.isdigit()):
            st.error("Invalid Phone Number! It must start with '03' and contain exactly 11 digits.")
        
        elif not (len(cnic) == 13 and cnic.isdigit()):
            st.error("Invalid CNIC! It must contain exactly 13 digits.")
            
        else:
            st.success("Account Created Successfully! Redirecting to login...")
            st.session_state.page = "auth"
            st.session_state.auth_page = "login"
            st.rerun()

    st.write("")
    if st.button("Already have an account? Log In here", use_container_width=True):
        st.session_state.page = "auth"
        st.session_state.auth_page = "login"
        st.rerun()