from pathlib import Path

import streamlit as st

st.set_page_config(page_title="ألعاب CLCJ", page_icon="🏅", layout="wide")

# شيل الهيدر والفوتر وقلّل الهوامش عشان الصفحة تاخد الشاشة كلها
st.markdown(
    """
    <style>
      #MainMenu, footer, header {visibility: hidden;}
      .block-container {padding: 0.4rem 0.4rem 0 0.4rem; max-width: 100%;}
    </style>
    """,
    unsafe_allow_html=True,
)

page = Path(__file__).parent / "clcj_games_offline.html"

if hasattr(st, "iframe"):  # النسخ الجديدة من Streamlit
    st.iframe(page, height=1100)
else:  # نسخ أقدم
    import streamlit.components.v1 as components

    components.html(page.read_text(encoding="utf-8"), height=1100, scrolling=True)
