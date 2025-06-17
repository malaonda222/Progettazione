from custom_types import *
from Ordine import Ordine

class Fornitore:
    _ragione_sociale: str
    _partita_iva: PartitaIva 
    _indirizzo: Indirizzo 
    _telefono: Telefono 
    _email: Email 
    _forn_ordine: Ordine

    def __init__(self, ragione_sociale: str, partita_iva: PartitaIva, indirizzo: Indirizzo, telefono: Telefono, email: Email, forn_ordine: Ordine):
        self.set_ragione_sociale(ragione_sociale)
        self._partita_iva = partita_iva 
        self.set_indirizzo(indirizzo)
        self.set_telefono(telefono)
        self.set_email(email)
        self._forn_ordine = set()

    def set_ragione_sociale(self, ragione_sociale: str) -> None:
        self._ragione_sociale = ragione_sociale
    
    def set_indirizzo(self, indirizzo: Indirizzo) -> None:
        self._indirizzo = indirizzo 

    def set_telefono(self, telefono: Telefono) -> None:
        self._telefono = telefono 

    def set_email(self, email: Email) -> None:
        self._email = email 
    
    def add_forn_ordine(self, forn_ordine: Ordine) -> None:
        self._forn_ordine.add(forn_ordine)
    
    def remove_forn_ordine(self, forn_ordine: Ordine) -> None:
        if len(self._forn_ordine) >= 1:
            self._forn_ordine.remove(forn_ordine)
    
    def get_ragione_sociale(self) -> str:
        return self._ragione_sociale
    
    def get_partita_iva(self) -> PartitaIva:
        return self._partita_iva
    
    def get_indirizzo(self) -> Indirizzo:
        return self._indirizzo 
    
    def get_telefono(self) -> Telefono:
        return self._telefono 
    
    def get_email(self) -> Email:
        return self._email 
    
    def get_forn_ordine(self) -> frozenset[Ordine]:
        return frozenset(self._forn_ordine)