import json

from datetime import datetime


# -----------------------------
# Loading & Saving Tasks
# -----------------------------

def load_tasks(filename = "to-do-list.json"):
    """
    Load tasks from a JSON file.

    Handles missing files and corrupted JSON gracefully.

    Args:
        filename (str): The name of the JSON file to load.

    Returns:
        list: A list of task dictionaries.
    """
    try:
        with open(filename, "r") as f:
            tasks = json.load(f)

            if not isinstance(tasks, list):
                raise ValueError("Invalid data format")

            print("To-do list loaded from file.")
            return tasks

    except (FileNotFoundError, json.JSONDecodeError, ValueError):
        print("No valid saved list found. Starting with an empty list.")
        return []


def save_tasks(tasks, filename="to-do-list.json"):
    """
    Save the current list of tasks to a JSON file.

    Args:
        tasks (list): The list of task dictionaries to save.
        filename (str): The name of the JSON file to write to.

    Returns:
        None
    """
    try:
        with open(filename, "w") as f:
            json.dump(tasks, f, indent=4)
        print("To-do list saved. Goodbye!")
    except Exception as e:
        print("Error saving tasks:", e)


# -----------------------------
# Core Task Operations
# -----------------------------

def add_task(tasks, description, priority="Medium", category="General", due_date=None):
    """
    Add a new task with optional priority, category, and due date.

    Args:
        tasks (list): The current list of tasks.
        description (str): The task description.
        priority (str): Task priority (High, Medium, Low).
        category (str): Task category.
        due_date (str): Optional due date in YYYY-MM-DD format.

    Returns:
        None
    """
    if not description.strip():
        print("Task description cannot be empty.")
        return

    if priority not in ["High", "Medium", "Low"]:
        print("Invalid priority. Using 'Medium'.")
        priority = "Medium"

    if due_date:
        try:
            datetime.strptime(due_date, "%Y-%m-%d")
        except ValueError:
            print("Invalid date format. Use YYYY-MM-DD.")
            due_date = None

    tasks.append({
        "task": description.strip(),
        "completed": False,
        "priority": priority,
        "category": category,
        "due_date": due_date
    })

    print("Task added successfully.")


def mark_task_completed(tasks, task_number):
    """Mark a specific task as completed."""
    if not tasks:
        print("No tasks available.")
        return

    if 1 <= task_number <= len(tasks):
        tasks[task_number - 1]["completed"] = True
        print("Task marked as completed.")
    else:
        print("Invalid task number.")


def delete_task(tasks, task_number):
    """Delete a task from the list."""
    if not tasks:
        print("No tasks available.")
        return

    if 1 <= task_number <= len(tasks):
        removed = tasks.pop(task_number - 1)
        print(f"Task '{removed['task']}' deleted.")
    else:
        print("Invalid task number.")


def search_tasks(tasks, keyword):
    """Search for tasks containing a keyword."""
    print(f"\nSearch results for '{keyword}':")
    results = [
        task for task in tasks
        if keyword.lower() in task["task"].lower()
    ]

    if not results:
        print("No matching tasks found.")
        return

    for index, task in enumerate(results, start=1):
        status = "[x]" if task["completed"] else "[ ]"
        print(f"{index}. {status} {task['task']} (Priority: {task['priority']}, Category: {task['category']})")


def sort_tasks(tasks, mode="priority"):
    """Sort tasks by priority, due date, completion, or alphabetically."""
    if mode == "priority":
        tasks.sort(key=lambda t: ["High", "Medium", "Low"].index(t["priority"]))
    elif mode == "due":
        tasks.sort(key=lambda t: t["due_date"] or "9999-12-31")
    elif mode == "alpha":
        tasks.sort(key=lambda t: t["task"])
    elif mode == "completed":
        tasks.sort(key=lambda t: t["completed"])
    else:
        print("Invalid sorting mode.")
        return

    print("Tasks sorted.")


def view_tasks(tasks):
    """Display all tasks with details."""
    if not tasks:
        print("No tasks to display.")
        return

    print("\nYour Tasks:")
    for index, task in enumerate(tasks, start=1):
        status = "[x]" if task["completed"] else "[ ]"
        due = task["due_date"] if task["due_date"] else "No due date"
        print(
            f"{index}. {status} {task['task']} "
            f"(Priority: {task['priority']}, Category: {task['category']}, Due: {due})"
        )


# -----------------------------
# Menu + App Controller
# -----------------------------

def display_menu():
    """Show the menu options."""
    print("\nTo-Do List Menu")
    print("1. Add task")
    print("2. Mark task as completed")
    print("3. Delete task")
    print("4. View tasks")
    print("5. Search tasks")
    print("6. Sort tasks")
    print("7. Exit")


def run_to_do_app():
    """Main loop for the to-do list application."""
    tasks = load_tasks()
    running = True

    while running:
        display_menu()
        choice = input("Choose an option: ").strip()

        if choice == "1":
            description = input("Task description: ")
            priority = input("Priority (High/Medium/Low): ").title()
            category = input("Category: ").title()
            due_date = input("Due date (YYYY-MM-DD or leave blank): ").strip() or None
            add_task(tasks, description, priority, category, due_date)

        elif choice == "2":
            view_tasks(tasks)
            try:
                number = int(input("Enter task number: "))
                mark_task_completed(tasks, number)
            except ValueError:
                print("Please enter a valid number.")

        elif choice == "3":
            view_tasks(tasks)
            try:
                number = int(input("Enter task number: "))
                delete_task(tasks, number)
            except ValueError:
                print("Please enter a valid number.")

        elif choice == "4":
            view_tasks(tasks)

        elif choice == "5":
            keyword = input("Enter search keyword: ")
            search_tasks(tasks, keyword)

        elif choice == "6":
            print("\nSort by:")
            print("1. Priority")
            print("2. Due date")
            print("3. Alphabetical")
            print("4. Completion status")
            mode_choice = input("Choose sorting mode: ")

            modes = {
                "1": "priority",
                "2": "due",
                "3": "alpha",
                "4": "completed"
            }

            sort_tasks(tasks, modes.get(mode_choice, "priority"))

        elif choice == "7":
            save_tasks(tasks)
            running = False

        else:
            print("Invalid choice. Try again.")


# Run the app
if __name__ == "__main__":
    run_to_do_app()