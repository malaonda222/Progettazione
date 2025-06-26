from DESIGN.ImpiegatoStudente.custom_types import *


class Modulo:
    _codice: str 

    def __init__(self, codice: str) -> None:
        self._codice = codice 

    def codice(self) -> str:
        return self._codice 
    
    def __has__(self):
        return hash(self._codice)
    


class Studente:
    _nome: str 
    _esami: dict[Modulo, 'esame._link'] #non noto alla nascita

    def __init__(self, nome: str) -> None:
        self._nome = nome 
        self._esame = dict()

    def nome(self) -> str:
        return self._nome 
    
    def esami(self) -> frozenset['esame._link']:
        return frozenset(self._esami.values())
    
    def add_esame(self, modulo: Modulo, voto: int) -> None: 
        if modulo in self._esami:
            raise ValueError(f"Lo studente aveva già superato l'esame del modulo {modulo}!")
        else:
            l: esame._link = esame._link(studente=self, modulo = Modulo, voto=voto)
            self._esami[modulo] = l 



class esame:
    class _link:
        _studente: 'Studente'
        _modulo: Modulo 
        _voto: int #<<imm>>

    def __init__(self, studente: 'Studente', modulo: Modulo, voto: int) -> None:
        self._studente = studente 
        self._modulo = modulo 
        self._voto = voto 

    def studente(self) -> 'Studente':
        return self._studente 
    
    def modulo(self) -> Modulo:
        return self._modulo 
    
