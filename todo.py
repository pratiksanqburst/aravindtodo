# define an empty list to hold our tasks
tasks = []

# define a function to add a task to the list
def add_task(task):
    # task = input("Enter task: ")
    tasks.append(task)
    print("Task added.")
    return task

# define a function to remove a task from the list
def remove_task():
    task = input("Enter task to remove: ")
    if task in tasks:
        tasks.remove(task)
        print("Task removed.")
        return task
    else:
        print("Task not found.")

# define a function to display all tasks in the list
def view_tasks():
    if tasks:
        for task in tasks:
            print(task)
            return tasks
    else:
        print("No tasks.")

# define a main function to run the program
def main():
    while True:
        print("\n1. Add task\n2. Remove task\n3. View tasks\n4. Quit")
        choice = input("Enter choice: ")
        if choice == "1":
            add_task()
        elif choice == "2":
            remove_task()
        elif choice == "3":
            view_tasks()
        elif choice == "4":
            print("Goodbye!")
            break
        else:
            print("Invalid choice.")

if __name__ == "__main__":
    main()










