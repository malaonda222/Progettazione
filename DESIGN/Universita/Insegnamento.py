from custom_types import *
from Universita.CorsoDiLaurea import CorsoDiLaurea

class Insegnamento:
    _codice_corso: str 
    _nome: str 
    _orario_lezione_minuti: IntGEZ
    _insegnamento_cdl: CorsoDiLaurea

    def __init__(self, codice_corso: str, nome: str, orario_lezione_minuti: IntGEZ, insegnamento_cdl: CorsoDiLaurea):
        self.set_corso(codice_corso)
        self.set_nome(nome)
        self.set_orario_lezione_minuti(orario_lezione_minuti)
        self._insegnamento_cdl = set()
        
        self.add_insegnamento_cdl = (insegnamento_cdl)

    def set_codice_corso(self, codice_corso: str) -> None:
        self._codice_corso = codice_corso

    def set_nome(self, nome: str) -> None:
        self._nome = nome 
    
    def set_orario_durata_minuti(self, orario_durata_lezione: IntGEZ) -> None:
        self._orario_durata_lezione = orario_durata_lezione
    
    def add_insegnamento_cdl(self, i: CorsoDiLaurea) -> None:
        self._insegnamento_cdl.add(i)

    def remove_insegnamento_cdl(self, i) -> None:
        if len(self._insegnamento_cdl) < 1: 
            raise RuntimeError("Errore. Deve esserci almeno un insegnamento per ogni corso di laurea")
        self._insegnamento_cdl.remove(i)

    def get_corso(self) -> str:
        return self._corso 
    
    def get_nome(self) -> str:
        return self._nome 

    def get_orario_durata_minuti(self) -> IntGEZ:
        return self._orario_durata_lezione
    
    def get_insegnamento_cdl(self) -> frozenset[CorsoDiLaurea]:
        return frozenset[self._insegnamento_cdl]
    


