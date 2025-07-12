from abc import ABC, abstractmethod
from datetime import *
from typing import *
from customtypes import *
from OggettodelPost import *
from asta_bid import *
from bid_ut import *


class Bid:
    _istante: datetime #noto alla nascita e immutabile
    _asta: Asta 
    _utentePrivato: UtentePrivato
    _asta_bid: _asta_bid 
    _bid_ut: _bid_ut

    def __init__(self, *, istante: datetime, u: UtentePrivato, a: Asta) -> None:
        self._istante = istante 
        self.crea_link_asta_bid(a)
        self.crea_link_bid_ut(u)
    
    def istante(self) -> datetime:
        return self._istante 
    
    def asta(self) -> Asta:
        return self._asta 
    
    def utentePrivato(self) -> UtentePrivato:
        return self._utentePrivato
    
    def crea_link_asta_bid(self, l: asta_bid):
        
    def crea_link_bid_ut(self, l: bid_ut):
        