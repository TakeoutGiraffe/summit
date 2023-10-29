from apiendpoints import APIEndpointsView
from dashboards import DashboardView
from schedules import SchedulesView
from scripts import ScriptsView
from security import SecurityView
from settings import SettingsView
from tasks import TasksView
from welcome import WelcomeView
import flet as ft
 
class Application(ft.UserControl):
    def __init__(self,page):
        super().__init__(self)
        self.page=page

    def switch_view(self.view):
        self.page.remove_at(0)
        self.page.add((ft.Row([rail,ft.VerticalDivider(),view,],expand=True)))
        self.page.update()

    def open_editor(e):
        print("clicky click")

    def new_screen_selected(self,e):
            if e.control.selected_index == 0:
                switch_view(APIEndpointsView())
            elif e.control.selected_index == 1:
                switch_view(ScriptsView(self))
            elif e.control.selected_index == 2:
                switch_view(TasksView())
            elif e.control.selected_index == 3:
                switch_view(SchedulesView())
            elif e.control.selected_index == 4:
                switch_view(DashboardView())
            elif e.control.selected_index == 5:
                switch_view(SecuityView())
            elif e.control.selected_index == 6:
                switch_view(SettingsView())

    def build(self):
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
                on_change=self.new_screen_selected,
                )

        self.page.appbar = ft.AppBar(
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

    
        return ft.Row([
            rail,
            ft.VerticalDivider(),
            WelcomeView(),
            ],height=700)
 
def main(page: ft.page):
    page.title = "Summit"
    page.padding = 0
    app=Application(page)
    page.add(app)
    page.update()

ft.app(target=main)