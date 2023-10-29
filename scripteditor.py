import flet as ft
import dbconnect as db

class ScriptEditorView(ft.Column):

    def __init__(self,script_id):
        super().__init__()

        header = ft.Text(script[1], size=36)

        script=db.get_script_with_id(script_id)
        script_text = ft.TextField(
            value=script[2]
            multiline=True
        )

        footer = ft.Row([ft.ElevatedButton("New Script", on_click=self.new_script_clicked)  ])
        self.controls=[header, script_text, footer]