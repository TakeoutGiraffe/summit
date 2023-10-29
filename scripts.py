import flet as ft
import dbconnect as db
from scripteditor import ScriptEditorView

class ScriptsView(ft.Column):

    def new_script_clicked(self,e):
        sev=ScriptEditorView()
        self.parent.switch_view(sev)

    def __init__(self,parent):
        super().__init__()
        self.parent = parent
        header = ft.Text("Scripts",size=36)
        scripts = db.get_scripts()
        table = ft.DataTable(
            bgcolor="white",
            border=ft.border.all(2, "black"),
            border_radius=10,
            vertical_lines=ft.border.BorderSide(3, "black"),
            horizontal_lines=ft.border.BorderSide(1, "black"),
        )
        footer = ft.Row([
            ft.ElevatedButton("New Script", on_click=self.new_script_clicked)   
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
        self.controls=[header,ft.Divider(),table,footer]