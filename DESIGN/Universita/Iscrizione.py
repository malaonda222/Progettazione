from Studente import *
from CorsoDiLaurea import *
from custom_types import *

class iscrizione:
    class _link:
        _studente: Studente 
        _corso_di_laurea: CorsoDiLaurea
        _data_iscrizione: datetime.date

    def __init__(self, studente: Studente, corso_laurea: CorsoDiLaurea, data_iscrizione: datetime.date):
        self._studente: Studente = studente 
        self._corso_laurea: CorsoDiLaurea = corso_laurea
        self._data_iscrizione: datetime.date = data_iscrizione

    def get_studente(self) -> Studente:
        return self._studente 
    
    def get_corso_laurea(self) -> CorsoDiLaurea:
        return self._corso_laurea
    
    def get_data_iscrizione(self) -> datetime.date:
        return self._data_iscrizione
    
    def __hash__(self) -> datetime.date:
        return hash( (self.get_studente(), self.get_corso_laurea()) )
    
    def __eq__(self, other: Any) -> bool:
        if type(self) != type(other) or hash(self) != hash(other):
            return False 
        return ( self.get_studente(), self.get_corso_laurea() ) == (other.get_studente(), other.get_corso_laurea() )
    
    