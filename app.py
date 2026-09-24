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


    /* ---------- Columns ---------- */

    [data-testid="stHorizontalBlock"] {

        gap: 8px !important;

        align-items: center;

        justify-content: center;
    }


    /* ---------- Link buttons ---------- */

    .stLinkButton {

        display: flex;

        justify-content: center;
    }


    .stLinkButton > a {

        background: transparent !important;

        border: none !important;

        box-shadow: none !important;

        padding: 0 !important;

        min-height: auto !important;

        height: auto !important;

        width: 100% !important;

        color: #fbbc04 !important;

        font-size: 45px !important;

        line-height: 1 !important;

        text-decoration: none !important;

        transition: transform 0.15s ease;
    }


    .stLinkButton > a:hover {

        background: transparent !important;

        border: none !important;

        color: #fbbc04 !important;

        transform: scale(1.12);
    }


    .stLinkButton > a:focus {

        box-shadow: none !important;

        color: #fbbc04 !important;
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

            font-size: 40px !important;
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

            font-size: 35px !important;
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
# Stars
# =========================

col1, col2, col3, col4, col5 = st.columns(5)

with col1:
    st.link_button(
        "★",
        GOOGLE_REVIEW_URL,
        use_container_width=True
    )

with col2:
    st.link_button(
        "★",
        GOOGLE_REVIEW_URL,
        use_container_width=True
    )

with col3:
    st.link_button(
        "★",
        GOOGLE_REVIEW_URL,
        use_container_width=True
    )

with col4:
    st.link_button(
        "★",
        GOOGLE_REVIEW_URL,
        use_container_width=True
    )

with col5:
    st.link_button(
        "★",
        GOOGLE_REVIEW_URL,
        use_container_width=True
    )