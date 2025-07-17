from CodiceCompleto import *

if __name__ == "__main__":
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

        asta1 = Asta(
            descrizione="Telefono Nokia",
            anni_garanzia=IntGEZ(0),
            prezzo=FloatGZ(10.0),
            pubblicazione= datetime.now(),
            condizione=Condizioni("buono"),
            prezzo_rialzo=FloatGZ(1.0),
            scadenza=datetime.now().date() + timedelta(days=7)
        )



        utente = UtentePrivato(
            username="mario_rossi",
            data_registrazione=datetime(2023, 6, 1)
        )

        utente1 = UtentePrivato(
            username="luigi_bianchi",
            data_registrazione=datetime(2023, 11, 7)
        )

        
        bid = Bid(
            istante=datetime.now(),
            a=asta,
            u=utente
        )

        print("BID REGISTRATO:")
        print(f"Asta: {asta.descrizione()}, prezzo: {asta.prezzo()}, scadenza: {asta.scadenza()}")
        print(f"Utente: {utente.username()}, Bid registrato: {bid.istante()}")
        print("Bids registrati nell'asta:", len(asta.bids()))
        print("Bids registrati nell'utente:", len(utente.bids()))


        print("BID REGISTATO:")
        print(f"Asta: {asta1.descrizione()}, prezzo: {asta1.prezzo()}, scadenza: {asta1.scadenza()}")
        print(f"Utente: {utente1.username()}, Bid registrato: {bid.istante()}")
        print(f"Bids registrati nell'asta: {len(asta1.bids())}")
        print(f"Bids registrati nell'utente: {len(utente1.bids())}")
        # Prova a reinserire lo stesso Bid (deve fallire con KeyError)
        try:
            asta._add_link(asta_bid._link(bid, asta))
        except KeyError as e:
            print("Atteso errore di duplicazione bid:", e)

        

    except Exception as e:
        print("Errore durante il test:", e)