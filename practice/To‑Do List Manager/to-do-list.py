import json

# Load existing to-do list from a file, or start with an empty list.
try:
    with open("to-do-list.json", "r") as m:
        to_do_list = json.load(m)
        print("To-do list loaded from file.")
except FileNotFoundError:
    to_do_list = []
    print("No saved to-do list found, starting with an empty list.")

running = True

while running:
    print("\nTo-Do List Menu")
    print("1. Add task")
    print("2. Mark task as completed")
    print("3. Delete task")
    print("4. View tasks")
    print("5. Exit")

    choice = input("Choose an option: ")

    # Option 1 — Add task
    if choice == "1":
        task = input("Enter task description: ")
        to_do_list.append({"task": task, "completed": False})
        print("Task added to the list.")

    # Option 2 — Mark task as completed
    elif choice == "2":
        if not to_do_list:
            print("No tasks available to mark as completed.")
        else:
            print("\nYour Tasks:")
            for index, task in enumerate(to_do_list, start=1):
                status = "[x]" if task["completed"] else "[ ]"
                print(f"{index}. {status} {task['task']}")

            try:
                task_number = int(input("Enter the task number to mark as completed: "))
                if 1 <= task_number <= len(to_do_list):
                    to_do_list[task_number - 1]["completed"] = True
                    print("Task marked as completed.")
                else:
                    print("Invalid task number.")
            except ValueError:
                print("Please enter a valid number.")

    # Option 3 — Delete task
    elif choice == "3":
        if not to_do_list:
            print("No tasks available to delete.")
        else:
            print("\nYour Tasks:")
            for index, task in enumerate(to_do_list, start=1):
                status = "[x]" if task["completed"] else "[ ]"
                print(f"{index}. {status} {task['task']}")

            try:
                task_number = int(input("Enter the task number to delete: "))
                if 1 <= task_number <= len(to_do_list):
                    removed_task = to_do_list.pop(task_number - 1)
                    print(f"Task '{removed_task['task']}' deleted.")
                else:
                    print("Invalid task number.")
            except ValueError:
                print("Please enter a valid number.")

    # Option 4 — View tasks
    elif choice == "4":
        if not to_do_list:
            print("No tasks to display.")
        else:
            print("\nYour Tasks:")
            for index, task in enumerate(to_do_list, start=1):
                status = "[x]" if task["completed"] else "[ ]"
                print(f"{index}. {status} {task['task']}")

    # Option 5 — Save and exit
    elif choice == "5":
        with open("to-do-list.json", "w") as m:
            json.dump(to_do_list, m, indent=4)
        print("To-do list saved. Goodbye!")
        running = False

    else:
        print("Invalid choice. Please try again.")
