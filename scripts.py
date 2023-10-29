import flet as ft
import dbconnect as db

def get_scripts_view():
    header = ft.Container(ft.Text("Scripts",size=36))
    scripts = db.get_scripts()
    table = ft.DataTable()
    tools = ft.Row([
        ft.ElevatedButton("New Script")   
    ])
    tools = ft.Row([
        ft.IconButton(
                    icon=ft.icons.PAUSE_CIRCLE_FILLED_ROUNDED,
                    icon_color="blue400",
                    icon_size=20,
                    tooltip="Pause record",
                ),
        ft.IconButton(
                    icon=ft.icons.PAUSE_CIRCLE_FILLED_ROUNDED,
                    icon_color="blue400",
                    icon_size=20,
                    tooltip="Pause record",
                ),
    ])
    table.columns = [
        ft.DataColumn(ft.Text('ID')),
        ft.DataColumn(ft.Text('Script Name')),
        ft.DataColumn(ft.Text('Tools'))
    ]
    for script in scripts:
        table.rows.append(ft.DataRow(
            cells=[
                ft.DataCell(ft.Text(script[0])),
                ft.DataCell(ft.Text(script[1])),
                ft.DataCell(ft.Text(""))
            ]
        ))
    return ft.Column([header,ft.Divider(),table,footer],expand=True)