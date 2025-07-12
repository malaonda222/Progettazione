from abc import ABC, abstractmethod
from datetime import *
from typing import *
from customtypes import *
from Utente import *
from Ebuy.OggettodelPost import *
from Bid import *


class asta_bid:
    _asta: Asta 
    _bid: Bid 

    def __init__(self, asta: Asta, bid: Bid) -> None:
        self._asta = asta 
        self._bid = bid 

    def create_asta_bid(l: _asta_bid) -> link:
        l

        