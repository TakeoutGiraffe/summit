import flet as ft
import dbconnect as db
from scripteditor import ScriptEditorView

class ScriptItem(ft.Row):

    def __init__(self,parent,id,name):
        super().__init__()
    
        def edit_script_clicked(e):
            print (id)

        self.id = id
        self.parent = parent
        cid = ft.Text(id),
        cname = ft.Text(name),
        crun = ft.IconButton(
                        icon=ft.icons.PLAY_ARROW,
                        icon_color="green",
                        icon_size=40,
                        tooltip="Run Script",
                    ),
        cedit = ft.IconButton(
                        icon=ft.icons.EDIT,
                        icon_color="blue400",
                        icon_size=40,
                        tooltip="Edit Script",
                        on_click=edit_script_clicked
                    ),
        cdel = ft.IconButton(
                        icon=ft.icons.DELETE,
                        icon_color="red",
                        icon_size=40,
                        tooltip="Delete Script",
                    ),
        self.controls=[cid,cname,crun,cedit,cdel]

class ScriptsView(ft.Column):

    def new_script_clicked(self,e):
        print("New Script")
        
    def __init__(self,parent):

        super().__init__()
        self.parent = parent
        header = ft.Text("Scripts",size=36)
        scripts = db.get_scripts()
       
        footer = ft.Row([
            ft.ElevatedButton("New Script", on_click=self.new_script_clicked)   
        ])
        table = ft.ListView()

        for script in scripts:
            table.controls.append(ScriptItem(self.parent, script[0], script[1]))

        self.controls=[header,ft.Divider(),table,footer]