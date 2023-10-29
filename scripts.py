import flet as ft
import dbconnect as db

def get_scripts_view():
    header = ft.Container(ft.Text("Script"))
    scripts = db.get_scripts()
    table = ft.DataTable()
    table.columns = [
        ft.DataColumn(ft.Text('ID')),
        ft.DataColumn(ft.Text('Script Name')),
        ft.DataColumn(ft.Text('Tools'))
    ]
    for script in scripts:
        table.rows.add(ft.DataRow(
            cells=[
                ft.DataCell(ft.Text(script[0])),
                ft.DataCell(ft.Text(script[0])),
                ft.DataCell(ft.Text(""))

            ]
        ))
    return ft.Column([header,table],expand=True)