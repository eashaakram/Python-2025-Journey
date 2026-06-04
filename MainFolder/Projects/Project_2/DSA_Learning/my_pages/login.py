import streamlit as st
import json
import os
import re

# Step 1: Add a professional header & footer, matching https://data-structure-and-algorithms.vercel.app/ style.
def app_header():
    st.markdown(
        """
        <header style="
            width:100vw;
            min-width:320px;
            background: linear-gradient(90deg, #001B2E 0%, #1679AB 80%);
            padding: 28px 0 15px 0;
            display: flex;
            flex-direction: column;
            align-items: center;
            box-shadow: 0px 2px 20px #10365277;">
            <h1 style="
                color: #fff;
                font-weight: 900;
                margin: 0;
                font-size: 2.2rem;
                letter-spacing: 2px;
                text-shadow: 0 1px 6px #143d5a60;
                font-family: 'Montserrat', 'Segoe UI', Arial, sans-serif;
            ">
                DSA VISUALIZER
            </h1>
            <nav style="margin-top: 8px;">
                <a style="color:#ACD2FA; text-decoration:none; margin:0 14px; font-weight:600;" href="/">Home</a>
                <a style="color:#ACD2FA; text-decoration:none; margin:0 14px; font-weight:600;" href="?page=login">Login</a>
                <a style="color:#ACD2FA; text-decoration:none; margin:0 14px; font-weight:600;" href="?page=auth&auth_page=signup">Sign Up</a>
            </nav>
        </header>
        """,
        unsafe_allow_html=True
    )

def app_footer():
    st.markdown(
        """
        <footer style="width:100vw; min-width:320px; text-align:center; margin-top: 40px; padding: 22px 0 10px 0; background: #001B2E; color: #d5eaff; font-size: 15px; border-top: 1px solid #143d5af5;">
            <span style="font-weight: 500">© 2024 DSA Visualizer</span>
            <span style="margin-left: 8px; color: #1679AB;">by Data Structure & Algorithms</span>
        </footer>
        """,
        unsafe_allow_html=True
    )

def is_valid_email(email):
    # Simple regex to check email validity (RFC 5322 simplified)
    return re.fullmatch(r"[^@\s]+@[^@\s]+\.[a-zA-Z0-9]{2,}$", email or "")

def show_login():
    app_header()

    # Step 2: Inject global/professional and mobile-centered CSS matching the reference and mobile
    st.markdown(
        """
        <style>
        html, body, .stApp {
            background: #051C31 !important;
        }
        .centered-card {
            max-width: 410px;
            min-width: 295px;
            margin: 32px auto 0 auto;
            box-shadow: 0 2px 16px #143d5a38;
            background: #0F2A43;
            border-radius: 18px;
            padding: 42px 26px 26px 26px;
            display: flex;
            flex-direction: column;
            align-items: center;
        }
        @media (max-width: 600px) {
            .centered-card {
                max-width: 100vw;
                border-radius: 0;
                padding: 34px 7vw 21px 7vw;
            }
        }
        .dsa-label {
            font-weight: 600;
            color: #A5D8FF !important;
            font-size: 15px;
            letter-spacing: 0.3px;
            margin-left: 2px;
        }
        .dsa-input input {
            background: #F0F8FF !important;
            color: #0F283E !important;
            border: 1.5px solid #92BCE3 !important;
            border-radius: 9px !important;
            padding: 13px 13px !important;
            font-size: 16px;
            margin-top: 2px !important;
        }
        .dsa-btn button {
            background: linear-gradient(90deg,#1679AB 65%,#69C3FA 135%) !important;
            color: #fff !important;
            border: none !important;
            border-radius: 9px !important;
            font-weight: 700 !important;
            letter-spacing: 1px;
            font-size: 17px !important;
            padding: 13px 0 !important;
            transition: filter .18s;
            margin-top: 8px;
        }
        .dsa-btn button:disabled {
            background: #badcf7 !important;
            color: #5075a1 !important;
            cursor: not-allowed;
            filter: grayscale(0.4);
        }
        .dsa-btn button:hover:enabled {
            filter: brightness(1.09);
        }
        .dsa-error {
            color: #FFA5A5 !important;
            background: #38233644 !important;
            font-weight: 500;
            margin-top: 2px;
            margin-bottom: 0;
            font-size: 13px;
            padding: 2px 0 0 5px;
        }
        .dsa-linkbar {
            display: flex; gap:16px; justify-content: center; align-items: center; margin: 15px 0 0 0;
        }
        .dsa-linkbar a {
            color: #96C7F8;
            text-decoration: none;
            font-size: 15px;
            font-weight: 600;
            transition: text-decoration-color .2s;
            padding: 0 2px;
        }
        .dsa-linkbar a:hover { text-decoration: underline; text-decoration-color: #379EFF;}
        .dsa-center-logo {
            margin-bottom: 18px;
            display:block;
            width:90px; height:90px;
            margin-left: auto; margin-right: auto;
            background:linear-gradient(135deg, #00BFFF 30%, #1E90FF 85%);
            border-radius:50%; box-shadow: 0 0 13px #52bfff66;
            display:flex; align-items:center; justify-content:center;
        }
        .dsa-page-h1 {
            text-align:center; color:#FBFCFF; font-size:1.8rem; font-weight: 800;
            margin: 10px 0 2px 0; font-family: 'Montserrat', 'Segoe UI', Arial, sans-serif;
        }
        .dsa-page-desc {
            text-align:center; color:#BBD6EF; margin-bottom:23px; font-size:15px; font-weight:500;
        }
        .dsa-divider {
            border-top: 1.5px solid #325179; margin: 26px 0 15px 0;
            width: 100%; display: block;
        }
        </style>
        """,
        unsafe_allow_html=True
    )

    # Step 3: Centered card for login form
    st.markdown('<div class="centered-card">', unsafe_allow_html=True)
    # Logo
    st.markdown("""
    <div class="dsa-center-logo">
        <svg width="55" height="55" viewBox="0 0 24 24" fill="white">
            <path d="M12 12c2.21 0 4-1.79 4-4s-1.79-4-4-4-4 1.79-4 4 1.79 4 4 4zm0 2c-2.67 0-8 1.34-8 4v2h16v-2c0-2.66-5.33-4-8-4z"/>
        </svg>
    </div>
    """, unsafe_allow_html=True)
    # Header
    st.markdown('<div class="dsa-page-h1">Welcome Back</div>', unsafe_allow_html=True)
    st.markdown('<div class="dsa-page-desc">Sign in to continue learning</div>', unsafe_allow_html=True)

    # Step 4: Real-time validation logic
    if "login_email_val" not in st.session_state: st.session_state.login_email_val = ""
    if "login_pass_val" not in st.session_state: st.session_state.login_pass_val = ""
    if "login_email_err" not in st.session_state: st.session_state.login_email_err = ""
    if "login_pass_err" not in st.session_state: st.session_state.login_pass_err = ""

    # -- Handle input changes (simulate "real-time" on user typing)
    def on_email_change():
        email = st.session_state.login_email_val
        if not email:
            st.session_state.login_email_err = "Email Address required"
        elif not is_valid_email(email):
            st.session_state.login_email_err = "Please enter a valid email"
        else:
            st.session_state.login_email_err = ""

    def on_pass_change():
        value = st.session_state.login_pass_val
        if not value:
            st.session_state.login_pass_err = "Password required"
        elif len(value) < 5:
            st.session_state.login_pass_err = "Password too short"
        else:
            st.session_state.login_pass_err = ""

    # Email Input
    st.markdown('<span class="dsa-label">Email Address</span>', unsafe_allow_html=True)
    st.text_input(
        label="Email",
        value=st.session_state.login_email_val,
        key="login_email_val",
        placeholder="easha@dsa.com",
        label_visibility="collapsed",
        on_change=on_email_change,
        help=None,
        disabled=False,
        args=None,
        kwargs=None,
        # custom class for targeting input styling
    )
    if st.session_state.login_email_err:
        st.markdown(f'<div class="dsa-error">{st.session_state.login_email_err}</div>', unsafe_allow_html=True)
    else:
        st.markdown("<div style='height:18px;'></div>", unsafe_allow_html=True)

    # Password Input
    st.markdown('<span class="dsa-label">Password</span>', unsafe_allow_html=True)
    st.text_input(
        label="Password",
        value=st.session_state.login_pass_val,
        key="login_pass_val",
        placeholder="•••••••",
        type="password",
        label_visibility="collapsed",
        on_change=on_pass_change,
        args=None,
        kwargs=None,
    )
    if st.session_state.login_pass_err:
        st.markdown(f'<div class="dsa-error">{st.session_state.login_pass_err}</div>', unsafe_allow_html=True)
    else:
        st.markdown("<div style='height:18px;'></div>", unsafe_allow_html=True)

    # Step 5: Buttons (Login, demo, nav links) styled in a consistent manner; disable login if not valid.
    form_valid = not st.session_state.login_email_err and not st.session_state.login_pass_err \
        and st.session_state.login_email_val.strip() and st.session_state.login_pass_val.strip()

    st.markdown('<div class="dsa-btn">', unsafe_allow_html=True)
    login_clicked = st.button("Login", use_container_width=True, disabled=not form_valid)
    st.markdown('</div>', unsafe_allow_html=True)

    # Demo login always enabled
    st.markdown('<div class="dsa-btn">', unsafe_allow_html=True)
    demo_clicked = st.button("⚡ Demo Login", use_container_width=True)
    st.markdown('</div>', unsafe_allow_html=True)

    # Feedback messages (for login only)
    if login_clicked:
        login_identity = st.session_state.login_email_val
        login_password = st.session_state.login_pass_val

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
            st.success(f"Welcome back, {matched_user_name}!")
            st.session_state.page = "home"
            st.rerun()
        else:
            st.error("Invalid Email or Password! Please create an account first.")

    if demo_clicked:
        st.session_state.page = "home"
        st.rerun()

    # Demo info
    st.markdown('<div style="text-align:center; color:#A0BBCC; font-size:13px; margin:6px 0 6px 0;">Use demo mode instantly (no signup required)</div>', unsafe_allow_html=True)

    # Divider
    st.markdown('<div class="dsa-divider"></div>', unsafe_allow_html=True)

    # Navigation Links (Signup and Login, always consistent)
    st.markdown(
        """
        <div class="dsa-linkbar">
            <span style="color:#A2B3BB;">New here?</span>
            <a href="?page=auth&auth_page=signup">Create Account</a>
            <span style="color:#2e4360;">·</span>
            <a href="?page=login">Login</a>
        </div>
        """,
        unsafe_allow_html=True
    )

    st.markdown("</div>", unsafe_allow_html=True)  # Close centered-card

    app_footer()