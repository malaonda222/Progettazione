from custom_types import *
import datetime
from Universita.Insegnamento import *
from Citta import Citta

class Professore:
    _nome: str
    _cognome: str 
    _data_nascita: datetime.date #<<imm>>
    _codice_fiscale: CodiceFiscale #<<imm>>
    _prof_insegnamento: Insegnamento
    _professore_nascita: Citta

def __init__(self, nome: str, cognome: str, data_nascita: datetime.date, codice_fiscale: CodiceFiscale, professore_nascita: Citta):
    self.set_nome(nome)
    self.set_cognome(cognome)
    self._data_nascita = data_nascita
    self._codice_fiscale = codice_fiscale
    self._prof_insegnamento = set()
    self._professore_nascita = professore_nascita

def set_nome(self, nome: str) -> None:
    self._nome = nome 

def set_cognome(self, cognome: str) -> None:
    self._cognome = cognome 

def add_prof_insegnamento(self, prof_insegnamento: Insegnamento) -> None:
    self._prof_insegnamento.add(prof_insegnamento)

def remove_prof_insegnamento(self, prof_insegnamento: Insegnamento) -> None:
    if len(self._prof_insegnamento) >= 1:
        self._prof_insegnamento.remove(prof_insegnamento)

def get_nome(self) -> str:
    return self._nome 

def get_cognome(self) -> str:
    return self._cognome 

def get_data_nascita(self) -> datetime.date:
    return self._data_nascita

def get_codice_fiscale(self) -> CodiceFiscale:
    return self._codice_fiscale

def get_prof_insegnamento(self) -> frozenset[Insegnamento]:
    return frozenset(self._prof_insegnamento)

def get_professore_nascita(self) -> Citta:
    return self._professore_nascita
    