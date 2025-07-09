from abc import ABC, abstractmethod
from datetime import *
from typing import *
from customtypes import *
import re

# classe utente 
class Utente(ABC):
    _username: str #immutabile
    _data_registrazione: datetime #immutabile
 
    @abstractmethod
    def __init__(self, *, username: str, data_registrazione: datetime):
        self._username = username
        self._data_registrazione = data_registrazione
    def username(self) -> str:
        return self._username
    def data_registrazione(self) -> datetime:
        return self._data_registrazione


class VenditoreProfessionale(Utente):
    _vetrina: Url | None #[0..1], mutabile
 
    def __init__(self, *, username: str, data_registrazione: datetime, vetrina: Url|None = None):
        super().__init__(username=username, data_registrazione=data_registrazione)
        self.set_vetrina(vetrina)
    def vetrina(self) -> Url|None:
        return self._vetrina
    def set_vetrina(self, vetrina: Url|None) -> None:
        try:
            if self._vetrina:
                raise ValueError("Errore, l'attributo è stato già assegnato")
        except AttributeError:
            pass
        self._vetrina = vetrina


class UtentePrivato(Utente):
 
    def __init__(self, *, username: str, data_registrazione: datetime):
        super().__init__(username=username, data_registrazione=data_registrazione)

class Bid:
    _istante: datetime #noto alla nascita e immutabile
    
    def __init__(self, *, istante: datetime) -> None:
        self._istante = istante 
    
    def istante(self) -> datetime:
        return self._istante 


class OggettoDelPost(ABC):
    _descrizione: str #mutabile noto alla nascita
    _anni_garanzia: IntGEZ #mutabile noto alla nascita
    _anni_garanzia2: IntGE2 | None #mutabile noto alla nascita 
    _pubblicazione: datetime #immutabile noto alla nascita
    _is_nuovo: bool #immutabile noto alla nascita
    _is_usato: bool #immutabile noto alla nascita 
    _condizione: Condizioni | None#[0..1] possibilmente non noto alla nascita 
    _prezzo: FloatGZ 

    @abstractmethod
    def __init__(self, *, descrizione: str, anni_garanzia: IntGEZ, anni_garanzia2: IntGE2|None = None, pubblicazione: datetime, condizione: Condizioni|None = None, prezzo: FloatGZ):
        self.set_descrizione(descrizione)
        self.set_anni_garanzia(anni_garanzia)
        self._pubblicazione = pubblicazione
        self.set_prezzo(prezzo)

        self._is_nuovo = False 
        self._is_usato = False
        self._anni_garanzia2 = anni_garanzia2 
        self._condizione = condizione

        if condizione is not None:
            self._is_usato = True 
        if anni_garanzia2 is not None:
            self._is_nuovo = True 

        if self.is_nuovo() and self.is_usato():
            raise ValueError("Un oggetto non può essere sia usato che nuovo")
          
    def set_descrizione(self, descrizione: str) -> None:
        if not isinstance(descrizione, str):
            raise ValueError("Errore. La descrizione deve essere una stringa")
        self._descrizione = descrizione

    def set_anni_garanzia(self, anni_garanzia: IntGEZ) -> None:
        self._anni_garanzia = anni_garanzia

    def set_prezzo(self, prezzo: FloatGZ) -> None:
        self._prezzo = prezzo 

    def descrizione(self) -> str:
        return self._descrizione
    
    def anni_garanzia(self) -> IntGEZ:
        return self._anni_garanzia
    
    def pubblicazione(self) -> datetime:
        return self._pubblicazione
    
    def is_nuovo(self) -> bool:
        return self._is_nuovo
    
    def is_usato(self) -> bool:
        return self._is_usato

    def prezzo(self) -> FloatGZ:
        return self._prezzo 
    
    def anni_garanzia2(self) -> IntGE2:
        if not self.is_nuovo():
            raise RuntimeError("Non è un oggetto nuovo")
        return self._anni_garanzia2
    
    def condizione(self) -> Condizioni:
        if not self.is_usato():
            raise RuntimeError("Non è un oggetto usato")
        return self._condizione
    

class Asta(OggettoDelPost):
    _prezzo_rialzo: FloatGZ #[0..1]
    _scadenza: date #[0..1]

    def __init__(self, *, descrizione: str, anni_garanzia: IntGEZ, anni_garanzia2: IntGE2| None = None, pubblicazione: datetime, condizione: Condizioni|None = None, prezzo_rialzo: FloatGZ|None = None, scadenza: date|None = None):
        super().__init__(descrizione=descrizione, anni_garanzia=anni_garanzia, anni_garanzia2=anni_garanzia2|None, pubblicazione=pubblicazione, condizione=condizione)
        self.set_prezzo_rialzo(prezzo_rialzo)
        self.set_scadenza(scadenza)

        if (prezzo_rialzo is None) != (scadenza is None):
            raise ValueError("Prezzo rialzo e scadenza devono essere entrambi None o entrambi non None")

    def prezzo_rialzo(self) -> FloatGZ | None:
        return self._prezzo_rialzo

    def scadenza(self) -> date | None:
        return self._scadenza 
    

class CompraloSubito(OggettoDelPost):

    def __init__(self, *, descrizione: str, anni_garanzia: IntGEZ, anni_garanzia2: IntGE2| None = None, pubblicazione: datetime, condizione: Condizioni|None = None, prezzo: FloatGZ):
        super().__init__(descrizione=descrizione, anni_garanzia=anni_garanzia, anni_garanzia2=anni_garanzia2|None, pubblicazione=pubblicazione, condizione=condizione)


        if condizione is not None:
            self._is_usato = True 
        if anni_garanzia2 is not None:
            self._is_nuovo = True 

        if self.is_nuovo() and self.is_usato():
            raise ValueError("Un oggetto non può essere sia usato che nuovo")
    
    def set_prezzo(self, prezzo: FloatGZ):
        self._prezzo = prezzo 

    def prezzo(self) -> FloatGZ:
        return self._prezzo 
    


