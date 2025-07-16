import CodiceCompleto 

if __name__ == "__main__":
    asta1 = Asta("Asta")
    utente1 = UtentePrivato("Mario Rossi")
    bid1 = Bid(istante=datetime.now(), a=asta1, u=utente1)

    print("Bid creato con istante:", bid1.istante())
    print("Asta associata:", bid1.asta().nome)
    print("Utente associato:", bid1.utentePrivato().nome)

    # Prova errore su collegamento duplicato
    try:
        bid1.set_collegamento_asta(Asta("Asta nuova"))
    except ValueError as e:
        print("Errore atteso:", e)