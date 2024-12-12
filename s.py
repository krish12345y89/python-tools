import os

def clear_screen():
    """Clear the console screen based on the operating system."""
    os.system('cls' if os.name == 'nt' else 'clear')

def display_menu():
    """Display the main menu."""
    print("\n--- To-Do List Manager ---")
    print("1. View Tasks")
    print("2. Add Task")
    print("3. Remove Task")
    print("4. Clear All Tasks")
    print("5. Exit")
    print("-------------------------")

def view_tasks(tasks):
    """Display the current tasks."""
    if not tasks:
        print("\nNo tasks in the list.")
    else:
        print("\nCurrent Tasks:")
        for i, task in enumerate(tasks, start=1):
            print(f"{i}. {task}")

def add_task(tasks):
    """Add a new task to the list."""
    task = input("\nEnter the task: ").strip()
    if task:
        tasks.append(task)
        print(f"Task '{task}' added successfully!")
    else:
        print("Task cannot be empty!")

def remove_task(tasks):
    """Remove a specific task by its number."""
    view_tasks(tasks)
    if tasks:
        try:
            task_num = int(input("\nEnter the task number to remove: "))
            if 1 <= task_num <= len(tasks):
                removed_task = tasks.pop(task_num - 1)
                print(f"Task '{removed_task}' removed successfully!")
            else:
                print("Invalid task number.")
        except ValueError:
            print("Please enter a valid number.")

def clear_tasks(tasks):
    """Remove all tasks."""
    confirm = input("\nAre you sure you want to clear all tasks? (y/n): ").strip().lower()
    if confirm == 'y':
        tasks.clear()
        print("All tasks cleared.")
    else:
        print("Operation canceled.")

def main():
    """Main function to run the To-Do List application."""
    tasks = []
    while True:
        clear_screen()
        display_menu()
        choice = input("\nChoose an option (1-5): ").strip()
        if choice == '1':
            clear_screen()
            view_tasks(tasks)
            input("\nPress Enter to return to the menu.")
        elif choice == '2':
            clear_screen()
            add_task(tasks)
            input("\nPress Enter to return to the menu.")
        elif choice == '3':
            clear_screen()
            remove_task(tasks)
            input("\nPress Enter to return to the menu.")
        elif choice == '4':
            clear_screen()
            clear_tasks(tasks)
            input("\nPress Enter to return to the menu.")
        elif choice == '5':
            print("\nGoodbye!")
            break
        else:
            print("\nInvalid option. Please choose a number between 1 and 5.")
            input("\nPress Enter to return to the menu.")

if __name__ == "__main__":
    main()
