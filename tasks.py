import flet as ft
import dbconnect as db
from taskoutput import TaskOutputView

class TasksToolbar(ft.Row):

    def __init__(self,parent,id):
        super().__init__()
    
        def script_output_clicked(e):
            parent.switch_view(TaskOutputView(id))

        self.id = id
        self.parent = parent
        self.height=40
        coutput = ft.IconButton(
                        icon=ft.icons.OUTPUT,
                        icon_color="green",
                        icon_size=20,
                        tooltip="Script Output",
                        on_click=script_output_clicked
                    )
        self.controls=[
            coutput,
        ]

class TasksView(ft.Column):
        
    def __init__(self,parent):

        super().__init__()
        self.parent = parent
        self.expand = True
        header = ft.Text("Tasks",size=36)
        tasks = db.get_tasks_for_taskview()
       
        footer = ft.Row([
        ])
        table = ft.DataTable(
            width=1200,
            bgcolor="white",
            border=ft.border.all(2, "black"),
        )
        table.columns=[
            ft.DataColumn(ft.Text("ID")),
            ft.DataColumn(ft.Text("Script")),
            ft.DataColumn(ft.Text("Status")),
            ft.DataColumn(ft.Text("Started")),
            ft.DataColumn(ft.Text("Finished")),
            ft.DataColumn(ft.Text("Tools"))
        ]
        for task in tasks:
            table.rows.append(ft.DataRow(cells=[
                ft.DataCell(ft.Text(task[0],)),
                ft.DataCell(ft.Text(task[1],)),
                ft.DataCell(ft.Text(task[2],)),
                ft.DataCell(ft.Text(task[3],)),
                ft.DataCell(ft.Text(task[4],)),
                ft.DataCell(TasksToolbar(parent,task[0]))
            ]))

        self.controls=[header,ft.Divider(),table,footer]