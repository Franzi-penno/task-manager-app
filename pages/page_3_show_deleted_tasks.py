import streamlit as st
from datetime import date

if 'tasks' not in st.session_state:
    st.session_state['tasks'] = {}

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
    "<h1 style='color:#d72660; text-align:center;'>🍒 Gelöschte Aufgaben 🍒</h1>",
    unsafe_allow_html=True
)

if "tasks" not in st.session_state:
    st.info("Keine Aufgaben vorhanden.")
else:
    deleted_tasks = [t for t in st.session_state.tasks if t.get("Liste") == "Gelöscht"]
    if deleted_tasks:
        for task in deleted_tasks:
            st.markdown(f"<b style='color:#d72660'>{task['Betreff']}</b>", unsafe_allow_html=True)
            st.write(f"**Beschreibung:** {task['Beschreibung']}")
            st.write(f"**Fällig am:** {task['Fällig am']}")
            st.write(f"**Erinnerung am:** {task['Erinnerung am']}")
            st.write(f"**Priorität:** {task['Priorität']}")
            st.markdown("---")
    else:
        st.info("Es gibt keine gelöschten Aufgaben.")