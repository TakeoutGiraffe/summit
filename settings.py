import flet as ft

class SettingsView(ft.Column):
    def __init__(self):
        super().__init__()
        self.controls= [ft.Text("Settings")]