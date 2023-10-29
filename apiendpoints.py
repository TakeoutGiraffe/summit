import flet as ft

class APIEndpointsView(ft.Column):

    def __init__(self):
        super().__init__()
        self.controls= ft.Text("APIEndpoints")