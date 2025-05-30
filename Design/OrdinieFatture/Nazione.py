from custom_types import *

class Nazione:
    _nazione: str 

    def __init__(self, nazione: str):
        self._nazione(nazione)

    def set_nazione(self, nazione: str) -> None:
        self._nazione = nazione 

    def get_nazione(self) -> str:
        return self._nazione 