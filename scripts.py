import flet as ft
import dbconnect as db

def get_scripts_view():
    header = ft.Container(ft.Text("Script"))
    scripts = db.get_scripts()
    lv = ft.ListView()
    for script in scripts:
        lv.controls.append(ft.Text(script[1]))
    return ft.Column([header,lv,],expand=True)