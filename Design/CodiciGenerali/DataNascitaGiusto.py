from typing import Self 
from datetime import date 

class DataGE1895(date):

    def __new__(cls, year: int, month: int, day: int) -> Self: #self perché deve costruire un nuovo oggetto della classe 

        if year < 1895:
            raise ValueError(f"La data {day}/{month}/{year} deve essere successiva all'1 gennaio 1895.")

        return super().__new__(cls, year=year, month=month, day=day)
    


    