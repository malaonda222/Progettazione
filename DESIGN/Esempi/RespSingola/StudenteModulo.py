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

    def add_link_esami(self, modulo: Modulo, voto: Voto) -> None: 
        l: esame.link = esame._link(self, modulo, voto)
        if modulo in self._esami:
            raise KeyError("Link duplicato.")
        self._esami[modulo] = l
    
    def remove_link_esami(self, l: esame.link) -> None:
        if l().studente() is not self:
            raise ValueError("Il link non coinvolge lo studente.")
        del self._esami[l().modulo()]

    def get_esami(self) -> frozenset[esame._link]:
        return frozenset[self._esame.link]
    
class Modulo:
    _nome: str

    def __init__(self, nome: str) -> None:
        self._nome = nome
    
    def nome(self) -> str:
        return self._nome 


class esame:
    class _link:
        _studente: Studente 
        _modulo: Modulo 
        _voto: Voto 

        def __init__(self, studente: Studente, modulo: Modulo, voto: Voto) -> None:
            self._studente = studente 
            self._modulo = modulo 
            self._voto = voto
        
        def get_studente(self) -> Studente:
            return self._studente 
        
        def get_modulo(self) -> Modulo:
            return self._modulo 

        def get_voto(self) -> Voto:
            return self._voto 
        
        def __hash__(self) -> int:
            return hash((self.get_studente()), (self.get_modulo()))

        def __eq__(self, other: Any) -> bool:
            if type(self) != type(other) or hash(self) != hash(other):
                return False 
            return ((self.get_studente(), self.get_modulo()) == (other.get_studente(), other.get_modulo()))
            