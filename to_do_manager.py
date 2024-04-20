def menu():
    print("To-Do List")
    print("1. Add a Task")
    print("2. View Tasks")
    print("3. Mark as Completed")
    print("4. Delete Task")
    print("5. Exit")


def read_tasks_from_file():
    try:
        with open("ToDoList.txt", "r") as file:
            tasks = file.readlines()
        return [task.strip() for task in tasks]
    except FileNotFoundError:
        return []


def save_tasks_to_file(tasks):
    with open("ToDoList.txt", "w") as file:
        for task in tasks:
            file.write(task + "\n")


def add_task(tasks):
    task = input("Enter Task: ")
    tasks.append(task)
    save_tasks_to_file(tasks)
    print("Task added successfully!")


def view_tasks(tasks):
    if tasks:
        print("Tasks:")
        for index, task in enumerate(tasks, start=1):
            print(f"{index}. {task}")
    else:
        print("No tasks to display.")


def mark_task_as_completed(tasks):
    view_tasks(tasks)
    task_index = input("Which task to mark as completed? : ")

    task_index = int(task_index)
    if 1 <= task_index <= len(tasks):
        tasks[task_index - 1] += " -Completed"
        save_tasks_to_file(tasks)
        print("Task marked as completed successfully!")
    else:
        print("Invalid task.")


def delete_task(tasks):
    view_tasks(tasks)
    task_index = input("Which task to delete? : ")

    task_index = int(task_index)
    if 1 <= task_index <= len(tasks):
        del tasks[task_index - 1]
        save_tasks_to_file(tasks)
        print("Task deleted successfully!")
    else:
        print("Invalid task.")


def main():
    tasks = read_tasks_from_file()

    while True:
        menu()
        choice = input("Enter your choice: ")

        if choice == "1":
            add_task(tasks)
        elif choice == "2":
            view_tasks(tasks)
        elif choice == "3":
            mark_task_as_completed(tasks)
        elif choice == "4":
            delete_task(tasks)
        elif choice == "5":
            print("Exiting...")
            quit()
        else:
            print("Invalid choice. Try again.")


main()
