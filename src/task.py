from datetime import datetime

class Task:
    def __init__(self, title, due_date=None, priority='Medium', category='General', completed=False):
        self.title = title
        self.due_date = due_date  # string: 'YYYY-MM-DD'
        self.priority = priority
        self.category = category
        self.completed = completed

    def mark_complete(self):
        self.completed = True

    def to_dict(self):
        return {
            'Title': self.title,
            'Due Date': self.due_date,
            'Priority': self.priority,
            'Category': self.category,
            'Completed': self.completed
        }

    @staticmethod
    def from_dict(data):
        return Task(
            title=data['Title'],
            due_date=data['Due Date'],
            priority=data['Priority'],
            category=data['Category'],
            completed=data['Completed'] == 'True'
        )
