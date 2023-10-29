import flet as ft
from welcome import Welcome
from apiendpoints import APIEndpoints
from schedules import Schedules
from scripts import Scripts
from security import Security
from tasks import Tasks
from settings import Settings 
from dashboards import Dashboards
 
def main(page: ft.page):

    welcome=Welcome()
    apiendpoints=APIEndpoints()
    schedules=Schedules()
    scripts=Scripts()
    security=Security()
    tasks=Tasks()
    settings=Settings()
    dashboards=Dashboards()
    selectedControl=self.welcome

    def newScreenSelected(self,e):
            if e.control.selected_index == 0:
                print ("API Endpoints")
                selectedControl = apiendpoints
                update()
            elif e.control.selected_index == 1:
                print ("Scripts")
                selectedControl = scripts
                page.update()
            elif e.control.selected_index == 2:
                print ("Tasks")
                selectedControl = tasks
                page.update()
            elif e.control.selected_index == 3:
                print ("Schedules")
                selectedControl = schedules
                page.update()
            elif e.control.selected_index == 4:
                print ("Dashboards")
                selectedControl = dashboards
                page.update()
            elif e.control.selected_index == 5:
                print ("Security")
                selectedControl = security
                page.update()
            elif e.control.selected_index == 6:
                print ("Settings")
                selectedControl = settings
                page.update()

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
            on_change=self.newScreenSelected,
            )

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
    page.add(ft.Row([
        rail,
        ft.VerticalDivider(),
        selectedControl,
        ],expand=True))
    page.update()
 
ft.app(target=main)