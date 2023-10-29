import flet as ft
import dbconnect as db

def get_scripts_view():
    return ft.Column([ft.Text("Scripts"),ft.Text("Hello"),],expand=True)