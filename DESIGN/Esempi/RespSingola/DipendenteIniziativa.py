from __future__ import annotations

from datetime import date
from custom_types import *
from typing import *

class Dipendente:
    _nome: str
    _eta: IntGEZ

    def __init__(self, nome: str, eta: IntGEZ) -> None:
        self.set_nome(nome)
        self._eta = eta 

    def set_nome(self, nome: str) -> None:
        self._nome = nome 

    def nome(self) -> str:
        return self._nome 
    
    def eta(self) -> IntGEZ:
        return self._eta 
    
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
    
    def coinvolti(self) -> frozenset[dip_iniz]:
        return frozenset(self._coinvolti.values())
    
    def add_dip_iniz(self, dipendente: Dipendente, data: DataGE1895) -> None:
        if dipendente in self.coinvolti:
            raise KeyError("L'iniziativa coinvolge già il dipendente.")
        l: dip_iniz = dip_iniz(self, dipendente, data)
        self._coinvolti[dipendente] = l
    
    def remove_dip_iniz(self, dipendente: Dipendente) -> None:
        try:
            del self.coinvolti[dipendente]
        except KeyError:
            raise KeyError("L'iniziativa non coinvolge il dipendente.")


class dip_iniz:
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
    
