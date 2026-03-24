import json

# Load existing inventory from a file

try:
    with open("to_do_list.json", "r") as f:
        to_do_list = json.load(f)
        print("To-do-list loaded from file.")
except FileNotFoundError:
    to_do_list = []
    print("No saved to-do-list found, starting with an empty list.")
    
    running = True
    
    while running:

        print("\nTo-do-list Menu")
        print("1. Add task")
        print("2. Mark task as completed")
        print("Delete task")
        print("4. View tasks")
        print("5. Exit")
        
        choice = input("Choose an option: ")

        # Add task

        if choice == "1":
            task = input("enter task description: ")
            to_do_list.append({"task": task, "completed": False})
            print("Task added to the list.")

        # Mark task as completed

        elif choice == "2":
            if not to_do_list:
                print("No tasks available to mark as completed")
            else:
                print("\nYour Tasks: ")
                for index, task in enumerate(to_do_list, start =1):
                    status = "[x]" if task ["completed"] else "[]"
                    print(f"{index}. {status} {task["task"]}")

                    try:
                        task_number = int(input("Enter the task number to mark as completd:"))
                        if 1 <= task_number <= len(to_do_list):
                            to_do_list[task_number -1]["completd"] = True
                            print("task marked as completed.")
                        else: 
                            print("invalid task number.")
                    except ValueError:
                        print("please enter a valid number.")
        
        # Delete task

        elif choice == "3":
            if not to_do_list:
                print("No tasks available to delete.")
            else:
                print("\nYour Tasks:")
                for index, task in enumerate(to_do_list, start =1):
                    status = "[x]" if task ["completed"] else "[]"
                    print(f"{index}. {status} {task["task"]}")

                    try:
                        task_number = int(input("Enter task number"))
                        if 1 <= task_number <= len(to_do_list):
                            removed_task = to_do_list.pop(task_number -1)
                            print(f"Task '{removed_task["task"]}' deleted.")
                        else:
                            print("invalid task number.")
                    except ValueError:
                            print("please enter a valid number.")
                        


