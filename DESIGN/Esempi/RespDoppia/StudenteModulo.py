from __future__ import annotations
from custom_types import *

class Studente:
    _nome: str 
    _esami: dict[Modulo, esame._link]

    def __init__(self, nome: str) -> None:
        self.set_nome(nome)
        self._esami = dict()

    def set_nome(self, nome: str) -> None:
        self._nome = nome 
    
    def nome(self) -> str:
        return self._nome 
    
    def esami(self) -> frozenset[esame._link]:
        return frozenset(self._esami.values())
    
    def _add_link_esami(self, l: esame._link) -> None:
        if l.studente() != self:
            raise ValueError("Il link non coinvolge me!")
        if l.modulo() in self._esami:
            raise KeyError("Questo modulo è già coinvolto nel link.")
        self._esami[l.modulo()] = l

    def _remove_link_esami(self, l: esame._link) -> None:
        if l.studente() != self:
            raise ValueError("Il link non coinvolge me!")
        if l.modulo() not in self._esami:
            raise KeyError("Non sono coinvolto nel link")
        del self._esami[l.modulo()]


class Modulo:
    _nome: str 
    _esami: dict[Studente, esame._link]

    def __init__(self, nome: str) -> None:
        self.set_nome(nome)
        self._esami = dict()
    
    def set_nome(self, nome: str) -> None:
        self._nome = nome 

    def nome(self) -> str:
        return self._nome 

    def esami(self) -> frozenset[esame._link]:
        return frozenset(self._esami.values())
    
    def _add_link_esame(self, l: esame._link) -> None:
        if l.modulo() != self:
            raise ValueError("Il link non coinvolge me!")
        if l.studente() in self._esami:
            raise KeyError("Sono già coinvolto nel link.")
        self._esami[l.studente()] = l 

    def _remove_link_esame(self, l: esame._link) -> None:
        if l.modulo() != self:
            raise ValueError("Il link non coinvolge me!")
        if l.studente() not in self._esami:
            raise KeyError("Non sono coinvolto nel link.")
        del self._esami[l.studente()]
    

class esame:
    @classmethod
    def add(cls, studente: Studente, modulo: Modulo, voto: Voto) -> None:
        l = esame._link(studente, modulo, voto)
        l.studente()._add_link_esame(l)
        l.modulo()._add_link_esame(l)
        return l

    @classmethod
    def remove(cls, l: esame._link) -> None:
        if l() is None:
            raise ValueError("Non posso essere None")
        l().studente()._remove_link_esame(l())
        l().modulo()._remove_link_esame(l())
        del l 


    class _link:
        _studente: Studente 
        _modulo: Modulo 
        _voto: Voto 

    def __init__(self, studente: Studente, modulo: Modulo, voto: Voto) -> None:
        self._studente = studente 
        self._modulo = modulo 
        self._voto = voto 

    def studente(self) -> Studente:
        return self._studente 
    
    def modulo(self) -> Modulo:
        return self._modulo 
    
    def voto(self) -> Voto:
        return self._voto 
    
    def __hash__(self) -> int:
        return hash((self.studente(), self.modulo()))
    
    def __eq__(self, other: Any) -> bool:
        if type(self) != type(other) or hash(self) != hash(other):
            return False 
        return (self.studente(), self.modulo() == other.studente(), other.modulo())