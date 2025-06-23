from __future__ import annotations

from datetime import date
from DESIGN.Esempi.RespDoppia.Simmetrica.custom_types import *
from typing import *

class Dipendente:
    _nome: str
    _eta: IntGEZ
    _partecipano: dict[Iniziativa, dip_iniz]

    def __init__(self, nome: str, eta: IntGEZ) -> None:
        self.set_nome(nome)
        self._eta = eta 

    def set_nome(self, nome: str) -> None:
        self._nome = nome 

    def nome(self) -> str:
        return self._nome 
    
    def eta(self) -> IntGEZ:
        return self._eta 
    
    def partecipano(self) -> frozenset[dip_iniz._link]:
        return frozenset(self._partecipano.values())
    
    def _add_link_dip_iniz(self, l: dip_iniz._link) -> None:
        if l.dipendente() != self:
            raise ValueError("Il link non coinvolge me!")
        if l.iniziativa() in self._coinvolti:
            raise KeyError("Questa iniziativa è già coinvolta nel link.")
        self._partecipano[l.iniziativa()] = l

    def remove_link_dip_iniz(self, l: dip_iniz._link) -> None:
        if l.dipendente() != self:
            raise ValueError("Il link non coinvolge me!")
        if l.Iniziativa() not in self._coinvolti:
            raise KeyError("Non sono coinvolto nel link.")
        del self._esami[l.iniziativa()]


class Iniziativa:
    _nome: str 
    _durata: IntGEZ
    _coinvolti: dict[Dipendente, dip_iniz]

    def __init__(self, nome: str, durata: IntGZ) -> None:
        self.set_nome(nome)
        self._durata = durata
        self._coinvolti = dict()

    def set_nome(self, nome: str) -> None:
        self._nome = nome 
    
    def nome(self) -> str:
        return self._nome 
    
    def durata(self) -> IntGZ:
        return self._durata
    
    def coinvolti(self) -> frozenset[dip_iniz._link]:
        return frozenset(self._coinvolti.values())
    
    def _add_link_dip_iniz(self, l: dip_iniz._link) -> None:
        if l.iniziativa() != self:
            raise ValueError("Il link non coinvolge me!")
        if l.dipendente() in self._coinvolti:
            raise KeyError("Il dipendente è già coinvolto nell'iniziativa.")
        self._coinvolti[l.dipendente()] = l
    
    def _remove_dip_iniz(self, l: dip_iniz._link) -> None:
        if l.iniziativa() != self:
            raise ValueError("Il link non coinvolge me!")
        if l.dipendente() not in self._coinvolti:
            raise KeyError("Non sono coinvolto nel link.")
        del self._coinvolti[l.dipendente()] 


class dip_iniz:

    @classmethod
    def add(cls, iniziativa: Iniziativa, dipendente: Dipendente, data: DataGE1895) -> dip_iniz._link:
        l = dip_iniz._link(iniziativa, dipendente, data)
        l.iniziativa()._add_link_dip_iniz(l)
        l.dipendente()._add_link_dip_iniz(l)
        return l

    @classmethod
    def remove(cls, l: dip_iniz._link) -> None:
        if l() is None:
            raise ValueError("Il link non può essere None.")
        l().iniziativa()._remove_link_dip_iniz(l())
        l().dipendente()._remove_link_dip_iniz(l())
        del l 

    class _link:
        _iniziativa: Iniziativa 
        _dipendente: Dipendente 
        _data: DataGE1895 

        def __init__(self, iniziativa: Iniziativa, dipendente: Dipendente, data: DataGE1895) -> None:
            self._iniziativa = iniziativa
            self._dipendente = dipendente
            self._data = data
        
        def iniziativa(self) -> Iniziativa:
            return self._iniziativa
        
        def dipendente(self) -> Dipendente:
            return self._dipendente
        
        def data(self) -> DataGE1895:
            return self._data 
        
        def __hash__(self) -> int:
            return hash((self.iniziativa(), self.dipendente()))
        
        def __eq__(self, other: Any) -> bool:
            if type(self) != type(other) or hash(self) != hash(other):
                return False 
            return ((self.iniziativa(), self.dipendente()) == (other.iniziativa(), other.dipendente()))
        
