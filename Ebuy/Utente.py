from abc import ABC, abstractmethod
from datetime import *
from typing import *
from customtypes import *
import re

# classe utente 
class Utente(ABC):
    _username: str #immutabile
    _data_registrazione: datetime #immutabile
 
    @abstractmethod
    def __init__(self, *, username: str, data_registrazione: datetime):
        self._username = username
        self._data_registrazione = data_registrazione
    def username(self) -> str:
        return self._username
    def data_registrazione(self) -> datetime:
        return self._data_registrazione


class VenditoreProfessionale(Utente):
    _vetrina: Url | None #[0..1], mutabile
 
    def __init__(self, *, username: str, data_registrazione: datetime, vetrina: Url|None = None):
        super().__init__(username=username, data_registrazione=data_registrazione)
        self.set_vetrina(vetrina)
    def vetrina(self) -> Url|None:
        return self._vetrina
    def set_vetrina(self, vetrina: Url|None) -> None:
        try:
            if self._vetrina:
                raise ValueError("Errore, l'attributo è stato già assegnato")
        except AttributeError:
            pass
        self._vetrina = vetrina


class UtentePrivato(Utente):
 
    def __init__(self, *, username: str, data_registrazione: datetime):
        super().__init__(username=username, data_registrazione=data_registrazione)    
    
    def add_link_bid_ut()


