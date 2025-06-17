from custom_types import *
import datetime
from Citta import Citta
from DipartimentoAziendale import DipartimentoAziendale

class Direttore:
    _nome: str 
    _cognome: str 
    _codice_fiscale: CodiceFiscale
    _data_nascita: datetime.date
    _anno_servizio: IntGEZ
    _citta_nascita: Citta
    _dirige: DipartimentoAziendale

    def __init__(self, nome: str, cognome: str, codice_fiscale: CodiceFiscale, data_nascita: datetime.date, anno_servizio: IntGEZ, citta_nascita: Citta):
        self.set_nome(nome)
        self.set_cognome(cognome)
        self._codice_fiscale = codice_fiscale
        self._data_nascita = data_nascita
        self.set_anno_servizio(anno_servizio)
        self._citta_nascita = citta_nascita
        self._dirige = set()

    def set_nome(self, nome: str) -> None:
        self._nome = nome 
    
    def set_cognome(self, cognome: str) -> None:
        self._cognome = cognome

    def set_anno_servizio(self, anno_servizio: IntGEZ) -> None:
        self._anno_servizio = anno_servizio

    def add_dirige(self, dirige: DipartimentoAziendale) -> None:
        self._dirige.add(dirige)

    def remove_dirige(self, dirige: DipartimentoAziendale) -> None:
        if len(self._dirige) >= 1:
            self._dirige.remove(dirige)

    def get_nome(self) -> str:
        return self._nome 
    
    def get_cognome(self) -> str:
        return self._cognome 
    
    def get_codice_fiscale(self) -> CodiceFiscale:
        return self._codice_fiscale
    
    def get_data_nascita(self) -> datetime.date:
        return self._data_nascita
    
    def get_citta_nascita(self) -> Citta:
        return self._citta_nascita

    def get_anni_servizio(self) -> IntGEZ:
        return self._anno_servizio
    
    def get_dirige(self) -> frozenset[DipartimentoAziendale]:
        return frozenset(self._dirige) 
    

