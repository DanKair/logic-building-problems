# To-Do List Application
# Input values:
# 1. Add Task
# 2. Edit Task
# 3. Delete Task
# 4. Exit

def todo_list():
    todo_list = []
    print("\nInput values (only numbers): " \
    "\n1. Add Task" \
    "\n2. Edit Task" \
    "\n3. Delete Task" \
    "\n4. View To-Do List" \
    "\n5. Exit")
    option = int(input("Select an option: "))
    while option != 5:
        match option:
        # CREATE functionality in CRUD
            case 1:
                task = input("Enter task: ")
                todo_list.append(task)
                print(f'Task: "{task}" added succesfully✔!')
                option = int(input("Select an option: "))

        # UPDATE method in CRUD
            case 2:
                task_index = int(input("Enter task index to edit: "))
                task_index -= 1
                if task_index >= len(todo_list):
                    print("Sorry, you cannot enter index out of range.")
                    task_index = input("Enter task index to edit: ")
                else:
                    todo_list[task_index] = input("Enter new task: ")
                    print("Task Edited Successfully✨!")
                    option = int(input("Select an option: "))

        # DELETE Functionality
            case 3:
                task_index = int(input("Enter task index to delete: "))
                task_index -= 1
                if task_index >= len(todo_list):
                    print("Sorry, you cannot enter index out of range.")
                    task_index = input("Enter task index to edit: ")
                else:
                    target_task = todo_list[task_index]
                    todo_list.remove(target_task)
                    print(f"Task '{target_task}' Deleted Successfully✨!")
                    option = int(input("Select an option: "))

        # READ functionality
            case 4:
                print(f"Your current To-Do-List: {todo_list}")
                option = int(input("Select an option: "))

            case 5:
                print("Exiting the application. Goodbye😘!")
                break

            case _:
                print("Oops, it seems you have entered invalid option." \
                "\nPlease Enter only numbers (without dots)")
                option = int(input("Select an option: "))

    return "Exiting the application. Goodbye😘!"
print(todo_list())  