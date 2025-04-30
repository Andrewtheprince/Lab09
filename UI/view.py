import flet as ft
from flet_core import MainAxisAlignment


class View(ft.UserControl):
    def __init__(self, page: ft.Page):
        super().__init__()
        self._btnAnalizzaAeroporti = None
        self._txtIn = None
        self._page = page
        self._page.title = "Flight Manager"
        self._page.horizontal_alignment = 'CENTER'
        self._page.theme_mode = ft.ThemeMode.LIGHT
        self._controller = None
        self._title = None
        self.txt_name = None
        self.btn_hello = None
        self.txt_result = None
        self.txt_container = None

    def load_interface(self):
        self._title = ft.Text("Flight Manager", color="blue", size=24)
        self._page.controls.append(self._title)
        self._txtIn = ft.TextField(label="Distanza Minima")
        self._btnAnalizzaAeroporti = ft.ElevatedButton(text="Analizza Aeroporti", on_click=self._controller.handleAnalizzaAeroporti)
        row1 = ft.Row([self._txtIn, self._btnAnalizzaAeroporti], alignment=MainAxisAlignment.CENTER, spacing=30)
        self.txt_result = ft.ListView(expand=1, spacing=10, padding=20, auto_scroll=True)
        self._page.add(row1, self.txt_result)
        self._page.update()

    @property
    def controller(self):
        return self._controller

    @controller.setter
    def controller(self, controller):
        self._controller = controller

    def set_controller(self, controller):
        self._controller = controller

    def create_alert(self, message):
        dlg = ft.AlertDialog(title=ft.Text(message))
        self._page.dialog = dlg
        dlg.open = True
        self._page.update()

    def update_page(self):
        self._page.update()
