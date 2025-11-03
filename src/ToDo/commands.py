import sqlite3
from .db import get_connection



def add_task(title):
    conn = get_connection()
    cur = conn.cursor()
    cur.execute("INSERT INTO tasks (title, status) VALUES (?, 'pending')", (title,))
    conn.commit()
    conn.close()
    print(f"Task added: {title}")






def mark_done(task_identifier):
    conn = get_connection()
    cur = conn.cursor()

    try:
        # بررسی اینکه ورودی عددیه (id) یا متن (عنوان)
        if task_identifier.isdigit():
            cur.execute("UPDATE tasks SET status = 'done' WHERE id = ?", (int(task_identifier),))
        else:
            cur.execute("UPDATE tasks SET status = 'done' WHERE title = ?", (task_identifier,))

        if cur.rowcount == 0:
            print(f"'{task_identifier}' is not found")
        else:
            print(f"task '{task_identifier}' is done ")

        conn.commit()

    except Exception as e:
        print("error in update your task ! Please try again", e)

    finally:
        conn.close()

def list_tasks(filter_status=None):
    conn = get_connection()
    cur = conn.cursor()

    if filter_status == "done":
        cur.execute("SELECT id, title, status FROM tasks WHERE status='done'")
    elif filter_status == "pending":
        cur.execute("SELECT id, title, status FROM tasks WHERE status='pending'")
    else:
        cur.execute("SELECT id, title, status FROM tasks")

    rows = cur.fetchall()

    if not rows:
        print("No tasks found.")
    else:
        print("📋 Task list : \n")
        for row in rows:
            status_icon = "✅" if row[2] == "done" else "🕓"
            print(f"{row[0]}. {row[1]} {status_icon}")

    conn.close()








def mark_undone(task_identifier):
    conn = get_connection()
    cur = conn.cursor()

    try:
        if task_identifier.isdigit():
            cur.execute("UPDATE tasks SET status = 'pending' WHERE id = ?", (int(task_identifier),))
        else:
            cur.execute("UPDATE tasks SET status = 'pending' WHERE title = ?", (task_identifier,))

        if cur.rowcount == 0:
            print("No tasks found.")
        else:
            print(f"task '{task_identifier}' is undone ")

        conn.commit()

    except Exception as e:
        print("error in update your task ! Please try again", e)

    finally:
        conn.close()





def remove_task(task_identifier):
    conn = get_connection()
    cur = conn.cursor()

    try:
        if task_identifier.isdigit():
            cur.execute("DELETE FROM tasks WHERE id = ?", (int(task_identifier),))
        else:
            cur.execute("DELETE FROM tasks WHERE title = ?", (task_identifier,))

        if cur.rowcount == 0:
            print("No tasks found.")
        else:
            print(f"task '{task_identifier}' is deleted ")

        conn.commit()

    except Exception as e:
        print("error in update your task ! Please try again", e)

    finally:
        conn.close()
