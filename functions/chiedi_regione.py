def chiedi_regione():
    contatore = 0
    while contatore < 3:
        try:
            regioni_italiane = [
                "Abruzzo",
                "Basilicata",
                "Calabria",
                "Campania",
                "Emilia-Romagna",
                "Friuli-Venezia Giulia",
                "Lazio",
                "Liguria",
                "Lombardia",
                "Marche",
                "Molise",
                "Piemonte",
                "Puglia",
                "Sardegna",
                "Sicilia",
                "Toscana",
                "Trentino-Alto Adige",
                "Umbria",
                "Valle d'Aosta",
                "Veneto"
            ]
            i = 1
            for regione in regioni_italiane:
                print(f"{i}. {regione}")
                i += 1
            regione = int(input("> inserisci il numero che corrisponde alla tua regione: "))
        except ValueError:
            print("> inserisci il numero della tua regione")
        else:
            if regione < 1 or regione > 20:
                print("> inserisci un numero compreso tra 1 e 20 per scegliere una regione")
            else:
                regione = regioni_italiane[regione - 1]
                return regione
        contatore += 1
    print("> errore: troppi tentativi falliti. impossibile definire la regione di appartenenza")
    return None