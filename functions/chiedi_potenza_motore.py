def chiedi_potenza_motore():
    contatore = 0
    while contatore < 3:
        try:
            potenza_motore = int(input("> inserisci la potenza del motore in cavalli: "))
        except ValueError:
            print("> inserisci un numero per la potenza del motore in cavalli")
        else:
            if potenza_motore < 1:
                print("> inserisci un numero > 0 per la potenza del motore in cavalli")
            else:
                potenza_motore = round(0.735499 * potenza_motore)
                return potenza_motore
        contatore += 1
    print("> errore: troppi tentativi falliti. impossibile ottenere la potenza del motore")
    return None