import argparse
from . import commands
from .config import APP_VERSION


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

# --- clear command ---

clear_parser = subparsers.add_parser("clear", help="Clear tasks")
group = clear_parser.add_mutually_exclusive_group()
group.add_argument("-d", "--done", action="store_true", help="Clear only done tasks")
group.add_argument("-p", "--pending", action="store_true", help="Clear only pending tasks")
clear_parser.add_argument("-f", "--force", action="store_true", help="Skip confirmation prompt")

# --- edite command ---

edit_parser = subparsers.add_parser("edit", help="Edit a task by ID or title")
edit_parser.add_argument("identifier", nargs="+", help="Task ID or current title (if multi-word, just type words with double quotes) + ")
edit_parser.add_argument("new_title", nargs="+",)

# --- version ---

parser.add_argument("-v", "--version", action="store_true", help="Show app version")




def main():
    args = parser.parse_args()

#         <---add--->
    if args.command == "add":
        titlee = " ".join(args.title)
        commands.add_task(titlee)
    
#           <---done--->
    elif args.command == "done":
        task_identifier = " ".join(args.task)
        commands.mark_done(task_identifier)

#          <---undone--->
    elif args.command == "undone":
        commands.mark_undone(args.task_identifier)

#           <---remove--->
    elif args.command == "remove":
        remove = " ".join(args.task_identifier)
        commands.remove_task(remove)

#            <---list--->
    elif args.command == "list":
        if args.done:
            commands.list_tasks(filter_status="done")
        elif args.pending:
            commands.list_tasks(filter_status="pending")
        else:
            commands.list_tasks()

#              <---clear--->
    elif args.command == "clear":
        if args.done:
            commands.clear_tasks("done", force=args.force)
        elif args.pending:
            commands.clear_tasks("pending", force=args.force)
        else:
            commands.clear_tasks(force=args.force)

#              <---edit--->
    elif args.command == "edit":
        # join identifier parts to single string (e.g. ["learn","python"] -> "learn python")
        identifier = " ".join(args.identifier).strip()

        if args.new_title:
            new_title = " ".join(args.new_title).strip()
            commands.edit_task(identifier, new_title)
        else:
            # interactive mode: show current title and ask for new title
            commands.edit_task_interactive(identifier)

    elif args.version:
        print(f"Erlave ToDo CLI v{APP_VERSION} ")
        return
    


    else:
        parser.print_help()














