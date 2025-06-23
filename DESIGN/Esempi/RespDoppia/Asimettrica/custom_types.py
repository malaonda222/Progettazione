from typing import Self, Type, Any
import re 
from datetime import date
from enum import *



class Telefono(str):
     def __new__(cls, tel: str | Self) -> Self:
        if re.fullmatch(r'^\d{10}$', tel):
            return super().__new__(cls, tel)
        raise ValueError(f"{tel} non è un numero di telefono italiano valido.")
     

class Email(str):
     def __new__(cls, email: str | Self) -> Self:
        if re.fullmatch(r"^[a-z0-9!#$%&'*+/=?^_`{|}~-]+(?:\.[a-z0-9!#$%&'*+/=?^_`{|}~-]+)*@(?:[a-z0-9](?:[a-z0-9-]*[a-z0-9])?\.)+[a-z0-9](?:[a-z0-9-]*[a-z0-9])?$", email):
            return super().__new__(cls, email)
        raise ValueError(f"{email} non è un'email valida.")


class Voto(int):
    def __new__(cls, voto:int|float|Self)->Self:
        if voto  < 18 or voto > 30:
            raise ValueError(f"Value v == {voto} must be between 18 and 30")
        return int.__new__(cls, voto)

class Importo(float):
    def __new__(cls, v:int|float|str) -> Self:
        if v < 0:
            raise ValueError(f"Value v == {v} must be >= 0")
        return float.__new__(cls, v)
    

class Genere(StrEnum):
    uomo = auto()
    donna = auto()


class DataGE1895(date):
    def __new__(cls, year: int, month: int, day: int) -> Self: #self perché deve costruire un nuovo oggetto della classe 
        if year < 1895:
            raise ValueError(f"La data {day}/{month}/{year} deve essere successiva all'1 gennaio 1895.")
        return super().__new__(cls, year=year, month=month, day=day)
    

class CodiceFiscale(str):
    def __new__(cls, cf: str | Self) -> Self:
        cff: str = cf.upper().strip()
        if re.fullmatch(r'^[A-Z]{6}[0-9]{2}[A-Z]{1}[0-9]{2}[A-Z]{1}[0-9]{3}[A-Z]{1}$', cff):
            return super().__new__(cls, cff)
        raise ValueError(f"{cff} non è un codice fiscale italiano valido.")


class CodiceFiscale:
    cf: str
    def __init__(self, cf: str):
        if not re.fullmatch(r'^[A-Z]{6}[0-9]{2}[A-Z]{1}[0-9]{2}[A-Z]{1}[0-9]{3}[A-Z]{1}$', cf):
            self.cf = cf
        else:
            raise ValueError(f"{cf} non è un codice fiscale italiano valido.")


class Indirizzo:
    # campi dati:
    # _via:str
    # _civico:...
    def __init__(self, via:str, civico:str):
        if via is None:
            raise ValueError(f"via cannot be None")
        if civico is None:
            raise ValueError(f"civ cannot be None")
       
        self._via:str = via


        if not re.search(r'^[0-9]+[a-zA-Z]*$', civico):
            raise ValueError(f"value for civico '{civico}' not allowed")
        self._civico:str = civico
   
    def via(self)->str:
        return self._via
    def civico(self)->str:
        return self._civico

    def __repr__(self)->str:
        return f"Indirizzo(via={self.via()}, civico={self.civico()})"
    
    def __hash__(self)->int:
        return hash( (self.via(), self.civico()) )
    
    def __eq__(self, other: Any)->bool:
        if other is None or not isinstance(other, type(self)) or hash(self) != hash(other):
            return False
        return (self.via(), self.civico() ) == (other.via(), other.civico())
    

class IntGZ(int):
    #tipo di dato specializzato Intero > 0

    def __new__(cls, v: Self | int | float | str | bool) -> Self:
        value: int = super().__new__(cls, v)
        if value <= 0:
            raise ValueError(f"Il valore {v} deve essere più grande di 0")
        return value 
    
class IntGEZ(int):
    #tipo di dato specializzato Intero >= 0

    def __new__(cls, v: Self | int | float | str | bool) -> Self:
        value: int = super().__new__(cls, v)
        if value < 0:
            raise ValueError(f"Il valore {v} deve essere più grande o uguale a0")
        return value 
    


    # Attenzione: in generale la differenza tra interi non dovrebbe essere toccata
    def __sub__(self, other: int | str | float | bool | Self) -> Self:
        if self <= other:
            raise ValueError(f"La differenza tra {self} e {other} non è un IntGZ!")
        res: int = int(self) - int(other)
        return IntGZ(res)
    
        #opzione con try
        other_int: int = int(other)
        try: 
            res: int = int(self) - other_int
            return IntGZ(res) 
        except: 
             raise ValueError(f"La differenza tra {self} - {other} è negativo!")
        


def build_int_ge_v(n: int) -> Type:
    class IntGZV(int):
        def __new__(cls, v: Self | int | float | str | bool) -> Self:
            value: int = super().__new__(cls, v)
            if value <= n:
                raise ValueError(f"Il valore {v} deve essere più grande di {n}")
            return value 
    return IntGZV 


