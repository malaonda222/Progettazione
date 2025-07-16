from abc import ABC, abstractmethod
from datetime import *
from typing import *
from customtypes import *
from bid_ut import *
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
    _bids: set[bid_ut._link]
 
    def __init__(self, *, username: str, data_registrazione: datetime):
        super().__init__(username=username, data_registrazione=data_registrazione)    
        self._bids = set() 
    
    def bids(self) -> frozenset[bid_ut._link]:
        return frozenset(self._bids)
    
    def _add_link(self, l: bid_ut._link) -> None:
        if l.utente() is not self:
            raise ValueError("Il link non fa riferimento a questo utente")
        if l in self._bids:
            raise KeyError("Link già presente")
        self._bids.add(l)


if __name__ == "__main__":
    utente1 = UtentePrivato("Mario Rossi", )
    bid1 = Bid(istante=datetime.now(), a=asta1, u=utente1)