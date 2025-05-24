from custom_types import *
from VoliAerei2 import *


class Volo:
    _codice: CodiceVolo #<<imm>> noto alla nascita
    _durata_minuti: Durata #noto alla nascita

    def __init__(self, codice: CodiceVolo, durata_minuti: Durata):
        self._codice = codice

        self.set_durata_minuti(durata_minuti)

    def set_durata_minuti(self, durata_minuti: Durata) -> None:
        self._durata_minuti = durata_minuti

    def get_codice(self) -> str:
        return self._codice 
    
    def get_durata_minuti(self) -> int:
        return self._durata_minuti


class Aeroporto:
    _codice: CodiceAeroporto
    _nome: str 

    def __init__(self, codice: CodiceAeroporto, nome: str):
        self._codice = codice 

        self.set_nome(nome)

    def set_nome(self, nome: str) -> None:
        if not isinstance(nome, str) or nome.strip() == "":
            raise ValueError("Errore. Nome non valido.")
        self._nome = nome 

    def get_nome(self) -> str:
        return self._nome 

    def get_codice(self) -> str:
        return self._codice 
    

class Città:
    _nome: str 
    _abitanti: Abitanti 

    def __init__(self, nome: str, abitanti: Abitanti):
        self.set_nome(nome)
        self.set_abitanti(abitanti)

    def set_nome(self, nome: str) -> None:
        if not isinstance(nome, str) or nome.strip() == "":
            raise ValueError("Errore. Nome non valido.")
        self._nome = nome 

    def set_abitanti(self, abitanti: Abitanti) -> None:
        self._abitanti = abitanti 

    def get_nome(self) -> str:
        return self._nome 
    
    def get_abitanti(self) -> int:
        return self._abitanti 
    


class CompagniaAerea:
    _nome: str 
    _anno_fondazione: Data1900 

    def __init__(self, nome: str, anno_fondazione: Data1900):
        self._anno_fondazione = anno_fondazione

        self.set_nome(nome)

    def set_nome(self, nome: str) -> None:
        if not isinstance(nome, str) or nome.strip() == "":
            raise ValueError("Errore. Nome non valido.")
        self._nome = nome
    
    def get_nome(self) -> str:
        return self._nome 
    
    def get_anno_fondazione(self) -> int:
        return self._anno_fondazione 
    


class Nazione:
    _nome: str 

    def __init__(self, nome: str):
        
        self.set_nome(nome)

    def set_nome(self, nome: str) -> None:
        if not isinstance(nome, str) or nome.strip() == "":
            raise ValueError("Errore. Nome non valido.")
        self._nome = nome 

    def get_nome(self) -> str:
        return self._nome 
    


    

    


    

    
    



