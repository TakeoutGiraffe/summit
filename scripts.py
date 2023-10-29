import flet as ft
import dbconnect as db

def get_scripts_view():
    header = ft.Container(ft.Text("Scripts",size=36))
    scripts = db.get_scripts()
    table = ft.DataTable()
    table.columns = [
        ft.DataColumn(ft.Text('ID')),
        ft.DataColumn(ft.Text('Script Name')),
        ft.DataColumn(ft.Text('Tools'))
    ]
    for script in scripts:
        table.rows.append(ft.DataRow(
            cells=[
                ft.DataCell(ft.Text(script[0])),
                ft.DataCell(ft.Text(script[0])),
                ft.DataCell(ft.Text(""))
            ]
        ))
    return ft.Column([header,ft.HorizontalLine(),table],expand=True)