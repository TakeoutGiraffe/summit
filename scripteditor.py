import flet as ft
import dbconnect as db

class ScriptEditorView(ft.Container):

    def __init__(self):
        super().__init__()
        self.controls= ft.Text("XX")