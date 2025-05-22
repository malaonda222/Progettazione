from typing import Self
import re 


class CodiceFiscale(str):
    def __new__(cls, cf: str | Self) -> Self:
        
        cff: str = cf.upper().strip()
        if re.fullmatch(r'^[A-Z]{6}[0-9]{2}[A-Z]{1}[0-9]{2}[A-Z]{1}[0-9]{3}[A-Z]{1}$', cff):
            return super().__new__(cls, cff)
        raise ValueError(f"{cff} non è un codice fiscale italiano valido.")
    
cff: CodiceFiscale = CodiceFiscale("AAABBB99C45J230H")




class CodiceFiscale:
    cf: str
    def __init__(self, cf: str):
        if not re.fullmatch(r'^[A-Z]{6}[0-9]{2}[A-Z]{1}[0-9]{2}[A-Z]{1}[0-9]{3}[A-Z]{1}$', cf):
            self.cf = cf
        else:
            raise ValueError(f"{cf} non è un codice fiscale italiano valido.")

codfis = CodiceFiscale("AAABBB88J52K635K")
codfis.cf 