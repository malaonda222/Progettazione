from custom_types import * 
from datetime import timedelta
from VoliAerei3 import *
from __future__ import annotations


class Volo:
    _codice: CodiceVolo 
    _durata_minuti: IntGZ
    _partenza: Aeroporto
    _arrivo: Aeroporto
    _volo_compagnia: CompagniaAerea

    def __init__(self, codice: str, durata_minuti: IntGZ, partenza: Aeroporto, arrivo: Aeroporto, volo_compagnia: CompagniaAerea) -> None:
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
    
    def get_partenza(self) -> Aeroporto:
        return self._partenza 
    
    def get_arrivo(self) -> Aeroporto:
        return self._arrivo 
    
    def get_volo_compagnia(self) -> CompagniaAerea:
        return self._volo_compagnia
   

class CompagniaAerea:
    _nome: str #noto alla nascita
    _anno_fondazione: Data1900 #<<imm>> noto alla nascita
    _comp_direzione_citta: Citta #noto alla nascita
    _voli_della_compagnia: set[Volo] #mutabile, non noto alla nascita

    def __init__(self, nome: str, anno_fondazione: Data1900, comp_direzione_citta: Citta) -> None:
        self.set_nome(nome)
        self._anno_fondazione = anno_fondazione
        self.set_comp_direzione_citta(comp_direzione_citta)
        self.set_voli_della_compagnia = set()

    def set_nome(self, nome: str) -> None:
        if not isinstance(nome, str) or nome.strip() == "":
            raise ValueError("Il nome deve essere una stringa senza spazi.")
        self._nome = nome

    def nome(self) -> str:
        return self._nome 
    
    def anno_fondazione(self) -> Data1900:
        return self._anno_fondazione
    
    def set_comp_direzione_citta(self, comp_direzione_citta: Citta) -> None:
        self._comp_direzione_citta = comp_direzione_citta

    def add_voli_della_compagnia(self, volo: Volo) -> None:
        self._voli_della_compagnia.add(volo)

    def remove_voli_della_compagnia(self, volo: Volo) -> None:
        if len(self._voli_della_compagnia) >= 1 and volo in self._voli_della_compagnia:
            self._voli_della_compagnia.remove(volo)
        else:
            raise ValueError(f"Il volo '{volo}' non è effettuato dalla compagnia aerea {self.nome}.")

    def comp_direzione_citta(self) -> Citta:
        return self._comp_direzione_citta
    
    def get_voli_della_compagnia(self) -> frozenset[Volo]:
        return frozenset(self._voli_della_compagnia)
    

class Aeroporto:
    _codice: CodiceAeroporto #<<imm>> noto alla nascita
    _nome: str #noto alla nascita
    _voli_partenza: set[Volo]
    _voli_arrivo: set[Volo]
    _aeroporto_citta: Citta

    def __init__(self, nome: str, codice: str, aeroporto_citta: Citta) -> None:
        self._codice = codice 
        self.set_nome(nome)
        self.voli_partenza = set()
        self.voli_arrivo = set()
        self.set_aeroporto_citta(aeroporto_citta)

    def set_nome(self, nome: str) -> None:
        if not isinstance(nome, str) or nome.strip() == "":
            raise ValueError("Il nome deve essere una stringa senza spazi.")
        self._nome = nome

    def add_voli_partenza(self, voli_partenza: Volo) -> None:
        self._voli_partenza.add(voli_partenza)

    def remove_voli_partenza(self, voli_partenza: Volo) -> None:
        if len(self._voli_partenza) >= 1 and voli_partenza in self.voli_partenza:
            self.voli_partenza.remove(voli_partenza)
        else:
            raise ValueError(f"Il volo '{voli_partenza}' non parte dall'aeroporto '{self._nome}'")
    
    def add_voli_arrivo(self, voli_arrivo: Volo) -> None:
        self._voli_arrivo.add(voli_arrivo)

    def remove_voli_arrivo(self, voli_arrivo: Volo) -> None:
        if len(self._voli_arrivo) >= 1 and voli_arrivo in self.voli_arrivo:
            self.voli_arrivo.remove(voli_arrivo)
        else:
            raise ValueError(f"Il volo '{voli_arrivo}' non arriva all'aeroporto '{self._nome}'")
    
    def set_aeroporto_citta(self, aeroporto_citta: Citta) -> None:
        self._aeroporto_citta = aeroporto_citta
       
    def nome(self) -> str:
        return self._nome 
    
    def codice(self) -> CodiceAeroporto:
        return self._codice 

    def get_voli_partenza(self) -> frozenset[Volo]:
        return frozenset(self._voli_partenza)

    def get_voli_arrivo(self) -> frozenset[Volo]:
        return frozenset(self._voli_arrivo)
    
    def get_aeroporto_citta(self) -> Citta:
        return self._aeroporto_citta
    

class Citta:
    _nome: str
    _abitanti: Abitanti 
    _aeroporto_citta: set[Aeroporto]
    _citta_nazione: Nazione

    def __init__(self, nome: str, abitanti: Abitanti, citta_nazione: Nazione) -> None:
        self.set_nome(nome) 
        self.set_abitanti(abitanti)
        self.set_aeroporto_citta = set()
        self.set_citta_nazione(citta_nazione)

    def nome(self) -> str:
        return self._nome 
    
    def codice(self) -> str:
        return self._codice 
    
    def set_nome(self, nome: str) -> None:
        if not isinstance(nome, str) or nome.strip() == "":
            raise ValueError("Il nome deve essere una stringa senza spazi.")
        self._nome = nome 

    def set_abitanti(self, abitanti: Abitanti) -> None:
        self._abitanti = abitanti 
    
    def add_aeroporto_citta(self, aeroporto_citta: Aeroporto) -> None:
        self._aeroporto_citta.add(aeroporto_citta)
    
    def remove_aeroporto_citta(self, aeroporto_citta: Aeroporto) -> None:
        if len(self._aeroporto_citta) >= 1 and aeroporto_citta in self._aeroporto_citta:
            self._aeroporto_citta.remove(aeroporto_citta)
        else:
            raise ValueError(f"L'aeroporto '{aeroporto_citta}' non si trova nella città di {self._nome}.")
    
    def get_aeroporto_citta(self) -> frozenset[Aeroporto]:
        return frozenset(self._aeroporto_citta)
    
    def set_citta_nazione(self, citta_nazione: Nazione) -> None:
        self._citta_nazione = citta_nazione
    
    def get_citta_nazione(self) -> Nazione:
        return self._citta_nazione


class Nazione:
    _nome: str #noto alla nascita
    _citta_nazione: set[Citta]

    def __init__(self, nome: str):
        self.set_nome(nome)
        self._citta_nazione = set()

    def set_nome(self, nome: str) -> None:
        if not isinstance(nome, str) or nome.strip() == "":
            raise ValueError("Il nome deve essere una stringa senza spazi.")
        self._nome: str = nome 
    
    def add_citta_nazione(self, c_nazione: Citta) -> None:
        self._citta_nazione.add(c_nazione)
    
    def remove_citta_nazione(self, c_nazione: Citta) -> None:
        if len(self._citta_nazione) >= 1 and c_nazione in self._citta_nazione:
            self._citta_nazione.remove(c_nazione)
        else:
            raise ValueError(f"La città '{c_nazione}' non si trova nella nazione {self._nome}")

    def get_nome(self) -> str:
        return self._nome 

    def get_citta_nazione(self) -> frozenset[Citta]:
        return frozenset(self._citta_nazione)