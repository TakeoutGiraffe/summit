import time

class Scheduler:

    def __init__(self):
        self.quit=False

    def loop(self):
        while (self.quit == False):
            print("Checking for new tasks")
            time.sleep(10)
        