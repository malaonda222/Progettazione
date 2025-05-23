from typing import Self
from datetime import date
import re

class IntGZ(int):
    def __new__(cls, d: Self | int | float | str | bool) -> Self:
        value: int = super().__new__(cls, d)
        if value <= 0:
            raise ValueError(f"Il valore {d} deve essere maggiore di zero.")
        return value 
    

class IntGEZ(int):
    def __new__(cls, a: Self | int | float | str | bool) -> Self:
        value: int = super().__new__(cls, a)
        if value < 0:
            raise ValueError(f"Il valore {a} deve essere maggiore di zero.")
        return value 
    

class IntG1900(int):
    def __new__(cls, y: Self) -> Self:
        value: int = super().__nw__(cls, y)
        if y < 1900:
            raise ValueError(f"L'anno {y} non è valido.")
        return super().__new__(cls, year=y)
    

class CodiceAeroporto(str):
    def __new__(cls, codice_aeroporto: str | Self) -> Self:
        cod_aeroporto: str = codice_aeroporto.upper().strip()
        if not re.fullmatch(r'^[A-Z]{3}$', cod_aeroporto):
            raise ValueError(f"Il codice dell'aeroporto {cod_aeroporto} deve essere composto da 3 lettere maiuscole.")
        return super().__new__(cls, cod_aeroporto)


class CodiceVolo(str):
    def __new__(cls, codice_volo: str | Self) -> Self:
        cod_volo: str = codice_volo.upper().strip()
        if not re.fullmatch(r'^\b[A-Z]{2}\d{1,4}\b$', cod_volo):
            raise ValueError(f"Il codice del volo {cod_volo} non è valido.")
        return super().__new__(cls, cod_volo)
        