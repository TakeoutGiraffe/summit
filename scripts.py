import flet as ft
import dbconnect as db

def get_script_view():
    return ft.Column([Text("Scripts"),Text("Hello"),],expand=True)