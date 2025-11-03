import argparse
from . import commands

# --- argparse config ---
parser = argparse.ArgumentParser(
    prog="todo",
    description="Erlave CLI Todo App"
)
subparsers = parser.add_subparsers(dest="command")


# --- add command ---
add_parser = subparsers.add_parser("add", help="Add a new task")
add_parser.add_argument("title", type=str, nargs="+", help="Title of the task to add")

# --- list command ---

list_parser = subparsers.add_parser("list", help="Show all tasks")


# --- mark done ---
done_parser = subparsers.add_parser("done", help="Mark a task as done")
done_parser.add_argument("task", type=str, nargs="+", help="Task ID or title")




def main():
    args = parser.parse_args()

    if args.command == "add":
        titlee = " ".join(args.title)
        commands.add_task(titlee)

    elif args.command == "list":
        commands.list_tasks()
    
    elif args.command == "done":
        task_identifier = " ".join(args.task)
        commands.mark_done(task_identifier)

    else:
        parser.print_help()












