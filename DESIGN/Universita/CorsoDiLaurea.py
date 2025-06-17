from Insegnamento import *
from custom_types import *
from Iscrizione import *
from Universita.TipoCorsoLaurea import *

class CorsoDiLaurea:
    _codice: str
    _nome: str 
    _insegnamento_cdl: Insegnamento
    _iscrizione: Studente
    _cdl_tipo: TipoCdL

    def __init__(self, codice: str, nome: str, cdl_tipo: CorsoDiLaurea):
        self.set_codice(codice)
        self.set_nome(nome)
        self._insegnamento_cdl = set()
        self._iscrizione = set()
        self.set_cdl_tipo(cdl_tipo)

    def set_codice(self, codice: str) -> None:
        self._codice = codice

    def set_nome(self, nome: str) -> None:
        self._nome = nome
    
    def set_cdl_tipo(self, cdl_tipo: CorsoDiLaurea) -> None:
        self._cdl_tipo = cdl_tipo

    def get_codice(self) -> str:
        return self._codice 
    
    def get_nome(self) -> str:
        return self._nome 
    
    def get_cdl_tipo(self) -> CorsoDiLaurea:
        return self._cdl_tipo
    
    def add_insegnamento_cdl(self, i: Insegnamento) -> None:
        self._insegnamento_cdl.add(i)
    
    def add_iscrizione(self, iscrizione: Studente) -> None:
        self._iscrizione.add(iscrizione)

    def remove_insegnamento_cdl(self, i: Insegnamento) -> None:
        if len(self._insegnamento_cdl) >= 1:
            self._insegnamento_cdl.remove(i) 

    def remove_iscrizione(self, iscrizione: Studente) -> None:
        if len(self._iscrizione) >= 1:
            self._iscrizione.remove(iscrizione)
    
    def get_insegnamento_cdl(self) -> frozenset[CorsoDiLaurea]:
        return frozenset(self._insegnamento_cdl) 
    
    def get_iscrizione(self) -> frozenset[Studente]:
        return frozenset(self._iscrizione)