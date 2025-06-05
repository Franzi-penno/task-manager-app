import streamlit as st
from datetime import date
from task_storage import load_tasks, save_tasks

if 'tasks' not in st.session_state:
    st.session_state['tasks'] = []

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
    "<h1 style='color:#00965c; text-align:center;'>🍒 Erledigte Aufgaben 🍒</h1>",
    unsafe_allow_html=True
)

if "tasks" not in st.session_state:
    st.info("Keine Aufgaben vorhanden.")
else:
    done_tasks = [t for t in st.session_state.tasks if t.get("Liste") == "Erledigt"]
    if done_tasks:
        for task in done_tasks:
            st.markdown(f"<b style='color:#00965c'>{task['Betreff']}</b>", unsafe_allow_html=True)
            st.write(f"**Beschreibung:** {task['Beschreibung']}")
            st.write(f"**Fällig am:** {task['Fällig am']}")
            st.write(f"**Erinnerung am:** {task['Erinnerung am']}")
            st.write(f"**Priorität:** {task['Priorität']}")
            st.markdown("---")
    else:
        st.info("Es gibt keine erledigten Aufgaben.")
