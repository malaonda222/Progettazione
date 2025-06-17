from typing import Self
from datetime import date
import re

class Durata(int):
    def __new__(cls, minuti: Self | int | float | str | bool) -> Self:
        minuti: int = super().__new__(cls, minuti)
        if minuti <= 0:
            raise ValueError(f"Il valore {minuti} deve essere maggiore di zero.")
        return minuti 
    

class Abitanti(int):
    def __new__(cls, abitanti: Self | int | float | str | bool) -> Self:
        abitanti: int = super().__new__(cls, abitanti)
        if abitanti < 0:
            raise ValueError(f"Il valore {abitanti} deve essere maggiore di zero.")
        return abitanti 
    

class Data1900(int):
    def __new__(cls, anno: Self) -> Self:
        anno: int = super().__new__(cls, anno)
        if anno < 1900:
            raise ValueError(f"L'anno {anno} non è valido.")
        return anno
    

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
        