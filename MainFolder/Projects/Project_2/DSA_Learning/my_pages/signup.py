import streamlit as st
from datetime import date
import json
import os

def show_signup():
    # Injecting professional uniform styles matching the login setup
    st.html(
        """
        <style>
            hr { display: none !important; }
            /* Global font and input boxes styling */
            div.stTextInput > label, div.stDateInput > label {
                font-weight: 500 !important;
                color: #FFFFFF !important;
            }
            div.stTextInput > div > div > input, div.stDateInput > div > div > input {
                background-color: #F0F8FF !important; /* Light background matching design */
                color: #000000 !important;
                border: 1px solid #2d2d2d !important;
                border-radius: 12px !important;
                padding: 12px !important;
            }
            
            /* Form container style cleanup */
            [data-testid="stForm"] {
                border: none !important;
                padding: 0 !important;
                background-color: transparent !important;
            }
            
            /* Custom button parameters matching primary premium design */
            div.stButton > button, div.stFormSubmitButton > button {
                background-color: #1E1E1E !important;
                color: #FFFFFF !important;
                border: 1px solid #00BFFF !important;
                border-radius: 10px !important;
                height: 50px !important;
                font-weight: 600 !important;
                transition: all 0.3s ease !important;
            }
            div.stButton > button:hover, div.stFormSubmitButton > button:hover {
                background-color: #00BFFF !important;
                color: #000000 !important;
            }
            
            /* Structural margin fix for floating labels overlay text visibility */
            div.stTextInput, div.stDateInput {
                margin-top: 25px !important;
                margin-bottom: 5px !important;
            }
        </style>
        """
    )
    
    # Premium Add-User Glow Profile Logo 
    st.markdown(
        """
        <div style="display: flex; justify-content: center; margin-bottom: 20px;">
            <div style="background: linear-gradient(135deg, #00BFFF, #1E90FF); 
                        width: 100px; height: 100px; border-radius: 50%; 
                        display: flex; justify-content: center; align-items: center;
                        box-shadow: 0 0 20px rgba(0, 191, 255, 0.4);">
                <svg width="50" height="50" viewBox="0 0 24 24" fill="white">
                    <path d="M15 12c2.21 0 4-1.79 4-4s-1.79-4-4-4-4 1.79-4 4 1.79 4 4 4zm-9-2V7H4v3H1v2h3v3h2v-3h3v-2H6zm9 4c-2.67 0-8 1.34-8 4v2h16v-2c0-2.66-5.33-4-8-4z"/>
                </svg>
            </div>
        </div>
        """, unsafe_allow_html=True
    )
    
    st.markdown("<h2 style='text-align:center; color:#FFFFFF; margin-bottom:0;'>Create Account</h2>", unsafe_allow_html=True)
    st.markdown("<p style='text-align:center; color:#888888; margin-bottom:30px;'>Join us and start your learning journey</p>", unsafe_allow_html=True)
    
    # Centered Column Grid
    col_l, col_mid, col_r = st.columns([1, 2.5, 1])
    
    with col_mid:
        with st.form("signup_form", clear_on_submit=False):
            
            # 👤 Full Name Input + Logo
            st.markdown(
                '<div style="display: flex; align-items: center; margin-bottom: -20px; position: relative; z-index: 99;">'
                '<svg width="18" height="18" viewBox="0 0 24 24" fill="#00BFFF" style="margin-right:8px;"><path d="M12 12c2.21 0 4-1.79 4-4s-1.79-4-4-4-4 1.79-4 4 1.79 4 4 4zm0 2c-2.67 0-8 1.34-8 4v2h16v-2c0-2.66-5.33-4-8-4z"/></svg>'
                '<span style="color:white; font-size:14px; font-weight: 500;">Full Name</span>'
                '</div>', unsafe_allow_html=True
            )
            full_name = st.text_input("", placeholder="Enter your name (e.g., Easha Akram)", label_visibility="collapsed", key="su_fullname")

            # ✉️ Email Input + Logo
            st.markdown(
                '<div style="display: flex; align-items: center; margin-bottom: -20px; margin-top:15px; position: relative; z-index: 99;">'
                '<svg width="18" height="18" viewBox="0 0 24 24" fill="#00BFFF" style="margin-right:8px;"><path d="M20 4H4c-1.1 0-1.99.9-1.99 2L2 18c0 1.1.9 2 2 2h16c1.1 0 2-.9 2-2V6c0-1.1-.9-2-2-2zm0 4l-8 5-8-5V6l8 5 8-5v2z"/></svg>'
                '<span style="color:white; font-size:14px; font-weight: 500;">Email Address</span>'
                '</div>', unsafe_allow_html=True
            )
            email = st.text_input("", placeholder="Enter your email (e.g., easha@dsa.com)", label_visibility="collapsed", key="su_email")

            # 📞 Phone Number Input + Logo
            st.markdown(
                '<div style="display: flex; align-items: center; margin-bottom: -20px; margin-top:15px; position: relative; z-index: 99;">'
                '<svg width="18" height="18" viewBox="0 0 24 24" fill="#00BFFF" style="margin-right:8px;"><path d="M6.62 10.79c1.44 2.83 3.76 5.14 6.59 6.59l2.2-2.2c.27-.27.67-.36 1.02-.24 1.12.37 2.33.57 3.57.57.55 0 1 .45 1 1V20c0 .55-.45 1-1 1-9.39 0-17-7.61-17-17 0-.55.45-1 1-1h3.5c.55 0 1 .45 1 1 0 1.25.2 2.45.57 3.57.11.35.03.74-.25 1.02l-2.2 2.2z"/></svg>'
                '<span style="color:white; font-size:14px; font-weight: 500;">Phone Number</span>'
                '</div>', unsafe_allow_html=True
            )
            phone = st.text_input("", placeholder="Enter phone number (e.g., 03001234567)", max_chars=11, label_visibility="collapsed", key="su_phone")

            # 🪪 CNIC Input + Logo
            st.markdown(
                '<div style="display: flex; align-items: center; margin-bottom: -20px; margin-top:15px; position: relative; z-index: 99;">'
                '<svg width="18" height="18" viewBox="0 0 24 24" fill="#00BFFF" style="margin-right:8px;"><path d="M20 4H4c-1.1 0-2 .9-2 2v12c0 1.1.9 2 2 2h16c1.1 0 2-.9 2-2V6c0-1.1-.9-2-2-2zm-1 11.5h-4v-1h4v1zm0-2.5h-4v-1h4v1zm-8-3c1.66 0 3 1.34 3 3s-1.34 3-3 3-3-1.34-3-3 1.34-3 3-3zm6-3H4v-1h11v1z"/></svg>'
                '<span style="color:white; font-size:14px; font-weight: 500;">CNIC Number</span>'
                '</div>', unsafe_allow_html=True
            )
            cnic = st.text_input("", placeholder="Enter 13-digit CNIC (e.g., 3520112345671)", max_chars=13, label_visibility="collapsed", key="su_cnic")

            # 📅 DOB Input + Logo
            st.markdown(
                '<div style="display: flex; align-items: center; margin-bottom: -20px; margin-top:15px; position: relative; z-index: 99;">'
                '<svg width="18" height="18" viewBox="0 0 24 24" fill="#00BFFF" style="margin-right:8px;"><path d="M19 3h-1V1h-2v2H8V1H6v2H5c-1.11 0-1.99.9-1.99 2L3 19c0 1.1.89 2 2 2h14c1.1 0 2-.9 2-2V5c0-1.1-.9-2-2-2zm0 16H5V8h14v11z"/></svg>'
                '<span style="color:white; font-size:14px; font-weight: 500;">Date of Birth</span>'
                '</div>', unsafe_allow_html=True
            )
            dob = st.date_input("", min_value=date(1950, 1, 1), max_value=date.today(), label_visibility="collapsed", key="su_dob")

            # 🔒 Password Input + Logo
            st.markdown(
                '<div style="display: flex; align-items: center; margin-bottom: -20px; margin-top:15px; position: relative; z-index: 99;">'
                '<svg width="18" height="18" viewBox="0 0 24 24" fill="#00BFFF" style="margin-right:8px;"><path d="M18 8h-1V6c0-2.76-2.24-5-5-5S7 3.24 7 6v2H6c-1.1 0-2 .9-2 2v10c0 1.1.9 2 2 2h12c1.1 0 2-.9 2-2V10c0-1.1-.9-2-2-2zm-6 9c-1.1 0-2-.9-2-2s.9-2 2-2 2 .9 2 2-.9 2-2 2zm3.1-9H8.9V6c0-1.71 1.39-3.1 3.1-3.1 1.71 0 3.1 1.39 3.1 3.1v2z"/></svg>'
                '<span style="color:white; font-size:14px; font-weight: 500;">Password</span>'
                '</div>', unsafe_allow_html=True
            )
            password = st.text_input("", type="password", placeholder="Enter a secure password (minimum 8 characters)", label_visibility="collapsed", key="su_password")

            st.markdown("<div style='margin-bottom: 25px;'></div>", unsafe_allow_html=True)
            submit_button = st.form_submit_button("Create Account", use_container_width=True)

        # Validation Logic processing 
        if submit_button:
            if not (full_name.strip() and email.strip() and phone.strip() and cnic.strip() and password.strip()):
                st.error("Please fill out all the fields before submitting!")

            elif not (phone.strip().startswith("03") and len(phone.strip()) == 11 and phone.strip().isdigit()):
                st.error("Invalid Phone Number!")

            elif not (len(cnic.strip()) == 13 and cnic.strip().isdigit()):
                st.error("Invalid CNIC!")

            else:
                user_data = {
                    "full_name": full_name.strip(),
                    "email": email.strip().lower(), # lowercase for safe matching
                    "phone": phone.strip(),
                    "cnic": cnic.strip(),
                    "dob": str(dob),
                    "password": password.strip()
                }

                os.makedirs("data", exist_ok=True)
                file_path = "data/users.json"

                # existing file load karo
                if os.path.exists(file_path):
                    with open(file_path, "r") as file:
                        try:
                            users = json.load(file)
                        except:
                            users = []
                else:
                    users = []

                # agar file dict hai to list bana do
                if isinstance(users, dict):
                    users = [users]

                # new user add karo
                users.append(user_data)

                # file save karo
                with open(file_path, "w") as file:
                    json.dump(users, file, indent=4)

                st.success("Account Created Successfully!")

                st.session_state.page = "auth"
                st.session_state.auth_page = "login"
                st.rerun()

        # Modern Divider Style 
        st.markdown(
            """
            <div style="border-top: 1px solid #333; margin: 25px 0; position: relative; text-align: center;">
                <span style="position: absolute; top: -10px; left: 50%; transform: translateX(-50%); background: #0E1117; padding: 0 15px; color: #555555; font-size: 13px;">
                    Already have an account?
                </span>
            </div>
            """, unsafe_allow_html=True
        )
        
        if st.button("Sign In", use_container_width=True):
            st.session_state.page = "auth"
            st.session_state.auth_page = "login"
            st.rerun()