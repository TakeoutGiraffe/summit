import flet as ft

class WelcomeView(ft.Column):
    def __init__(self):
        super().__init__()
        controls=[ft.Text("Welcome")]
        expand=True