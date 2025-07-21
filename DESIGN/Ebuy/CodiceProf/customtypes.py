from typing import Self, Type, Any
import re 
from enum import *

class Condizioni(StrEnum):
    ottimo = auto()
    buono = auto()
    discreto = auto()
    da_sistemare = auto()
    

class Popolarita(StrEnum):
    bassa = auto()
    media = auto()
    alta = auto()

class Url(str):
    def __new__(cls, url: str | Self) -> Self:
 
        url_1 = url.lower().strip()
        if re.fullmatch(r"^(https?:\/\/)?([\da-z\.-]+)\.([a-z\.]{2,6})([\/\w \.-]*)*\/?$", url_1):
            return super().__new__(cls, url_1)
        raise ValueError(f"{url_1} non valida")
    

class IntGEZ(int):
    #tipo di dato specializzato Intero >= 0

    def __new__(cls, v: Self | int | float | str | bool) -> Self:
        value: int = super().__new__(cls, v)
        if value < 0:
            raise ValueError(f"Il valore {v} deve essere più grande o uguale a 0")
        return value
    
class IntGE2(int):
    #tipo di dato specializzato Intero >= 2

    def __new__(cls, v: Self | int | float | str | bool) -> Self:
        value: int = super().__new__(cls, v)
        if value < 2:
            raise ValueError(f"Il valore {v} deve essere più grande o uguale a 0")
        return value
    

class FloatGZ(float):

    def __new__(cls, v: Self | int | float | str | bool) -> Self:
        value: float = super().__new__(cls, v)
        if value <= 0:
            raise ValueError(f"Il valore {v} deve essere più grande o uguale a 0")
        return value
    

class FloatGEZ(int):
    #tipo di dato specializzato Intero > 0
    def __new__(cls, v: Self | int | float | str | bool) -> Self:
        value: float = super().__new__(cls, v)
        if value < 0:
            raise ValueError(f"Il valore {v} deve essere più grande di 0")
        return value 
    

class Condizioni(StrEnum):
    ottimo = auto()
    buono = auto()
    discreto = auto()
    da_sistemare = auto()


class Popolarita(StrEnum):
    alta = auto()
    media = auto()
    bassa = auto() 


class Voto(int):
    def __new__(cls, voto:int|float|Self)->Self:
        if voto < 0 or voto > 5:
            raise ValueError(f"Value v == {voto} must be between 0 and 5")
        return int.__new__(cls, voto)