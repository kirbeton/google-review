import streamlit as st

# =========================
# Google Review URL
# =========================

GOOGLE_REVIEW_URL = "https://www.google.com/search?q=%D7%A4%D7%99%D7%A6%D7%94+%D7%A9%D7%99%D7%A8%D7%95%D7%A7%D7%95&sca_esv=8b590ccd188bc65d&sxsrf=APpeQntiHbWoQB6zq7r4bihYhZ1huOydeQ%3A1790184622842&ei=rgy0auvwMuzYhbIP0JS70QI&biw=1920&bih=912&oq=%D7%A4%D7%99%D7%A6%D7%94+%D7%A9%D7%99%D7%A8&gs_lp=Egxnd3Mtd2l6LXNlcnAiD9ek15nXpteUINep15nXqCoFCAIYgAQyBRAAGIAEMgUQABiABDIFEAAYgAQyBRAAGIAEMgUQABiABDIFEAAYgAQyCxAuGIAEGMcBGK8BMgUQABiABDIFEAAYgAQyBRAAGIAESKmJAVDqAljnenADeAGQAQCYAd0BoAHyB6oBBTAuNC4yuAEByAEA-AEBmAIJoAKlCMICChAAGEcY1gQYsAPCAg0QABiABBiKBRhDGLADwgIXEC4Y3AYYuAYY2gYY2AIYyAMYsAPYAQHCAggQABiABBjLAcICEBAuGIAEGIoFGEMYxwEY0QPCAgoQABiABBiKBRhDwgIFEC4YgATCAgYQABgWGB7CAggQABgWGB4YCsICBxAAGIAEGA3CAgcQLhiABBgNwgIGEAAYHhgNmAMAiAYBkAYRugYGCAEQARgZkgcFMy40LjKgB5MzsgcFMC40LjK4B5AIwgcHMC4yLjYuMcgHJoAIAQ&sclient=gws-wiz-serp#sv=CAESzQEKuQEStgEKd0FKaVQ0dElnSF9fWlR5NWt4QW15V2RBeC04RkZaTUxVbVpESUY0NWxNZ2RfMUVCN0hXMF9kUHVJZkNnckRiRDRyaC1POEl1eWg0Q3dCeF9pQ1RCWEhVb3ZQY1RDZVB3OXZUZlI2ZGg3Q1kybzFXMndFVEtxdHk4Ehc1d3kwYXYteUR0T09oYklQNGRxSWdBbxoiQURzcjlmU1poVUVmTGRXUVJkM3NwMzhKUjljSGNQUG9ZQRIEODA1MRoBMyoAMAA4AUAAGAAgx5XC8Qk6AEoCEAE"


# =========================
# Page config
# =========================

st.set_page_config(
    page_title="דרגו אותנו בגוגל",
    page_icon="⭐",
    layout="centered",
    initial_sidebar_state="collapsed"
)


# =========================
# CSS
# =========================

st.markdown(
    """
    <style>

    /* ---------- Streamlit ---------- */

    #MainMenu {
        visibility: hidden;
    }

    footer {
        visibility: hidden;
    }

    header {
        visibility: hidden;
    }

    [data-testid="stToolbar"] {
        display: none !important;
    }

    [data-testid="stDecoration"] {
        display: none !important;
    }

    [data-testid="stStatusWidget"] {
        display: none !important;
    }


    /* ---------- Background ---------- */

    html,
    body,
    .stApp,
    [data-testid="stAppViewContainer"],
    [data-testid="stMain"] {

        background: #ffffff !important;
    }


    /* ---------- Main Streamlit container ---------- */

    .block-container {

        max-width: 560px !important;

        padding-top: 12vh !important;
        padding-bottom: 30px !important;

        padding-left: 20px !important;
        padding-right: 20px !important;

        margin: auto !important;
    }


    /* ---------- Google logo ---------- */

    [data-testid="stImage"] {

        display: flex;
        justify-content: center;

        margin-bottom: 15px;
    }


    /* ---------- Text ---------- */

    .title {

        text-align: center;

        font-family:
            Arial,
            Helvetica,
            sans-serif;

        color: #202124;

        font-size: 32px;
        font-weight: 700;

        margin-top: 5px;
        margin-bottom: 8px;
    }


    .subtitle {

        text-align: center;

        font-family:
            Arial,
            Helvetica,
            sans-serif;

        color: #70757a;

        font-size: 17px;

        margin-bottom: 30px;
    }


/* ---------- Stars row ---------- */

/* שומר על כל 5 הכוכבים בשורה אחת */
[data-testid="stHorizontalBlock"] {
    display: flex !important;
    flex-direction: row !important;
    flex-wrap: nowrap !important;

    width: 100% !important;

    gap: 2px !important;

    align-items: flex-start !important;
    justify-content: center !important;
}

/* כל כוכב מקבל חמישית מהשורה */
[data-testid="stHorizontalBlock"] > div {
    flex: 1 1 20% !important;
    width: 20% !important;
    min-width: 0 !important;
}


/* ---------- Star buttons ---------- */

/* גם link_button וגם button */
.stLinkButton,
.stButton {
    display: flex !important;
    justify-content: center !important;
    width: 100% !important;
}


/* הכפתורים עצמם */
.stLinkButton > a,
.stButton > button {
    background: transparent !important;

    border: none !important;
    box-shadow: none !important;

    padding: 0 !important;

    width: 100% !important;

    min-height: 95px !important;
    height: 95px !important;

    display: flex !important;
    align-items: center !important;
    justify-content: center !important;

    color: #fbbc04 !important;

    text-decoration: none !important;

    transition: transform 0.15s ease;
}


/* הכוכב עצמו */
.stLinkButton a p,
.stLinkButton a span,
.stButton button p,
.stButton button span {
    font-size: 75px !important;

    line-height: 1 !important;

    color: #fbbc04 !important;

    margin: 0 !important;
    padding: 0 !important;
}


/* Hover - זהה לכולם */
.stLinkButton > a:hover,
.stButton > button:hover {
    background: transparent !important;

    border: none !important;
    box-shadow: none !important;

    color: #fbbc04 !important;

    transform: scale(1.08);
}


/* לחיצה / פוקוס */
.stLinkButton > a:focus,
.stLinkButton > a:active,
.stLinkButton > a:visited,
.stButton > button:focus,
.stButton > button:active {
    background: transparent !important;

    border: none !important;
    box-shadow: none !important;

    color: #fbbc04 !important;
}


/* מונע מ-Streamlit לשנות את צבע הכוכב */
.stButton > button:hover p,
.stButton > button:hover span,
.stButton > button:focus p,
.stButton > button:focus span,
.stButton > button:active p,
.stButton > button:active span {
    color: #fbbc04 !important;
}


/* ---------- Rating numbers ---------- */

.rating-number {
    text-align: center;

    color: #4a4a4a;

    font-family: Arial, Helvetica, sans-serif;

    font-size: 28px;
    font-weight: 700;

    line-height: 1;

    margin-top: 8px;
}

/* ---------- Thank you message ---------- */

.thank-you {
    text-align: center;
    direction: rtl;

    color: #202124;

    font-family: Arial, Helvetica, sans-serif;

    font-size: 24px;
    font-weight: 700;

    margin-top: 35px;
}

    /* ---------- Mobile ---------- */

    @media (max-width: 600px) {

        .block-container {

            padding-top: 15vh !important;

            padding-left: 18px !important;
            padding-right: 18px !important;
        }


        .title {

            font-size: 27px;
        }


        .subtitle {

            font-size: 16px;

            margin-bottom: 25px;
        }


        .stLinkButton > a {
    min-height: 95px !important;
    height: 95px !important;
}

.stLinkButton a p,
.stLinkButton a span {
    font-size: 70px !important;
}


        [data-testid="stHorizontalBlock"] {

            gap: 2px !important;
        }
    }


    /* ---------- Very small phones ---------- */

    @media (max-width: 360px) {

        .title {

            font-size: 24px;
        }


        .subtitle {

            font-size: 15px;
        }


        .stLinkButton > a {

            font-size: 100px !important;
        }
    }

    </style>
    """,
    unsafe_allow_html=True
)


# =========================
# Google logo
# =========================

st.image(
    "https://www.gstatic.com/firebasejs/ui/2.0.0/images/auth/google.svg",
    width=80
)


# =========================
# Title
# =========================

st.markdown(
    """
    <div class="title">
        דרגו אותנו בגוגל
    </div>
    """,
    unsafe_allow_html=True
)


st.markdown(
    """
    <div class="subtitle">
        לחצו על כוכב כדי לדרג אותנו
    </div>
    """,
    unsafe_allow_html=True
)


# =========================
# Stars / Thank you
# =========================

# אם כבר נבחר דירוג של 1-3,
# מסתירים את הכוכבים ומציגים תודה
if st.session_state.get("rating") in [1, 2, 3]:

    st.markdown(
        """
        <div class="thank-you">
            🙏 תודה על הדירוג!
        </div>
        """,
        unsafe_allow_html=True
    )

else:

    # הסדר על המסך:
    # 5  ★ ★ ★ ★ ★  1

    col5, col4, col3, col2, col1 = st.columns(5)


    # ⭐ 5 - פותח Google
    with col5:
        st.link_button(
            "★",
            GOOGLE_REVIEW_URL,
            use_container_width=True
        )

        st.markdown(
            '<div class="rating-number">5</div>',
            unsafe_allow_html=True
        )


    # ⭐ 4 - פותח Google
    with col4:
        st.link_button(
            "★",
            GOOGLE_REVIEW_URL,
            use_container_width=True
        )


    # ⭐ 3 - נשאר באתר
    with col3:
        if st.button(
            "★",
            key="rating_3",
            use_container_width=True
        ):
            st.session_state["rating"] = 3
            st.rerun()


    # ⭐ 2 - נשאר באתר
    with col2:
        if st.button(
            "★",
            key="rating_2",
            use_container_width=True
        ):
            st.session_state["rating"] = 2
            st.rerun()


    # ⭐ 1 - נשאר באתר
    with col1:
        if st.button(
            "★",
            key="rating_1",
            use_container_width=True
        ):
            st.session_state["rating"] = 1
            st.rerun()

        st.markdown(
            '<div class="rating-number">1</div>',
            unsafe_allow_html=True
        )

# =========================
# Thank you message
# =========================

if st.session_state.get("rating") in [1, 2, 3]:
    st.markdown(
        """
        <div class="thank-you">
            תודה על הדירוג! 🙏
        </div>
        """,
        unsafe_allow_html=True
    )