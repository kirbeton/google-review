import streamlit as st

# הקישור הישיר של העסק בגוגל
GOOGLE_REVIEW_URL = "https://www.google.com/search?q=%D7%A4%D7%99%D7%A6%D7%94+%D7%A9%D7%99%D7%A8%D7%95%D7%A7%D7%95&sca_esv=8b590ccd188bc65d&sxsrf=APpeQntiHbWoQB6zq7r4bihYhZ1huOydeQ%3A1790184622842&ei=rgy0auvwMuzYhbIP0JS70QI&biw=1920&bih=912&oq=%D7%A4%D7%99%D7%A6%D7%94+%D7%A9%D7%99%D7%A8&gs_lp=Egxnd3Mtd2l6LXNlcnAiD9ek15nXpteUINep15nXqCoFCAIYgAQyBRAAGIAEMgUQABiABDIFEAAYgAQyBRAAGIAEMgUQABiABDIFEAAYgAQyCxAuGIAEGMcBGK8BMgUQABiABDIFEAAYgAQyBRAAGIAESKmJAVDqAljnenADeAGQAQCYAd0BoAHyB6oBBTAuNC4yuAEByAEA-AEBmAIJoAKlCMICChAAGEcY1gQYsAPCAg0QABiABBiKBRhDGLADwgIXEC4Y3AYYuAYY2gYY2AIYyAMYsAPYAQHCAggQABiABBjLAcICEBAuGIAEGIoFGEMYxwEY0QPCAgoQABiABBiKBRhDwgIFEC4YgATCAgYQABgWGB7CAggQABgWGB4YCsICBxAAGIAEGA3CAgcQLhiABBgNwgIGEAAYHhgNmAMAiAYBkAYRugYGCAEQARgZkgcFMy40LjKgB5MzsgcFMC40LjK4B5AIwgcHMC4yLjYuMcgHJoAIAQ&sclient=gws-wiz-serp#sv=CAESzQEKuQEStgEKd0FKaVQ0dElnSF9fWlR5NWt4QW15V2RBeC04RkZaTUxVbVpESUY0NWxNZ2RfMUVCN0hXMF9kUHVJZkNnckRiRDRyaC1POEl1eWg0Q3dCeF9pQ1RCWEhVb3ZQY1RDZVB3OXZUZlI2ZGg3Q1kybzFXMndFVEtxdHk4Ehc1d3kwYXYteUR0T09oYklQNGRxSWdBbxoiQURzcjlmU1poVUVmTGRXUVJkM3NwMzhKUjljSGNQUG9ZQRIEODA1MRoBMyoAMAA4AUAAGAAgx5XC8Qk6AEoCEAE"

st.set_page_config(page_title="דירוג חוויית שירות", layout="centered")

# עיצוב מימין לשמאל ומרכזת את העמוד
st.markdown("""
    <style>
    .main { text-align: center; }
    div[data-testid="stHorizontalBlock"] { justify-content: center; }
    </style>
""", unsafe_allow_html=True)

st.title("איך הייתה החוויה שלך איתנו?")
st.write("נשמח לדעת לדרג מ-1 עד 5")

if "low_rating" not in st.session_state:
    st.session_state.low_rating = False

if not st.session_state.low_rating:
    cols = st.columns(5)

    # 1 עד 3: כפתורים רגילים שפותחים טופס משוב פנימי
    for i in range(1, 4):
        if cols[i - 1].button(f"⭐ {i}", key=f"star_{i}"):
            st.session_state.low_rating = True
            st.rerun()

    # 4 ו-5: כפתורי קישור ישירים לגוגל (נפתחים מיד בלחיצה)
    cols[3].link_button("⭐ 4", GOOGLE_REVIEW_URL)
    cols[4].link_button("⭐ 5", GOOGLE_REVIEW_URL)

# הצגת טופס פנימי לדירוגים 1 עד 3
if st.session_state.low_rating:
    st.subheader("מצטערים לשמוע! נשמח לדעת מה נוכל לשפר:")
    feedback = st.text_area("הערות או הצעות לשיפור:")

    if st.button("שליחה"):
        if feedback:
            with open("feedback_log.txt", "a", encoding="utf-8") as f:
                f.write(f"{feedback}\n---\n")

        st.success("תודה! המשוב שלך התקבל ויטופל בהקדם.")
        st.session_state.low_rating = False