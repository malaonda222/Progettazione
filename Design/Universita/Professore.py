from custom_types import *
import datetime


class Professore:
    _nome: str
    _cognome: str 
    _data_nascita: datetime.date #<<imm>>
    _codice_fiscale: CodiceFiscale #<<imm>>

def __init__(self, nome: str, cognome: str, data_nascita: datetime.date, codice_fiscale: CodiceFiscale):
    self.set_nome(nome)
    self.set_cognome(cognome)
    self._data_nascita = data_nascita
    self._codice_fiscale = codice_fiscale

def set_nome(self, nome: str) -> None:
    self.nome = nome 

def set_cognome(self, cognome: str) -> None:
    self.cognome = cognome 

def get_nome(self) -> str:
    return self.nome 

def get_cognome(self) -> str:
    return self.cognome 

def get_data_nascita(self) -> datetime.date:
    return self.data_nascita

def get_codice_fiscale(self) -> CodiceFiscale:
    return self._codice_fiscale
    