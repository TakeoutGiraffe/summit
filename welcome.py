import flet as ft

class WelcomeView(ft.Column):
    def __init__(self):
        super().__init__()
        self.controls=[ft.Text("Welcome")]
        self.expand=True