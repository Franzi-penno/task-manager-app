import streamlit as st
from streamlit_calendar import calendar
from task_storage import load_tasks

if 'tasks' not in st.session_state:
    st.session_state['tasks'] = load_tasks()

st.markdown("<h2 style='color:#d72660;'>📅 Kalenderansicht deiner Aufgaben</h2>", unsafe_allow_html=True)

# Aufgaben in Kalender-Events umwandeln
events = []
for task in st.session_state['tasks']:
    # Nur Aufgaben mit Fälligkeitsdatum anzeigen, die NICHT erledigt oder gelöscht sind
    if (
        "Fällig am" in task and task["Fällig am"]
        and task.get("Liste") not in ["Erledigt", "Gelöscht"]
    ):
        events.append({
            "title": task["Betreff"],
            "start": str(task["Fällig am"]),
            "end": str(task["Fällig am"]),
            "color": "#d72660" if task.get("Priorität") == "High" else "#fbb13c" if task.get("Priorität") == "Medium" else "#00965c",
            "description": f"""
                <b>Beschreibung:</b> {task.get('Beschreibung', '')}<br>
                <b>Priorität:</b> {task.get('Priorität', '')}<br>
                <b>Liste:</b> {task.get('Liste', '')}
            """
        })

calendar_options = {
    "initialView": "dayGridMonth",
    "headerToolbar": {
        "left": "prev,next today",
        "center": "title",
        "right": "dayGridMonth,timeGridWeek,timeGridDay"
    },
    "locale": "de"
}

calendar(events=events, options=calendar_options)