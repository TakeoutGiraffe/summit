import flet as ft
 
class Workspace(ft.UserControl):
    def build(self):
        return ft.Text("Hello")

def main(page: ft.page):
    page.title = "Summit"
    page.padding = 0
    page.bgcolor = ft.colors.BLUE_GREY_200
    workspace = Workspace()
    page.add(workspace)
    page.update()
 
ft.app(target=main)