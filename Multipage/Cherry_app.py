import streamlit as st
from datetime import date

# Seite konfigurieren
st.set_page_config(
    page_icon="🍒",
    page_title="Cherry Task Manager",
    layout="centered"
)

st.sidebar.success("Select a demo above.")

# Hintergrundfarbe anpassen
st.markdown(
    """
    <style>
    body {
        background-color: #ffdbe4;
    }
    .stApp {
        background-color: #ffdbe4;
    }
    </style>
    """,
    unsafe_allow_html=True
)
# Titel und Untertitel
st.markdown(
    "<h1 style='color:#d72660; text-align:center;'>🍒 Cherry Task Manager 🍒</h1>",
    unsafe_allow_html=True
)
st.markdown('<span style="color: #00965c; font-size: 22px; text-align:center;">🍒 Willkommen bei Cherry Task Manager! Erstelle To Do Listen 🍒</span>', unsafe_allow_html=True)


