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
    "<h1 style='color:#d72660; text-align:center;'>🍒 Cherry Task Manager 🍒</h1>",
    unsafe_allow_html=True
)

# Aufgaben nach Liste filtern
chosen_list = st.selectbox("Welche Liste anzeigen?", st.session_state.lists, key="view_list")
tasks_to_show = [t for t in st.session_state.tasks if t["Liste"] == chosen_list]

# Aufgaben nach Priorität sortieren (High > Medium > Low)
priority_order = {"High": 0, "Medium": 1, "Low": 2}
tasks_to_show = sorted(tasks_to_show, key=lambda t: priority_order.get(t["Priorität"], 3))

# Aufgabenliste anzeigen (nur gefilterte Aufgaben)
if tasks_to_show:
    st.subheader(f"Aufgabenliste: {chosen_list}")
    if "edit_index" not in st.session_state:
        st.session_state.edit_index = None

    for i, task in enumerate(tasks_to_show):
        col1, col2, col3, col4 = st.columns([4, 1, 1, 1])
        with col1:
            if st.session_state.edit_index == i:
                new_subject = st.text_input("Betreff", value=task["Betreff"], key=f"edit_subject_{i}")
                new_description = st.text_area("Beschreibung", value=task["Beschreibung"], key=f"edit_desc_{i}")
                new_due = st.date_input("Fällig am", value=task["Fällig am"], key=f"edit_due_{i}")
                new_reminder = st.date_input("Erinnerung am", value=task["Erinnerung am"], key=f"edit_rem_{i}")
                new_priority = st.selectbox("Priorität", ["High", "Medium", "Low"], index=["High", "Medium", "Low"].index(task["Priorität"]), key=f"edit_prio_{i}")
                if st.button("Speichern", key=f"save_{i}"):
                    st.session_state.tasks[i] = {
                        "Betreff": new_subject,
                        "Beschreibung": new_description,
                        "Fällig am": new_due,
                        "Erinnerung am": new_reminder,
                        "Priorität": new_priority,
                        "Erledigt": task["Erledigt"],
                        "Liste": task["Liste"]
                    }
                    st.session_state.edit_index = None
                    st.rerun()
                if st.button("Abbrechen", key=f"cancel_{i}"):
                    st.session_state.edit_index = None
                    st.rerun()
            else:
                st.markdown(f"### {task['Betreff']}")
                st.write(f"**Beschreibung:** {task['Beschreibung']}")
                st.write(f"**Fällig am:** {task['Fällig am']}")
                st.write(f"**Erinnerung am:** {task['Erinnerung am']}")
                st.write(f"**Priorität:** {task['Priorität']}")
        with col2:
            done = st.checkbox("Erledigt", key=f"done_{i}")
            if done:
                # Erledigt-Liste automatisch anlegen
                if "Erledigt" not in st.session_state.lists:
                    st.session_state.lists.append("Erledigt")
                # Aufgabe verschieben
                task["Liste"] = "Erledigt"
                st.session_state.tasks.append(task)
                st.session_state.tasks.remove(task)
                st.rerun()
        with col3:
            if st.button("Löschen", key=f"delete_{i}"):
                # Gelöscht-Liste automatisch anlegen
                if "Gelöscht" not in st.session_state.lists:
                    st.session_state.lists.append("Gelöscht")
                # Aufgabe verschieben
                task["Liste"] = "Gelöscht"
                st.session_state.tasks.append(task)
                st.session_state.tasks.remove(task)
                st.rerun()
        with col4:
            if st.button("change", key=f"edit_{i}"):
                st.session_state.edit_index = i
                st.rerun()
        st.markdown("---")
else:
    st.info("Noch keine Aufgaben in dieser Liste gespeichert.")
