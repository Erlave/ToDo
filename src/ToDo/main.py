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

list_group = list_parser.add_mutually_exclusive_group()
list_group.add_argument("-d", "--done", action="store_true", help="Show only done tasks")
list_group.add_argument("-p", "--pending", action="store_true", help="Show only pending tasks")

# --- mark done command ---

done_parser = subparsers.add_parser("done", help="Mark a task as done")
done_parser.add_argument("task", type=str, nargs="+", help="Task ID or title")

# --- undone command ---

undone_parser = subparsers.add_parser("undone", help="Mark a task as pending again")
undone_parser.add_argument("task_identifier", help="Task ID or title to mark as pending")

# --- remove command ---

remove_parser = subparsers.add_parser("remove", help="Remove a task by ID or title")
remove_parser.add_argument("task_identifier",nargs="+", help="Task ID or title to remove")










def main():
    args = parser.parse_args()

    if args.command == "add":
        titlee = " ".join(args.title)
        commands.add_task(titlee)
    
    elif args.command == "done":
        task_identifier = " ".join(args.task)
        commands.mark_done(task_identifier)

    elif args.command == "undone":
        commands.mark_undone(args.task_identifier)

    elif args.command == "remove":
        remove = " ".join(args.task_identifier)
        commands.remove_task(remove)


    elif args.command == "list":
        if args.done:
            commands.list_tasks(filter_status="done")
        elif args.pending:
            commands.list_tasks(filter_status="pending")
        else:
            commands.list_tasks()

    else:
        parser.print_help()












