import re

import streamlit as st

# Design tokens — match codeflames.netlify.app reference
BRAND_NAME = "DSA Visualizer"
BRAND_TAGLINE = "Master Data Structures & Algorithms"
ACCENT = "#5d78ff"
ACCENT_HOVER = "#4962e6"
ACCENT_CYAN = "#00BFFF"
BG_DARK = "#12151a"
BG_CARD = "#1a1d24"
BORDER = "#2a2f38"
TEXT_MUTED = "#9ca3af"
AUTH_MAX_WIDTH = "440px"


def inject_global_styles(layout_mode="app"):
    """Inject site-wide CSS. layout_mode: 'auth' (narrow centered) or 'app' (wide content)."""
    max_width = AUTH_MAX_WIDTH if layout_mode == "auth" else "1200px"

    st.markdown(
        f"""
        <style>
        [data-testid="stSidebar"] {{ display: none; }}
        [data-testid="collapsedControl"] {{ display: none; }}
        #MainMenu {{ visibility: hidden; }}
        footer {{ visibility: hidden; }}
        header[data-testid="stHeader"] {{
            background: transparent;
        }}

        .block-container {{
            max-width: {max_width} !important;
            padding-top: 1rem !important;
            padding-left: 1rem !important;
            padding-right: 1rem !important;
            margin-left: auto !important;
            margin-right: auto !important;
        }}

        .site-shell-header {{
            background: linear-gradient(180deg, #1a1d24 0%, #12151a 100%);
            border-bottom: 1px solid {BORDER};
            border-radius: 0 0 12px 12px;
            padding: 14px 18px 12px 18px;
            margin-bottom: 8px;
        }}
        .site-brand-row {{
            display: flex;
            align-items: center;
            gap: 12px;
            margin-bottom: 10px;
        }}
        .site-avatar {{
            width: 42px;
            height: 42px;
            border-radius: 50%;
            background: linear-gradient(135deg, {ACCENT}, {ACCENT_CYAN});
            display: flex;
            align-items: center;
            justify-content: center;
            color: white;
            font-weight: 700;
            font-size: 14px;
            flex-shrink: 0;
            box-shadow: 0 0 14px rgba(93, 120, 255, 0.35);
        }}
        .site-brand-text h1 {{
            font-size: 1.15rem;
            font-weight: 700;
            margin: 0;
            color: #ffffff;
            line-height: 1.2;
        }}
        .site-brand-text p {{
            font-size: 0.78rem;
            color: {TEXT_MUTED};
            margin: 2px 0 0 0;
        }}

        .site-nav-label {{
            font-size: 0.72rem;
            color: {TEXT_MUTED};
            text-transform: uppercase;
            letter-spacing: 0.06em;
            margin-bottom: 6px;
        }}

        div.stButton > button[key="nav_home"],
        div.stButton > button[key="nav_login"],
        div.stButton > button[key="nav_signup"] {{
            background-color: #252a33 !important;
            color: #e5e7eb !important;
            border: 1px solid {BORDER} !important;
            border-radius: 8px !important;
            font-size: 0.82rem !important;
            font-weight: 600 !important;
            padding: 0.35rem 0.5rem !important;
            min-height: 2rem !important;
        }}
        div.stButton > button[key="nav_home"]:hover,
        div.stButton > button[key="nav_login"]:hover,
        div.stButton > button[key="nav_signup"]:hover {{
            background-color: {ACCENT} !important;
            color: white !important;
            border-color: {ACCENT} !important;
        }}

        .site-footer {{
            margin-top: 2.5rem;
            padding: 18px 12px 24px 12px;
            border-top: 1px solid {BORDER};
            text-align: center;
        }}
        .site-footer p {{
            margin: 0;
            color: {TEXT_MUTED};
            font-size: 0.78rem;
            line-height: 1.6;
        }}
        .site-footer .footer-brand {{
            color: {ACCENT_CYAN};
            font-weight: 600;
        }}

        .auth-card {{
            background: {BG_CARD};
            border: 1px solid {BORDER};
            border-radius: 16px;
            padding: 28px 22px 22px 22px;
            margin: 8px auto 0 auto;
            box-shadow: 0 8px 32px rgba(0, 0, 0, 0.25);
        }}
        .auth-card-icon {{
            display: flex;
            justify-content: center;
            margin-bottom: 16px;
        }}
        .auth-card-icon-inner {{
            background: linear-gradient(135deg, {ACCENT_CYAN}, {ACCENT});
            width: 72px;
            height: 72px;
            border-radius: 50%;
            display: flex;
            align-items: center;
            justify-content: center;
            box-shadow: 0 0 20px rgba(93, 120, 255, 0.35);
        }}
        .auth-title {{
            text-align: center;
            color: #ffffff;
            font-size: 1.45rem;
            font-weight: 700;
            margin: 0 0 4px 0;
        }}
        .auth-subtitle {{
            text-align: center;
            color: {TEXT_MUTED};
            font-size: 0.9rem;
            margin: 0 0 22px 0;
        }}

        .field-label-row {{
            display: flex;
            align-items: center;
            gap: 8px;
            margin-bottom: 4px;
            color: #ffffff;
            font-size: 0.85rem;
            font-weight: 500;
        }}
        .field-label-row svg {{
            flex-shrink: 0;
        }}

        div.stTextInput > div > div > input,
        div.stDateInput > div > div > input {{
            background-color: #f0f8ff !important;
            color: #111827 !important;
            border: 1px solid #3d4450 !important;
            border-radius: 10px !important;
            padding: 10px 12px !important;
        }}
        div.stTextInput > div > div > input:focus,
        div.stDateInput > div > div > input:focus {{
            border-color: {ACCENT} !important;
            box-shadow: 0 0 0 2px rgba(93, 120, 255, 0.2) !important;
        }}

        .validation-msg {{
            font-size: 0.78rem;
            margin: 4px 0 10px 0;
            padding: 0 2px;
        }}
        .validation-ok {{ color: #34d399; }}
        .validation-warn {{ color: #fbbf24; }}
        .validation-error {{ color: #f87171; }}
        .validation-neutral {{ color: {TEXT_MUTED}; }}

        .strength-bar-wrap {{
            height: 4px;
            background: #2a2f38;
            border-radius: 4px;
            margin: 6px 0 4px 0;
            overflow: hidden;
        }}
        .strength-bar-fill {{
            height: 100%;
            border-radius: 4px;
            transition: width 0.2s ease;
        }}

        div.stFormSubmitButton > button {{
            background-color: {ACCENT} !important;
            color: white !important;
            border: none !important;
            border-radius: 10px !important;
            font-weight: 600 !important;
            min-height: 46px !important;
        }}
        div.stFormSubmitButton > button:hover {{
            background-color: {ACCENT_HOVER} !important;
        }}

        div.stButton > button[key="auth_primary"],
        div.stFormSubmitButton > button[key="auth_primary"] {{
            background-color: {ACCENT} !important;
            color: white !important;
            border: none !important;
            border-radius: 10px !important;
            font-weight: 600 !important;
            min-height: 46px !important;
        }}
        div.stButton > button[key="auth_primary"]:hover,
        div.stFormSubmitButton > button[key="auth_primary"]:hover {{
            background-color: {ACCENT_HOVER} !important;
        }}

        div.stButton > button[key="auth_secondary"] {{
            background-color: #252a33 !important;
            color: #e5e7eb !important;
            border: 1px solid {BORDER} !important;
            border-radius: 10px !important;
            font-weight: 600 !important;
            min-height: 46px !important;
        }}
        div.stButton > button[key="auth_secondary"]:hover {{
            background-color: #2f3640 !important;
        }}

        div.stButton > button[key="auth_demo"] {{
            background-color: transparent !important;
            color: {ACCENT_CYAN} !important;
            border: 1px dashed {ACCENT_CYAN} !important;
            border-radius: 10px !important;
            font-weight: 600 !important;
            min-height: 46px !important;
        }}

        [data-testid="stForm"] {{
            border: none !important;
            padding: 0 !important;
            background: transparent !important;
        }}

        div.stTextInput, div.stDateInput {{
            margin-top: 8px !important;
            margin-bottom: 0 !important;
        }}

        .auth-divider {{
            border-top: 1px solid {BORDER};
            margin: 20px 0;
            position: relative;
            text-align: center;
        }}
        .auth-divider span {{
            position: absolute;
            top: -10px;
            left: 50%;
            transform: translateX(-50%);
            background: {BG_CARD};
            padding: 0 12px;
            color: {TEXT_MUTED};
            font-size: 0.75rem;
        }}

        .hero-section h2 {{
            font-size: 1.75rem;
            font-weight: 700;
            margin-bottom: 8px;
            color: #ffffff;
        }}
        .hero-section p {{
            font-size: 1rem;
            color: {TEXT_MUTED};
        }}

        div.stButton > button[key="btn_welcome_start"] {{
            background-color: {ACCENT} !important;
            color: white !important;
            border: none !important;
            border-radius: 12px !important;
            font-weight: 700 !important;
            box-shadow: 0 0 15px rgba(93, 120, 255, 0.45) !important;
        }}
        div.stButton > button[key="btn_welcome_start"]:hover {{
            background-color: {ACCENT_HOVER} !important;
        }}

        div.stButton > button[key="btn_logout"] {{
            background-color: {ACCENT} !important;
            color: white !important;
            border-radius: 8px !important;
            border: none !important;
            font-weight: 600 !important;
        }}
        </style>
        """,
        unsafe_allow_html=True,
    )


def render_site_header(student_label="4th Semester Student"):
    st.markdown(
        f"""
        <div class="site-shell-header">
            <div class="site-brand-row">
                <div class="site-avatar">UR</div>
                <div class="site-brand-text">
                    <h1>{BRAND_NAME}</h1>
                    <p>{student_label}</p>
                </div>
            </div>
        </div>
        """,
        unsafe_allow_html=True,
    )

    st.markdown('<div class="site-nav-label">Navigation</div>', unsafe_allow_html=True)
    nav1, nav2, nav3 = st.columns(3)
    with nav1:
        if st.button("Home", key="nav_home", use_container_width=True):
            st.session_state.page = "welcome"
            st.rerun()
    with nav2:
        if st.button("Login", key="nav_login", use_container_width=True):
            st.session_state.page = "auth"
            st.session_state.auth_page = "login"
            st.rerun()
    with nav3:
        if st.button("Signup", key="nav_signup", use_container_width=True):
            st.session_state.page = "auth"
            st.session_state.auth_page = "signup"
            st.rerun()


def render_site_footer():
    st.markdown(
        f"""
        <div class="site-footer">
            <p class="footer-brand">{BRAND_NAME}</p>
            <p>{BRAND_TAGLINE} · Interactive visual learning platform</p>
            <p>© 2025 · Built for students who learn by seeing</p>
        </div>
        """,
        unsafe_allow_html=True,
    )


def render_auth_card_open(title, subtitle, icon_path):
    st.markdown(
        f"""
        <div class="auth-card">
            <div class="auth-card-icon">
                <div class="auth-card-icon-inner">
                    <svg width="36" height="36" viewBox="0 0 24 24" fill="white">
                        <path d="{icon_path}"/>
                    </svg>
                </div>
            </div>
            <h2 class="auth-title">{title}</h2>
            <p class="auth-subtitle">{subtitle}</p>
        """,
        unsafe_allow_html=True,
    )


def render_auth_card_close():
    st.markdown("</div>", unsafe_allow_html=True)


def render_field_label(icon_path, label):
    st.markdown(
        f"""
        <div class="field-label-row">
            <svg width="18" height="18" viewBox="0 0 24 24" fill="{ACCENT_CYAN}">
                <path d="{icon_path}"/>
            </svg>
            <span>{label}</span>
        </div>
        """,
        unsafe_allow_html=True,
    )


def render_validation(status, message):
    css_class = {
        "ok": "validation-ok",
        "warn": "validation-warn",
        "error": "validation-error",
        "neutral": "validation-neutral",
    }.get(status, "validation-neutral")
    st.markdown(
        f'<p class="validation-msg {css_class}">{message}</p>',
        unsafe_allow_html=True,
    )


def validate_name(name):
    name = name.strip()
    if not name:
        return "neutral", "Enter your full name"
    if len(name) < 2:
        return "error", "Name must be at least 2 characters"
    if not re.match(r"^[A-Za-z\s'.-]+$", name):
        return "error", "Name can only contain letters and spaces"
    return "ok", "Name looks good"


def validate_email(email):
    email = email.strip()
    if not email:
        return "neutral", "Enter a valid email address"
    pattern = r"^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$"
    if not re.match(pattern, email):
        return "error", "Invalid email format (e.g. you@example.com)"
    return "ok", "Email format is valid"


def validate_password_strength(password):
    if not password:
        return "neutral", "Use at least 8 characters with letters and numbers", 0, "#2a2f38"

    score = 0
    if len(password) >= 8:
        score += 1
    if re.search(r"[A-Z]", password):
        score += 1
    if re.search(r"[0-9]", password):
        score += 1
    if re.search(r"[^A-Za-z0-9]", password):
        score += 1

    levels = [
        ("error", "Weak — add more characters", 25, "#f87171"),
        ("warn", "Fair — add uppercase or numbers", 50, "#fbbf24"),
        ("warn", "Good — add a special character", 75, "#fbbf24"),
        ("ok", "Strong password", 100, "#34d399"),
    ]
    status, message, width, color = levels[min(score, 3)]
    return status, message, width, color


def render_password_strength(password):
    status, message, width, color = validate_password_strength(password)
    st.markdown(
        f"""
        <div class="strength-bar-wrap">
            <div class="strength-bar-fill" style="width:{width}%; background:{color};"></div>
        </div>
        """,
        unsafe_allow_html=True,
    )
    render_validation(status, message)


def validate_phone_live(phone):
    phone = phone.strip()
    if not phone:
        return "neutral", "Pakistani format: 03XXXXXXXXX (11 digits)"
    if not phone.isdigit():
        return "error", "Phone must contain digits only"
    if not phone.startswith("03"):
        return "error", "Phone must start with 03"
    if len(phone) < 11:
        return "warn", f"{len(phone)}/11 digits entered"
    if len(phone) > 11:
        return "error", "Phone must be exactly 11 digits"
    return "ok", "Phone number is valid"


def validate_cnic_live(cnic):
    cnic = cnic.strip()
    if not cnic:
        return "neutral", "Enter 13-digit CNIC without dashes"
    if not cnic.isdigit():
        return "error", "CNIC must contain digits only"
    if len(cnic) < 13:
        return "warn", f"{len(cnic)}/13 digits entered"
    if len(cnic) > 13:
        return "error", "CNIC must be exactly 13 digits"
    return "ok", "CNIC format is valid"
