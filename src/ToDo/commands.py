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
        print("error in remove your task ! Please try again", e)

    finally:
        conn.close()



def clear_tasks(filter_status=None, force=False):
    conn = get_connection()
    cur = conn.cursor()

    try:
        # توضیح پیام بر اساس وضعیت
        if filter_status == "done":
            message = "All completed tasks will be deleted. Are you sure? (y/n): "
        elif filter_status == "pending":
            message = "All running tasks will be deleted. Are you sure? (y/n): "
        else:
            message = "This will delete all tasks and reset the ids! Are you sure? (y/n): "

        # اگه force فعال نباشه، تأییدیه بگیر
        if not force:
            confirm = input(message).strip().lower()
            if confirm != "y":
                print("The operation was canceled.")
                return

        # حذف رکوردها
        if filter_status == "done":
            cur.execute("DELETE FROM tasks WHERE status='done'")
            print("Completed tasks were deleted.")
        elif filter_status == "pending":
            cur.execute("DELETE FROM tasks WHERE status='pending'")
            print("Tasks in progress were deleted.")
        else:
            cur.execute("DELETE FROM tasks")
            cur.execute("DELETE FROM sqlite_sequence WHERE name='tasks'")
            print("All tasks were deleted and the counter was reset.")

        conn.commit()

    except Exception as e:
        print("Error deleting tasks:", e)

    finally:
        conn.close()






from .db import get_connection

def edit_task(identifier, new_title):

    conn = get_connection()
    cur = conn.cursor()
    try:
        if identifier.isdigit():
            cur.execute("SELECT id, title FROM tasks WHERE id = ?", (int(identifier),))
        else:
            cur.execute("SELECT id, title FROM tasks WHERE title = ?", (identifier,))
        row = cur.fetchone()

        if not row:
            print("No tasks found.")
            return

        task_id = row[0]
        old_title = row[1]

        cur.execute("UPDATE tasks SET title = ? WHERE id = ?", (new_title, task_id))
        conn.commit()
        print(f" Task #{task_id} was successfully edited.")
        print(f"    old: {old_title}")
        print(f"    new:  {new_title}")

    except Exception as e:
        print("Error edite tasks:", e)
    finally:
        conn.close()


def edit_task_interactive(identifier):

    conn = get_connection()
    cur = conn.cursor()
    try:
        if identifier.isdigit():
            cur.execute("SELECT id, title FROM tasks WHERE id = ?", (int(identifier),))
        else:
            cur.execute("SELECT id, title FROM tasks WHERE title = ?", (identifier,))

        row = cur.fetchone()
        if not row:
            print("No tasks found.")
            return

        task_id, old_title = row
        print(f"Current task title #{task_id}: {old_title}")
        new_title = input("Enter a new title (leave blank and press Enter to cancel): ").strip()
        if not new_title:
            print("The editing operation was canceled.")
            return

        cur.execute("UPDATE tasks SET title = ? WHERE id = ?", (new_title, task_id))
        conn.commit()
        print(f" Task #{task_id} was successfully changed to '{new_title}'.")

    except Exception as e:
        print("Error editing task (interactive):", e)
    finally:
        conn.close()











