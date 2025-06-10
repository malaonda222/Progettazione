from custom_types import * 
from datetime import timedelta
from Design.VoliAerei.VoliAerei2 import *
from Design.VoliAerei.VoliAerei3 import *
from __future__ import annotations


class Volo:
    _codice: CodiceVolo 
    _durata_minuti: IntGZ
    _partenza: _partenza 
    _arrivo: _arrivo
    _volo_compagnia: _volo_compagnia

    def __init__(self, codice: str, durata_minuti: IntGZ, partenza: _partenza, arrivo: _arrivo, volo_compagnia: _volo_compagnia) -> None:
        self._codice = codice 
        self.set_durata_minuti(durata_minuti)
        self._partenza = partenza 
        self._arrivo = arrivo 
        self._volo_compagnia = volo_compagnia

    def codice(self) -> CodiceVolo:
        return self._codice 
    
    def durata_minuti(self) -> IntGZ:
        return self._durata_minuti 
    
    def set_durata_minuti(self, durata: IntGZ) -> None:
        self._durata_minuti = durata
    
    def get_partenza(self) -> _partenza:
        return self._partenza 
    
    def get_arrivo(self) -> _arrivo:
        return self._arrivo 
    
    def get_volo_compagnia(self) -> _volo_compagnia:
        return self._volo_compagnia
   

class CompagniaAerea:
    _nome: str #noto alla nascita
    _anno_fondazione: Data1900 #<<imm>> noto alla nascita
    _comp_direzione_citta: Citta #noto alla nascita
    _voli_della_compagnia: set[_volo_compagnia] #mutabile, non noto alla nascita

    def __init__(self, nome: str, anno_fondazione: Data1900, citta_sede: Citta) -> None:
        self.set_nome(nome)
        self._anno_fondazione = anno_fondazione
        self.set_citta_sede(citta_sede)
        self.set_voli_della_compagnia = set()

    def set_nome(self, nome: str) -> None:
        self._nome = nome

    def nome(self) -> str:
        return self._nome 
    
    def anno_fondazione(self) -> Data1900:
        return self._anno_fondazione
    
    def set_citta_sede(self, c: Citta) -> None:
        self._comp_direzione_citta = c

    def add_voli_della_compagnia(self, volo: _volo_compagnia) -> None:
        self._voli_della_compagnia.add(volo)

    def remove_voli_della_compagnia(self, volo: _volo_compagnia) -> None:
        if len(self._voli_della_compagnia) >= 1:
            self._voli_della_compagnia.remove(volo)

    def citta_sede(self) -> Citta:
        return self._comp_direzione_citta
    
    def comp_direzione_citta(self) -> Citta:
        return self.citta_sede()
    
    def get_voli_della_compagnia(self) -> frozenset[_volo_compagnia]:
        return frozenset(self._voli_della_compagnia)
    

class Aeroporto:
    _codice: CodiceAeroporto #<<imm>> noto alla nascita
    _nome: str #noto alla nascita
    _voli_partenza: set[_partenza]
    _voli_arrivo: set[_arrivo]

    def __init__(self, nome: str, codice: str) -> None:
        self._codice = codice 
        self.set_nome(nome)
        self.voli_partenza = set()
        self.voli_arrivo = set()

    def set_nome(self, nome: str) -> None:
        self._nome = nome

    def add_voli_partenza(self, voli_partenza: _partenza) -> None:
        self._voli_partenza.add(voli_partenza)

    def remove_voli_partenza(self, voli_partenza: _partenza) -> None:
        if len(self._voli_partenza) >= 1:
            self.voli_partenza.remove(voli_partenza)
    
    def add_voli_partenza(self, voli_arrivo: _arrivo) -> None:
        self._voli_arrivo.add(voli_arrivo)

    def remove_voli_partenza(self, voli_arrivo: _arrivo) -> None:
        if len(self._voli_arrivo) >= 1:
            self.voli_arrivo.remove(voli_arrivo)
       
    def nome(self) -> str:
        return self._nome 
    
    def codice(self) -> CodiceAeroporto:
        return self._codice 

    def get_voli_partenza(self) -> frozenset[_partenza]:
        return frozenset(self._voli_partenza)

    def get_voli_arrivo(self) -> frozenset[_arrivo]:
        return frozenset(self._voli_arrivo)
    

class Citta:
    _nome: str
    _abitanti: Abitanti 

    def __init__(self, nome: str, abitanti: Abitanti) -> None:
        self.set_nome(nome) 
        self.set_abitanti(abitanti)

    def nome(self) -> str:
        return self._nome 
    
    def codice(self) -> str:
        return self._codice 
    
    def set_nome(self, nome: str) -> None:
        self._nome = nome 

    def set_abitanti(self, abitanti: Abitanti) -> None:
        self._abitanti = abitanti 


class Nazione:
    _nome: str #noto alla nascita

    def __init__(self, nome: str):
        self.set_nome(nome)

    def set_nome(self, nome: str) -> None:
        if not isinstance(nome, str) or nome.strip() == "":
            raise ValueError("Errore. Nome non valido.")
        self._nome: str = nome 

    def get_nome(self) -> str:
        return self._nome 


class _partenza:

    class _link:
        _volo: Volo
        _aeroporto: Aeroporto

    def get_volo(self) -> Volo:
        return self._volo
    
    def get_aeroporto(self) -> Aeroporto:
        return self._aeroporto 
    
    def __init__(self, volo: Volo, aeroporto: Aeroporto) -> None:
        self._volo = volo 
        self._aeroporto = aeroporto

    def __hash__(self) -> int:
        return hash((self.get_volo(), self._aeroporto()))
    
    def __eq__(self, other: Any) -> bool:
        if type(self) != type(other) or hash(self) != hash(other):
            return False 
        return (self.get_volo(), self.get_aeroporto()) == (other.get_volo(), other.get_aeroporto())
    

class _arrivo:
    class _link:
        _volo: Volo
        _aeroporto: Aeroporto

    def get_volo(self) -> Volo:
        return self._volo
    
    def get_aeroporto(self) -> Aeroporto:
        return self._aeroporto 
    
    def __init__(self, volo: Volo, aeroporto: Aeroporto) -> None:
        self._volo = volo 
        self._aeroporto = aeroporto

    def __hash__(self) -> int:
        return hash(self.get_volo(), self._aeroporto())
    
    def __eq__(self, other: Any) -> bool:
        if type(self) != type(other) or hash(self) != hash(other):
            return False 
        return (self.get_volo(), self.get_aeroporto()) == (other.get_volo(), other.get_aeroporto())
    


class _volo_compagnia:
    class _link:
        _volo: Volo 
        _compagnia: CompagniaAerea

    def get_volo(self) -> Volo:
        return self._volo 
    
    def get_compagnia(self) -> CompagniaAerea:
        return self._compagnia
    
    def __init__(self, volo: Volo, compagnia: CompagniaAerea):
        self._volo = volo 
        self._compagnia = compagnia

    def __hash__(self) -> int:
        return hash(self.get_volo(), self._compagnia())
    
    def __eq__(self, other: Any) -> bool:
        if type(self) != type(other) or hash(self) != hash(other):
            return False 
        return (self.get_volo(), self.get_compagnia()) == (other.get_volo(), other.get_compagnia())