from __future__ import annotations

class Studente:
    _nome: str 

    def __init__(self, nome: str) -> None:
        self.set_nome(nome)

    def set_nome(self, nome: str) -> None:
        self._nome = nome 
    
    def nome(self) -> str:
        return self._nome 

class Modulo:
    _nome: str 

    def __init__(self, nome: str) -> None:
        self.set_nome(nome)
    
    def set_nome(self, nome: str) -> None:
        self._nome = nome 

    def nome(self) -> str:
        return self._nome 



