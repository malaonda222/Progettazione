from __future__ import annotations
from custom_types import *


class Modulo:
    _nome: str 

    def __init__(self, nome: str) -> None:
        self._nome = nome 
    
    def nome(self) -> str:
        return self._nome 
    

class Studente:
    _nome: str 
    _esami: dict[Modulo, _esame._link] #mutabile e non noto alla nascita

    def __init__(self, nome: str) -> None:
        self.set_nome(nome)
        self._esami = dict()
    
    def set_nome(self, nome: str) -> None:
        self._nome = nome 
    
    def nome(self) -> str:
        return self._nome 

    def esami(self) -> frozenset[_esame._link]:
        return frozenset(self._esami.values())
    
    def add_link_esame(self, modulo: Modulo, voto: Voto) -> None:
        l = _esame._link(self, modulo, voto)
        if modulo in self._esami:
            raise KeyError("Errore. Modulo già esistente.")
        self._esami[modulo] = l

    def remove_link_esame(self, l: _esame._link) -> None:
        if l.studente() is not self:
            raise ValueError("Il link non coinvolge lo studente.")
        del self._esami[l.modulo()]


class _esame:
    class _link:
        _studente: Studente 
        _modulo: Modulo 
        _voto: Voto
    
        def __init__(self, studente: Studente, modulo: Modulo, voto: Voto) -> None:
            self._studente = studente 
            self._modulo = modulo 
            self._voto = voto 
        
        def studente(self) -> Studente:
            return self._studente 
        
        def modulo(self) -> Modulo:
            return self._modulo 
        
        def voto(self) -> Voto:
            return self._voto 
        
        def __hash__(self) -> int:
            return hash((self.studente(), self.modulo()))

        def __eq__(self, other: Any) -> bool:
            if type(self) != type(other) or hash(self) != hash(other):
                return False 
            return ((self.studente(), self.modulo()) == (other.studente() == other.modulo()))
        

from custom_types import Voto

if __name__ == "__main__":
    # Crea moduli
    m1 = Modulo("Analisi 1")
    m2 = Modulo("Fisica")
 
    # Crea studente
    s = Studente("Alice")
 
    # Inizializza manualmente il dizionario esami
    s._esami = {}

    # Crea voti
    voto1 = Voto(28)
    voto2 = Voto(30)
 
    # Aggiungi link esami
    s.add_link_esame(m1, voto1)
    s.add_link_esame(m2, voto2)
 
    # Stampa gli esami registrati
    print("\n Esami registrati:")
    for link in s.esami():
        print(f"{s.nome()} ha sostenuto {link.modulo().nome()} con voto {link.voto()}")
 
    # Rimuovi uno degli esami (primo della lista)
    links = list(s.esami())
    s.remove_link_esame(links[0])

    # Stampa dopo la rimozione
    print("\n Esami dopo la rimozione:")
    for link in s.esami():
        print(f"{s.nome()} ha sostenuto {link.modulo().nome()} con voto {link.voto()}")
 
    # Verifica che ne sia rimasto solo uno
    assert len(s.esami()) == 1, "Errore: Rimozione non riuscita"
    print("\n Test completato con successo.")

