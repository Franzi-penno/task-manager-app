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
st.markdown('<span style="color: #00965c; font-size: 22px; text-align:center;">🍒 Willkommen bei unserem Cherry Task Manager! Erstelle To Do Listen 🍒</span>', unsafe_allow_html=True)
st.markdown('<span style="color: #00965c; font-size: 22px; text-align:center;">sahnecake better be not late</span>', unsafe_allow_html=True)
st.markdown('<span style="color: #00965c; font-size: 22px; text-align:center;">or your organisation is fake.</span>', unsafe_allow_html=True)
st.markdown('<span style="color: #00965c; font-size: 22px; text-align:center;">be aware of the cherry</span>', unsafe_allow_html=True)
st.markdown('<span style="color: #00965c; font-size: 22px; text-align:center;">because its important when you marry</span>', unsafe_allow_html=True)
st.markdown('<span style="color: #00965c; font-size: 22px; text-align:center;">so youre not gonna be a larry</span>', unsafe_allow_html=True)
st.markdown('<span style="color: #00965c; font-size: 22px; text-align:center;">but never forget the alkohol in the sahne</span>', unsafe_allow_html=True)
st.markdown('<span style="color: #00965c; font-size: 22px; text-align:center;">because I would miss your fahne</span>', unsafe_allow_html=True)
st.markdown('<span style="color: #00965c; font-size: 22px; text-align:center;">and one recomendation</span>', unsafe_allow_html=True)
st.markdown('<span style="color: #00965c; font-size: 22px; text-align:center;">better be on time</span>', unsafe_allow_html=True)
st.markdown('<span style="color: #00965c; font-size: 22px; text-align:center;">then everything is fine</span>', unsafe_allow_html=True)

