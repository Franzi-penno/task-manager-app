import streamlit as st
from datetime import date

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
    "<h1 style='color:#d72660; text-align:center;'>🍒 Priorität 🍒</h1>",
    unsafe_allow_html=True
)

# Aufgaben nach Priorität sortieren (High > Medium > Low)
priority_order = {"High": 0, "Medium": 1, "Low": 2}
all_tasks = sorted(
    [t for t in st.session_state.tasks if t.get("Liste") not in ["Gelöscht"]],
    key=lambda t: priority_order.get(t.get("Priorität", "Low"), 3)
)

if all_tasks:
    for task in all_tasks:
        st.markdown(f"<b style='color:#d72660'>{task['Betreff']}</b>", unsafe_allow_html=True)
        st.write(f"**Beschreibung:** {task['Beschreibung']}")
        st.write(f"**Fällig am:** {task['Fällig am']}")
        st.write(f"**Erinnerung am:** {task['Erinnerung am']}")
        st.write(f"**Priorität:** {task['Priorität']}")
        st.write(f"**Liste:** {task['Liste']}")
        st.markdown("---")
else:
    st.info("Es gibt keine Aufgaben.")
