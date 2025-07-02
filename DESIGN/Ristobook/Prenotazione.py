from __future__ import annotations
from datetime import date
from custom_types import *

class Prenotazione:
    _istante_creazione: date 
    _numero_commensali: IntGZ 
    _data_ora_prenotata: date 
    _is_rifiutata: bool 
    _is_accettata: bool 
    _istante_accettazione: date | None 
    _istante_rifiuto: date | None
    
    def __init__(self, *, istante_creazione: date, numero_commensali: IntGZ, data_ora_prenotata: date, istante_accettazione: date | None, istante_rifiuto: date| None) -> None:
    
        self._istante_creazione = istante_creazione
        self._numero_commensali = numero_commensali
        self._data_ora_prenotata = data_ora_prenotata
        
        self._istante_accettazione = None 
        self._istante_rifiuto = None
        self._is_accettata = False 
        self._is_rifiutata = False
    
        if istante_accettazione is not None:
            self._istante_accettazione = istante_accettazione 
            self._is_accettata = True 
        
        if istante_rifiuto is not None:
            self._istante_rifiuto = istante_rifiuto 
            self._is_rifiutata = True 
            
        if not (self.is_accettata() or self.is_rifiutata()):
            raise ValueError("Ogni prenotazione deve essere accettata o rifiutata.")
        
    def istante_creazione(self) -> date:
        return self._istante_creazione
    
    def numero_commensali(self) -> IntGZ:
        return self._numero_commensali
    
    def is_accettata(self) -> bool:
        return self._is_accettata
    
    def is_rifiutata(self) -> bool:
        return self._is_rifiutata
    
    def istante_accettazione(self) -> date | None:
        return self._istante_accettazione
    
    def istante_rifiuto(self) -> date | None:
        return self._istante_rifiuto
        