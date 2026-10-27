import flet as ft
from UI.view import View
from model.model import DepositoStrumenti

'''
    CONTROLLER:
    - Funziona da intermediario tra MODELLO e VIEW
    - Gestisce la logica del flusso dell'applicazione
'''

class Controller:
    def __init__(self, view: View, model: DepositoStrumenti):
        self._model = model
        self._view = view

    def get_nome(self):
        return self._model.nome

    def get_responsabile(self):
        return self._model.responsabile

    def set_responsabile(self, responsabile):
        self._model.responsabile = responsabile

    def conferma_responsabile(self, e):
        self._model.responsabile = self._view.input_responsabile.value
        self._view.txt_responsabile.value = f"Responsabile: {self._model.responsabile}"
        self._view.update()

    # Altre Funzioni Event Handler
    # TODO
    def show_list(self, e):
        if self._model.get_strumenti() is not None:
            self._view.lista_strumenti.controls = [ft.Text(f"{i}") for i in self._model.get_strumenti()]
            # utilizzo di una list comprehension
        else :
            self._view.lista_strumenti.controls = [ft.Text("Nessuno strumento da visualizzare, database vuoto")]
        self._view.update()

    def cerca_per_tipo(self, e):
        self._tipo_cercato = self._view.input_tipo_strumento.value
        if self._model.cerca_strumenti_per_tipo(self._tipo_cercato) is not None:
            self._view.lista_strumenti_ricerca.controls = [ft.Text(f"{i}") for i in self._model.cerca_strumenti_per_tipo(self._tipo_cercato)]
        else :
            self._view.lista_strumenti_ricerca.controls = [ft.Text("Nessuno strumento da visualizzare per il tipo da lei inserito")]
        self._view.update()