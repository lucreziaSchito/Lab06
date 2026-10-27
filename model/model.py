from database.DB_connect import get_connection
from model.strumento import Strumento
from model.prestito import Prestito

'''
    MODELLO:
    - Rappresenta la struttura dati
    - Si occupa di gestire lo stato dell'applicazione
    - Interagisce con il database
'''

class DepositoStrumenti:
    def __init__(self, nome, responsabile):
        self._nome = nome
        self._responsabile = responsabile

    @property
    def nome(self):
        return self._nome

    @nome.setter
    def nome(self, nome):
        self._nome = nome

    @property
    def responsabile(self):
        return self._responsabile

    @responsabile.setter
    def responsabile(self, responsabile):
        self._responsabile = responsabile

    def get_strumenti(self) -> list[Strumento] | None:
        """
            Funzione che legge tutti gli strumenti nel database
            :return: una lista con tutti gli strumenti presenti oppure None
        """
        # TODO
        self._lista_strumenti = []
        connessione = get_connection()
        cursore_dizionario = connessione.cursor(dictionary=True)
        # Il parametro dictionary=True modifica il formato con cui il modulo mysql-connector-python
        # restituisce i risultati delle query, trasformando ogni riga estratta in un dizionario Python
        # anziché nella classica tupla.

        query = """SELECT * FROM strumento"""
        cursore_dizionario.execute(query)


        for riga in cursore_dizionario:
            strumento_estratto = Strumento(riga["codice"], riga["tipo"], riga["marca"], riga["anno_acquisto"], riga["valore"])
            self._lista_strumenti.append(strumento_estratto)
        connessione.close()

        if len(self._lista_strumenti) > 0:
            return self._lista_strumenti
        else :
            return None

    def cerca_strumenti_per_tipo(self, tipo) -> list[Strumento] | None:
        """
            Funzione che recupera una lista con tutti gli strumenti presenti nel database di un certo tipo
            :param tipo: il tipo dello strumento (es. "Chitarra")
            :return: una lista con tutti gli strumenti del tipo indicato oppure None
        """
        # TODO
        self._lista_strumenti_ord_tipo = []
        connessione = get_connection()
        cursore_dizionario = connessione.cursor(dictionary=True)

        query = f"""SELECT * 
                FROM strumento
                WHERE tipo = %s"""
        cursore_dizionario.execute(query, (tipo, ))


        for riga in cursore_dizionario:
            strumento_estratto = Strumento(riga["codice"], riga["tipo"], riga["marca"], riga["anno_acquisto"],
                                           riga["valore"])
            self._lista_strumenti_ord_tipo.append(strumento_estratto)
        connessione.close()

        if len(self._lista_strumenti_ord_tipo) > 0:
            return self._lista_strumenti_ord_tipo
        else :
            return None
