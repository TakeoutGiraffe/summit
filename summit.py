import flet as ft
from welcome import Welcome
from apiendpoints import APIEndpoints
from schedules import Schedules
from scripts import Scripts
from security import Security
from tasks import Tasks
from settings import Settings
from dashboards import Dashboards
 
class Workspace(ft.UserControl):

    def __init__(self):
        super().__init__()
        self.selectedControl=Welcome()

    def build(self):

        def newScreenSelected(e):
            print (e.control.selected_index)
            if e.control.selected_index == 0:
                self.selectedControl = APIEndpoints()
                update()
            elif e.control.selected_index == 1:
                self.selectedControl = Scripts()
                update()
            elif e.control.selected_index == 2:
                self.selectedControl = Tasks()
                update()
            elif e.control.selected_index == 3:
                self.selectedControl = Schedules()
                update()
            elif e.control.selected_index == 4:
                self.selectedControl = Dashboards()
                update()
            elif e.control.selected_index == 5:
                self.selectedControl = Security()
                update()
            elif e.control.selected_index == 6:
                self.selectedControl = Settings()
                update()

        rail = ft.NavigationRail(
            selected_index=0,
            label_type=ft.NavigationRailLabelType.ALL,
            min_width=100,
            min_extended_width=300,
            extended=True,
            group_alignment=-0.9,
            destinations=[
                ft.NavigationRailDestination(
                    icon=ft.icons.FAVORITE_BORDER, selected_icon=ft.icons.FAVORITE, label="API Endpoints"
                ),
                ft.NavigationRailDestination(
                    icon=ft.icons.FAVORITE_BORDER, selected_icon=ft.icons.FAVORITE, label="Scripts"
                ),
                ft.NavigationRailDestination(
                    icon=ft.icons.FAVORITE_BORDER, selected_icon=ft.icons.FAVORITE, label="Running Tasks"
                ),
                ft.NavigationRailDestination(
                    icon=ft.icons.FAVORITE_BORDER, selected_icon=ft.icons.FAVORITE, label="Schedules"
                ),
                ft.NavigationRailDestination(
                    icon=ft.icons.FAVORITE_BORDER, selected_icon=ft.icons.FAVORITE, label="Dashboards"
                ),
                ft.NavigationRailDestination(
                    icon=ft.icons.FAVORITE_BORDER, selected_icon=ft.icons.FAVORITE, label="Security"
                ),
                ft.NavigationRailDestination(
                    icon=ft.icons.FAVORITE_BORDER, selected_icon=ft.icons.FAVORITE, label="Settings"
                ),
            ],
            on_change=newScreenSelected,
            )
        print(type(self.selectedControl))
        return ft.Row([
            rail,
            ft.VerticalDivider(),
            self.selectedControl
            ],expand=True)


def main(page: ft.page):
    page.appbar = ft.AppBar(
        leading=ft.Icon(ft.icons.PALETTE),
        leading_width=40,
        title=ft.Text("AppBar Example"),
        center_title=False,
        bgcolor=ft.colors.SURFACE_VARIANT,
        actions=[
            ft.IconButton(ft.icons.WB_SUNNY_OUTLINED),
            ft.IconButton(ft.icons.FILTER_3),
            ft.PopupMenuButton(
                items=[
                    ft.PopupMenuItem(text="Item 1"),
                    ft.PopupMenuItem(),  # divider
                ]
            ),
        ],
    )
    page.title = "Summit"
    page.padding = 0
    workspace = ft.Container(Workspace(),height=1300)
    page.add(workspace)
    page.update()
 
ft.app(target=main)