from task_manager import TaskManager
from task import Task

FILE_PATH = '../data/tasks.csv'

def main():
    manager = TaskManager(FILE_PATH)

    while True:
        print("\n--- TASK MANAGER ---")
        print("1. Add Task")
        print("2. List Tasks")
        print("3. List Incomplete Tasks")
        print("4. Complete Task")
        print("5. Exit")
        choice = input("Choose an option: ")

        if choice == '1':
            title = input("Task title: ")
            due = input("Due date (YYYY-MM-DD): ")
            priority = input("Priority (Low/Medium/High): ")
            category = input("Category (e.g., Work/Study/Health): ")
            task = Task(title=title, due_date=due, priority=priority, category=category)
            manager.add_task(task)

        elif choice == '2':
            manager.list_tasks()

        elif choice == '3':
            manager.list_tasks(show_completed=False)

        elif choice == '4':
            index = int(input("Enter task number to mark complete: ")) - 1
            manager.complete_task(index)

        elif choice == '5':
            print("👋 Goodbye!")
            break

        else:
            print("Invalid option.")

if __name__ == '__main__':
    main()
