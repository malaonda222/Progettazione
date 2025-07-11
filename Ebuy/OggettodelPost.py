from abc import ABC, abstractmethod
from datetime import *
from typing import *
from customtypes import *
from Utente import *
from asta_bid import *

class OggettoDelPost(ABC):
    _descrizione: str #mutabile noto alla nascita
    _anni_garanzia: IntGEZ #mutabile noto alla nascita
    _anni_garanzia2: IntGE2 | None #mutabile noto alla nascita 
    _pubblicazione: datetime #immutabile noto alla nascita
    _is_nuovo: bool #immutabile noto alla nascita
    _is_usato: bool #immutabile noto alla nascita 
    _condizione: Condizioni | None#[0..1] possibilmente non noto alla nascita 
    _prezzo: FloatGZ 

    @abstractmethod
    def __init__(self, *, descrizione: str, anni_garanzia: IntGEZ, anni_garanzia2: IntGE2|None = None, pubblicazione: datetime, condizione: Condizioni|None = None, prezzo: FloatGZ):
        self.set_descrizione(descrizione)
        self.set_anni_garanzia(anni_garanzia)
        self._pubblicazione = pubblicazione
        self.set_prezzo(prezzo)

        self._is_nuovo = False 
        self._is_usato = False
        self._anni_garanzia2 = anni_garanzia2 
        self._condizione = condizione

        if condizione is not None:
            self._is_usato = True 
        if anni_garanzia2 is not None:
            self._is_nuovo = True 

        if self.is_nuovo() and self.is_usato():
            raise ValueError("Un oggetto non può essere sia usato che nuovo")
          
    def set_descrizione(self, descrizione: str) -> None:
        if not isinstance(descrizione, str):
            raise ValueError("Errore. La descrizione deve essere una stringa")
        self._descrizione = descrizione

    def set_anni_garanzia(self, anni_garanzia: IntGEZ) -> None:
        self._anni_garanzia = anni_garanzia

    def set_prezzo(self, prezzo: FloatGZ) -> None:
        self._prezzo = prezzo 

    def descrizione(self) -> str:
        return self._descrizione
    
    def anni_garanzia(self) -> IntGEZ:
        return self._anni_garanzia
    
    def pubblicazione(self) -> datetime:
        return self._pubblicazione
    
    def is_nuovo(self) -> bool:
        return self._is_nuovo
    
    def is_usato(self) -> bool:
        return self._is_usato

    def prezzo(self) -> FloatGZ:
        return self._prezzo 
    
    def anni_garanzia2(self) -> IntGE2:
        if not self.is_nuovo():
            raise RuntimeError("Non è un oggetto nuovo")
        return self._anni_garanzia2
    
    def condizione(self) -> Condizioni:
        if not self.is_usato():
            raise RuntimeError("Non è un oggetto usato")
        return self._condizione
    

class Asta(OggettoDelPost):
    _prezzo_rialzo: FloatGZ #[0..1]
    _scadenza: date #[0..1]
    _bids: set[asta_bid._link]

    def __init__(self, *, descrizione: str, anni_garanzia: IntGEZ, prezzo: FloatGZ, anni_garanzia2: IntGE2 | None = None, pubblicazione: datetime, condizione: Condizioni|None = None, prezzo_rialzo: FloatGZ|None = None, scadenza: date|None = None):
        super().__init__(descrizione=descrizione, anni_garanzia=anni_garanzia, prezzo=prezzo, anni_garanzia2=anni_garanzia2, pubblicazione=pubblicazione, condizione=condizione)
        if (prezzo_rialzo is None) != (scadenza is None):
            raise ValueError("Prezzo rialzo e scadenza devono essere entrambi None o entrambi non None")
        
        self.set_prezzo_rialzo(prezzo_rialzo)
        self.set_scadenza(scadenza)
        self._bids = set()

    def set_prezzo_rialzo(self, prezzo_rialzo: FloatGZ) -> None:
        self._prezzo_rialzo = prezzo_rialzo
    
    def set_scadenza(self, scadenza: date) -> None:
        self._scadenza = scadenza 

    def prezzo_rialzo(self) -> FloatGZ | None:
        return self._prezzo_rialzo

    def scadenza(self) -> date | None:
        return self._scadenza 
    
    def bids(self) -> frozenset[asta_bid._link]:
        return frozenset(self._bids)
    
    def _add_link(self, l: asta_bid._link) -> None:
        if l.asta() is not self:
            raise ValueError("Il link non fa riferimento a questa asta")
        if l in self._bids:
            raise KeyError("Link già presente")
        self._bids.add(l)

    

class CompraloSubito(OggettoDelPost):

    def __init__(self, *, descrizione: str, anni_garanzia: IntGEZ, anni_garanzia2: IntGE2| None = None, pubblicazione: datetime, condizione: Condizioni|None = None, prezzo: FloatGZ):
        super().__init__(descrizione=descrizione, anni_garanzia=anni_garanzia, anni_garanzia2=anni_garanzia2|None, pubblicazione=pubblicazione, condizione=condizione)

        if self.is_nuovo() and self.is_usato():
            raise ValueError("Un oggetto non può essere sia usato che nuovo")
    
    def set_prezzo(self, prezzo: FloatGZ):
        self._prezzo = prezzo 

    def prezzo(self) -> FloatGZ:
        return self._prezzo 