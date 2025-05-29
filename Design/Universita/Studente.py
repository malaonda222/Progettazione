from custom_types import *
import datetime
from Insegnamento import * 

class Studente:
    _nome: str
    _cognome: str 
    _data_nascita: datetime.date #<<imm>>
    _codice_fiscale: CodiceFiscale #<<imm>>
    _codice_matricola: IntGEZ #<<imm>>
    _corso_superato: Insegnamento

    def __init__(self, nome: str, cognome: str, data_nascita: datetime.date, codice_fiscale: CodiceFiscale, codice_matricola: IntGEZ):
        self.set_nome(nome)
        self.set_cognome(cognome)
        self._data_nascita = data_nascita
        self._codice_fiscale = codice_fiscale
        self._codice_matricola = codice_matricola
        self._corso_superato = set()


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
    
    def get_codice_matricola(self) -> IntGEZ:
        return self.codice_matricola 

    def add_corso_superato(self, esame_superato: Insegnamento) -> None:
        self.corso_superato.append(esame_superato)
    
    def get_corso_superato(self) -> Insegnamento:
        return self._corso_superato
