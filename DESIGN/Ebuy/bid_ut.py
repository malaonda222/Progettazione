from typing import *
from customtypes import *
from Utente import *
from Ebuy.OggettodelPost import UtentePrivato  
from Bid import *


class bid_ut:
    class _link:
        _bid: Bid 
        _utentePrivato: UtentePrivato

        def __init__(self, b: Bid, u: UtentePrivato) -> None:
            self._bid = b 
            self._utentePrivato = u

        def bid(self) -> Bid:
            return self._bid 
        
        def utentePrivato(self) -> UtentePrivato:
            return self._utentePrivato
        
        def __hash__(self) -> int:
            return hash( (self.bid(), self.utentePrivato()) )
        
        def __eq__(self, other: Any) -> bool:
            if type(self) != type(other) or hash(self) != hash(other):
                return False 
            return (self.bid(), self.utentePrivato()) == (other.bid(), other.utentePrivato())
        