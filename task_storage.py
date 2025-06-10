# filepath: /Users/helenscheuch/Desktop/task-manager-app/task_storage.py
import streamlit as st
import json
import os
from datetime import date, datetime

TASKS_FILE = "tasks.json"
LISTS_FILE = "lists.json"

def serialize_task(task):
    # Alle date-Objekte in ISO-Strings umwandeln
    task_copy = task.copy()
    for key in ["Fällig am", "Erinnerung am"]:
        if isinstance(task_copy.get(key), date):
            task_copy[key] = task_copy[key].isoformat()
    return task_copy

def deserialize_task(task):
    # ISO-Strings zurück in date-Objekte umwandeln
    for key in ["Fällig am", "Erinnerung am"]:
        if key in task and isinstance(task[key], str):
            try:
                task[key] = datetime.strptime(task[key], "%Y-%m-%d").date()
            except Exception:
                pass
    return task

def load_tasks():
    if os.path.exists(TASKS_FILE):
        with open(TASKS_FILE, "r") as f:
            tasks = json.load(f)
            return [deserialize_task(t) for t in tasks]
    return []

def save_tasks(tasks):
    tasks_serialized = [serialize_task(t) for t in tasks]
    with open(TASKS_FILE, "w") as f:
        json.dump(tasks_serialized, f)

def load_lists():
    if os.path.exists(LISTS_FILE):
        with open(LISTS_FILE, "r") as f:
            return json.load(f)
    return ["Allgemein"]

def save_lists(lists):
    with open(LISTS_FILE, "w") as f:
        json.dump(lists, f)