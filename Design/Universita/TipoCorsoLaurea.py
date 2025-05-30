from Universita.CorsoDiLaurea import *

class TipoCdL:
    _nome: str 
    _cdl_tipo: CorsoDiLaurea

    def __init__(self, nome: str):
        self.set_nome(nome)
        self._cdl_tipo = set()

    def set_nome(self, nome) -> None:
        self._nome = nome 

    def add_cdl(self, cdl_tipo: CorsoDiLaurea) -> None:
        self._cdl_tipo.add(cdl_tipo)

    def remove(self, cdl_tipo: CorsoDiLaurea) -> None:
        if len(self._cdl_tipo) >= 1:
            self._cdl_tipo.remove(cdl_tipo)

    def get_nome(self) -> str:
        return self._nome 
    
    def get_cdl_tipo(self) -> frozenset[CorsoDiLaurea]:
        return frozenset(self._cdl_tipo)
    

    
