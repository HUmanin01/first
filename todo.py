# Function to display the menu
def display_menu():
    print("\n--- To-Do List Menu ---")
    print("1. View tasks")
    print("2. Add a task")
    print("3. Remove a task")
    print("4. Exit")

# Function to add a task to the list
def add_task(tasks):
    task = input("Enter the task: ")
    tasks.append(task)
    print(f"Task '{task}' added.")

# Function to view all tasks
def view_tasks(tasks):
    if not tasks:
        print("No tasks found!")
    else:
        print("\nYour tasks:")
        for i, task in enumerate(tasks, start=1):
            print(f"{i}. {task}")

# Function to remove a task by its number
def remove_task(tasks):
    view_tasks(tasks)
    try:
        task_num = int(input("Enter the task number to remove: "))
        removed_task = tasks.pop(task_num - 1)
        print(f"Task '{removed_task}' removed.")
    except (ValueError, IndexError):
        print("Invalid task number!")

# Function to save tasks to a file
def save_tasks(tasks, filename="tasks.txt"):
    with open(filename, "w") as file:
        for task in tasks:
            file.write(task + "\n")

# Function to load tasks from a file
def load_tasks(filename="tasks.txt"):
    try:
        with open(filename, "r") as file:
            return [line.strip() for line in file.readlines()]
    except FileNotFoundError:
        return []

# Main function to control the flow of the program
def main():
    tasks = load_tasks()  # Load tasks from the file
    while True:
        display_menu()
        choice = input("Choose an option (1-4): ")

        if choice == "1":
            view_tasks(tasks)
        elif choice == "2":
            add_task(tasks)
        elif choice == "3":
            remove_task(tasks)
        elif choice == "4":
            save_tasks(tasks)
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

# Run the main function if this file is executed directly
if __name__ == "__main__":
    main()
