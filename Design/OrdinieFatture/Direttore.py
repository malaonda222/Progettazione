from custom_types import *
import datetime

class Direttore:
    _nome: str 
    _cognome: str 
    _codice_fiscale: CodiceFiscale
    _data_nascita: datetime.date
    _anno_servizio: IntGEZ

    def __init__(self, nome: str, cognome: str, codice_fiscale: CodiceFiscale, data_nascita: datetime.date, anno_servizio: IntGEZ):
        self.set_nome(nome)
        self.set_cognome(cognome)
        self._codice_fiscale = codice_fiscale
        self._data_nascita = datetime.date 
        self.set_anno_servizio(anno_servizio)

    def set_nome(self, nome: str) -> None:
        self._nome = nome 
    
    def set_cognome(self, cognome: str) -> None:
        self._cognome = cognome

    def set_anno_servizio(self, anno_servizio: IntGEZ) -> None:
        self._anno_servizio = anno_servizio

    def get_nome(self) -> str:
        return self._nome 
    
    def get_cognome(self) -> str:
        return self._cognome 
    
    def get_codice_fiscale(self) -> CodiceFiscale:
        return self._codice_fiscale
    
    def get_data_nascita(self) -> datetime.date:
        return self._data_nascita
    

