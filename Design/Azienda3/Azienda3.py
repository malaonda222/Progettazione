from __future__ import annotations
from typing import Self
import re 
from datetime import date
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
    

class Impiegato:
    _nome: str #noto alla nascita
    _cognome: str #noto alla nascita
    _nascita: date #non facciamo il set perché è un dato immutabile e noto alla nascita
    _stipendio: Importo #noto alla nascita
    _afferenza: _afferenza | None #da associazione 'afferenza[0..1] noto alla nascita
    
    def __init__(self, nome: str, cognome: str, nascita: date, stipendio: Importo, dipartimento_afferenza: Dipartimento | None = None, data_afferenza: date | None = None) -> None:
        self.set_nome(nome)
        self.set_cognome(cognome)
        self._nascita = nascita
        self.set_stipendio(stipendio)
        self.set_link_afferenza(dipartimento_afferenza, data_afferenza)
    
    def set_link_afferenza(self, dipartimento_afferenza: Dipartimento | None = None, data_afferenza: date | None=None) -> None:
        if (dipartimento_afferenza is None) != (data_afferenza is None):
            raise ValueError("Dipartimento e data di afferenza devono essere entrambi None o entrambi non None")
        if dipartimento_afferenza:
            self._afferenza = _afferenza(impiegato=self, dipartimento=dipartimento_afferenza, data_afferenza=data_afferenza)
            dipartimento_afferenza._add_impiegato(self._afferenza)
        else:
            try: 
                if self.get_link_afferenza():
                    self.get_link_afferenza().dipartimento()._remove_impiegato(self.get_link_afferenza())
            except AttributeError: #il campo _afferenza non era mai stato settato: questo metodo è stato quindi chiamato dal costruttore
                pass
            self._afferenza = None
        
    def nome(self) -> str:
        return self._nome 
    
    def cognome(self) -> str:
        return self._cognome 
    
    def nascita(self) -> date:
        return self._nascita
    
    def stipendio(self) -> Importo:
        return self._stipendio 
    
    def dipartimento_afferenza(self) -> date: #inserisco afferenza
        return self._afferenza
    
    def set_nome(self, nome: str) -> None:
        self._nome = nome

    def set_cognome(self, cognome: str) -> None:
        self._cognome = cognome 
    
    def set_stipendio(self, stipendio: Importo) -> None:
        self._stipendio = stipendio 

    def set_dipartimento(self, dipartimento_afferenza: Dipartimento | None, data_afferenza: date | None) -> None:
        self._dipartimento_afferenza = dipartimento_afferenza
        self._data_afferenza = data_afferenza

    def data_afferenza(self) -> date:
        return self.data_afferenza
    
    def get_link_afferenza(self) -> _afferenza:
        return self._afferenza 
    
    def __eq__(self, other: Any) -> bool:
        if type(self) != type(other) or hash(self) != hash(other):
            return False 
        return (self.)
    
    def __hash__
        
   
    def __str__(self) -> str:
        afferenza: str = f"che afferisce al dip. {self.afferenza().nome()} dal {self.data_afferenza()}" if self.dipartimento_afferenza else ""
        return f"Impiegato: {self.nome()} {self.cognome()} {afferenza}"
    


class Dipartimento:
    _nome: str 
    _telefono: Telefono 
    _impiegati: set[_afferenza] #da associazione 'afferenza' 0*

    def __init__(self, nome: str, telefono: Telefono) -> None:
        self.set_nome(nome)
        self.set_telefono(telefono) 
        self._impiegati = set()     

    def nome(self) -> str:
        return self._nome 
    
    def telefono(self) -> Telefono:
        return self._telefono
    
    def set_nome(self, nome: str) -> None:
        self._nome = nome 
    
    def set_telefono(self, telefono: Telefono) -> None:
        self._telefono = telefono 
    
    def impiegati(self) -> frozenset[_afferenza]:
        return frozenset(self._impiegati)

    def _add_impiegato(self, afferenza: _afferenza) -> None:
        self._impiegati.add(impiegato)

    def _remove_impiegato(self, afferenza: _afferenza) -> None:
        self._impiegati.remove(impiegato)


class _afferenza:

    class _link:
        _impiegato: Impiegato #ovviamente noto alla nascita e immutabile 
        _dipartimento: Dipartimento #ovviamente noto alla nascita e immutabile  
        _data_afferenza = date #immutabile e noto alla nascita 

    def __init__(self, impiegato: Impiegato, dipartimento: Dipartimento, data_afferenza: date) -> None:
        self._impiegato = impiegato 
        self._dipartimento = dipartimento 
        self._data_afferenza = data_afferenza  
    
    def impiegato(self) -> Impiegato:
        return self._impiegato
    
    def dipartimento(self) -> Dipartimento:
        return self._dipartimento 
    
    def data_afferenza(self) -> date:
        return self._data_afferenza 
    
          
    
    def __hash__(self):
        return hash( (self.impiegato(), self.dipartimento()))
    
    def __eq__(self, other: Any) -> bool:
        if type(self) != type(other) or hash(self) != hash(other):
            return False 
        return ( self.impiegato(), self.dipartimento() ) == (other.impiegato(), other.dipartimento() )

    

class Progetto:
    _nome: str
    _budget: Importo 

    def __init__(self, nome:str, budget: Importo) -> None:
        self.set_nome(nome)
        self.set_budget(budget)

    def nome(self) -> str:
        self._nome = nome 
    

class afferenza:

    class _link:
        _impiegato: Impiegato 
        _dipartimento: Dipartimento 
        _data_afferenza = date 

    def impiegato(self) -> Impiegato:
        return self._impiegato
    
    def dipartimento(self) -> Dipartimento:
        return self._dipartimento 
    
    def data_afferenza(self) -> datetime.time:
        return self._data_afferenza 
    
    def __init__(self, impiegato: Impiegato, dipartimento: Dipartimento, data_afferenza: datetime.date):
        self._impiegato = impiegato 
        self._dipartimento = dipartimento 
        self._data_afferenza = data_afferenza        
    
    def __hash__(self):
        return hash( (self.impiegato(), self.dipartimento()))
    
    def __eq__(self, other: Any) -> bool:
        if type(self) != type(other) or hash(self) != hash(other):
            return False 
        return ( self.impiegato(), self.dipartimento() ) == (other.impiegato(), other.dipartimento() )
    


vendite: Dipartimento = Dipartimento(nome="vendite", telefono=Telefono("1524630"))

alice: Impiegato = Impiegato("Alice", "Alberelli", nascita=date.today() - timedelta(weeks=52*25), stipendio=Importo(45000), afferenza=vendite)

biagio: Impiegato = Impiegato("Biagio", "Alberelli", nascita=date.today() - timedelta(weeks=52*25), stipendio=Importo(45000), afferenza=vendite))
