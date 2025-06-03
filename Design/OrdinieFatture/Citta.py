from custom_types import *
from Regione import Regione
from Direttore import Direttore 

class Citta:
    _citta: str 
    _citta_regione: Regione
    _citta_nascita: Direttore

    def __init__(self, citta: str, citta_regione: Regione):
        self.set_citta(citta)
        self.set_citta_regione(citta_regione)
        self.set_citta_nascita = set()

    def set_citta(self, citta: str) -> None:
        self._citta = citta
    
    def set_citta_regione(self, citta_regione: Regione) -> None:
        self._citta_regione = citta_regione

    def add_citta_nascita(self, citta_nascita: Direttore) -> None:
        self._citta_nascita.add(citta_nascita)

    def remove_citta_nascita(self, citta_nascita: Direttore) -> None:
        if len(self._citta_nascita) >= 1:
            self._citta_nascita.remove(citta_nascita)

    def get_citta(self) -> str:
        return self._citta 
    
    def get_citta_regione(self) -> Regione:
        return self._citta_regione
    
    def get_citta_nascita(self) -> frozenset[Direttore]:
        return frozenset(self._citta_nascita)