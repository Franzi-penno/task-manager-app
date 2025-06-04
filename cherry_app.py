import streamlit as st
from datetime import date

# Seite konfigurieren
st.set_page_config(
    page_icon="🍒",
    page_title="Cherry Task Manager",
    layout="centered"
)

st.title("Cherry Task Manager")
st.markdown("Herzlich willkommen!")

# Session State initialisieren
if "tasks" not in st.session_state:
    st.session_state.tasks = []

# Eingabefelder
due_date = st.date_input("Fälligkeitsdatum auswählen", value=date.today())
reminder_date = st.date_input("Erinnerungsdatum wählen", value=date.today())
subject = st.text_input("Aufgabenbetreff eingeben")
description = st.text_area("Beschreibung einfügen")
priority = st.selectbox("Priorität wählen", ["High", "Medium", "Low"])

# Aufgabe speichern
if st.button("Aufgabe hinzufügen"):
    if subject:  # nur speichern, wenn Betreff nicht leer
        task = {
            "Fällig am": due_date,
            "Erinnerung am": reminder_date,
            "Betreff": subject,
            "Beschreibung": description,
            "Priorität": priority,
            "Erledigt": False
        }
        st.session_state.tasks.append(task)
        st.success("Aufgabe hinzugefügt!")
    else:
        st.warning("Bitte gib einen Aufgabenbetreff ein.")

# Aufgabenliste anzeigen
if st.session_state.tasks:
    st.subheader("Aufgabenliste")
    for i, task in enumerate(st.session_state.tasks):
        col1, col2 = st.columns([4, 1])
        with col1:
            st.markdown(f"### {task['Betreff']}")
            st.write(f"**Beschreibung:** {task['Beschreibung']}")
            st.write(f"**Fällig am:** {task['Fällig am']}")
            st.write(f"**Erinnerung am:** {task['Erinnerung am']}")
            st.write(f"**Priorität:** {task['Priorität']}")
        with col2:
            done = st.checkbox("Erledigt", key=f"done_{i}")
            if done:
                st.session_state.tasks.pop(i)
                st.experimental_rerun()
        st.markdown("---")
else:
    st.info("Noch keine Aufgaben gespeichert.")

# Hallo Welt das ist eine neue Zeile