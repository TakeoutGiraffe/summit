import flet as ft

class SchedulesView(ft.Column):
    def __init__(self):
        super().__init__()
        self.controls= ft.Text("Schedules")