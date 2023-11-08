import flet as ft
import dbconnect as db

class ScriptEditorView(ft.Column):

    def save_clicked(self,e):
        db.save_script(self.script_id, self.script_text.value)

    def __init__(self,script_id):
        super().__init__()

        script=db.get_script_with_id(script_id)[0]
        self.expand=True
        print(script)
        header = ft.Text(script[1], size=36)

        self.script_text = ft.TextField(
            expand=True,
            value=script[2],
            multiline=True
        )

        footer = ft.Row([ft.ElevatedButton("Save", on_click = self.save_clicked)  ])
        self.controls=[header, self.script_text, footer]