import streamlit as st
from datetime import date
from task_storage import load_tasks, save_tasks, load_lists, save_lists

if 'tasks' not in st.session_state:
    st.session_state['tasks'] = load_tasks()
if 'lists' not in st.session_state:
    st.session_state['lists'] = load_lists()

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

# Titel
st.markdown(
    "<h1 style='color:#d72660; text-align:center;'>🍒 Cherry Task Manager 🍒</h1>",
    unsafe_allow_html=True
)

# Session State initialisieren
if 'tasks' not in st.session_state:
    st.session_state['tasks'] = load_tasks()

# Listen initialisieren
if "lists" not in st.session_state:
    st.session_state.lists = ["Allgemein"]

# Neue Liste hinzufügen
new_list = st.text_input("Neue Liste anlegen", key="new_list")
if st.button("Liste hinzufügen"):
    if new_list and new_list not in st.session_state.lists:
        st.session_state.lists.append(new_list)
        save_lists(st.session_state.lists)
        st.success(f"Liste '{new_list}' hinzugefügt!")
# Eingabefelder
due_date = st.date_input("Fälligkeitsdatum auswählen", value=date.today())
reminder_date = st.date_input("Erinnerungsdatum wählen", value=date.today())
subject = st.text_input("Aufgabenbetreff eingeben")
description = st.text_area("Beschreibung einfügen")
priority = st.selectbox("Priorität wählen", ["High", "Medium", "Low"])

# Liste für neue Aufgabe auswählen
selected_list = st.selectbox("Liste auswählen", st.session_state.lists, key="select_list")

# Aufgabe speichern (jetzt mit Listen-Zuordnung)
if st.button("Aufgabe hinzufügen"):
    if subject:  # nur speichern, wenn Betreff nicht leer
        task = {
            "Fällig am": due_date,
            "Erinnerung am": reminder_date,
            "Betreff": subject,
            "Beschreibung": description,
            "Priorität": priority,
            "Erledigt": False,
            "Liste": selected_list
        }
        st.session_state.tasks.append(task)
        save_tasks(st.session_state['tasks'])
        st.success("Aufgabe hinzugefügt!")
    else:
        st.warning("Bitte gib einen Aufgabenbetreff ein.")
