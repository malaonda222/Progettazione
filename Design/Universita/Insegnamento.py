from custom_types import *


class Insegnamento:
    _codice_corso: str 
    _nome: str 
    _orario_lezione_minuti: IntGEZ

    def __init__(self, codice_corso: str, nome: str, orario_lezione_minuti: IntGEZ):
        self.set_corso(codice_corso)
        self.set_nome(nome)
        self.set_orario_lezione_minuti(orario_lezione_minuti)

    def set_codice_corso(self, codice_corso: str) -> None:
        self.codice_corso = codice_corso

    def set_nome(self, nome: str) -> None:
        self.nome = nome 
    
    def set_orario_durata_minuti(self, orario_durata_lezione: IntGEZ) -> None:
        self.orario_durata_lezione = orario_durata_lezione

    def get_corso(self) -> str:
        return self.corso 
    
    def get_nome(self) -> str:
        return self.nome 

    def get_orario_durata_minuti(self) -> IntGEZ:
        return self.orario_durata_lezione
    


