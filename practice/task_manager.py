class TaskManager:
    def __init__(self, filepath)->None:
        self.filepath = filepath,
        self.task = []
        self.load_task()

