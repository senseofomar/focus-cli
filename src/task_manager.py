import csv
import os
from task import Task

class TaskManager:
    def __init__(self, filepath):
        self.filepath = filepath
        self.tasks = []
        self.load_tasks()

    def add_task(self, task):
        self.tasks.append(task)
        self.save_tasks()

    def list_tasks(self, show_completed=True):
        for idx, task in enumerate(self.tasks, start=1):
            if not show_completed and task.completed:
                continue
            status = '✅' if task.completed else '❌'
            print(f"{idx}. {task.title} | Due: {task.due_date} | Priority: {task.priority} | Category: {task.category} | {status}")

    def complete_task(self, index):
        if 0 <= index < len(self.tasks):
            self.tasks[index].mark_complete()
            self.save_tasks()
        else:
            print("❗ Invalid task number.")

    def save_tasks(self):
        with open(self.filepath, mode='w', newline='', encoding='utf-8') as f:
            writer = csv.DictWriter(f, fieldnames=['Title', 'Due Date', 'Priority', 'Category', 'Completed'])
            writer.writeheader()
            for task in self.tasks:
                writer.writerow(task.to_dict())

    def load_tasks(self):
        if not os.path.exists(self.filepath):
            return
        with open(self.filepath, mode='r', newline='', encoding='utf-8') as f:
            reader = csv.DictReader(f)
            for row in reader:
                try:
                    self.tasks.append(Task.from_dict(row))
                except KeyError as e:
                    print(f"⚠️ Skipping row due to missing column: {e}")
