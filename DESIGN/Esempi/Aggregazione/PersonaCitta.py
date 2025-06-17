from __future__ import annotations

class Citta:
    _nome: str 

    def __init__(self, nome: str) -> None:
        self.set_nome(nome)

    def set_nome(self, nome: str) -> None:
        self._nome = nome  
    
    def nome(self) -> str:
        return self._nome  

class Persona:
    _nome: str 
    _ha_visitato: set[Citta]

    def __init__(self, nome: str):
        self.set_nome(nome)
        self._ha_visitato = set()
    
    def set_nome(self, nome: str):
        self._nome = nome 

    def nome(self) -> str:
        return self._nome 

    def add_ha_visitato(self, c: Citta) -> None:
        return self._ha_visitato.add(c)
    
    def remove_ha_visitato(self, c: Citta) -> None:
        if c not in self._ha_visitato:
            raise ValueError("La città non è presente nella lista delle città.")
        return self._ha_visitato.remove(c)
    
    def ha_visitato(self) -> frozenset[Citta]:
        return frozenset(self._ha_visitato)  

    def __str__(self):
        citta_str = "\n- ".join(citta.nome() for citta in self.ha_visitato()) 
        return f"{self._nome} ha visitato:\n-{citta_str}"



if __name__ == '__main__':
    c1: Citta = Citta("Roma")
    c2: Citta = Citta("Milano")
    c3: Citta = Citta("Edimburgo")
    c4: Citta = Citta("Londra")



    p1: Persona = Persona("Alice")

    p1.add_ha_visitato(c1)

    p1.add_ha_visitato(c2)

    p1.remove_ha_visitato(c1)

    print(p1)


