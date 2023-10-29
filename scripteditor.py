import flet as ft
import dbconnect as db

class ScriptEditorView(ft.Column):

    def __init__(self,script_id):
        super().__init__()
        db=get_script_with_id(script_id)
        self.controls=[ ft.Text("XX")]