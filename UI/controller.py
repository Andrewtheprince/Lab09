import flet as ft


class Controller:
    def __init__(self, view, model):
        self._view = view
        self._model = model

    def handleAnalizzaAeroporti(self, e):
        distanzaMassima = self._view._txtIn.value
        if distanzaMassima.isdigit():
            distanzaMassima = int(distanzaMassima)
        else:
            self._view.create_alert("Devi inserire un valore numerico!")
            self._view._txtIn.clean()
            return

