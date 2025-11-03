import sqlite3
from .db import get_connection

def add_task(title):
    conn = get_connection()
    c = conn.cursor()
    c.execute("INSERT INTO tasks (title) VALUES (?)", (title,))
    conn.commit()
    conn.close()
    print(f"Task added: {title}")


def list_tasks():
    conn = get_connection()
    c = conn.cursor()
    c.execute("SELECT id, title, done FROM tasks ORDER BY id")
    rows = c.fetchall()
    conn.close()

    if not rows:
        print(" There is no task ...!")
        return

    print("📋 Task list : \n")
    for id, title, done in rows:
        status = "✔️" if done else "⏳"
        print(f"{id}. {status} {title}")







def mark_done(task_identifier):
    conn = get_connection()
    c = conn.cursor()

    # بررسی اینکه task_identifier عدد هست یا نه
    if task_identifier.isdigit():
        # بر اساس id
        c.execute("UPDATE tasks SET done = 1 WHERE id = ?", (int(task_identifier),))
    else:
        # بر اساس title
        c.execute("UPDATE tasks SET done = 1 WHERE title = ?", (task_identifier,))

    conn.commit()

    if c.rowcount == 0:
        print(f"'{task_identifier}' is not found")
    else:
        print(f"task '{task_identifier}' is done ")

    conn.close()