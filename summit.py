import flet as ft
import welcome
import apiendpoints
import schedules
import scripts
import security
import tasks
import settings 
import dashboards
 
def main(page: ft.page):

    def newScreenSelected(e):
            if e.control.selected_index == 0:
                print ("API Endpoints")
                page.remove_at(0)
                page.add((ft.Row([rail,ft.VerticalDivider(),get_api_endpoints_view(),],expand=True)))
                page.update()
            elif e.control.selected_index == 1:
                print ("Scripts")
                page.remove_at(0)
                page.add((ft.Row([rail,ft.VerticalDivider(),get_scripts_view(),],expand=True)))
                page.update()
            elif e.control.selected_index == 2:
                print ("Tasks")
                page.remove_at(0)
                page.add((ft.Row([rail,ft.VerticalDivider(),get_tasks_view(),],expand=True)))
                page.update()
            elif e.control.selected_index == 3:
                print ("Schedules")
                page.remove_at(0)
                page.add((ft.Row([rail,ft.VerticalDivider(),get_schedules_view(),],expand=True)))
                page.update()
            elif e.control.selected_index == 4:
                print ("Dashboards")
                page.remove_at(0)
                page.add((ft.Row([rail,ft.VerticalDivider(),get_dashboards_view(),],expand=True)))
                page.update()
            elif e.control.selected_index == 5:
                print ("Security")
                page.remove_at(0)
                page.add((ft.Row([rail,ft.VerticalDivider(),get_security_view(),],expand=True)))
                page.update()
            elif e.control.selected_index == 6:
                print ("Settings")
                page.remove_at(0)
                page.add((ft.Row([rail,ft.VerticalDivider(),get_settings_view,],expand=True)))
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
            on_change=newScreenSelected,
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
        get_welcome_view(),
        ],expand=True))
    page.update()
 
ft.app(target=main)