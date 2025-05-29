from custom_types import *
from Design.VoliAerei.VoliAerei2 import *


class Volo:
    _codice: CodiceVolo #<<imm>> noto alla nascita
    _durata_minuti: Durata #noto alla nascita

    def __init__(self, codice: CodiceVolo, durata_minuti: Durata):
        self._codice = codice

        self.set_durata_minuti(durata_minuti)

    def set_durata_minuti(self, durata_minuti: Durata) -> None:
        self._durata_minuti: Durata = durata_minuti

    def get_codice(self) -> CodiceAeroporto:
        return self._codice 
    
    def get_durata_minuti(self) -> Durata:
        return self._durata_minuti


class Aeroporto:
    _codice: CodiceAeroporto #<<imm>> noto alla nascita
    _nome: str #noto alla nascita

    def __init__(self, codice: CodiceAeroporto, nome: str):
        self._codice = codice 

        self.set_nome(nome)

    def set_nome(self, nome: str) -> None:
        if not isinstance(nome, str) or nome.strip() == "":
            raise ValueError("Errore. Nome non valido.")
        self._nome: str = nome 

    def get_nome(self) -> str:
        return self._nome 

    def get_codice(self) -> CodiceAeroporto:
        return self._codice 
    

class Citta:
    _nome: str #noto alla nascita
    _abitanti: Abitanti #noto alla nascita

    def __init__(self, nome: str, abitanti: Abitanti):
        self.set_nome(nome)
        self.set_abitanti(abitanti)

    def set_nome(self, nome: str) -> None:
        if not isinstance(nome, str) or nome.strip() == "":
            raise ValueError("Errore. Nome non valido.")
        self._nome: str = nome 

    def set_abitanti(self, abitanti: Abitanti) -> None:
        self._abitanti: Abitanti = abitanti 

    def get_nome(self) -> str:
        return self._nome 
    
    def get_abitanti(self) -> Abitanti:
        return self._abitanti 
    


class CompagniaAerea:
    _nome: str #noto alla nascita
    _anno_fondazione: Data1900 #<<imm>> noto alla nascita

    def __init__(self, nome: str, anno_fondazione: Data1900):
        self._anno_fondazione = anno_fondazione

        self.set_nome(nome)

    def set_nome(self, nome: str) -> None:
        if not isinstance(nome, str) or nome.strip() == "":
            raise ValueError("Errore. Nome non valido.")
        self._nome: str = nome
    
    def get_nome(self) -> str:
        return self._nome 
    
    def get_anno_fondazione(self) -> Data1900:
        return self._anno_fondazione 
    

class Nazione:
    _nome: str
    _citta_nazione: set[Citta]

    def __init__(self, nome: str) -> None:
        self.set_nome(nome)
        self._citta_nazione = set()
    
    def set_nome(self, nome: str) -> None:
        self._nome = nome 

    def nome(self) -> str:
        return self._nome 
    
    def add_citta_nazione(self, c:Citta) -> None:
        self._citta_nazione.add(c)

    def remove_citta_nazione(self, c:Citta) -> None:
        if c in self._citta_nazione: #o if c:
            self._citta_nazione.remove(c)
        else:
            raise ValueError("La città non è presente nella lista delle città.")

    def citta_nazione(self) -> frozenset[Citta]:
        return frozenset(self._citta_nazione) 


    

    


    

    
    



