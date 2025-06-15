from __future__ import annotations

class Studente:
    _nome: str #immutabile
    _iscritto: CorsoDiLaurea

    def __init__(self, nome: str, iscritto: CorsoDiLaurea) -> None:
        self.set_nome(nome) 
        self.set_iscritto(iscritto) 

    def set_nome(self, nome: str) -> None:
        self._nome = nome 
    
    def nome(self) -> str:
        return self._nome 

    def set_iscritto(self, iscritto: CorsoDiLaurea) -> None:
        self._iscritto = iscritto 

    def iscritto(self) -> CorsoDiLaurea:
        return self._iscritto
    
    

class CorsoDiLaurea:
    _nome: str 

    def __init__(self, nome: str) -> None:
        self._nome = nome 
    
    def nome(self) -> str:
        self._nome 

if __name__ == '__main__':

    c1: CorsoDiLaurea = CorsoDiLaurea("Informatica")
    c2: CorsoDiLaurea = CorsoDiLaurea("Fisica")

    s1: Studente = Studente("Alice", iscritto=c1)
    s1.set_iscritto(c2)