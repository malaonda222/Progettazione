from typing import Type, Self

def build_int_ge_v(n: int) -> Type:
    class IntGZV(int):
        def __new__(cls, v: Self | int | float | str | bool) -> Self:
            value: int = super().__new__(cls, v)
            if value <= n:
                raise ValueError(f"Il valore {v} deve essere più grande di {n}")
            return value 

        
    return IntGZV 
