from abc import ABC, abstractmethod
from datetime import *

# classe utente 
class Utente(ABC):
    _username: str 
    _data_registrazione: date 

    def username(self) -> str:
        return self._username 
    
    def data_registrazione(self) -> date:
        return self._data_registrazione