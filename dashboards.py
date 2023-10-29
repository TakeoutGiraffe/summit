import flet as ft

class DashboardView(ft.Column):
    def __init__(self):
            super().__init__()
            self.controls= ft.Text("Dashboards")