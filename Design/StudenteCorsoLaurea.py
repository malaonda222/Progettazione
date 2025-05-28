from __future__ import annotations
import beartype

"""
 ___________________                       ___________________
|                   |                     |                   |
|     Studente      |  0..* iscritto 1..1 |   CorsoDiLaurea   |
|___________________|<>------------------>|___________________|
| +nome:str <<imm>> |                     | +nome:str <<imm>> |
|___________________|                     |___________________|

"""


class CorsoDiLaurea:
	_nome:str # <<imm>>
	
	def nome(self)->str:
		return self._nome
	
	def __init__(self, nome:str)->None:
		self._nome = nome
	
	def __repr__(self)->str:
		return f"CorsoDiLaurea(nome={self._nome})"

class Studente:	
	_nome:str
	_iscritto:CorsoDiLaurea

	def nome(self)->str:
		return self._nome

	def iscritto(self)->CorsoDiLaurea:
		return self._iscritto

	def set_nome(self, nome:str)->None:
		self._nome = nome

	def set_iscritto(self, iscritto:CorsoDiLaurea)->None:
		self._iscritto = iscritto

	def __init__(self, *, nome:str, iscritto:CorsoDiLaurea)->None:
		self.set_nome(nome)
		self.set_iscritto(iscritto)

	def __repr__(self)->str:
		return f"Studente(nome={self._nome}, iscritto={self.iscritto()})"




if __name__ == '__main__':

	print("Creating instance c1 of class CorsoDiLaurea:", c1 := CorsoDiLaurea("Informatica"))
	print("Creating instance c2 of class CorsoDiLaurea:", c2 := CorsoDiLaurea("Fisica"))	

	print("Creating instance s1 of class Studente", s1 := Studente(nome='Alice', iscritto=c1))
	print("Changing iscritto for s1")
	s1.set_iscritto(c2)
	print("s1:", s1)
	
	try:
		print("Trying to remove iscritto for s1")
		s1.set_iscritto(None)
	except beartype.roar.BeartypeCallHintParamViolation as e:
		print(f"--> Expected {type(e)}: {e}")

	try:
		print("Trying to create instance s2 of class Studente with no iscritto")
		s2 = Studente(nome='Biagio', iscritto=None)
	except beartype.roar.BeartypeCallHintParamViolation as e:
		print(f"--> Expected {type(e)}: {e}")