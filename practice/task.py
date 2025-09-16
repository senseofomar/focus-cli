class Task:
    def __init__(self, title, priority = 'Medium', deadline = None, category = 'General', completed = False ):
        self.tt = title
        self.prt = priority
        self.dd = deadline
        self.cat = category
        self.comp = completed

    def mark_complete(self):
        self.comp =True

    def to_dict(self):
        return{
            "Title" : self.tt,
            "Priority" : self.prt,
            "Deadline" : self.dd,
            "Category" : self.cat,
            "Completed" : self.comp
        }


    @staticmethod
    def from_dict(data):
        return Task(#So when calling Task(...), the names must match what __init__ expects,
            # OR you must pass in positional arguments in the correct order.
            #Task(data["Title"], data["Deadline"], data["Priority"], data["Category"], data["Completed"]=="True")
            #using positional arguments above
            title = data["Title"],
            priority = data["Priority"],
            deadline = data["Deadline"],
            category = data["Category"],
            completed = data["Completed"]
        )


# t1.mark_complete() is equivalent internally to: Task.mark_complete(t1)