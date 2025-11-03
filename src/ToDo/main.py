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
add_parser.add_argument("title", type=str, help="Title of the task to add")

# --- list command ---

list_parser = subparsers.add_parser("list", help="Show all tasks")




def main():
    args = parser.parse_args()

    if args.command == "add":
        commands.add_task(args.title)
    elif args.command == "list":
        commands.list_tasks()
    else:
        parser.print_help()












