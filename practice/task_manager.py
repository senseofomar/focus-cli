import csv


class TaskManager:
    def __init__(self, filepath)->None:
        self.filepath = filepath,
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