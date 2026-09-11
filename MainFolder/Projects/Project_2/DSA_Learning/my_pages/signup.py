import streamlit as st
from datetime import date
import json
import os
import re  # Email validation ke liye regex use hoga

# Strict Real-World Domain Validation (Only allows real extensions)
def is_valid_email(email):
    # Yeh pattern sirf real extensions (.com, .pk, .edu, .org, .net, .gov, .co) ko accept karega
    # Koi bhi .kom, .con, .commm, .pkkk likhega toh block ho jayega
    pattern = r"^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.(com|pk|edu|org|net|gov|co)$"
    return bool(re.match(pattern, email.strip().lower()))

# Password Strength Validation Function
def is_strong_password(password):
    # Minimum 8 characters, at least one uppercase, one lowercase, one number, and one special character
    if len(password) < 8:
        return False
    if not re.search(r"[A-Z]", password):
        return False
    if not re.search(r"[a-z]", password):
        return False
    if not re.search(r"[0-9]", password):
        return False
    if not re.search(r"[_@#$%^&+=!£*()\-<>?/\\|}{~:;.,`'\"\[\]]", password):
        return False
    return True

def show_signup():
    # Injecting professional uniform styles matching the login setup
    st.html(
        """
        <style>
            hr { display: none !important; }
            header, footer, [data-testid="stHeader"] { display: none !important; }
            
            /* Main container background */
            .stApp {
                background-color: #0e1117 !important;
            }
            
            /* Target ONLY the second (middle) column for the card box wrapper */
            div[data-testid="stColumn"]:nth-of-type(2) {
                background-color: #1a1a1a !important; /* Dark grey container background */
                border-radius: 20px !important;
                padding: 40px 30px !important;
                box-shadow: 0 4px 15px rgba(0, 0, 0, 0.5) !important;
            }
            
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
                caret-color: auto !important; /* Ensures cursor is fully visible while typing */
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

            /* Error border for empty fields or invalid format */
            .error-box input {
                border: 2px solid #FF4B4B !important;
            }
        </style>
        """
    )
    
    # Initialize all individual error states in session state if they don't exist
    if "su_name_error" not in st.session_state: st.session_state.su_name_error = False
    if "su_email_error" not in st.session_state: st.session_state.su_email_error = False
    if "su_email_invalid" not in st.session_state: st.session_state.su_email_invalid = False
    if "su_phone_error" not in st.session_state: st.session_state.su_phone_error = False
    if "su_cnic_error" not in st.session_state: st.session_state.su_cnic_error = False
    if "su_dob_error" not in st.session_state: st.session_state.su_dob_error = False
    if "su_pass_error" not in st.session_state: st.session_state.su_pass_error = False
    if "su_pass_weak" not in st.session_state: st.session_state.su_pass_weak = False
    if "su_confirm_pass_error" not in st.session_state: st.session_state.su_confirm_pass_error = False
    if "su_pass_mismatch" not in st.session_state: st.session_state.su_pass_mismatch = False
    
    # Centered Column Grid (Card Wrapper columns setup)
    col_l, col_mid, col_r = st.columns([1, 1.8 , 1])
    
    # EVERYTHING goes inside col_mid now so it stays inside the card box wrapper
    with col_mid:
        
        # Premium Add-User Glow Profile Logo 
        st.markdown(
            """
            <div style="display: flex; justify-content: center; margin-top: 10px; margin-bottom: 20px;">
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
        
        with st.form("signup_form", clear_on_submit=False):
            
            # 👤 Full Name Input + Logo
            st.markdown(
                '<div style="display: flex; align-items: center; margin-bottom: -20px; position: relative; z-index: 99;">'
                '<svg width="18" height="18" viewBox="0 0 24 24" fill="#00BFFF" style="margin-right:8px;"><path d="M12 12c2.21 0 4-1.79 4-4s-1.79-4-4-4-4 1.79-4 4 1.79 4 4 4zm0 2c-2.67 0-8 1.34-8 4v2h16v-2c0-2.66-5.33-4-8-4z"/></svg>'
                '<span style="color:white; font-size:14px; font-weight: 500;">Full Name</span>'
                '</div>', unsafe_allow_html=True
            )
            if st.session_state.su_name_error:
                st.markdown('<div class="error-box">', unsafe_allow_html=True)
            full_name = st.text_input("", placeholder="Enter your name (e.g., Easha Akram)", label_visibility="collapsed", key="su_fullname")
            if st.session_state.su_name_error:
                st.markdown('</div>', unsafe_allow_html=True)
                st.markdown("<p style='color: #FF4B4B; font-size: 14px; margin-top: -5px;'>Please enter your full name.</p>", unsafe_allow_html=True)


            # ✉️ Email Input + Logo
            st.markdown(
                '<div style="display: flex; align-items: center; margin-bottom: -20px; margin-top:15px; position: relative; z-index: 99;">'
                '<svg width="18" height="18" viewBox="0 0 24 24" fill="#00BFFF" style="margin-right:8px;"><path d="M20 4H4c-1.1 0-1.99.9-1.99 2L2 18c0 1.1.9 2 2 2h16c1.1 0 2-.9 2-2V6c0-1.1-.9-2-2-2zm0 4l-8 5-8-5V6l8 5 8-5v2z"/></svg>'
                '<span style="color:white; font-size:14px; font-weight: 500;">Email Address</span>'
                '</div>', unsafe_allow_html=True
            )
            show_email_error = st.session_state.su_email_error or st.session_state.su_email_invalid
            if show_email_error:
                st.markdown('<div class="error-box">', unsafe_allow_html=True)
            email = st.text_input("", placeholder="Enter your email (e.g., easha@dsa.com)", label_visibility="collapsed", key="su_email")
            if show_email_error:
                st.markdown('</div>', unsafe_allow_html=True)
                if st.session_state.su_email_error:
                    st.markdown("<p style='color: #FF4B4B; font-size: 14px; margin-top: -5px;'>Please enter your email address.</p>", unsafe_allow_html=True)
                elif st.session_state.su_email_invalid:
                    st.markdown("<p style='color: #FF4B4B; font-size: 14px; margin-top: -5px;'>Please enter a valid email address.</p>", unsafe_allow_html=True)


            # 📞 Phone Number Input + Logo
            st.markdown(
                '<div style="display: flex; align-items: center; margin-bottom: -20px; margin-top:15px; position: relative; z-index: 99;">'
                '<svg width="18" height="18" viewBox="0 0 24 24" fill="#00BFFF" style="margin-right:8px;"><path d="M6.62 10.79c1.44 2.83 3.76 5.14 6.59 6.59l2.2-2.2c.27-.27.67-.36 1.02-.24 1.12.37 2.33.57 3.57.57.55 0 1 .45 1 1V20c0 .55-.45 1-1 1-9.39 0-17-7.61-17-17 0-.55.45-1 1-1h3.5c.55 0 1 .45 1 1 0 1.25.2 2.45.57 3.57.11.35.03.74-.25 1.02l-2.2 2.2z"/></svg>'
                '<span style="color:white; font-size:14px; font-weight: 500;">Phone Number</span>'
                '</div>', unsafe_allow_html=True
            )
            if st.session_state.su_phone_error:
                st.markdown('<div class="error-box">', unsafe_allow_html=True)
            phone = st.text_input("", placeholder="Enter phone number (e.g., 03001234567)", max_chars=11, label_visibility="collapsed", key="su_phone")
            if st.session_state.su_phone_error:
                st.markdown('</div>', unsafe_allow_html=True)
                st.markdown("<p style='color: #FF4B4B; font-size: 14px; margin-top: -5px;'>Invalid Phone Number! Format must be 03XXXXXXXXX (11 digits).</p>", unsafe_allow_html=True)


            # 🪪 CNIC Input + Logo
            st.markdown(
                '<div style="display: flex; align-items: center; margin-bottom: -20px; margin-top:15px; position: relative; z-index: 99;">'
                '<svg width="18" height="18" viewBox="0 0 24 24" fill="#00BFFF" style="margin-right:8px;"><path d="M20 4H4c-1.1 0-2 .9-2 2v12c0 1.1.9 2 2 2h16c1.1 0 2-.9 2-2V6c0-1.1-.9-2-2-2zm-1 11.5h-4v-1h4v1zm0-2.5h-4v-1h4v1zm-8-3c1.66 0 3 1.34 3 3s-1.34 3-3 3-3-1.34-3-3 1.34-3 3-3zm6-3H4v-1h11v1z"/></svg>'
                '<span style="color:white; font-size:14px; font-weight: 500;">CNIC Number</span>'
                '</div>', unsafe_allow_html=True
            )
            if st.session_state.su_cnic_error:
                st.markdown('<div class="error-box">', unsafe_allow_html=True)
            cnic = st.text_input("", placeholder="Enter 13-digit CNIC (e.g., 3520112345671)", max_chars=13, label_visibility="collapsed", key="su_cnic")
            if st.session_state.su_cnic_error:
                st.markdown('</div>', unsafe_allow_html=True)
                st.markdown("<p style='color: #FF4B4B; font-size: 14px; margin-top: -5px;'>Invalid CNIC! Must be exactly 13 digits without dashes.</p>", unsafe_allow_html=True)


            # 📅 DOB Input + Logo
            st.markdown(
                '<div style="display: flex; align-items: center; margin-bottom: -20px; margin-top:15px; position: relative; z-index: 99;">'
                '<svg width="18" height="18" viewBox="0 0 24 24" fill="#00BFFF" style="margin-right:8px;"><path d="M19 3h-1V1h-2v2H8V1H6v2H5c-1.11 0-1.99.9-1.99 2L3 19c0 1.1.89 2 2 2h14c1.1 0 2-.9 2-2V5c0-1.1-.9-2-2-2zm0 16H5V8h14v11z"/></svg>'
                '<span style="color:white; font-size:14px; font-weight: 500;">Date of Birth</span>'
                '</div>', unsafe_allow_html=True
            )
            if st.session_state.su_dob_error:
                st.markdown('<div class="error-box">', unsafe_allow_html=True)
            dob = st.date_input("", min_value=date(1950, 1, 1), max_value=date.today(), label_visibility="collapsed", key="su_dob")
            if st.session_state.su_dob_error:
                st.markdown('</div>', unsafe_allow_html=True)
                st.markdown("<p style='color: #FF4B4B; font-size: 14px; margin-top: -5px;'>Registration Denied! You must be at least 15 years old to register.</p>", unsafe_allow_html=True)


            # 🔒 Password Input + Logo
            st.markdown(
                '<div style="display: flex; align-items: center; margin-bottom: -20px; margin-top:15px; position: relative; z-index: 99;">'
                '<svg width="18" height="18" viewBox="0 0 24 24" fill="#00BFFF" style="margin-right:8px;"><path d="M18 8h-1V6c0-2.76-2.24-5-5-5S7 3.24 7 6v2H6c-1.1 0-2 .9-2 2v10c0 1.1.9 2 2 2h12c1.1 0 2-.9 2-2V10c0-1.1-.9-2-2-2zm-6 9c-1.1 0-2-.9-2-2s.9-2 2-2 2 .9 2 2-.9 2-2 2zm3.1-9H8.9V6c0-1.71 1.39-3.1 3.1-3.1 1.71 0 3.1 1.39 3.1 3.1v2z"/></svg>'
                '<span style="color:white; font-size:14px; font-weight: 500;">Password</span>'
                '</div>', unsafe_allow_html=True
            )
            show_pass_error = st.session_state.su_pass_error or st.session_state.su_pass_weak
            if show_pass_error:
                st.markdown('<div class="error-box">', unsafe_allow_html=True)
            password = st.text_input("", type="password", placeholder="Enter a secure password (e.g., Secure@123)", label_visibility="collapsed", key="su_password")
            if show_pass_error:
                st.markdown('</div>', unsafe_allow_html=True)
                if st.session_state.su_pass_error:
                    st.markdown("<p style='color: #FF4B4B; font-size: 14px; margin-top: -5px;'>Please enter a password.</p>", unsafe_allow_html=True)
                elif st.session_state.su_pass_weak:
                    st.markdown("<p style='color: #FF4B4B; font-size: 14px; margin-top: -5px;'>Password is weak! Must be at least 8 characters long and contain uppercase, lowercase, numbers, and special characters.</p>", unsafe_allow_html=True)


            # 🔄 Confirm Password Input + Logo
            st.markdown(
                '<div style="display: flex; align-items: center; margin-bottom: -20px; margin-top:15px; position: relative; z-index: 99;">'
                '<svg width="18" height="18" viewBox="0 0 24 24" fill="#00BFFF" style="margin-right:8px;"><path d="M12 22c5.523 0 10-4.477 10-10S17.523 2 12 2 2 6.477 2 12s4.477 10 10 10zM11 7h2v6h-2V7zm0 8h2v2h-2v-2z"/></svg>'
                '<span style="color:white; font-size:14px; font-weight: 500;">Confirm Password</span>'
                '</div>', unsafe_allow_html=True
            )
            show_confirm_pass_error = st.session_state.su_confirm_pass_error or st.session_state.su_pass_mismatch
            if show_confirm_pass_error:
                st.markdown('<div class="error-box">', unsafe_allow_html=True)
            confirm_password = st.text_input("", type="password", placeholder="Re-enter your password to confirm", label_visibility="collapsed", key="su_confirm_password")
            if show_confirm_pass_error:
                st.markdown('</div>', unsafe_allow_html=True)
                if st.session_state.su_confirm_pass_error:
                    st.markdown("<p style='color: #FF4B4B; font-size: 14px; margin-top: -5px;'>Please confirm your password.</p>", unsafe_allow_html=True)
                elif st.session_state.su_pass_mismatch:
                    st.markdown("<p style='color: #FF4B4B; font-size: 14px; margin-top: -5px;'>Passwords do not match! Both fields must be identical.</p>", unsafe_allow_html=True)

            st.markdown("<div style='margin-bottom: 25px;'></div>", unsafe_allow_html=True)
            submit_button = st.form_submit_button("Create Account", use_container_width=True)

        # Validation Logic processing 
        if submit_button:
            # 1. Update individual error states based on inputs
            st.session_state.su_name_error = not bool(full_name.strip())
            st.session_state.su_email_error = not bool(email.strip())
            
            # Email format validation check if not empty
            if not st.session_state.su_email_error:
                st.session_state.su_email_invalid = not is_valid_email(email)
            else:
                st.session_state.su_email_invalid = False

            # Phone number syntax check
            st.session_state.su_phone_error = not (phone.strip().startswith("03") and len(phone.strip()) == 11 and phone.strip().isdigit())
            
            # CNIC validation check
            st.session_state.su_cnic_error = not (len(cnic.strip()) == 13 and cnic.strip().isdigit())
            
            # 15+ Age validation logic check
            today = date.today()
            age = today.year - dob.year - ((today.month, today.day) < (dob.month, dob.day))
            st.session_state.su_dob_error = (age < 15)

            # Password checks
            st.session_state.su_pass_error = not bool(password.strip())
            if not st.session_state.su_pass_error:
                st.session_state.su_pass_weak = not is_strong_password(password.strip())
            else:
                st.session_state.su_pass_weak = False

            # Confirm Password checks
            st.session_state.su_confirm_pass_error = not bool(confirm_password.strip())
            if not st.session_state.su_confirm_pass_error and not st.session_state.su_pass_error:
                st.session_state.su_pass_mismatch = (password.strip() != confirm_password.strip())
            else:
                st.session_state.su_pass_mismatch = False

            # 2. Check if ANY error is active, trigger rerun to paint red box
            has_errors = (
                st.session_state.su_name_error or 
                st.session_state.su_email_error or 
                st.session_state.su_email_invalid or 
                st.session_state.su_phone_error or 
                st.session_state.su_cnic_error or 
                st.session_state.su_dob_error or
                st.session_state.su_pass_error or 
                st.session_state.su_pass_weak or
                st.session_state.su_confirm_pass_error or
                st.session_state.su_pass_mismatch
            )

            if has_errors:
                st.rerun()
            else:
                # Clear error states on complete successful data validation
                st.session_state.su_name_error = False
                st.session_state.su_email_error = False
                st.session_state.su_email_invalid = False
                st.session_state.su_phone_error = False
                st.session_state.su_cnic_error = False
                st.session_state.su_dob_error = False
                st.session_state.su_pass_error = False
                st.session_state.su_pass_weak = False
                st.session_state.su_confirm_pass_error = False
                st.session_state.su_pass_mismatch = False

                user_data = {
                    "full_name": full_name.strip(),
                    "email": email.strip().lower(), 
                    "phone": phone.strip(),
                    "cnic": cnic.strip(),
                    "dob": str(dob),
                    "password": password.strip()
                }

                os.makedirs("data", exist_ok=True)
                file_path = "data/users.json"

                # Existing file load karo
                if os.path.exists(file_path):
                    with open(file_path, "r") as file:
                        try:
                            users = json.load(file)
                            if isinstance(users, dict):
                                users = [users]
                        except:
                            users = []
                else:
                    users = []

                # New user add karo
                users.append(user_data)

                # File save karo
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
                <span style="position: absolute; top: -10px; left: 50%; transform: translateX(-50%); background: #1a1a1a; padding: 0 15px; color: #555555; font-size: 13px;">
                    Already have an account?
                </span>
            </div>
            """, unsafe_allow_html=True
        )
        
        if st.button("Sign In", use_container_width=True):
            # Clean up active validation error messages when switching views manually
            st.session_state.su_name_error = False
            st.session_state.su_email_error = False
            st.session_state.su_email_invalid = False
            st.session_state.su_phone_error = False
            st.session_state.su_cnic_error = False
            st.session_state.su_dob_error = False
            st.session_state.su_pass_error = False
            st.session_state.su_pass_weak = False
            st.session_state.su_confirm_pass_error = False
            st.session_state.su_pass_mismatch = False
            
            st.session_state.page = "auth"
            st.session_state.auth_page = "login"
            st.rerun()