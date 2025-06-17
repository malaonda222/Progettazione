from custom_types import *
from Direttore import Direttore 
from Ordine import Ordine

class DipartimentoAziendale:
    _nome: str
    _indirizzo: Indirizzo 
    _dirige: Direttore 
    _dipartimento_ordine: Ordine 

    def __init__(self, nome: str, indirizzo: Indirizzo, dirige: Direttore):
        self.set_nome(nome)
        self.set_indirizzo(indirizzo)
        self.set_dirige(dirige)
        self.set_dipartimento_ordine = set()

    def set_nome(self, nome: str) -> None:
        self._nome = nome 

    def set_indirizzo(self, indirizzo: Indirizzo) -> None:
        self._indirizzo = indirizzo 

    def set_dirige(self, dirige: Direttore) -> None:
        self._dirige = dirige 

    def add_dipartiment_ordine(self, dipartimento_ordine: Ordine) -> None:
        self._dipartimento_ordine.add(dipartimento_ordine)

    def remove_dipartimento_ordine(self, dipartimento_ordine: Ordine) -> None:
        if len(self._dipartimento_ordine) >= 1:
            self._dipartimento.remove(dipartimento_ordine)

    def get_nome(self) -> str:
        return self._nome 
    
    def get_indirizzo(self) -> Indirizzo:
        return self._indirizzo 
    
    def get_dirige(self) -> Direttore:
        return self._dirige 
    
    def get_dipartimento_ordine(self) -> frozenset[Ordine]:
        return frozenset[self._dipartimento_ordine]
    
    
    
    
    