import dbconnect as db
class TaskRunner:
    
    def __init__(self,task):
        self.task = task
        
    def run(self):
        db.set_task_status(self.task, 1)
