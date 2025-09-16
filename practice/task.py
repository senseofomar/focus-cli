class Task:
    def __init__(self, title, priority = 'Medium', deadline = None, category = 'General', completion = False ):
        self.tt = title
        self.prt = priority
        self.dd = deadline
        self.cat = category
        self.comp = completion

    def mark_complete(self):
        self.comp =True

    def to_dict(self):
        return{
            "Title" : self.tt,
            "Priority" : self.prt,
            "Deadline" : self.dd,
            "Category" : self.cat,
            "Completion" : self.comp
        }


    @staticmethod
    def from_dict(data):
        return Task(
            title = data["Title"],
            priority = data["Priority"],
            deadline = data["Deadline"],
            category = data["Category"],
            completion = data["Completion"]
        )