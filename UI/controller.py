import flet as ft


class Controller:
    def __init__(self, view, model):
        self._view = view
        self._model = model

    def handleAnalizzaAeroporti(self, e):
        self._view.txt_result.controls.clear()
        distanzaMassima = self._view._txtIn.value
        if distanzaMassima.isdigit():
            distanzaMassima = int(distanzaMassima)
        else:
            self._view.create_alert("Devi inserire un valore numerico!")
            self._view._txtIn.clean()
            return
        self._model.buildGraph(distanzaMassima)
        numVertici = self._model.getNumNodi()
        numArchi = self._model.getNumArchi()
        archi = self._model.archi()
        self._view.txt_result.controls.append(ft.Text(f"Sono presenti {int(numVertici/2)} Nodi"))
        self._view.txt_result.controls.append(ft.Text(f"Sono presenti {numArchi} archi"))
        self._view.txt_result.controls.append(ft.Text(f"Gli archi sono: "))
        for u,v, data in archi(data=True):
            self._view.txt_result.controls.append(ft.Text(f"{u}-----{v}-----Distanza Media: {data['weight']}"))
        self._view.update_page()
