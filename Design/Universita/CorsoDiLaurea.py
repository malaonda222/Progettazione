class CorsoDiLaurea:
    _codice: str
    _nome: str 

    def __init__(self, codice: str, nome: str):
        self.set_codice(codice)
        self.set_nome(nome)

    def set_codice(self, codice: str) -> None:
        self.codice = codice