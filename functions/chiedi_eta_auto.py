def chiedi_eta_auto():
    contatore = 0
    while contatore < 3:
        try:
            eta_auto = int(input("> inserisci l'età dell'auto': "))
        except ValueError:
            print("> inserisci un numero >= 0 per l'età della tua auto")
        else:
            if eta_auto < 0:
                print("> inserisci un numero >= 0 per l'età della tua auto")
            else:
                return eta_auto
        contatore += 1
    print("> errore: troppi tentativi falliti. impossibile determinare l'età della tua auto")
    return None