from __future__ import annotations
from typing import TYPE_CHECKING, Any, Self
from abc import ABC, abstractmethod
from py.custom_types.integers import IntGEZ, IntGET
from py.custom_types.floats import FloatGEZ, FloatGZ
from py.custom_types.enums import Condizioni

if TYPE_CHECKING:
    from py.classes.Index import Index
    from py.classes.Bid import Bid
    from py.classes.asta_bid import asta_bid

import datetime 


class OggettoDelPost(ABC):
    _descrizione: str #mutabile noto alla nascita
    _anni_garanzia: IntGEZ #mutabile noto alla nascita
    _pubblicazione: datetime #immutabile noto alla nascita
    _prezzo: FloatGZ 
    _is_nuovo: bool #immutabile noto alla nascita
    _condizioni: Condizioni | None#[0..1] possibilmente non noto alla nascita 
    _index: Index[int,Self] = Index[int,Self]('OggettoDelPost')
    

    @abstractmethod
    def __init__(self, *, descrizione: str, anni_garanzia: IntGEZ, prezzo: FloatGEZ, is_nuovo: bool, id: int, condizioni: Condizioni | None = None) -> None:
        self.set_descrizione(descrizione)
        self.set_anni_garanzia(anni_garanzia)
        self._pubblicazione = datetime.datetime.now()
        self.set_prezzo(prezzo)
        self.set_is_nuovo(is_nuovo) 
        if condizioni:
            self.set_condizione(condizioni)
        self._set_id()

    @classmethod 
    def all(cls):
        return cls._index.all()
    
    @classmethod
    def get(cls, key: Any) -> Self|None:
        return cls._index.get(key)
    
    def _set_id(self) -> None:
        key_list = list(self._index.all_keys())
        if len(key_list) > 0:
            last_id = max(key_list)
            id = last_id + 1 
        else:
            id = 0
        self._index.add(id, self)
        self._id = id
          
    def set_descrizione(self, descrizione: str) -> None:
        if not isinstance(descrizione, str):
            raise ValueError("Errore. La descrizione deve essere una stringa")
        self._descrizione = descrizione

    def set_anni_garanzia(self, anni_garanzia: IntGEZ) -> None:
        if self.is_nuovo():
            anni_garanzia = IntGE2(anni_garanzia)
        self._anni_garanzia = anni_garanzia

    def set_prezzo(self, prezzo: FloatGZ) -> None:
        self._prezzo = prezzo 

    def set_condizioni(self, condizioni: Condizioni) -> None:
        if self.is_nuovo():
            raise ValueError("Non si possono impostare le condzioni se l'oggetto è nuovo")
        self._condizoni = condizioni

    def descrizione(self) -> str:
        return self._descrizione
    
    def anni_garanzia(self) -> IntGEZ:
        return self._anni_garanzia
    
    def pubblicazione(self) -> datetime:
        return self._pubblicazione
    
    def prezzo(self) -> FloatGZ:
        return self._prezzo 
    
    def is_nuovo(self) -> bool:
        return self._is_nuovo 
    
    def condizioni(self) -> Condizioni:
        return self._condizione
    
    def id(self) -> int:
        return self._id 

    def __repr__(self):
        return f"OggettodelPost(descrizione={self.descrizione()}\n \
                anni_garanzia={self.anni_garanzia()}\n \
                pubblicazione={self.pubblicazione()}\n \
                prezzo={self.prezzo()}, is_nuovo={self.is_nuovo()}\n \
                condizioni={self.condizioni()}"
       

class Asta(OggettoDelPost):
    _scadenza: datetime #[0..1]
    _prezzo_rialzo: FloatGEZ #[0..1]
    _bids: dict[Bid, asta_bid._link] = {}

    def __init__(self, *, descrizione: str, anni_garanzia: IntGEZ, prezzo: FloatGZ, is_nuovo: bool, condizioni: Condizioni|None = None, scadenza: datetime, prezzo_rialzo: FloatGEZ) -> None:
        super().__init__(descrizione=descrizione, anni_garanzia=anni_garanzia, prezzo=prezzo, is_nuovo=is_nuovo, condizioni=condizioni)        
        self.set_prezzo_rialzo(prezzo_rialzo)
        self.set_scadenza(scadenza)


    def set_prezzo_rialzo(self, p: FloatGZ) -> None:
        #a evoluzione controllata
        self.__check_bids()
        self._prezzo_rialzo = p
    
    def set_scadenza(self, s: datetime) -> None:
        #a evoluzione controllata
        self.__check_bids()
        if self.scadenza() < self.pubblicazione():
            raise ValueError("Scadenza deve essere maggiore della pubblicazione!")
        self._scadenza = s 
    
    def set_descrizione(self, descrizione: str) -> None:
        self.__check_bids()
        super().set_descrizione(descrizione)

    def set_anni_garanzia(self, anni_garanzia: IntGEZ) -> None:
        self.__check_bids()
        super().set_anni_garanzia(anni_garanzia)
    
    def set_prezzo(self, prezzo: FloatGEZ) -> None:
        self.__check_bids()
        super().set_prezzo(prezzo)

    def set_is_nuovo(self, is_nuovo: bool) -> None:
        self.__check_bids()
        super().set_is_nuovo(is_nuovo)
    
    def set_condizioni(self, condizioni: Condizioni) -> None:
        self.__check_bids()
        super().set_condizioni(condizioni)

    def __check_bids(self) -> None:
        if self._bids:
            raise ValueError("L'asta non è modificabile dopo aver ricevuto un bid")
    
    def _add_asta_bid(self, l: asta_bid) -> None:
        if l.asta() is not self:
            raise ValueError("Il link non coinvolge questa asta")
        if l.bid() in self._bids:
            raise KeyError("Link duplicato")
        self._bids[l.bid()] = l 

    def scadenza(self) -> datetime:
        return self._scadenza
    
    def prezzo_rialzo(self) -> FloatGZ:
        return self._prezzo_rialzo
    
    def ultimo_bid(self, i: datetime) -> Bid | None:
        max_bid: Bid | None = None
        for l in self._bids.values():
            if l.bid().istante() <= i:
                if not max_bid:
                    max_bid = l.bid()
                else:
                    if l.bid().istante() > max_bid.istante():
                        max_bid = l.bid()
        return max_bid 

    def conclusa(self) -> bool:
        if self.scadenza() <= datetime.now():
            return True
        return False 
    
    def vincitore(self) -> UtentePrivato | None:
        if not self.conclusa():
            return None 
        return self.ultimo_bid(datetime.now()).bid_ut().utente_privato()
    
    def __repr__(self):
        return f"Asta(OggettoDelPost = {super().__repr__()},\nscadenza={self._scadenza}\nprezzo_rialzo={self._prezzo_rialzo}\nbids={self._bids})"



class CompraloSubito(OggettoDelPost):

    def __init__(self, *, descrizione: str, anni_garanzia: IntGEZ, anni_garanzia2: IntGE2| None = None, pubblicazione: datetime, condizione: Condizioni|None = None, prezzo: FloatGZ):
        super().__init__(descrizione=descrizione, anni_garanzia=anni_garanzia, anni_garanzia2=anni_garanzia2|None, pubblicazione=pubblicazione, condizione=condizione)

        if self.is_nuovo() and self.is_usato():
            raise ValueError("Un oggetto non può essere sia usato che nuovo")
    
    def set_prezzo(self, prezzo: FloatGZ):
        self._prezzo = prezzo 

    def prezzo(self) -> FloatGZ:
        return self._prezzo 



if __name__ == "__main__":
    from py.classes.Utente import UtentePrivato
    
    a = Asta(
        descrizione="Test",
        anni_garanzia=IntGEZ(1),
        prezzo=FloatGEZ(10.0),
        is_nuovo=True,
        scadenza=datetime.datetime.now(),
        prezzo_rialzo=FloatGEZ(2),
        condizioni=Condizioni("ottimo")
    )
    
    #print(a)
    
    a.add_bid(UtentePrivato("test_user"))
    
    #print("\nAfter adding a bid:")
    #print(a)
    
    print(a.ultimo_bid())
    
    print("Vincitore:", a.vincitore())