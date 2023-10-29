import flet as ft

class SecurityView(ft.Column):
    def __init__(self):
        super().__init__()
        self.controls= [ft.Text("Security")]