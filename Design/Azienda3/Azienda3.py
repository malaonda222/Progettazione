from __future__ import annotations
from typing import *
from datetime import date
from typing import Any 
from custom_types import Telefono, Importo

    
class Impiegato:
    _nome: str #noto alla nascita
    _cognome: str #noto alla nascita
    _nascita: date #non facciamo il set perché è un dato immutabile e noto alla nascita
    _stipendio: Importo #noto alla nascita
    _afferenza: _afferenza | None #da associazione 'afferenza[0..1]' possibilmente non noto alla nascita
    
    def __init__(self, nome: str, cognome: str, nascita: date, stipendio: Importo, dipartimento_aff: Dipartimento | None = None, data_afferenza: date | None = None) -> None:
        self.set_nome(nome)
        self.set_cognome(cognome)
        self._nascita = nascita
        self.set_stipendio(stipendio)
        self.set_link_afferenza(dipartimento_aff, data_afferenza)
    
    
    def set_link_afferenza(self, dipartimento_aff: Dipartimento | None = None, data_afferenza: date | None = None) -> None:
        if (dipartimento_aff is None) != (data_afferenza is None):
            #serve per verificare se esattamente uno dei due valori è None, ma non entrambi e non nessuno
            raise ValueError("Dipartimento e data di afferenza devono essere entrambi None o entrambi non None")
        
        #se afferiva a un dipartimento, devo rimuoverlo da esso
        try: 
            if self.get_link_afferenza():
                self.get_link_afferenza().dipartimento()._remove_impiegato(self.get_link_afferenza())
        except AttributeError: #il campo _afferenza non era mai stato settato: questo metodo è stato quindi chiamato dal costruttore
            pass

        if dipartimento_aff: #sono entrambi not None
            self._afferenza = _afferenza(impiegato=self, dipartimento=dipartimento_aff, data_afferenza=data_afferenza)
            dipartimento_aff._add_impiegato(self._afferenza)
        else: #se sono entrambi None   
            self._afferenza = None
    
    def get_link_afferenza(self) -> _afferenza:
        return self._afferenza
        
    def nome(self) -> str:
        return self._nome 
    
    def cognome(self) -> str:
        return self._cognome 
    
    def set_nome(self, nome: str) -> None:
        self._nome = nome

    def set_cognome(self, cognome: str) -> None:
        self._cognome = cognome 
    
    def set_stipendio(self, stipendio: Importo) -> None:
        self._stipendio = stipendio 

    def nascita(self) -> date:
        return self._nascita
    
    def stipendio(self) -> Importo:
        return self._stipendio 

    # def __str__(self) -> str:
    #     afferenza: str = f"che afferisce al dip. {self.afferenza().nome()} dal {self.data_afferenza()}" if self.dipartimento_afferenza else ""
    #     return f"Impiegato: {self.nome()} {self.cognome()} {afferenza}"


class Dipartimento:
    _nome: str 
    _telefono: Telefono 
    _impiegati: set[_afferenza] #da associazione 'afferenza' [0..*] certamente non noti alla nascita

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
        self._impiegati.add(afferenza)

    def _remove_impiegato(self, afferenza: _afferenza) -> None:
        self._impiegati.remove(afferenza)


class _afferenza:

    class _link:
        _impiegato: Impiegato #ovviamente noto alla nascita e immutabile 
        _dipartimento: Dipartimento #ovviamente noto alla nascita e immutabile  
        _data_afferenza = date #immutabile, noto alla nascita 

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
        return hash((self.impiegato(), self.dipartimento()))
    
    def __eq__(self, other: Any) -> bool:
        if type(self) != type(other) or hash(self) != hash(other):
            return False 
        return (self.impiegato() == self.dipartimento()) == (other.impiegato(), other.dipartimento())


class Progetto:
    _nome: str #noto alla nascita
    _budget: Importo
    _coinvolti: dict[Impiegato, date]

    def __init__(self, nome: str, budget: Importo) -> None:
        self.set_nome(nome)
        self.set_budget(budget)
        self._coinvolti = dict()
    
    def set_nome(self, nome: str) -> None:
        self._nome = nome 

    def nome(self) -> str:
        return self._nome 

    def set_budget(self, budget: Importo) -> None:
        self._budget = budget 

    def budget(self) -> Importo:
        return self._budget

    def coinvolti(self) -> frozenset[tuple[Impiegato, date]]:
        return frozenset(self._coinvolti.items())
        # return frozenset((imp, data) for imp, data in self._coinvolti.items())

    def add_impiegato(self, impiegato:Impiegato, data: date) -> None:
        if impiegato in self._coinvolti:
            raise ValueError(f"L'impiegato {impiegato.nome()} è già coinvolto nel progetto dal {self._coinvolti[impiegato]}")
        self._coinvolti[impiegato] = data

    def add_impiegato_oggi(self, impiegato: Impiegato) -> None:
        self.add_impiegato(impiegato, date.today())
    
    def remove_impiegato_progetto(self, impiegato: Impiegato) -> None:
        if not impiegato in self._coinvolti:
            raise ValueError(f"L'impiegato {impiegato.nome()} non era coinvolto nel progetto")
        del self._coinvolti[impiegato]  

    def is_coinvolto(self, impiegato: Impiegato) -> bool:
        return impiegato in self._coinvolti 

    def __contains__(self, item: Any) -> bool:
        if not isinstance(item, Impiegato):
            return False 
        return self.is_coinvolto(item) 

    # if type(item) != Impiegato
    #   return False 
    # return item in self._coinvolti
    
    '''def is_coinvolto_brutto(self, impiegato: Impiegato) -> bool:
        #funziona perché abbiamo implementato has ed eq di _imp_progetto
        l: _imp_progetto = _imp_progetto(self, impiegato, date.today())
        return l in self._impiegati_progetti'''
    
    def add_impiegato(self, impiegato: Impiegato, data: date) -> None:
        if impiegato in self._coinvolti:
            raise KeyError("Il progetto coinvolge già questo impiegato.")
        l: _imp_prog = _imp_prog(self, impiegato, data)
        self._imp_prog(impiegato) = l

    def remove_impiegato(self, impiegato: Impiegato) -> None:
        if not impiegato in self._coinvolti:
            raise KeyError("Il progetto non coinvolge l'impiegato.")
        del self._coinvolti[impiegato]

    def remove_impiegato2(self, impiegato: Impiegato) -> None:
        try: 
            del self._coinvolti[impiegato]
        except KeyError:
            raise KeyError("Il progetto non coinvolge l'impiegato.")
    
    def data_coinvolgimento(self, impiegato: Impiegato) -> date:
        try:
            return self._impiegati_progetti[impiegato].data()
        except KeyError:
            raise KeyError("Il progetto non coinvolge l'impiegato.")
        
    def ultimo_impiegato_coinvolto(self) -> Impiegato:
        if not self._coinvolti():
            raise RuntimeError("Il progetto non ha impiegati coinvolti.")
        date_coinvolgimento: set[date] = set()
        for l in self._coinvolti.values():
            date_coinvolgimento.add(l.data())
       # date_coinvolgimento = [l.data() for l in self._impiegati_progetti.values()]
        ultima_data: date = max(date_coinvolgimento)
        for imp in self._coinvolti:
            if self.data_coinvolgimento(imp) == ultima_data:
                return imp

    def ultimo_impiegato_coinvolto(self) -> Impiegato:
        # restituisce l'impiegato coinvolto nel progetto da più tempo
        # (in caso di impiegati assunti nello stesso giorno, ne restituisce uno scelto in modo arbitrario
        if len(self._coinvolti) == 0:
            raise RuntimeError(f"Il progetto {self.nome()} non ha impiegati coinvolti!")

        ultima_data: date = max(self._coinvolti.values())
        for impiegato, data in self._coinvolti.items():
            if data == ultima_data:
                return impiegato


class _imp_prog:
    class _link:
        _impiegato: Impiegato
        _progetto: Progetto 
        _data_afferenza_prog: date 

        def __init__(self, impiegato: Impiegato, progetto: Progetto, data_afferenza_prog: date):
            self._impiegato = impiegato 
            self._progetto = progetto 
            self._data_afferenza_prog = data_afferenza_prog
        
        def get_impiegato(self) -> Impiegato:
            return self._impiegato 
        
        def get_progetto(self) -> Progetto:
            return self._progetto
        
        def get_data_afferenza_prog(self) -> date:
            return self._data_afferenza_prog
        
        def __hash__(self) -> int:
            return hash(self.get_impiegato(), self.get_progetto)
        
        def __eq__(self, other: Any) -> bool:
            if type(self) != type(other) or hash(self) != hash(other):
                return False 
            return (self.get_impiegato(), self.get_progetto()) == (other.get_impiegato(), other.get_progetto())