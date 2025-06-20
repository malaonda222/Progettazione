from __future__ import annotations
from datetime import date


class Persona:
    _nome: str 
    _cognome: str 
    _ha_mangiato: set[Ristorante] 

    def __init__(self, nome: str, cognome: str) -> None:
        self.set_nome(nome)
        self.set_cognome(cognome)
        self._ha_mangiato = set()
    
    def set_nome(self, nome: str) -> None:
        self._nome = nome 
    
    def set_cognome(self, cognome: str) -> None:
        self._cognome = cognome 
    
    def nome(self) -> str:
        return self._nome 
    
    def cognome(self) -> str:
        return self._cognome 
    
    def add_ha_mangiato(self, r: Ristorante) -> None:
        self._ha_mangiato.add(r)
    
    def remove_ha_mangiato(self, r: Ristorante) -> None:
        if r not in self._ha_mangiato:
            raise ValueError("Il ristorante non si trova nella lista dei ristoranti.")
        self._ha_mangiato.remove(r)
    
    def ha_mangiato(self) -> frozenset[Ristorante]:
        return frozenset(self._ha_mangiato)
    
    def __str__(self) -> str:
        rist_str = " \n- ".join(ristorante.nome() for ristorante in self.ha_mangiato())
        return f"{self._nome} ha mangiato nei seguenti ristoranti:\n- {rist_str}"
   
    

class Ristorante:
    _nome: str
    _anno_fondazione: date
    
    def __init__(self, nome: str, anno_fondazione: date) -> None:
        self.set_nome(nome)
        self._anno_fondazione = anno_fondazione
    
    def set_nome(self, nome: str) -> None:
        self._nome = nome 
    
    def nome(self) -> str:
        return self._nome 
    
    def anno_fondazione(self) -> date:
        return self._anno_fondazione
    

if __name__ == '__main__':
    r1: Ristorante = Ristorante("Da Nino", 1986)
    r2: Ristorante = Ristorante("Dondolo", 1963)
    r3: Ristorante = Ristorante("Giullare", 2008)

    p1: Persona = Persona("Lisa", "Bim")
    p1.add_ha_mangiato(r1)
    p1.add_ha_mangiato(r3)
    p1.add_ha_mangiato(r2)

    p1.remove_ha_mangiato(r3)

    print(p1)
    
