from typing import Self

class IntGZ(int):
    #tipo di dato specializzato Intero > 0

    def __new__(cls, v: Self | int | float | str | bool) -> Self:
        value: int = super().__new__(cls, v)
        if value <= 0:
            raise ValueError(f"Il valore {v} deve essere più grande di 0")
        return value 
    

    

    # Attenzione: in generale la differenza tra interi non dovrebbe essere toccata
    def __sub__(self, other: int | str | float | bool | Self) -> Self:
        if self <= other:
            raise ValueError(f"La differenza tra {self} e {other} non è un IntGZ!")
        res: int = int(self) - int(other)
        return IntGZ(res)
    
        #opzione con try
        other_int: int = int(other)
        try: 
            res: int = int(self) - other_int
            return IntGZ(res) 
        except: 
             raise ValueError(f"La differenza tra {self} - {other} è negativo!")
    



n3: IntGZ = IntGZ(3)
print(type(n3))
print(n3 + 9)
print(n3 - 9)

n6 : IntGZ = IntGZ(6)
print(n6)
print(IntGZ(n6))