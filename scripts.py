import flet as ft
import dbconnect as db

def get_scripts_view():
    header = ft.Container(ft.Text("Scripts",size=36))
    scripts = db.get_scripts()
    table = ft.DataTable(
        bgcolor="white",
        border=ft.border.all(2, "black"),
        border_radius=10,
        vertical_lines=ft.border.BorderSide(3, "black"),
        horizontal_lines=ft.border.BorderSide(1, "black"),
    )
    footer = ft.Row([
        ft.ElevatedButton("New Script")   
    ])
    tools = ft.Row([
        ft.IconButton(
                    icon=ft.icons.PLAY_ARROW,
                    icon_color="green",
                    icon_size=40,
                    tooltip="Run Script",
                ),
        ft.IconButton(
                    icon=ft.icons.EDIT,
                    icon_color="blue400",
                    icon_size=40,
                    tooltip="Edit Script",
                ),
        ft.IconButton(
                    icon=ft.icons.DELETE,
                    icon_color="red",
                    icon_size=40,
                    tooltip="Delete Script",
                ),
    ])
    table.columns = [
        ft.DataColumn(ft.Text('ID')),
        ft.DataColumn(ft.Text('Script Name')),
        ft.DataColumn(ft.Text("Tools"))
    ]
    for script in scripts:
        table.rows.append(ft.DataRow(
            cells=[
                ft.DataCell(ft.Text(script[0])),
                ft.DataCell(ft.Text(script[1])),
                ft.DataCell(tools)
            ]
        ))
    return ft.Column([header,ft.Divider(),table,footer],expand=True)