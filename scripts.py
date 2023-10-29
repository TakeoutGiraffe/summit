import flet as ft
import dbconnect as db

class Scripts(ft.UserControl):

    def __init__(self):
        super().__init__(self)
        self.scripts = db.get_scripts()

    def build(self):
        lv = ft.ListView(expand=true)
        for script in self.scripts:
            lv.controls.append(ft.Text(script[1]))
        return lv