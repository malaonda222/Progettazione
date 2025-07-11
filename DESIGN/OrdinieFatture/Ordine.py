from custom_types import *
import datetime 
from DipartimentoAziendale import DipartimentoAziendale
from Fornitore import Fornitore

class Ordine:
    _data_stipula: datetime.date 
    _descrizione_bene: str 
    _importo_imponibile: FloatGEZ
    _aliquota_iva: FloatGEZ #[0..1]
    _stato_ordine: StatoOrdine
    _dipartimento_ordine: DipartimentoAziendale
    _forn_ordine: Fornitore

    def __init__(self, data_stipula: datetime.date, descrizione_bene: str, importo_imponibile: FloatGEZ, aliquota_iva: FloatGEZ | None, stato_ordine: StatoOrdine, dipartimento_ordine: DipartimentoAziendale, forn_ordine: Fornitore):
        self.set_data_stipula(data_stipula)
        self.set_descrizione_bene(descrizione_bene)
        self.set_importo_imponibile(importo_imponibile)
        self.set_aliquota_iva(aliquota_iva)
        self.set_stato_ordine(stato_ordine)
        self.set_dipartimento_ordine(dipartimento_ordine)
        self.set_forn_ordine(forn_ordine)

    def set_data_stipula(self, data_stipula: datetime.date) -> None:
        self._data_stipula = data_stipula

    def set_descrizione_bene(self, descrizione_bene: str) -> None:
        self._descrizione_bene = descrizione_bene

    def set_importo_imponibile(self, importo_imponibile: FloatGEZ) -> None:
        self._importo_imponibile = importo_imponibile

    def set_aliquota_iva(self, aliquota_iva: FloatGEZ | None) -> None:
        if aliquota_iva is not None:
            self._aliquota_iva = aliquota_iva

    def set_stato_ordine(self, stato_ordine: StatoOrdine) -> None:
        self._stato_ordine = stato_ordine
    
    def set_dipartimento_ordine(self, dipartimento_ordine: DipartimentoAziendale) -> None:
        self._dipartimento_ordine = dipartimento_ordine

    def set_forn_ordine(self, forn_ordine: Fornitore) -> None:
        self._forn_ordine = forn_ordine

    def get_data_stipula(self) -> datetime.date:
        return self._data_stipula
    
    def get_descrizione_bene(self) -> str:
        return self._descrizione_bene
    
    def get_importo_imponibile(self) -> FloatGEZ:
        return self._importo_imponibile
    
    def get_aliquota_iva(self) -> FloatGEZ | None:
        return self._aliquota_iva 

    def get_stato_ordine(self) -> StatoOrdine:
        return self._stato_ordine
    
    def get_dipartimento_ordine(self) -> DipartimentoAziendale:
        return self._dipartimento_ordine
    
    def get_forn_ordine(self) -> Fornitore:
        return self._forn_ordine 
    
    
