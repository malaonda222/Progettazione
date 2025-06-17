from Citta import Citta


class Regione:
    _nome: str 
    _citta_regione: Citta

    def __init__(self, nome: str):
        self.set_nome(nome)
        self._citta_regione: Regione = set()

    def set_nome(self, nome) -> None:
        self._nome = nome 

    def add_citta_regione(self, citta_regione: Citta) -> None:
        self._citta_regione.add(citta_regione)

    def remove_citta_regione(self, citta_regione: Citta) -> None:
        if len(citta_regione) >= 1:
            self._citta_regione.remove(citta_regione)

    def get_nome(self):
        return self._nome 
    
    def get_citta_regione(self) -> frozenset[Citta]:
        return frozenset(self._citta_regione)
    