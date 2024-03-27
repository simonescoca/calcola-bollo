def chiedi_classe_ambientale():
    contatore = 0
    while contatore < 3:
        try:
            classe_ambientale = int(input("> inserisci la classe ambientale: Euro "))
        except ValueError:
            print("> inserisci un numero compreso tra 0 e 6 per la classe ambientale")
        else:
            if classe_ambientale < 0 or classe_ambientale > 6:
                print("> inserisci un numero compreso tra 0 e 6 per la classe ambientale")
            else:
                return classe_ambientale
        contatore += 1
    print("> errore: troppi tentativi falliti. impossibile ottenere la classe ambientale")
    return None