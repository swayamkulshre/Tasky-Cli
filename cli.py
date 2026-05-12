import argparse
import sys
from .manager import TaskManager

def main():
    manager = TaskManager()
    parser = argparse.ArgumentParser(description="Tasky - A Simple CLI Task Manager")
    subparsers = parser.add_subparsers(dest="command", help="Available commands")

    # Add command
    add_parser = subparsers.add_parser("add", help="Add a new task")
    add_parser.add_argument("description", type=str, help="Task description")

    # List command
    subparsers.add_parser("list", help="List all tasks")

    # Complete command
    complete_parser = subparsers.add_parser("complete", help="Mark a task as completed")
    complete_parser.add_argument("id", type=int, help="Task ID")

    # Delete command
    delete_parser = subparsers.add_parser("delete", help="Delete a task")
    delete_parser.add_argument("id", type=int, help="Task ID")

    args = parser.parse_args()

    if args.command == "add":
        task = manager.add_task(args.description)
        print(f"Added task: [{task.id}] {task.description}")

    elif args.command == "list":
        tasks = manager.list_tasks()
        if not tasks:
            print("No tasks found.")
        else:
            for task in tasks:
                status = "✔" if task.completed else " "
                print(f"{task.id}. [{status}] {task.description}")

    elif args.command == "complete":
        if manager.complete_task(args.id):
            print(f"Task {args.id} marked as completed.")
        else:
            print(f"Task {args.id} not found.")

    elif args.command == "delete":
        if manager.delete_task(args.id):
            print(f"Task {args.id} deleted.")
        else:
            print(f"Task {args.id} not found.")

    else:
        parser.print_help()

if __name__ == "__main__":
    main()
