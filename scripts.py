import flet as ft
import dbconnect as db

def get_scripts_view():
    return ft.Column([Text("Scripts"),Text("Hello"),],expand=True)