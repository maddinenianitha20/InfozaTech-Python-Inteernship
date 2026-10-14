import json
import os
from datetime import datetime

FILE_NAME = "tasks.json"


# Load saved tasks from JSON file
def load_tasks():
    if os.path.exists(FILE_NAME):
        try:
            with open(FILE_NAME, "r") as file:
                return json.load(file)
        except (json.JSONDecodeError, OSError):
            print("Could not load saved tasks. Starting with an empty list.")
    return []


# Save tasks to JSON file
def save_tasks(tasks):
    try:
        with open(FILE_NAME, "w") as file:
            json.dump(tasks, file, indent=4)
    except OSError:
        print("Error: Could not save tasks!")


# Add a new task
def add_task(tasks):
    description = input("Enter task description: ").strip()

    if not description:
        print("Task description cannot be empty!")
        return

    # Prevent duplicate task descriptions
    for task in tasks:
        if task["description"].casefold() == description.casefold():
            print("This task already exists!")
            return

    due_date = input("Enter due date (YYYY-MM-DD): ").strip()

    try:
        datetime.strptime(due_date, "%Y-%m-%d")
    except ValueError:
        print("Invalid date! Use YYYY-MM-DD format.")
        return

    priority = input("Enter priority (High/Medium/Low): ").strip().capitalize()

    if priority not in ["High", "Medium", "Low"]:
        print("Invalid priority! Choose High, Medium, or Low.")
        return

    task = {
        "description": description,
        "due_date": due_date,
        "priority": priority,
        "completed": False
    }

    tasks.append(task)
    save_tasks(tasks)

    print("Task added successfully!")


# Display all tasks
def view_tasks(tasks):
    if not tasks:
        print("No tasks available.")
        return

    print("\n========== TO-DO LIST ==========")

    for index, task in enumerate(tasks, start=1):
        status = "Completed" if task["completed"] else "Pending"

        print(
            f"{index}. {task['description']} | "
            f"Due: {task['due_date']} | "
            f"Priority: {task['priority']} | "
            f"Status: {status}"
        )


# Mark a task as completed
def complete_task(tasks):
    if not tasks:
        print("No tasks available to complete.")
        return

    view_tasks(tasks)

    try:
        number = int(input("Enter task number to complete: "))

        if 1 <= number <= len(tasks):
            if tasks[number - 1]["completed"]:
                print("This task is already completed!")
            else:
                tasks[number - 1]["completed"] = True
                save_tasks(tasks)
                print("Task marked as completed!")
        else:
            print("Invalid task number!")

    except ValueError:
        print("Please enter a valid number!")


# Remove a task
def remove_task(tasks):
    if not tasks:
        print("No tasks available to remove.")
        return

    view_tasks(tasks)

    try:
        number = int(input("Enter task number to remove: "))

        if 1 <= number <= len(tasks):
            removed_task = tasks.pop(number - 1)
            save_tasks(tasks)
            print(f"Removed task: {removed_task['description']}")
        else:
            print("Invalid task number!")

    except ValueError:
        print("Please enter a valid number!")


# Sort tasks by priority or due date
def sort_tasks(tasks):
    if not tasks:
        print("No tasks available to sort.")
        return

    print("\n1. Sort by priority")
    print("2. Sort by due date")

    choice = input("Choose sorting option: ").strip()

    if choice == "1":
        priority_order = {
            "High": 1,
            "Medium": 2,
            "Low": 3
        }

        tasks.sort(key=lambda task: priority_order[task["priority"]])
        print("Tasks sorted by priority!")

    elif choice == "2":
        tasks.sort(key=lambda task: task["due_date"])
        print("Tasks sorted by due date!")

    else:
        print("Invalid choice!")
        return

    save_tasks(tasks)
    view_tasks(tasks)


# Main program
tasks = load_tasks()

while True:
    print("\n===== TO-DO LIST APPLICATION =====")
    print("1. Add Task")
    print("2. View Tasks")
    print("3. Complete Task")
    print("4. Remove Task")
    print("5. Sort Tasks")
    print("6. Exit")

    choice = input("Enter your choice: ").strip()

    if choice == "1":
        add_task(tasks)

    elif choice == "2":
        view_tasks(tasks)

    elif choice == "3":
        complete_task(tasks)

    elif choice == "4":
        remove_task(tasks)

    elif choice == "5":
        sort_tasks(tasks)

    elif choice == "6":
        print("Thank you for using the To-Do List Application!")
        break

    else:
        print("Invalid choice! Please try again.")