import flet as ft
import dbconnect as db

class Scripts(ft.UserControl):

    def __init__(self):
        self.scripts = db.get_scripts()

    def build(self):
        rv = ft.Row()
        for script in self.scripts:
            rv.controls.append(ft.Text(script[1]))
        return rv