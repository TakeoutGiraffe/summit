import dbconnect as db
class TaskRunner:
    
    def __init__(self,task):
        self.task = task
        
    def run(self):
        print(f"Starting Task {self.task}")
        db.set_task_status(self.task, 1)
        db.set_task_start(self.task)
