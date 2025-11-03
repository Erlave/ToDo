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