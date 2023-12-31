import flet as ft
import dbconnect as db

class TaskOutputView(ft.Column):

    def __init__(self,task_id):
        super().__init__()
        self.script_id = task_id
        output=db.get_task_output(task_id)[0]
        self.expand=True
        header = ft.Row([ft.Text(output[1],size=36), ft.Text(output[0],size=32)])

        self.script_text = ft.TextField(
            expand=True,
            value=output[2],
            multiline=True
        )

        footer = ft.Row([])
        self.controls=[header, self.script_text, footer]