import flet as ft

class TasksView(ft.Container):
    def __init__(self):
        super().__init__()
        self.controls= ft.Text("Tasks")