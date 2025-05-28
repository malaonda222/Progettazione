from typing import Self
import re 
from datetime import *
from typing import Any 



class Importo(float):
    def __new__(cls, v:int|float|str) -> Self:
        if v < 0:
            raise ValueError(f"Value v == {v} must be >= 0")
        return float.__new__(cls, v)
    

class Telefono(str):
    def __new__(cls, v:int|float|str) -> Self:
        if not re.fullmatch(r'\+?[0-9]+', v):
            raise ValueError(f"Value v == {v} doesn't satisfy the standard")
        return str.__new__(cls, v)
    

class Dipartimento:
    _nome: str 
    _telefono: Telefono 

    def nome(self) -> str:
        return self._nome 
    
    def telefono(self) -> Telefono:
        return self._telefono
    
    def set_nome(self, nome: str) -> None:
        self._nome = nome 
    
    def set_telefono(self, telefono: Telefono) -> None:
        self._telefono = telefono 

    def __init__(self, nome: str, telefono: Telefono) -> None:
        self.set_nome(nome)
        self.set_telefono(telefono)
           


class Impiegato:
    _nome: str 
    _cognome: str 
    _nascita: datetime.date #non facciamo il set perché è un dato immutabile e noto alla nascita
    _stipendio: Importo 
    _afferenza: Dipartimento
    
    def nome(self) -> str:
        return self._nome 
    
    def cognome(self) -> str:
        return self._cognome 
    
    def nascita(self) -> datetime.date:
        return self._nascita
    
    def stipendio(self) -> Importo:
        return self._stipendio 
    
    def afferenza(self) -> datetime.date:
        return self._afferenza
    
    def set_nome(self, nome: str) -> None:
        self._nome = nome

    def set_cognome(self, cognome: str) -> None:
        self._cognome = cognome 
    
    def set_stipendio(self, stipendio: Importo) -> None:
        self._stipendio = stipendio 
    

    def __init__(self, nome: str, cognome: str, nascita: datetime.date, stipendio: Importo, afferenza: datetime.date):

        self.set_nome(nome)
        self.set_cognome(cognome)
        self._nascita = nascita
        self.set_stipendio(stipendio)
        self._afferenza = afferenza 
        

class afferenza:

    class _link:
        _impiegato: Impiegato 
        _dipartimento: Dipartimento 
        _data_afferenza = datetime.date 

    def impiegato(self) -> Impiegato:
        return self._impiegato
    
    def dipartimento(self) -> Dipartimento:
        return self._dipartimento 
    
    def data_afferenza(self) -> datetime.time:
        return self._data_afferenza 
    
    def __init__(self, impiegato: Impiegato, dipartimento: Dipartimento, data_afferenza: datetime.date):
        self._impiegato = impiegato 
        self._dipartimento = dipartimento 
        self.data_afferenza = data_afferenza        
    
    def __hash__(self):
        return hash( (self.impiegato(), self.dipartimento()))
    
    def __eq__(self, other: Any) -> bool:
        if type(self) != type(other) or hash(self) != hash(other):
            return False 
        return ( self.impiegato(), self.dipartimento() ) == (other.impiegato(), other.dipartimento() )
    
