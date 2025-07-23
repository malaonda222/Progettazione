from __future__ import annotations
from typing import TYPE_CHECKING
from abc import *
from py.custom_types.enums import Popolarita
from py.custom_types.floats import FloatGZ
import datetime

if TYPE_CHECKING:
    from py.classes.Bid import Bid
    from py.classes.bid_ut import bid_ut

# classe utente 
class Utente(ABC):
    _username: str #immutabile
    _registrazione: datetime #immutabile
 
    @abstractmethod
    def __init__(self, *, username: str, registrazione: datetime):
        self._username = username
        self._registrazione = datetime.datetime.now()
    
    def username(self) -> str:
        return self._username
    
    def data_registrazione(self) -> datetime:
        return self._data_registrazione
    
    def popolarita(i: datetime) -> Popolarita:
        pass

    def affidabilita(self) -> FloatGZ:
        pass

    def __repr__(self):
        return f"Utente(username={self.username()}, registrazione={self.registrazione})"


class VenditoreProfessionale(Utente):
    _vetrina: Url | None #[0..1], mutabile
 
    def __init__(self, *, username: str, registrazione: datetime, vetrina: Url|None = None):
        super().__init__(username=username, registrazione=registrazione)
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
    _bid_ut_link: dict[Bid, bid_ut._link] = {}
 
    def __init__(self, *, username: str, registrazione: datetime) -> None:
        super().__init__(username=username, registrazione=registrazione)    
    
    def _add_bid_ut_link(self, l) -> None:
        if l.utente_privato() is not self:
            raise ValueError("Il link non fa riferimento a questo utente")
        if l.bid() in self._bid_ut_link:
            raise KeyError("Link duplicato")
        self._bid_ut_link[l.bid()] = l 

    def __repr__(self):
        return f"UtentePrivato{super().__repr__()}"