import streamlit as st
import json
import os
import re  # Email format validation k liye regex use karenge

def is_valid_email(email):
    # Standard email validation pattern
    pattern = r"^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$"
    return bool(re.match(pattern, email.strip()))

def show_login():
    # Hide unwanted lines and inject professional centered card styling
    st.html(
        """
        <style>
            hr { display: none !important; }
            header, footer, [data-testid="stHeader"] { display: none !important; }
            
            /* Main container background */
            .stApp {
                background-color: #0e1117 !important;
            }
            
            /* Target ONLY the second (middle) column for the card box */
            div[data-testid="stColumn"]:nth-of-type(2) {
                background-color: #1a1a1a !important; /* Dark grey container background */
                border-radius: 20px !important;
                padding: 40px 30px !important;
                box-shadow: 0 4px 15px rgba(0, 0, 0, 0.5) !important;
            }
            
            /* Global font and input styling */
            div.stTextInput > label {
                font-weight: 500 !important;
                color: #FFFFFF !important;
            }
            div.stTextInput > div > div > input {
                background-color: #F0F8FF !important; /* Light background like the image */
                color: #000000 !important;
                border: 1px solid #2d2d2d !important;
                border-radius: 12px !important;
                padding: 12px !important;
            }
            /* Button Styling */
            div.stButton > button {
                background-color: #1E1E1E !important;
                color: #FFFFFF !important;
                border: 1px solid #00BFFF !important;
                border-radius: 10px !important;
                height: 50px !important;
                font-weight: 600 !important;
                transition: all 0.3s ease !important;
            }
            div.stButton > button:hover {
                background-color: #00BFFF !important;
                color: #000000 !important;
            }
            
            /* Fix layout overlap when using collapsed label visibility */
            div.stTextInput {
                margin-top: 25px !important;
                margin-bottom: 5px !important;
            }

            /* Error border for empty fields or invalid format */
            .error-box input {
                border: 2px solid #FF4B4B !important;
            }
        </style>
        """
    )
    
    # Initialize error states in session state if they don't exist
    if "email_error" not in st.session_state:
        st.session_state.email_error = False
    if "email_invalid" not in st.session_state:
        st.session_state.email_invalid = False
    if "pass_error" not in st.session_state:
        st.session_state.pass_error = False

    # Centered Container Layout
    col_l, col_mid, col_r = st.columns([1, 1.8, 1])
    
    with col_mid:
        
        # Glow Profile Logo
        st.markdown(
            """
            <div style="display: flex; justify-content: center; margin-top: 10px; margin-bottom: 20px;">
                <div style="background: linear-gradient(135deg, #00BFFF, #1E90FF); 
                            width: 100px; height: 100px; border-radius: 50%; 
                            display: flex; justify-content: center; align-items: center;
                            box-shadow: 0 0 20px rgba(0, 191, 255, 0.4);">
                    <svg width="50" height="50" viewBox="0 0 24 24" fill="white">
                        <path d="M12 12c2.21 0 4-1.79 4-4s-1.79-4-4-4-4 1.79-4 4 1.79 4 4 4zm0 2c-2.67 0-8 1.34-8 4v2h16v-2c0-2.66-5.33-4-8-4z"/>
                    </svg>
                </div>
            </div>
            """, unsafe_allow_html=True
        )
        
        # Headings
        st.markdown("<h2 style='text-align:center; color:#FFFFFF; margin-bottom:0;'>Welcome Back</h2>", unsafe_allow_html=True)
        st.markdown("<p style='text-align:center; color:#888888; margin-bottom:30px;'>Sign in to continue learning</p>", unsafe_allow_html=True)
        
        # Email Input with Icon 
        st.markdown(
            '<div style="display: flex; align-items: center; margin-bottom: -20px; position: relative; z-index: 99;">'
            '<svg width="20" height="20" viewBox="0 0 24 24" fill="#00BFFF" style="margin-right:10px;"><path d="M20 4H4c-1.1 0-1.99.9-1.99 2L2 18c0 1.1.9 2 2 2h16c1.1 0 2-.9 2-2V6c0-1.1-.9-2-2-2zm0 4l-8 5-8-5V6l8 5 8-5v2z"/></svg>'
            '<span style="color:white; font-size:14px; font-weight: 500;">Email Address</span>'
            '</div>', unsafe_allow_html=True
        )
        
        # Applying red border if email is missing OR invalid
        show_email_border_error = st.session_state.email_error or st.session_state.email_invalid
        
        if show_email_border_error:
            st.markdown('<div class="error-box">', unsafe_allow_html=True)
        login_identity = st.text_input("", placeholder="easha@dsa.com", key="email_val", label_visibility="collapsed")
        if show_email_border_error:
            st.markdown('</div>', unsafe_allow_html=True)
            
            # Alag message khali hone par aur alag message format galat hone par
            if st.session_state.email_error:
                st.markdown("<p style='color: #FF4B4B; font-size: 14px; margin-top: -5px; margin-bottom: 15px;'>Please enter your email address.</p>", unsafe_allow_html=True)
            elif st.session_state.email_invalid:
                st.markdown("<p style='color: #FF4B4B; font-size: 14px; margin-top: -5px; margin-bottom: 15px;'>Please enter a valid email (e.g. example@gmail.com).</p>", unsafe_allow_html=True)

        # Password Input with Icon
        st.markdown(
            '<div style="display: flex; align-items: center; margin-bottom: -20px; margin-top:15px; position: relative; z-index: 99;">'
            '<svg width="20" height="20" viewBox="0 0 24 24" fill="#00BFFF" style="margin-right:10px;"><path d="M18 8h-1V6c0-2.76-2.24-5-5-5S7 3.24 7 6v2H6c-1.1 0-2 .9-2 2v10c0 1.1.9 2 2 2h12c1.1 0 2-.9 2-2V10c0-1.1-.9-2-2-2zm-6 9c-1.1 0-2-.9-2-2s.9-2 2-2 2 .9 2 2-.9 2-2 2zm3.1-9H8.9V6c0-1.71 1.39-3.1 3.1-3.1 1.71 0 3.1 1.39 3.1 3.1v2z"/></svg>'
            '<span style="color:white; font-size:14px; font-weight: 500;">Password</span>'
            '</div>', unsafe_allow_html=True
        )
        
        # Applying red border if password is missing
        if st.session_state.pass_error:
            st.markdown('<div class="error-box">', unsafe_allow_html=True)
        login_password = st.text_input("", type="password", placeholder="•••••", key="pass_val", label_visibility="collapsed")
        if st.session_state.pass_error:
            st.markdown('</div>', unsafe_allow_html=True)
            st.markdown("<p style='color: #FF4B4B; font-size: 14px; margin-top: -5px; margin-bottom: 15px;'>Please enter your password.</p>", unsafe_allow_html=True)

        st.markdown("<div style='margin-bottom: 25px;'></div>", unsafe_allow_html=True)

        # Login Button
        if st.button("Login", use_container_width=True):
            # 1. Khali check karo pehle
            st.session_state.email_error = not bool(login_identity.strip())
            st.session_state.pass_error = not bool(login_password.strip())
            
            # 2. Agar khali nahi hai, to format validate karo
            if not st.session_state.email_error:
                st.session_state.email_invalid = not is_valid_email(login_identity)
            else:
                st.session_state.email_invalid = False
            
            # Agar koi bhi validation fail ho to rerun karo database check kiye bagair
            if st.session_state.email_error or st.session_state.email_invalid or st.session_state.pass_error:
                st.rerun()
            else:
                file_path = "data/users.json"
                user_authenticated = False
                matched_user_name = ""

                if os.path.exists(file_path):
                    with open(file_path, "r") as file:
                        try:
                            users = json.load(file)
                            if isinstance(users, dict):
                                users = [users]
                        except:
                            users = []
                    
                    for user in users:
                        if user.get("email", "").strip().lower() == login_identity.strip().lower() and user.get("password", "") == login_password:
                            user_authenticated = True
                            matched_user_name = user.get("full_name", "User")
                            break
                
                if user_authenticated:
                    # Reset errors on successful login
                    st.session_state.email_error = False
                    st.session_state.email_invalid = False
                    st.session_state.pass_error = False
                    st.success(f"Welcome back, {matched_user_name}!")
                    st.session_state.page = "home"
                    st.rerun()
                else:
                    st.error("Invalid Email or Password! Please create an account first.")

        # Demo Login
        demo_btn_label = "⚡ Demo Login"
        if st.button(demo_btn_label, use_container_width=True):
            st.session_state.email_error = False
            st.session_state.email_invalid = False
            st.session_state.pass_error = False
            st.session_state.page = "home"
            st.rerun()
        
        st.markdown("<p style='text-align:center; color:#666666; font-size:12px; margin-top:-10px;'>Use demo mode instantly (no signup required)</p>", unsafe_allow_html=True)
        
        # Divider and Signup
        st.markdown("<div style='border-top: 1px solid #333; margin: 20px 0; position: relative;'><span style='position: absolute; top: -10px; left: 22%; background: #1a1a1a; padding: 0 10px; color: #555; font-size: 12px;'>Don't have an account?</span></div>", unsafe_allow_html=True)
        
        if st.button("👤+ Create New Account", use_container_width=True):
            st.session_state.email_error = False
            st.session_state.email_invalid = False
            st.session_state.pass_error = False
            st.session_state.page = "auth"
            st.session_state.auth_page = "signup"
            st.rerun()