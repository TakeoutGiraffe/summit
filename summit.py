from apiendpoints import APIEndpointsView
from dashboards import DashboardView
from schedules import SchedulesView
from scripts import ScriptsView
from security import SecurityView
from settings import SettingsView
from tasks import TasksView
from welcome import WelcomeView
from taskmanager import TaskManager
import flet as ft
import threading as t
 
class Application(ft.Row):
        
    def switch_view(self,view):
       del self.controls[2]
       self.controls.append(view) 
       self.page.update()

    def open_editor(e):
        print("clicky click")

    def new_screen_selected(self,e):
            if e.control.selected_index == 0:
                self.switch_view(APIEndpointsView())
            elif e.control.selected_index == 1:
                self.switch_view(ScriptsView(self))
            elif e.control.selected_index == 2:
                self.switch_view(TasksView(self))
            elif e.control.selected_index == 3:
                self.switch_view(SchedulesView())
            elif e.control.selected_index == 4:
                self.switch_view(DashboardView())
            elif e.control.selected_index == 5:
                self.switch_view(SecurityView())
            elif e.control.selected_index == 6:
                self.switch_view(SettingsView())
    
    def login_user(self,e):
        if self.login.value=="admin" and self.pwd.value=="dydx32&c":
            self.page.session.set('userlogin','admin')
            self.build(self.page)
        self.page.update()

    def build(self,page:ft.page):
        if page.session.contains_key("userlogin"):
            rail = ft.NavigationRail(
                    selected_index=0,
                    label_type=ft.NavigationRailLabelType.ALL,
                    min_width=100,
                    min_extended_width=300,
                    extended=True,
                    group_alignment=-0.9,
                    destinations=[
                        ft.NavigationRailDestination(
                            icon=ft.icons.API, selected_icon=ft.icons.FAVORITE, label="API Endpoints"
                        ),
                        ft.NavigationRailDestination(
                            icon=ft.icons.DESCRIPTION, selected_icon=ft.icons.FAVORITE, label="Scripts"
                        ),
                        ft.NavigationRailDestination(
                            icon=ft.icons.TASK, selected_icon=ft.icons.FAVORITE, label="Tasks"
                        ),
                        ft.NavigationRailDestination(
                            icon=ft.icons.SCHEDULE, selected_icon=ft.icons.FAVORITE, label="Schedules"
                        ),
                        ft.NavigationRailDestination(
                            icon=ft.icons.DASHBOARD, selected_icon=ft.icons.FAVORITE, label="Dashboards"
                        ),
                        ft.NavigationRailDestination(
                            icon=ft.icons.SECURITY, selected_icon=ft.icons.FAVORITE, label="Security"
                        ),
                        ft.NavigationRailDestination(
                            icon=ft.icons.SETTINGS, selected_icon=ft.icons.FAVORITE, label="Settings"
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

            self.height=700
            self.controls=[
                rail,
                ft.VerticalDivider(),
                WelcomeView(),
                ]
        else:
            self.height=700
            self.login = ft.TextField(label="Login")
            self.pwd=ft.TextField(label="Password",password=True)
            self.loginbtn=ft.ElevatedButton("Login",on_click=self.login_user)
            self.controls=[
                self.login,
                self.pwd,
                self.loginbtn
            ]

    def __init__(self,page:ft.page):
        super().__init__()
        self.page=page
        self.taskmanager = TaskManager()
        self.taskmanager_thread = t.Thread(target=self.taskmanager.loop)
        self.taskmanager_thread.start()
        self.build(self.page)
    
def main(page: ft.page):
    page.title = "Summit"
    page.padding = 0
    app=Application(page)
    page.add(app)
    page.update()

ft.app(target=main)