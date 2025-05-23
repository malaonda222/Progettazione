from typing import Self 
import enum
import re 

class Telefono(str):
     def __new__(cls, tel: str | Self) -> Self:
        if re.fullmatch(r'^\d{10}$', tel):
            return super().__new__(cls, tel)
        raise ValueError(f"{tel} non è un numero di telefono italiano valido.")