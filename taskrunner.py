import dbconnect as db
from io import StringIO
from contextlib import redirect_stdout

class TaskRunner:
    
    def __init__(self,task):
        self.task = task
        
    def run(self):
        print(f"Starting Task {self.task}")
        db.set_task_status(self.task, 1)
        db.set_task_start(self.task)

        details = db.get_task_details(self.task)

        f = StringIO()
        with redirect_stdout(f):
            exec(details[0][1])

        s = f.getvalue()

        db.set_task_finish(self.task)
        db.set_task_status(self.task,10)
        db.set_task_output(self.task,s)

