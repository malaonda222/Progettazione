from __future__ import annotations
from DESIGN.ImpiegatoStudente.custom_types import *
from datetime import date

class Persona:
    _nome: str
    _cognome: str 
    _cf: CodiceFiscale
    _data_nascita: date

    _is_uomo: bool #da fusione
    _is_donna: bool #da fusione
    _num_maternita: IntGEZ | None #da fusione con Donna
    _posizione_militare: PosizioneMilitare | None #da fusione con Uomo e aggregazione di pos_uomo

    def __init__(self, *, nome: str, cognome: str, cf: CodiceFiscale, nascita: date, maternita: IntGEZ|None = None, posizione_militare: PosizioneMilitare| None = None):
        self.set_nome(nome)
        self.set_nome(cognome)
        self.set_cf(cf)
        self._nascita = nascita

        if maternita is not None:
            self.set_attributi_donna(maternita)
        else:
            self.remove_attributi_donna()

        if posizione_militare is not None:
            self.set_attributi_uomo(posizione_militare)
        else:
            self.remove_attributi_uomo()
        
        if not (self.is_uomo() or self.is_donna()):# 
            raise ValueError("Ogni persona deve essere uomo, donna o entrambi!")
        
    def set_nome(self,nome: str) -> None:
        self._nome = nome 

    def set_cognome(self, cognome: str) -> None:
        self._cognome = cognome 

    def set_attributi_donna(self, maternita: IntGEZ) -> None:
        self._is_donna = True 
        self._maternita = maternita

    def remove_attributi_donna(self) -> None:
        try: 
            if not self.is_donna():
                raise RuntimeError("La persona non era una donna!")
        except AttributeError:
            pass 

        try:
            if not self.is_uomo():
                raise RuntimeError("La persona non era anche un uomo quindi non può rimanere senza un genere!")
        except AttributeError:
                pass
        self._is_donna = False 
        self._maternita = None 

    def set_attributi_uomo(self, posizione_militare: PosizioneMilitare) -> None:
        if not self.is_uomo():
            raise RuntimeError("La persona non era un uomo!")
        self._is_uomo = True  
        self._posizione_militare = posizione_militare
    
    def remove_attributi_uomo(self) -> None:
        try: 
            if not self.is_uomo():
                raise RuntimeError("La persona non era un uomo!")
        except AttributeError:
            pass 
        self._is_uomo = False 
        self._posizione_militare = None

    def is_uomo(self) -> bool:
        return self._is_uomo

    
    def is_donna(self) -> bool:
        try:
            return self._is_donna
        except AttributeError:
            return False
     

class PosizioneMilitare:
    _nome: str #id 

    def __init__(self, nome: str) -> None:
        self._nome = nome 
    
    def posizione_militare(self) -> PosizioneMilitare:
        return self._posizione_militare
