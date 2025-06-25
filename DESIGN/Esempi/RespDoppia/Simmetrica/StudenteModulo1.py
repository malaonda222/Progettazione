# Esercizio 01 - simmetrico
from __future__ import annotations
from typing import Any 
from custom_types import *

"""                         

                      Esame (voto <<imm>>)

____________________           |                    ___________________

|                   |          |          |                   |

|     Studente      |  0..*    |     0..* |             Modulo       |

|___________________|---------------------|___________________|

| +nome:str            |                     | +nome:str <<imm>> |

|___________________|                     |___________________|

"""

from typing import Any 
from custom_types import *


class esame:
    @classmethod
    def add(cls, studente: Studente, modulo: Modulo, voto: Voto) -> None:
        l = esame._link(studente, modulo, voto)
        l.studente()._add_link_esame(l)
        l.modulo()._add_link_esame(l)
    
    @classmethod 
    def remove(cls, l: esame._link) -> None:
        if l is None:
            raise ValueError("Non posso essere None")
        l.studente()._remove_link_esame(l)
        l.modulo()._remove_link_esame(l)
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
            return ((self.studente(), self.modulo()) == (other.studente(), other.modulo()))
        
        def __str__(self) -> str:
            return f"Link = (nome = {self.studente().nome()}, modulo = {self.modulo().nome()}, voto = {self.voto()})"

class Studente:
    _nome: str 
    _esami: dict[Modulo, esame._link]

    def __init__(self, nome: str) -> None:
        self.set_nome(nome)
        self._esami = dict()
    
    def set_nome(self, nome: str) -> None:
        if not isinstance(nome, str):
            raise ValueError(f"Errore. Nome non valido.")
        self._nome = nome 
    
    def nome(self) -> str:
        return self._nome 
    
    def esami(self) -> frozenset[esame._link]:
        return frozenset(self._esami.values())
    
    def esame(self, modulo: Modulo) -> esame._link:
        return self._esami[modulo]
    
    def _add_link_esame(self, l: esame._link) -> None:
        if l.studente() is not self:
            raise ValueError(f"Il link '{l.studente()}' non mi coinvolge")
        if l.modulo() in self._esami:
            raise KeyError(f"Link duplicato: ({self}, {l.modulo()}) non consentito")
        self._esami[l.modulo()] = l

    def _remove_link_esame(self, l: esame._link) -> None:
        if l.studente() is not self:
            raise ValueError(f"Il link '{l.studente()}' non mi coinvolge")
        if l.modulo() not in self._esami:
            raise KeyError(f"Non sono coinvolto nel link {l.modulo()}")
        del self._esami[l.modulo()]

    def __str__(self) -> str:
        return f"{self._nome}"

    

class Modulo:
    _nome: str 
    _esami : dict[Studente, esame._link]

    def __init__(self, nome: str) -> None:
        self._nome = nome 
        self._esami = dict()
    
    def nome(self) -> str:
        return self._nome 
    
    def esami(self) -> frozenset[esame._link]:
        return frozenset(self._esami.values())
    
    def esame(self, studente: Studente) -> esame._link:
        return self._esami[studente]
    
    def _add_link_esame(self, l: esame._link) -> None:
        if l.modulo() is not self:
            raise ValueError(f"Il link {l.modulo()} non mi coinvolge.")
        if l.studente() in self._esami:
            raise KeyError(f"Errore. Duplicato: ({self}, {l.studente()}) non consentito.")
        self._esami[l.studente()] = l 

    def _remove_link_esame(self, l: esame._link) -> None:
        if l.modulo() is not self:
            raise ValueError(f"Il link '{l.modulo()}' non mi riguarda.")
        if l.studente() not in self._esami:
            raise KeyError(f"Link duplicato: ({self}, {l.studente()}) non consentito.")
        del self._esami[l.studente()]
    
    def __str__(self) -> str:
        return f"{self.nome()}"



if __name__ == "__main__":
    s1: Studente = Studente("Gianni")
    s2: Studente = Studente("Mimmo")
    s3: Studente = Studente("Paola")

    m1: Modulo = Modulo("Matematica")
    m2: Modulo = Modulo("Inglese")
    m3: Modulo = Modulo("Logica")


    v1: Voto = Voto(29)
    v2: Voto = Voto(30)
    v3: Voto = Voto(27)

    esame.add(s1, m1, v1)
    esame.add(s2, m2, v2)
    esame.add(s3, m3, v3)

    print(f"Esami {s1}: ")
    for l in s1.esami():
        print(f"{l.modulo().nome()}: {l.voto()}")
    
    print()
    
    print(f"Esami {s2}: ")
    for l in s2.esami():
        print(f"{l.modulo().nome()}: {l.voto()}")
    
    print()

    print(f"Esami {s3}:")
    for l in s3.esami():
        print(f"{l.modulo().nome()}: {l.voto()}")

    print()

    print(f"Studenti iscritti a {m1}: ")
    for l in m1.esami():
        print(f"{l.studente().nome()}: {l.voto()}")
    
    print()

    print(f"Studenti iscritti a {m2}: ")
    for l in m1.esami():
        print(f"{l.studente().nome()}: {l.voto()}")
    
    print() 
    
    print(f"Rimozione del link esame del modulo {m1}")
    try:
        esame.remove(s1.esame(m1))
        print("Modulo eliminato")
    except KeyError:
        print(f"Non esiste il modulo {m1.nome()}")
    
    print()

    print(f"Riprovo a rimuovere lo stesso esame per il modulo {m1}:")
    try:
        esame.remove(s1.esame(m1))
        print("Errore. L'esame non doveva esistere.")
    except KeyError:
        print(f"Nessun esame da rimuovere per il modulo {m1.nome()}")
    




