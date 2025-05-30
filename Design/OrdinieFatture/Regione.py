from custom_types import *

class Regione:
    _regione: str 

    def __init__(self, regione: str):
        self._regione(regione)

    def set_nazione(self, regione: str) -> None:
        self._regione = regione 

    def get_regione(self) -> str:
        return self._regione 