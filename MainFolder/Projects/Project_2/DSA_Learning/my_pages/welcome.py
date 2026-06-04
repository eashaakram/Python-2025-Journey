import streamlit as st

from my_pages.layout import ACCENT_CYAN, BORDER, TEXT_MUTED


def show_welcome():
    st.markdown(
        """
        <div class="hero-section" style="text-align:center; padding: 12px 0 24px 0;">
            <h2 style="font-size:1.85rem; font-weight:800; color:#ffffff; margin-bottom:8px;">
                Welcome to my Frontend Project
            </h2>
            <p style="color:#9ca3af; font-size:0.95rem; max-width:360px; margin:0 auto; line-height:1.55;">
                An interactive DSA learning platform designed for students who want to master
                Data Structures &amp; Algorithms through stunning visualizations and smooth animations.
            </p>
        </div>
        """,
        unsafe_allow_html=True,
    )

    st.markdown(
        f"""
        <div style="background-color:#1a1d24; padding:14px 18px; border-radius:12px;
                    border:1px solid {BORDER}; text-align:center; margin-bottom:22px;">
            <p style="color:#ffffff; font-size:0.9rem; margin:0; line-height:1.55;">
                <b>What is this website?</b><br>
                This platform animates dry code into real-time visuals. Watch how data structures
                move, change, and sort instantly.
            </p>
        </div>
        """,
        unsafe_allow_html=True,
    )

    col_feat1, col_feat2, col_feat3 = st.columns(3)

    with col_feat1:
        st.markdown(
            f"""
            <div style="background-color:#161616; padding:14px; border-radius:10px; min-height:110px;
                        text-align:center; border:1px solid {BORDER}; border-top:3px solid {ACCENT_CYAN};">
                <h5 style="color:{ACCENT_CYAN}; margin:0 0 6px 0; font-size:0.85rem;">Sorting &amp; Searching</h5>
                <p style="color:{TEXT_MUTED}; font-size:0.75rem; margin:0;">Animate Bubble Sort and Binary Search live.</p>
            </div>
            """,
            unsafe_allow_html=True,
        )

    with col_feat2:
        st.markdown(
            f"""
            <div style="background-color:#161616; padding:14px; border-radius:10px; min-height:110px;
                        text-align:center; border:1px solid {BORDER}; border-top:3px solid {ACCENT_CYAN};">
                <h5 style="color:{ACCENT_CYAN}; margin:0 0 6px 0; font-size:0.85rem;">Data Structures</h5>
                <p style="color:{TEXT_MUTED}; font-size:0.75rem; margin:0;">See Linked Lists and Queues in action.</p>
            </div>
            """,
            unsafe_allow_html=True,
        )

    with col_feat3:
        st.markdown(
            f"""
            <div style="background-color:#161616; padding:14px; border-radius:10px; min-height:110px;
                        text-align:center; border:1px solid {BORDER}; border-top:3px solid {ACCENT_CYAN};">
                <h5 style="color:{ACCENT_CYAN}; margin:0 0 6px 0; font-size:0.85rem;">Advanced Trees</h5>
                <p style="color:{TEXT_MUTED}; font-size:0.75rem; margin:0;">Visualize BST and AVL Trees step-by-step.</p>
            </div>
            """,
            unsafe_allow_html=True,
        )

    st.markdown("<div style='margin-bottom: 20px;'></div>", unsafe_allow_html=True)

    c1, c2, c3 = st.columns([1, 1.4, 1])
    with c2:
        if st.button("Begin Your DSA Journey", key="btn_welcome_start", use_container_width=True):
            st.session_state.page = "auth"
            st.session_state.auth_page = "login"
            st.rerun()

    st.markdown(
        """
        <p style="text-align:center; color:#9ca3af; font-size:0.8rem; margin-top:10px;">
            Or use the navigation above to Sign In / Sign Up
        </p>
        """,
        unsafe_allow_html=True,
    )
