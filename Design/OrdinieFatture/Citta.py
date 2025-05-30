from custom_types import *

class Citta:
    _citta: str 

    def __init__(self, citta: str):
        self._citta(citta)

    def set_nazione(self, citta: str) -> None:
        self._citta = citta 

    def get_nazione(self) -> str:
        return self._citta 