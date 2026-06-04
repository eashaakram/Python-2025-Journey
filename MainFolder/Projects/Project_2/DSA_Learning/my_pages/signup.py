import json
import os
from datetime import date

import streamlit as st

from my_pages.layout import (
    render_auth_card_close,
    render_auth_card_open,
    render_field_label,
    render_password_strength,
    render_validation,
    validate_cnic_live,
    validate_email,
    validate_name,
    validate_password_strength,
    validate_phone_live,
)

ICON_USER_ADD = "M15 12c2.21 0 4-1.79 4-4s-1.79-4-4-4-4 1.79-4 4 1.79 4 4 4zm-9-2V7H4v3H1v2h3v3h2v-3h3v-2H6zm9 4c-2.67 0-8 1.34-8 4v2h16v-2c0-2.66-5.33-4-8-4z"
ICON_EMAIL = "M20 4H4c-1.1 0-1.99.9-1.99 2L2 18c0 1.1.9 2 2 2h16c1.1 0 2-.9 2-2V6c0-1.1-.9-2-2-2zm0 4l-8 5-8-5V6l8 5 8-5v2z"
ICON_PHONE = "M6.62 10.79c1.44 2.83 3.76 5.14 6.59 6.59l2.2-2.2c.27-.27.67-.36 1.02-.24 1.12.37 2.33.57 3.57.57.55 0 1 .45 1 1V20c0 .55-.45 1-1 1-9.39 0-17-7.61-17-17 0-.55.45-1 1-1h3.5c.55 0 1 .45 1 1 0 1.25.2 2.45.57 3.57.11.35.03.74-.25 1.02l-2.2 2.2z"
ICON_CNIC = "M20 4H4c-1.1 0-2 .9-2 2v12c0 1.1.9 2 2 2h16c1.1 0 2-.9 2-2V6c0-1.1-.9-2-2-2zm-1 11.5h-4v-1h4v1zm0-2.5h-4v-1h4v1zm-8-3c1.66 0 3 1.34 3 3s-1.34 3-3 3-3-1.34-3-3 1.34-3 3-3zm6-3H4v-1h11v1z"
ICON_CAL = "M19 3h-1V1h-2v2H8V1H6v2H5c-1.11 0-1.99.9-1.99 2L3 19c0 1.1.89 2 2 2h14c1.1 0 2-.9 2-2V5c0-1.1-.9-2-2-2zm0 16H5V8h14v11z"
ICON_LOCK = "M18 8h-1V6c0-2.76-2.24-5-5-5S7 3.24 7 6v2H6c-1.1 0-2 .9-2 2v10c0 1.1.9 2 2 2h12c1.1 0 2-.9 2-2V10c0-1.1-.9-2-2-2zm-6 9c-1.1 0-2-.9-2-2s.9-2 2-2 2 .9 2 2-.9 2-2 2zm3.1-9H8.9V6c0-1.71 1.39-3.1 3.1-3.1 1.71 0 3.1 1.39 3.1 3.1v2z"


def show_signup():
    render_auth_card_open(
        "Create Account",
        "Join us and start your learning journey",
        ICON_USER_ADD,
    )

    with st.form("signup_form", clear_on_submit=False):
        render_field_label(ICON_USER_ADD, "Full Name")
        full_name = st.text_input(
            "",
            placeholder="Enter your name (e.g., Easha Akram)",
            label_visibility="collapsed",
            key="su_fullname",
        )
        name_status, name_msg = validate_name(full_name)
        render_validation(name_status, name_msg)

        render_field_label(ICON_EMAIL, "Email Address")
        email = st.text_input(
            "",
            placeholder="Enter your email (e.g., easha@dsa.com)",
            label_visibility="collapsed",
            key="su_email",
        )
        email_status, email_msg = validate_email(email)
        render_validation(email_status, email_msg)

        render_field_label(ICON_PHONE, "Phone Number")
        phone = st.text_input(
            "",
            placeholder="Enter phone number (e.g., 03001234567)",
            max_chars=11,
            label_visibility="collapsed",
            key="su_phone",
        )
        phone_status, phone_msg = validate_phone_live(phone)
        render_validation(phone_status, phone_msg)

        render_field_label(ICON_CNIC, "CNIC Number")
        cnic = st.text_input(
            "",
            placeholder="Enter 13-digit CNIC (e.g., 3520112345671)",
            max_chars=13,
            label_visibility="collapsed",
            key="su_cnic",
        )
        cnic_status, cnic_msg = validate_cnic_live(cnic)
        render_validation(cnic_status, cnic_msg)

        render_field_label(ICON_CAL, "Date of Birth")
        dob = st.date_input(
            "",
            min_value=date(1950, 1, 1),
            max_value=date.today(),
            label_visibility="collapsed",
            key="su_dob",
        )
        render_validation("ok" if dob else "neutral", "Select your date of birth")

        render_field_label(ICON_LOCK, "Password")
        password = st.text_input(
            "",
            type="password",
            placeholder="Enter a secure password (minimum 8 characters)",
            label_visibility="collapsed",
            key="su_password",
        )
        render_password_strength(password)

        st.markdown("<div style='margin-bottom: 8px;'></div>", unsafe_allow_html=True)
        submit_button = st.form_submit_button(
            "Create Account",
            use_container_width=True,
            type="primary",
        )

    if submit_button:
        if not (full_name.strip() and email.strip() and phone.strip() and cnic.strip() and password.strip()):
            st.error("Please fill out all the fields before submitting!")
        elif name_status != "ok":
            st.error("Please enter a valid full name.")
        elif email_status != "ok":
            st.error("Please enter a valid email address.")
        elif not (phone.strip().startswith("03") and len(phone.strip()) == 11 and phone.strip().isdigit()):
            st.error("Invalid Phone Number!")
        elif not (len(cnic.strip()) == 13 and cnic.strip().isdigit()):
            st.error("Invalid CNIC!")
        elif validate_password_strength(password)[0] not in ("ok", "warn"):
            st.error("Password is too weak. Use at least 8 characters.")
        else:
            user_data = {
                "full_name": full_name.strip(),
                "email": email.strip().lower(),
                "phone": phone.strip(),
                "cnic": cnic.strip(),
                "dob": str(dob),
                "password": password.strip(),
            }

            os.makedirs("data", exist_ok=True)
            file_path = "data/users.json"

            if os.path.exists(file_path):
                with open(file_path, "r") as file:
                    try:
                        users = json.load(file)
                    except json.JSONDecodeError:
                        users = []
            else:
                users = []

            if isinstance(users, dict):
                users = [users]

            users.append(user_data)

            with open(file_path, "w") as file:
                json.dump(users, file, indent=4)

            st.success("Account Created Successfully!")
            st.session_state.page = "auth"
            st.session_state.auth_page = "login"
            st.rerun()

    st.markdown(
        '<div class="auth-divider"><span>Already have an account?</span></div>',
        unsafe_allow_html=True,
    )

    if st.button("Sign In", key="auth_secondary", use_container_width=True):
        st.session_state.page = "auth"
        st.session_state.auth_page = "login"
        st.rerun()

    render_auth_card_close()
