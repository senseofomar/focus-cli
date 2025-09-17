import csv
import os

from src.task import Task


class TaskManager:
    def __init__(self, filepath)-> None:
        self.filepath = filepath
        self.tasks = []
        self.load_tasks()

    def add_tasks(self)-> None:
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
                self.tasks.append(Task.from_dict())