from custom_types import * 
from datetime import timedelta
from Design.VoliAerei.VoliAerei2 import *
from Design.VoliAerei.VoliAerei3 import *


class Volo:
    _codice: str 
    _durata_minuti: IntGZ


    def __init__(self, codice: str, durata_minuti: IntGZ) -> None:
        self._codice = codice 
        self.set_durata_minuti(durata_minuti)

    def set_codice(self) -> str:
        return self._codice 
    
    def durata_minuti(self) -> IntGZ:
        return self._durata_minuti 
    
    def set_durata_minuti(self, durata: IntGZ) -> None:
        self._durata_minuti = durata

    
    #oppure
    def durata(self) -> timedelta:
        return timedelta(minutes=self.durata_minuti())
    

class CompagniaAerea:
    _nome: str #noto alla nascita
    _anno_fondazione:Data1900 #<<imm>> noto alla nascita
    _comp_direzione_citta: Citta #noto alla nascita


    def __init__(self, nome: str, anno_fondazione: Data1900, citta_sede: Citta) -> None:
        self.set_nome(nome)
        self._anno_fondazione = anno_fondazione
        self.set_citta_sede(citta_sede)

    def nome(self) -> str:
        return self._nome 
    
    def anno_fondazione(self) -> Data1900:
        return self._anno_fondazione
    
    def set_nome(self, nome: str) -> None:
        self._nome = nome 

    def citta_sede(self) -> Citta:
        return self._comp_direzione_citta
    
    def comp_direzione_citta(self) -> Citta:
        return self.citta_sede()
    
    def set_citta_sede(self, c: Citta) -> None:
        self._comp_direzione_citta = c


class Aeroporto:
    _codice: str #<<imm>> noto alla nascita
    _nome: str #noto alla nascita

    def __init__(self, nome: str, codice: str) -> None:
        self._codice = codice 
        self.set_nome(nome)
    
    def nome(self) -> str:
        return self._nome 
    
    def codice(self) -> str:
        return self._codice 
    
    def set_nome(self, nome: str) -> None:
        self._nome = nome 


class Citta:
    _nome: str
    _abitanti: Abitanti 

    def __init__(self, nome: str, abitanti: Abitanti) -> None:
        self.set_nome(nome) 
        self.set_abitanti(abitanti)

    def nome(self) -> str:
        return self._nome 
    
    def codice(self) -> str:
        return self._codice 
    
    def set_nome(self, nome: str) -> None:
        self._nome = nome 

    def set_abitanti(self, abitanti: Abitanti) -> None:
        self._abitanti = abitanti 


class Nazione:
    _nome: str #noto alla nascita

    def __init__(self, nome: str):
        self.set_nome(nome)

    def set_nome(self, nome: str) -> None:
        if not isinstance(nome, str) or nome.strip() == "":
            raise ValueError("Errore. Nome non valido.")
        self._nome: str = nome 

    def get_nome(self) -> str:
        return self._nome 

    
    
