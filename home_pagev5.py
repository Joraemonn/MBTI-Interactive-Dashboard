import streamlit as st
from utils_ui_pages import load_theme, inject_css_bg, render_side_menu

# Shared chrome stays in the entrypoint while individual pages change.
st.set_page_config(page_title="MBTI Career Quest", page_icon="logov3.png", layout="wide")
page = st.navigation(
    [
        st.Page("home_content.py", title="MBTI Career Quest", default=True),
        st.Page("pages/About.py", title="About", url_path="About"),
        st.Page("pages/explore.py", title="Explore", url_path="explore"),
        st.Page("pages/More.py", title="Find Out More", url_path="More"),
    ],
    position="hidden",
)
load_theme()
inject_css_bg("background.png")
render_side_menu()
page.run()
