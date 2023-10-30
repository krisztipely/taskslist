# taskslist
This is a simple Python script that allows users to manage their tasks. The program provides basic functionality to view tasks, add new tasks, mark tasks as completed, and exit the application. Task data is stored in a text file, enabling persistence across application sessions.

## Features

**File Operations:**

The script utilizes file operations to load existing tasks from a file ('tasks.txt') and save tasks back to the file.

**Task Management:**

Users can view their tasks, add new tasks, and mark tasks as completed.

**User Interface:**

The application employs a console-based menu system for easy user interaction.

## Usage

**Clone the repository to your local machine:**
```
git clone https://github.com/krisztipely/tasklist.git
```
**Navigate to the project directory:**
```
cd tasklist
```
**Run the Python script:**
```
list.py
```
Follow the on-screen prompts to manage your to-do list.

## Customization

**Feel free to customize the script based on your requirements:**

- Modify the file name or path for task storage.
- Add new features such as due dates, priority levels, or task categories.
  
**Example**

```
Options:
1. View tasks
2. Add task
3. Mark task as completed
4. Exit

Enter your choice (1-4): 2
Enter the new task: Complete project report
Task 'Complete project report' added successfully.

Options:
1. View tasks
2. Add task
3. Mark task as completed
4. Exit

Enter your choice (1-4): 1
Tasks:
1. Complete project report

Options:
1. View tasks
2. Add task
3. Mark task as completed
4. Exit

Enter your choice (1-4): 3
Tasks:
1. Complete project report
Enter the task number to mark as completed: 1
Task 'Complete project report' marked as completed.

Options:
1. View tasks
2. Add task
3. Mark task as completed
4. Exit

Enter your choice (1-4): 4
Exiting the to-do list application.
```
## License
MIT 2023, Krisztina-Ronkainen Lakner
