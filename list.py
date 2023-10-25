import os

# Function to load tasks from a file
def load_tasks():
    if os.path.exists('tasks.txt'):
        with open('tasks.txt', 'r') as file:
            tasks = file.read().splitlines()
        return tasks
    else:
        return []

# Function to save tasks to a file
def save_tasks(tasks):
    with open('tasks.txt', 'w') as file:
        for task in tasks:
            file.write(task + '\n')

# Function to display tasks
def display_tasks(tasks):
    print("Tasks:")
    for index, task in enumerate(tasks, start=1):
        print(f"{index}. {task}")
    print()

# Main function
def main():
    tasks = load_tasks()

    while True:
        print("Options:")
        print("1. View tasks")
        print("2. Add task")
        print("3. Mark task as completed")
        print("4. Exit")

        choice = input("Enter your choice (1-4): ")

        if choice == '1':
            display_tasks(tasks)
        elif choice == '2':
            new_task = input("Enter the new task: ")
            tasks.append(new_task)
            save_tasks(tasks)
            print(f"Task '{new_task}' added successfully.\n")
        elif choice == '3':
            display_tasks(tasks)
            task_index = int(input("Enter the task number to mark as completed: ")) - 1

            if 0 <= task_index < len(tasks):
                completed_task = tasks.pop(task_index)
                print(f"Task '{completed_task}' marked as completed.\n")
                save_tasks(tasks)
            else:
                print("Invalid task number. Please try again.\n")
        elif choice == '4':
            print("Exiting the to-do list application.")
            break
        else:
            print("Invalid choice. Please enter a number between 1 and 4.\n")

if __name__ == "__main__":
    main()
