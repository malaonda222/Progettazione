from typing import Self 
import enum
import re 

class Email(str):
     def __new__(cls, e: str | Self) -> Self:
        if re.fullmatch(r"^[a-z0-9!#$%&'*+/=?^_`{|}~-]+(?:\.[a-z0-9!#$%&'*+/=?^_`{|}~-]+)*@(?:[a-z0-9](?:[a-z0-9-]*[a-z0-9])?\.)+[a-z0-9](?:[a-z0-9-]*[a-z0-9])?$", e):
            return super().__new__(cls, e)
        raise ValueError(f"{e} non è un'email valida.")
     

