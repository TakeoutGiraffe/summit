import flet as ft
import dbconnect as db

class Scripts(ft.UserControl):

    def __init__(self):
        self.scripts = db.get_scripts()

    def build(self):
        return ft.Text(self.scripts)