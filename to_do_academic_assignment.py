# Import necessary module
import json
import os

# Define the file path for storing tasks
FILE_PATH = 'todo_tasks.json'

def load_tasks():
    #Load tasks from the JSON file.
    if os.path.exists(FILE_PATH):
        with open(FILE_PATH, 'r') as file:
            tasks = json.load(file)
    else:
        tasks = []
    return tasks

def save_tasks(tasks):
    #Save tasks to the JSON file.
    with open(FILE_PATH, 'w') as file:
        json.dump(tasks, file)

def add_task(task):
    #Add a new task to the task list.
    tasks = load_tasks()
    tasks.append({'task': task, 'done': False})
    save_tasks(tasks)
    print(f'Task "{task}" added.')

def view_tasks():
    #View all tasks in the task list.
    tasks = load_tasks()
    if tasks:
        for index, task in enumerate(tasks, start=1):
            status = 'Done' if task['done'] else 'Pending'
            print(f"{index}. {task['task']} [{status}]")
    else:
        print("No tasks available.")

def delete_task(task_number):
    #Delete a task from the task list
    tasks = load_tasks()
    if 0 < task_number <= len(tasks):
        removed_task = tasks.pop(task_number - 1)
        save_tasks(tasks)
        print(f'Task "{removed_task["task"]}" deleted.')
    else:
        print("Invalid task number.")

def mark_task_done(task_number):
    #Mark a task as done 
    tasks = load_tasks()
    if 0 < task_number <= len(tasks):
        tasks[task_number - 1]['done'] = True
        save_tasks(tasks)
        print(f'Task "{tasks[task_number - 1]["task"]}" marked as done.')
    else:
        print("Invalid task number.")

def main():
    #Main function to interact with the to-do app.
    while True:
        print("\nTo-Do App Menu:")
        print("1. Add Task")
        print("2. View Tasks")
        print("3. Delete Task")
        print("4. Mark Task as Done")
        print("5. Exit")
        
        choice = input("Enter your choice (1-5): ")
        
        if choice == '1':
            task = input("Enter the task: ")
            add_task(task)
        elif choice == '2':
            view_tasks()
        elif choice == '3':
            task_number = int(input("Enter task number to delete: "))
            delete_task(task_number)
        elif choice == '4':
            task_number = int(input("Enter task number to mark as done: "))
            mark_task_done(task_number)
        elif choice == '5':
            print("Exiting To-Do App. Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

# Entry point of the program
if __name__ == "__main__":
    main()
