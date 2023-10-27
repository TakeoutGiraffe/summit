import flet as ft
from welcome import Welcome
 
class Workspace(ft.UserControl):
    def build(self):

        rail = ft.NavigationRail(
            selected_index=0,
            label_type=ft.NavigationRailLabelType.ALL,
            min_width=100,
            min_extended_width=400,
            extend=True,
            leading=ft.FloatingActionButton(icon=ft.icons.CREATE, text="Add"),
            group_alignment=-0.9,
            destinations=[
                ft.NavigationRailDestination(
                    icon=ft.icons.FAVORITE_BORDER, selected_icon=ft.icons.FAVORITE, label="First"
                ),
                ft.NavigationRailDestination(
                    icon_content=ft.Icon(ft.icons.BOOKMARK_BORDER),
                    selected_icon_content=ft.Icon(ft.icons.BOOKMARK),
                    label="Second",
                ),
                ft.NavigationRailDestination(
                    icon=ft.icons.SETTINGS_OUTLINED,
                    selected_icon_content=ft.Icon(ft.icons.SETTINGS),
                    label_content=ft.Text("Settings"),
                ),
            ],
            on_change=lambda e: print("Selected destination:", e.control.selected_index),
        )

        return ft.Row([
            rail,
            Welcome()
        ],expand=True)

def main(page: ft.page):
    page.title = "Summit"
    page.padding = 0
    page.bgcolor = ft.colors.BLUE_GREY_200
    workspace = Workspace()
    page.add(workspace)
    page.update()
 
ft.app(target=main)