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
                title = title,
                priority = priority if priority else "Medium",
                deadline = deadline if deadline else None,
                category = category if category else "General"
            )
            manager.add_task(task)
            print('✅ Task added!')

        elif choice =='2':
            manager.list_tasks()

        elif choice =='3':
            manager.list_tasks(show_completed = False)

        elif choice == '4':
            manager.list_tasks(show_completed = True)
            completed_task = int(input('No of the task you completed :' ))
            manager.complete_task(completed_task -1)


        else:
            print('You chose an invalid option')


if __name__ =='__main__':
    main()
