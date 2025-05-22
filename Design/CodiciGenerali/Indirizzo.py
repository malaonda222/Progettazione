import re 

class Indirizzo:
    # campi dati:
    # _via:str
    # _civico:...
    def __init__(self, via:str, civico:str):
        if via is None:
            raise ValueError(f"via cannot be None")
        if civico is None:
            raise ValueError(f"civ cannot be None")
       
        self._via:str = via


        if not re.search(r'^[0-9]+[a-zA-Z]*$', civico):
            raise ValueError(f"value for civico '{civico}' not allowed")
        self._civico:str = civico
   
    def via(self)->str:
        return self._via
    def civico(self)->str:
        return self._civico

    def __repr__(self)->str:
        return f"Indirizzo(via={self.via()}, civico={self.civico()})"


