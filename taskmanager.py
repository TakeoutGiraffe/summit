import time
import dbconnect as db
import threading as t
from taskrunner import TaskRunner

class TaskManager:

    def __init__(self):
        self.quit=False
        print("Task Manager initialilised")

    def loop(self):
        while (self.quit == False):
            print("Checking for new tasks")

            tasks = db.get_pending_tasks()
            for task in tasks:
                tr = TaskRunner(task[0])
                trf = t.Thread(target=tr.run)
                trf.start()

            time.sleep(60)
        