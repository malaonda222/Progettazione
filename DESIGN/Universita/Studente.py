from custom_types import *
import datetime
from Insegnamento import * 
from Iscrizione import * 
from CorsoDiLaurea import *
from Citta import *

class Studente:
    _nome: str
    _cognome: str 
    _data_nascita: datetime.date #<<imm>>
    _codice_fiscale: CodiceFiscale #<<imm>>
    _codice_matricola: IntGEZ #<<imm>>
    _corso_superato: Insegnamento
    _iscrizione: CorsoDiLaurea 
    _studente_nascita: Citta

    def __init__(self, nome: str, cognome: str, data_nascita: datetime.date, codice_fiscale: CodiceFiscale, codice_matricola: IntGEZ, iscrizione: CorsoDiLaurea, studente_nascita: Citta):
        self.set_nome(nome)
        self.set_cognome(cognome)
        self._data_nascita = data_nascita
        self._codice_fiscale = codice_fiscale
        self._codice_matricola = codice_matricola
        self._iscrizione = iscrizione 
        self._corso_superato = set()
        self._studente_nascita = studente_nascita

    def set_nome(self, nome: str) -> None:
        self._nome = nome 

    def set_cognome(self, cognome: str) -> None:
        self._cognome = cognome 

    def get_nome(self) -> str:
        return self._nome 
    
    def get_cognome(self) -> str:
        return self._cognome 
    
    def get_data_nascita(self) -> datetime.date:
        return self._data_nascita
    
    def get_codice_fiscale(self) -> CodiceFiscale:
        return self._codice_fiscale
    
    def get_codice_matricola(self) -> IntGEZ:
        return self._codice_matricola 
    
    def get_iscrizione(self) -> CorsoDiLaurea:
        return self._iscrizione

    def add_corso_superato(self, esame_superato: Insegnamento) -> None:
        self.corso_superato.append(esame_superato)
    
    def get_corso_superato(self) -> frozenset[Insegnamento]:
        return frozenset(self._corso_superato)
    
    def get_studente_nascita(self) -> Citta:
        return self._studente_nascita
