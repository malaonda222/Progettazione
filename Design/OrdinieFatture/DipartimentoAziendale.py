from custom_types import *

class DipartimentoAziendale:
    _nome: str
    _indirizzo: Indirizzo 

    def __init__(self, nome: str, indirizzo: Indirizzo):
        self.set_nome(nome)
        self.set_indirizzo(indirizzo)

    def set_nome(self, nome: str) -> None:
        self._nome = nome 

    def set_indirizzo(self, indirizzo: Indirizzo) -> None:
        self._indirizzo = indirizzo 

    def get_nome(self) -> str:
        return self._nome 
    
    def get_indirizzo(self) -> Indirizzo:
        return self._indirizzo 
    
    