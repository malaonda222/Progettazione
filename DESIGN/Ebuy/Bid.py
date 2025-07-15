from abc import ABC, abstractmethod
from datetime import *
from typing import *
from customtypes import *
from OggettodelPost import UtentePrivato, Asta
from asta_bid import *
from bid_ut import *


class Bid:
    _istante: datetime #noto alla nascita e immutabile
    _asta_link: asta_bid._link | None
    _utente_link: bid_ut._link | None

    def __init__(self, *, istante: datetime, a: Asta, u: UtentePrivato) -> None:
        self._istante = istante 
        self._asta_link = None
        self._utente_link = None

        self.set_collegamento_asta(a)
        self.set_collegamento_utente(u)
    
    def istante(self) -> datetime:
        return self._istante 
    
    def asta(self) -> Asta | None:
        if not self._asta_link:
            return None
        return self._asta_link.asta()
    
    def utentePrivato(self) -> UtentePrivato | None:
        if not self._utente_link:
            return None
        return self._utente_link.utente()
            
    def set_collegamento_asta(self, a: Asta) -> None:
         if self._asta_link is not None:
              raise ValueError("Questo Bid è già collegato a un'asta")
         l = asta_bid._link(self, a)
         self._asta_link = l 
         a._add_link(l)

    def set_collegamento_utente(self, u: UtentePrivato) -> None:
        if self._utente_link is not None:
            raise ValueError("Questo Bid è già collegato a un utente")
        l = bid_ut._link(self, u)
        self._utente_link = l 
        u._add_link(l)

    
    
    
