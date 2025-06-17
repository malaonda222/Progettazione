from Professore import *
from Studente import Studente
from Regione import *

class Citta:
    _nome: str
    _professore_nascita: Professore 
    _studente_nascita: Studente
    _citta_regione: Regione

    def __init__(self, nome: str, citta_regione: Regione):
        self.set_nome(nome)
        self._professore_nascita: Professore = set()
        self._studente_nascita: Studente = set()
        self.set_citta_regione(citta_regione)

    def set_nome(self, nome) -> None:
        self._nome = nome 

    def add_professore_nascita(self, professore_nascita: Professore) -> None:
        self._professore_nascita.add(professore_nascita)
    
    def remove_professore_nascita(self, professore_nascita: Professore) -> None:
        if len(self._professore_nascita) >= 1:
            self._professore_nascita.remove(professore_nascita)

    def add_studente_nascita(self, studente_nascita: Studente) -> None:
        self._studente_nascita.add(studente_nascita)

    def remove_studente_nascita(self, studente_nascita: Studente) -> None:
        if len(self._studente_nascita) >= 1:
            self._studente_nascita.remove(studente_nascita)

    def set_citta_regione(self, citta_regione: Regione) -> None:
        self._citta_regione = citta_regione
        
    def get_nome(self) -> str:
        return self._nome 

    def get_professore_nascita(self) -> frozenset[Professore]:
        return frozenset(self._professore_nascita)
    
    def get_studente_nascita(self) -> frozenset[Studente]:
        return frozenset(self._studente_nascita)
    
    def get_citta_regione(self) -> Regione:
        return self._citta_regione
    
