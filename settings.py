import flet as ft

class SettingsView(ft.Container):
    def __init__(self):
        super().__init__()
        self.controls= ft.Text("Settings")