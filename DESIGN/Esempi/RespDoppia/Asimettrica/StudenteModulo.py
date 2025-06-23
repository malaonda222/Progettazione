from __future__ import annotations
from custom_types import *
import statistics 
  

class Modulo:
    _nome: str 
    _esami: dict[Studente, _esame._link]

    def __init__(self, nome: str) -> None:
        self._nome = nome 
        self._esami = dict()

    def nome(self) -> str:
        return self._nome 
    
    def add_link_esame(self, l: _esame._link) -> None:
        if l.modulo() is not self:
            raise ValueError("Link non mi riguarda")
        if l.studente() in self._esami:
            raise KeyError("Link duplicato")
        self._esami[l.studente()] = l

    def remove_link_esame(self, l: _esame._link) -> None:
        if l.modulo() is not self:
            raise ValueError("Il link non mi riguarda.")
        del self._esami[l.studente()]

    def __repr__(self) -> str:
        return f"Modulo(nome={self._nome})"    

    def esami(self) -> frozenset[_esame._link]:
        return frozenset(self._esame._link.values())
    

class Studente:
    _nome: str 
    _esami: dict[Modulo, _esame._link]

    def __init__(self, nome: str) -> None:
        self._nome = nome 
        self._esami = dict()
    
    def nome(self) -> str:
        return self._nome 
    
    def add_link_esame(self, m: Modulo, v: Voto) -> None:
        if m in self._esami:
            raise KeyError("Link duplicato.")
        l = _esame._link(self, m, v)
        self._esami[m] = l
        m._add_link_esame(l) #l'laltra classe non cambia

    def remove_link_esame(self, l: _esame._link) -> None:
        if l.studente() is not self:
            raise ValueError("Il link non mi riguarda.")
        del self._esami[l.modulo()]
        l.modulo()._remove_link_esame(l)
        del l 
    
    def esami(self) -> frozenset[_esame._link]:
        return frozenset(self._esami.values())
    
    def media(self) -> float|None:
        try:
            return statistics.mean(
                [float(l.voto()) for l in self.esami()]
            )
        except statistics.StatisticsError:
            return None
        
    def __repr__(self)-> str:
        result:str = f"Studente({self._nome}, esami=("
        esami = self.esami()
        if esami:
            for l in esami:
                result += f"\n                  - {str(l)}"
            result += "\n                "
    
        result += f"), media={self.media()}"
    
        if esami:
            result += "\n"
        
        result += ")"
        return result

class _esame:
    class _link:
        _studente: Studente
        _modulo: Modulo
        _voto: Voto
    
        def __init__(self, s: Studente, m: Modulo, v: Voto) -> None:
            self._studente = s
            self._modulo = m 
            self._voto = v 
        
        def studente(self) -> Studente:
            return self._studente
        
        def modulo(self) -> Modulo:
            return self._modulo 
        
        def voto(self) -> Voto:
            return self._voto 
        
        def __hash__(self) -> int:
            return hash((self.studente(), self.modulo()))
        
        def __eq__(self, other: Any) -> bool:
            if type(self) != type(other) or hash(self) != self(other):
                return False 
            return hash((self.studente(), self.modulo()) == (other.studente(). other.modulo()))
        
        def __repr__(self) -> str:
            return f"_esame._link(nome='{self.studente().nome()}', modulo='{self.modulo().nome()}', voto={self.voto()})"



if __name__ == '__main__':
	print("Creating studente s: ", s := Studente('Alice'))
	print("Creating modulo m1: ", m1 := Modulo('Python'))
	print("Creating modulo m2: ", m2 := Modulo('Java'))
	try:
		print("Creating modulo m3 with nome=None:", end=' ')
		print(m3 := Modulo(None))
	except RuntimeError as e:
		print(f"--> Expected {type(e)}:", e)

	print("Adding m1 to s")
	s.add_link_esame(m1, Voto(Voto(28) + (4 - 2)))

	print("Adding m2 to s")
	s.add_link_esame(m2, Voto(27))
	try:
		print("Adding m2 to s again")
		s.add_link_esame(m2, Voto(26))
	except KeyError as e:
		print(f"KeyError raised as expected: ", e)
	
	print("Studente s: ", s)