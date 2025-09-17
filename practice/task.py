class Task:
    def __init__(self, title, priority = 'Medium', deadline = None, category = 'General', completed = False ):
        self.tt = title
        self.prt = priority
        self.dd = deadline
        self.cat = category
        self.comp = completed

    def mark_complete(self):
        self.comp =True

    def to_dict(self):  #  # return dictionary version (for CSV)
        return{
            "Title" : self.tt,
            "Priority" : self.prt,
            "Deadline" : self.dd,
            "Category" : self.cat,
            "Completed" : self.comp
        }


    @staticmethod
    def from_dict(data):    #  # rebuild Task from dictionary
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
'''
Simple Analogy

Think of Task like a cookie cutter 🍪:

__init__ → bakes a cookie (task) with title, date, etc.

mark_complete() → bites a piece off the cookie (changes the state).

to_dict() → flattens cookie into a recipe card (dictionary).

from_dict() → takes a recipe card and bakes a new cookie.

from_dict doesn’t care about any already-baked cookies → it just knows how to create a fresh one. That’s why it’s @staticmethod.
'''

# t1.mark_complete() is equivalent internally to: Task.mark_complete(t1)