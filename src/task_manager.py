import csv
import os

from src.task import Task


class TaskManager:
    def __init__(self, filepath)-> None:
        self.filepath = filepath
        self.tasks = []
        self.load_tasks()

    def add_tasks(self, task)-> None:
        self.tasks.append(task)
        self.save_tasks()

    def save_tasks(self)-> None:
        with open (self.filepath, mode = 'w', newline = '', encoding = 'utf-8') as f:
            writer = csv.DictWriter(f, fieldnames =[
                            'Title', 'Deadline', 'Priority',
                            'Category', 'Completion'])
            writer.writeheader()
            for task in self.tasks:
                writer.writerows(task.to_dict())

    def load_tasks(self)->None:
        if not os.path.exists(self.filepath):
            return
        with open (self.filepath, mode ='r', newline = '', encoding = 'utf-8') as f:
            reader = csv.DictReader(f)
            for row in reader:
                try:
                    self.tasks.append(Task.from_dict(row))
                except KeyError as e:
                    print(f"⚠️ Skipping row due to missing column: {e}")

    def list_tasks(self, show_completed =True)->None:
        for idx, task in enumerate( self.tasks, start = 1):
            if not show_completed and task.completed:
                continue
            status = "✅" if task.completed else "❌"
            print(
                f"{idx}. {task.title}| Deadline: {task.due_date} | Priority: {task.priority} | Category: {task.category} | Completed: {status}")


    def complete_task(self, idx)->None:
        if 0<= idx< len(self.tasks):
            self.tasks[idx].mark_complete()
            self.save_tasks()
        else:
            print("❗ Invalid task number.")


