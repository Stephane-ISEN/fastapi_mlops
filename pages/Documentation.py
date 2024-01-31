import streamlit.components.v1 as components
import streamlit as st

st.set_page_config(
    page_title="Documentation API",
    page_icon="🧑",
    layout="wide",
)

st.title("Documentation API")

components.html(
"""<iframe
  width="1200"
  height="3000"
  src="https://api-isen-stephane-61231a5c217a.herokuapp.com/docs">
</iframe>
    """,
    height=2000,
)