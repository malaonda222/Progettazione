from __future__ import annotations

from datetime import date
from custom_types import *

from typing import *

class Impiegato:
    _nome: str 
    _cognome: str 
    _nascita: date 
    _stipendio: Importo 

    def __init__(self, nome: str, cognome: str, nascita: date, stipendio: Importo) -> None:
        self.set_nome(nome)
        self.set_cognome(cognome)
        self._nascita = nascita 
        self.set_stipendio(stipendio)

    def set_nome(self, nome: str) -> None:
        self._nome = nome 
    
    def set_cognome(self, cognome: str) -> None:
        self._cognome = cognome 
    
    def set_stipendio(self, stipendio: Importo) -> None:
        self._stipendio = stipendio 

    def nome(self) -> str:
        return self._nome 
    
    def cognome(self) -> str:
        return self._cognome 
    
    def stipendio(self) -> Importo:
        return self._stipendio 
    
    def nascita(self) -> date:
        return self._nascita 
    

class Progetto:
    _nome: str
    _budget: Importo 
    _coinvolti: dict[Impiegato, imp_prog]

    def __init__(self, nome: str, budget: Importo) -> None:
        self.set_nome(nome)
        self.set_budget(budget)
        self._imp_prog = dict()
    
    def set_nome(self, nome: str) -> None:
        self._nome = nome 

    def set_budget(self, budget: Importo) -> None:
        self._budget = budget 
    
    def nome(self) -> str:
        return self._nome 
    
    def budget(self) -> Importo:
        return self._budget
    
    def coinvolti(self) -> frozenset[imp_prog]:
        return frozenset(self._coinvolti.values())

    def add_imp_prog(self, impiegato: Impiegato, data: date) -> None:
        if impiegato in self._coinvolti:
            raise KeyError("Link duplicato.")
        l: imp_prog = imp_prog(self, impiegato, data)
        self._coinvolti[impiegato] = l   

    def remove_imp_prog(self, impiegato: Impiegato) -> None:
        try: 
           del self._coinvolti[impiegato]
        except KeyError:
           raise KeyError("Il progetto non coinvolge l'impiegato")
        
    def data_coinvolgimento(self, impiegato: Impiegato) -> date:
        try: 
            return self._coinvolti[impiegato].data()
        except KeyError:
            raise KeyError("Il progetto non coinvolge l'impiegato.")

class imp_prog:
    _progetto: Progetto
    _impiegato: Impiegato 
    _data: date 
    
    def __init__(self, progetto: Progetto, impiegato: Impiegato, data: date) -> None:
        self._progetto = progetto 
        self._impiegato = impiegato
        self._data = data
    
    def progetto(self) -> Progetto:
        return self._progetto
    
    def impiegato(self) -> Impiegato:
        return self._impiegato
    
    def data(self) -> date:
        return self._data 
    
    def __hash__(self) -> int:
        return hash(self.progetto(), self.impiegato())
    
    def __eq__(self, other: Any) -> bool:
        if type(self) != type(other) or hash(self) != hash(other):
            return False 
        return hash((self.progetto(), self.impiegato()) == (other.progetto(), other.impiegato()))
