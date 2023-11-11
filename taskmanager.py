import time
import dbconnect as db

class TaskManager:

    def __init__(self):
        self.quit=False
        print("Task Manager initialilised")

    def loop(self):
        while (self.quit == False):
            print("Checking for new tasks")

            tasks = db.get_pending_tasks()
            for task in tasks:
                db.set_taskStatus(task[0], 1)

            time.sleep(60)
        