from custom_types import *
from Regione import Regione

class Nazione:
    _nazione: str
    _regione_nazione: Regione 

    def __init__(self, nazione: str):
        self._nazione(nazione)
        self._regione_nazione = set()

    def set_nazione(self, nazione: str) -> None:
        self._nazione = nazione 
    
    def add_regione_nazione(self, regione_nazione: Regione) -> None:
        self._regione_nazione.add(regione_nazione)

    def remove_regione_nazione(self, regione_nazione: Regione) -> None:
        if len(self._regione_nazione) >= 1:
            self._regione_nazione.remove(regione_nazione)

    def get_nazione(self) -> str:
        return self._nazione 
    
    def get_regione_nazione(self) -> frozenset[Regione]:
        return frozenset(self._regione_nazione)
    