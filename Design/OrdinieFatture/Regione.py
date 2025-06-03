from custom_types import *
from Citta import Citta
from Nazione import Nazione

class Regione:
    _regione: str 
    _citta_regione: str 
    _regione_nazione: Nazione

    def __init__(self, regione: str, regione_nazione: Nazione):
        self.set_regione(regione)
        self._citta_regione = set()
        self.set_regione_nazione(regione_nazione)

    def set_nazione(self, regione: str) -> None:
        self._regione = regione 

    def add_citta_regione(self, regione: Citta) -> None:
        self._regione.add(regione)
    
    def remove_citta_regione(self, regione: Citta) -> None:
        if len(self._citta_regione) >= 1:
            self._citta_regione.remove(regione)
    
    def set_regione_nazione(self, regione_nazione: Nazione) -> None:
        self._regione_nazione = regione_nazione 

    def get_regione(self) -> str:
        return self._regione 
    
    def get_citta_regione(self) -> frozenset[Citta]:
        return frozenset[self._citta_regione]
    
    def get_regione_nazione(self) -> Nazione:
        return self._regione_nazione 