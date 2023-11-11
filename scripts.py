import flet as ft
import dbconnect as db
from scripteditor import ScriptEditorView

class ScriptToolbar(ft.Row):

    def __init__(self,parent,id):
        super().__init__()
    
        def edit_script_clicked(e):
            parent.switch_view(ScriptEditorView(id))

        def run_script_clicked(e):
            db.add_task(id)

        self.id = id
        self.parent = parent
        self.height=40
        crun = ft.IconButton(
                        icon=ft.icons.PLAY_ARROW,
                        icon_color="green",
                        icon_size=20,
                        tooltip="Run Script",
                        on_click=run_script_clicked
                    )
        cedit = ft.IconButton(
                        icon=ft.icons.EDIT,
                        icon_color="blue400",
                        icon_size=20,
                        tooltip="Edit Script",
                        on_click=edit_script_clicked
                    )
        cdel = ft.IconButton(
                        icon=ft.icons.DELETE,
                        icon_color="red",
                        icon_size=20,
                        tooltip="Delete Script",
                    )
        self.controls=[
            crun,
            cedit,
            cdel
        ]

class ScriptsView(ft.Column):

    def close_dialog(self,e):
        self.new_script_dialog.open = False
        self.parent.page.update()

    def confirm_new_script(self,e):
        self.new_script_dialog.open = False
        db.add_script(self.new_script_dialog.content.value)
        self.parent.page.update()

    def new_script_clicked(self,e):
        self.page.dialog = self.new_script_dialog
        self.new_script_dialog.open = True
        self.parent.page.update()
        
    def __init__(self,parent):

        super().__init__()
        self.parent = parent
        self.expand = True
        header = ft.Text("Scripts",size=36)
        scripts = db.get_scripts()
       
        self.new_script_dialog = ft.AlertDialog(
            modal=True,
            title=ft.Text("Create New Script"),
            content=ft.TextField(label="Name")
            actions=[
                ft.TextButton("OK", on_click=self.confirm_new_script),
                ft.TextButton("Cancel", on_click=self.close_dialog),
            ],
            actions_alignment=ft.MainAxisAlignment.END,
        )

        footer = ft.Row([
            ft.ElevatedButton("New Script", on_click=self.new_script_clicked)   
        ])
        table = ft.DataTable(
            width=1000,
            bgcolor="white",
            border=ft.border.all(2, "black"),
        )
        table.columns=[
            ft.DataColumn(ft.Text("ID")),
            ft.DataColumn(ft.Text("Name")),
            ft.DataColumn(ft.Text("Tools"))
        ]
        for script in scripts:
            table.rows.append(ft.DataRow(cells=[
                ft.DataCell(ft.Text(script[0],)),
                ft.DataCell(ft.Text(script[1],)),
                ft.DataCell(ScriptToolbar(parent,script[0]))
            ]))

        self.controls=[header,ft.Divider(),table,footer]