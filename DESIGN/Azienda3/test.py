from custom_types import *
from datetime import date, timedelta
from Azienda3resp_doppia import *


vendite: Dipartimento = Dipartimento(nome="vendite", telefono=Telefono("5265496851"))
print(vendite.impiegati())
print()
print("Creo Alice in vendite")
alice: Impiegato = Impiegato("Alice", "Alberelli",
                             nascita=date.today() - timedelta(weeks=52*25),
                             stipendio=Importo(45000),
                             dipartimento_aff=vendite, data_afferenza=date.today())

lisa: Impiegato = Impiegato("Lisa", "Ban",
                             nascita=date.today() - timedelta(weeks=52*26),
                             stipendio=Importo(60000),
                             dipartimento_aff=vendite, data_afferenza=date.today())

marco: Impiegato = Impiegato("Marco", "Gini",
                             nascita=date.today() - timedelta(weeks=52*36),
                             stipendio=Importo(50000))

print(f"\tVendite: {[l.impiegato().cognome() for l in vendite.impiegati()]}\n")
print(f"\tVendite: {[l.impiegato().nome() for l in vendite.impiegati()]}\n")
marco.set_link_afferenza(vendite, date.today())
print(f"\tVendita; {[l.impiegato().nome() for l in vendite.impiegati()]}")

acquisti: Dipartimento = Dipartimento(nome="Acquisti", telefono=Telefono("1462549356"))
marketing: Dipartimento = Dipartimento(nome="Marketing", telefono=Telefono("1462549357"))
print(marketing.impiegati())

print("Creo Biagio senza dipartimento")
biagio: Impiegato = Impiegato("Biagio", "Bianchi",
                              nascita=date.today() - timedelta(weeks=52*65),
                              stipendio=Importo(45000))
print()
print("Creo Mario senza dipartimento")
mario: Impiegato = Impiegato("Mario", "Rosi",
                            nascita=date.today() - timedelta(weeks=52*40),
                            stipendio=Importo(35000))
print()
print("Aggiungo Biagio a Vendite")
biagio.set_link_afferenza(vendite, date.today())
print()
print("Aggiungo Mario a Marketing")
mario.set_link_afferenza(marketing, date.today())
print()
print(f"\tVendite: {[l.impiegato().nome() for l in vendite.impiegati()]}\n")
print(f"\tMarketing: {[l.impiegato().nome() for l in marketing.impiegati()]}\n")

print("Sposto Biagio in Acquisti\n")
biagio.set_link_afferenza(acquisti, date.today())
print("Sposto Alice in Marketing")
alice.set_link_afferenza(marketing, date.today())


print("Impiegati di ogni dipartimento:")
print(f"\tVendite: {[l.impiegato().nome() for l in vendite.impiegati()]}")
print(f"\tAcquisti: {[l.impiegato().nome() for l in acquisti.impiegati()]}")
print(f"\tMarketing: {[l.impiegato().nome() for l in marketing.impiegati()]}")

print()
print("Rimuovo Alice dal suo dipartimento\n")
alice.set_link_afferenza(None, None)

print("Rimuovo Lisa dal suo dipartimento\n")
lisa.set_link_afferenza(None, None)

print("Impiegati di ogni dipartimento:")
print(f"\tVendite: {[l.impiegato().nome() for l in vendite.impiegati()]}")
print(f"\tAcquisti: {[l.impiegato().nome() for l in acquisti.impiegati()]}")
print(f"\tMarketing: {[l.impiegato().nome() for l in marketing.impiegati()]}")