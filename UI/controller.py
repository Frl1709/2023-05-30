import warnings

import flet as ft


class Controller:
    def __init__(self, view, model):
        # the view, with the graphical elements of the UI
        self._view = view
        # the model, which implements the logic of the program and holds the data
        self._model = model

    def fillDD(self):
        team = self._model.listTeams
        for t in team:
            self._view.ddteam.options.append(ft.dropdown.Option(t.name))

    def details(self,e):
        v0 = self._view.ddyear.value
        archi = self._model.getDetails(int(v0))
        self._view.txtOut.controls.append(ft.Text("Dettagli per l'anno scelto"))
        for a in archi:
            self._view.txtOut.controls.append(ft.Text(f"{a[0]} <--> {a[1]}, peso= {a[2]}"))
        self._view.update_page()

    def handle_graph(self, e):
        if self._view.ddteam.value is None:
            self._view.create_alert("Inserire una squadra")
            return

        self._model.buildGraph(self._view.ddteam.value)
        nN, nE = self._model.getGraphSize()
        self._view.txtOut.clean()
        self._view.txtOut.controls.append(ft.Text(f"Grafo creato con {nN} nodi e {nE} archi"))

        anni = self._model.listYear
        for a in anni:
            self._view.ddyear.options.append(ft.dropdown.Option(a))
        self._view.update_page()

    def handle_search(self, e):
        pass
