from typing import *
from customtypes import *
from Utente import *
from Ebuy.OggettodelPost import Asta
from Bid import *


class asta_bid:
    class _link:
        _bid: Bid
        _asta: Asta 
        def __init__(self, b: Bid, a: Asta) -> None:
            self._bid = b
            self._asta = a 
        
        def bid(self) -> Bid:
            return self._bid 
        
        def asta(self) -> Asta:
            return self._asta 
        
        def __hash__(self) -> int:
            return hash( (self.bid(), self.asta()) )
        
        def __eq__(self, other: Any) -> bool:
            if type(self) != type(other) or hash(self) != hash(other):
                return False 
            return (self.bid(), self.asta()) == (other.bid(), other.asta())

        