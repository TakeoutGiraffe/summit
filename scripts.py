import flet as ft
import dbconnect as db

class Scripts(ft.UserControl):

    def __init__(self):
        self.scripts = db.get_scripts()

    def build(self):
        rv = ft.Column()
        for x in self.scripts:
            rv.add(ft.Text((script[0]))
        return rv