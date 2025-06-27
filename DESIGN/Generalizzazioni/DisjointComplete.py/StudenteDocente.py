from __future__ import annotations
from abc import ABC, abstractmethod
import datetime 
from custom_types import *


'''                ______________________
                  |                      |
                  | Persona <<abstract>> |
                  |______________________|
                  | +nome:str            |
                  | +tel:Telefono [0..*] |
                  |______________________|      
                             ^
                            /_\
             ________________|________________________
            |            {disjoint}                   |
 ___________|____________             ________________|_______________
|                        |           |                                |
|        Studente        |	         |           Docente              |
|________________________|           |________________________________|
| +matricola:str <<imm>> |           | +nascita:datetime.date <<imm>> |
|________________________|           |________________________________|'''

class Persona(ABC):
    _nome: str 
    _telefono: set[Telefono]

    @abstractmethod
    def __init__(self, nome: str, telefono: Telefono=None) -> None:
        self.set_nome(nome) 
        self._telefono: set[Telefono] = set()
        # if telefono: self.add_telefono(telefono)

    def set_nome(self, nome: str) -> None:
        if not isinstance(nome, str) or not nome.strip():
            raise ValueError("Errore. Input non valido.")
        self._nome = nome 
    
    def nome(self) -> str:
        return self._nome 
    
    def add_telefono(self, telefono: Telefono) -> None:
        if telefono not in self._telefono:
            self._telefono.add(telefono)
        else:
            raise ValueError("Il telefono è già presente nella lista telefoni")

    def remove_telefono(self, telefono: Telefono) -> None:
        if telefono not in self._telefono:
            self._telefono.remove(telefono)
        else:
            raise ValueError("Il telefono non è presente nella lista telefoni")
    
    def telefono(self) -> frozenset[Telefono]:
        return frozenset(self._telefono)
    
    def __str__(self)-> str:
        return f"nome: {self._nome}, telefono: {self._telefono}"


class Studente(Persona):
    _matricola: str #immutabile nota alla nascita

    def __init__(self, *, nome: str, telefono: Telefono = None, matricola: str) -> None:
        super().__init__(nome = nome, telefono = telefono)
        self._matricola = matricola

    def matricola(self) -> str:
        return self._matricola 
    
    def __str__(self) -> str:
        return f"Studente: \n{super().__str__()}, matricola: {self._matricola}"
    
    
class Docente(Persona):
    _nascita: datetime.date 

    def __init__(self, *, nome: str, telefono: Telefono = None, nascita: datetime) -> None:
        super().__init__(nome = nome, telefono = telefono)
        self._nascita = nascita if isinstance(nascita, datetime.date) else datetime.date.fromisoformat(nascita)
        assert isinstance(self._nascita, datetime.date)

    def nascita(self) -> datetime.date:
        return self._nascita 

    def __str__(self) -> str:
        return f"Docente:\n{super().__str__()}, nascita: {self._nascita}"

if __name__ == '__main__':
    print("Creo oggetto studente s1:")
    s1: Studente = Studente(nome="Lisa", telefono=Telefono("3772982651"), matricola="54A45")
    s1.add_telefono(Telefono("3336712984"))
    print("s1 ->", s1)
    print()
    print("Creo oggetto docente d1:")
    d1: Docente = Docente(nome="Paolo", telefono=Telefono("3275649865"), nascita="2020-01-01")
    d1.add_telefono("3772546315")
    print("d1 ->", d1)
