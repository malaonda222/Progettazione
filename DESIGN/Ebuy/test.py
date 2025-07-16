from CodiceCompleto import *

if __name__ == "__main__":
    from datetime import datetime, date
    from customtypes import IntGEZ, IntGE2, FloatGZ, Condizioni, Url

    # Dummy types
    IntGEZ = int
    IntGE2 = int
    FloatGZ = float
    Condizioni = str  # es: 'buono', 'ottimo', etc.
    Url = str

    try:
        # Creazione di un oggetto Asta (nuovo)
        asta = Asta(
            descrizione="Laptop da gaming",
            anni_garanzia=2,
            anni_garanzia2=1,  # rende l'oggetto "nuovo"
            pubblicazione=datetime.now(),
            prezzo=999.99,
            condizione=None,
            prezzo_rialzo=10.0,
            scadenza=date(2025, 12, 31)
        )

        # Creazione utente privato
        utente = UtentePrivato(
            username="mario_rossi",
            data_registrazione=datetime(2023, 6, 1)
        )

        # Creazione di un Bid
        bid = Bid(
            istante=datetime.now(),
            a=asta,
            u=utente
        )

        print(f"Asta: {asta.descrizione()}, prezzo: {asta.prezzo()}, scadenza: {asta.scadenza()}")
        print(f"Utente: {utente.username()}, Bid registrato: {bid.istante()}")
        print("Bids registrati nell'asta:", len(asta.bids()))
        print("Bids registrati nell'utente:", len(utente.bids()))

        # Prova a reinserire lo stesso Bid (deve fallire con KeyError)
        try:
            asta._add_link(asta_bid._link(bid, asta))
        except KeyError as e:
            print("Atteso errore di duplicazione bid:", e)

    except Exception as e:
        print("Errore durante il test:", e)