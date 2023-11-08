import flet as ft
import dbconnect as db
from io import StringIO
from contextlib import redirect_stdout

class ScriptOutputView(ft.Column):

    def save_clicked(self,e):
        db.save_script(self.script_id, self.script_text.value)

    def __init__(self,script_id):
        super().__init__()
        self.script_id = script_id
        script=db.get_script_with_id(script_id)[0]
        self.expand=True
        header = ft.Text(script[1], size=36)

        f = StringIO()
        with redirect_stdout(f):
            exec(script[2])
        s = f.getvalue()

        self.script_text = ft.TextField(
            expand=True,
            value=s,
            multiline=True
        )

        footer = ft.Row([ft.ElevatedButton("Save", on_click = self.save_clicked)  ])
        self.controls=[header, self.script_text, footer]