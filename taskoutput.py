import flet as ft
import dbconnect as db

class TaskOutputView(ft.Column):

    def __init__(self,task_id):
        super().__init__()
        self.script_id = script_id
        output=db.get_task_output(task_id)[0]
        self.expand=True
        header = ft.Text(script[1], size=36)

        self.script_text = ft.TextField(
            expand=True,
            value=output,
            multiline=True
        )

        footer = ft.Row([])
        self.controls=[header, self.script_text, footer]