from __future__ import annotations
from custom_types import *


class partita:
    @classmethod
    def add(cls, societa: Societa, sportivo: Sportivo, data: date) -> None:
        l = partita._link(societa, sportivo, data)
        societa._add_link_partita(l)
        sportivo._add_link_partita(l)
        return l

    @classmethod
    def remove(cls, l: partita._link) -> None:
        if l() is None:
            raise ValueError("Non posso essere None")
        l.societa()._remove_link_partita(l)
        l.sportivo()._remove_link_partita(l)
        del l 

    class _link:
        _societa: Societa
        _sportivo: Sportivo
        _data_partita: date

    def __init__(self, societa: Societa, sportivo: Sportivo, data_partita: date) -> None:
        self._societa = societa 
        self._sportivo = sportivo 
        self._data_partita = data_partita 

    def societa(self) -> Societa:
        return self._societa 

    def sportivo(self) -> Sportivo:
        return self._sportivo 

    def data_partita(self) -> date:
        return self._data_partita

    def __hash__(self) -> int:
        return hash((self.societa(), self.sportivo()))

    def __eq__(self, other: Any) -> bool:
        if type(self) != type(other) or hash(self) != hash(other):
            return False 
        return ((self.societa(), self.sportivo() == other.societa(), other.sportivo()))  


class Societa:
    _nome: str 
    _data_fondazione: date
    _partite: dict[Sportivo, partita._link]

    def __init__(self, nome: str, data_fondazione: date) -> None:
        self.set_nome(nome)
        self._data_fondazione = data_fondazione
        self._partite = dict()

    def set_nome(self, nome: str) -> None:
        self._nome = nome 

    def nome(self) -> str:
        return self._nome 

    def data_fondazione(self) -> date:
        return self._data_fondazione 

    def partite(self) -> frozenset[partita._link]:
        return frozenset(self._partite.values())

    def _add_link_partite(self, l: partita._link) -> None:
        if l.societa() != self:
            return ValueError("Il link non coinvolge me!")
        if l.sportivo() in self:
            return KeyError("Chiave di valore duplicata.")
        self._partite[l._sportivo()] = l 
    
    def _remove_link_partite(self, l: partita._link) -> None:
        if l.societa() != self:
            raise ValueError("Il link non coinvolge me!")
        if l.sportivo() not in self._partite:
            raise KeyError("Non sono coinvolto nel link.")
        del self._partite[l.sportivo()]


class Sportivo:
    _nome: str 
    _cognome: str 
    _eta: IntGEZ
    _partite: dict[Societa, partita._link]

    def __init__(self, nome: str, cognome: str, eta: int) -> None:
        self.set_nome(nome)
        self.set_cognome(cognome)
        self._eta = eta 
        self._giocatori = dict() 

    def set_nome(self, nome: str) -> None:
        self._nome = nome 
    
    def set_cognome(self, cognome: str) -> None:
        self._cognome = cognome 
    
    def nome(self) -> str:
        return self._nome 
    
    def cognome(self) -> str:
        return self._cognome 
    
    def eta(self) -> IntGEZ:
        return self._eta 

    def partite(self) -> frozenset[partita._link]:
        return frozenset(self._partite.values())

    def _add_link_partite(self, l: partita._link) -> None:
        if l.sportivo() != self:
            raise ValueError("Il link non coinvolge me!")
        if l.societa() in self._partite:
            raise KeyError("Chiave di valore duplicata.")
        self._partite[l._societa()] = l 
    
    def _remove_link_partite(self, l: partita._link) -> None:
        if l.sportivo() != self:
            raise ValueError("Il link non coinvolge me!")
        if l.societa() not in self.partite:
            raise KeyError("Non sono coinvolto nel link.")
        del self._partite[l.societa()]
