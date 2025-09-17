import csv
import os
from practice.task import Task


class TaskManager:
    def __init__(self, filepath)->None:
        self.filepath = filepath
        self.tasks = []
        self.load_tasks()

    def add_task(self, task)->None:
        self.tasks.append(task)
        self.save_tasks()

    def save_tasks(self)->None:
        with open(self.filepath, mode = "w", newline="", encoding="utf-8") as f:
            writer = csv.DictWriter(f, fieldnames=[
                'Title', 'Priority', 'Deadline',
                'Category', 'Completed'])
            writer.writeheader() #Writes the first row of the CSV — the column headers (Title, Due Date, Priority, Category, Completed).
            for task in self.tasks:
                writer.writerow(task.to_dict()) #Writes one row to the CSV for each task.


    def load_tasks(self)->None:
        if not os.path.exists(self.filepath):
            return
        with open(self.filepath, mode ='r',newline ='' ,encoding ='utf-8') as f:
            reader = csv.DictReader(f)
            for row in reader:
                try:
                    self.tasks.append(Task.from_dict(row))
                except KeyError as e:
                    print(f"⚠️ Skipping row due to missing column: {e}")


    def list_tasks(self, show_completed = True)->None:
        for index, task in enumerate(self.tasks, start =1):
            if not show_completed and task.completed:
                continue
            status = "✅" if task.completed else "❌"
            print(
                f"{index}. {task.tt}| Deadline: {task.dd} | Priority: {task.prt} | Category: {task.cat} | Completed: {status}")


    def complete_task(self, index)-> None:
        if 0<= index<len(self.tasks):
            self.tasks[index].mark_complete()
            self.save_tasks()
        else:
            print("❗ Invalid task number.")