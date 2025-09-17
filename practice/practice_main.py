from task_manager import TaskManager
from task import Task

FILE_PATH = 'practice_tasks.csv'

def main():
    manager = TaskManager(FILE_PATH)
    while True:
        print("\n--- TASK MANAGER ---")
        print("1. Add Task")
        print("2. List Tasks")
        print("3. List Incomplete Tasks")
        print("4. Complete Task")
        print("5. Exit")

        choice = input('Choose an option:')

        if choice == '5':
            print('👋 Goodbye')
            break

        elif choice == '1':
            title = input("Enter task title: ")
            priority = input("Enter priority (High/Medium/Low, default=Medium): ")
            deadline = input("Enter due date (YYYY-MM-DD, or leave blank): ")
            category = input("Enter category (default=General): ")

            task = Task(
                title,
                priority if priority else "Medium",
                deadline if deadline else None,
                category if category else "General"
            )

            manager.add_task(task)
            print('✅ Task added!')

        elif choice =='2':
            manager.list_tasks()

        else:
            print('You chose option :', choice)


if __name__ =='__main__':
    main()
