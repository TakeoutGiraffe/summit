import flet as ft
import dbconnect as db

class Scripts(ft.UserControl):

    def __init__(self):
        super().__init__(self)
        self.scripts = db.get_scripts()
        #self.height=height

    def build(self):
        #lv = ft.ListView()
       # for script in self.scripts:
        #    lv.controls.append(ft.Text(script[1]))
        return ft.Column([Text("Scripts"),Text("Hello"),],expand=True)