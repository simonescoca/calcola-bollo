def calcola(classe_ambientale, potenza_motore, regione, eta_auto):
    if regione == "Lazio":
        if classe_ambientale == 0:
            fino_a_cento_kw = 3.30
            oltre_cento_kw = 4.95
        elif classe_ambientale == 1:
            fino_a_cento_kw = 3.19
            oltre_cento_kw = 4.79
        elif classe_ambientale == 2:
            fino_a_cento_kw = 3.08
            oltre_cento_kw = 4.62
        elif classe_ambientale == 3:
            fino_a_cento_kw = 2.97
            oltre_cento_kw = 4.46
        elif classe_ambientale >= 4:
            fino_a_cento_kw = 2.84
            oltre_cento_kw = 4.26

    if potenza_motore <= 100:
        costo_bollo = fino_a_cento_kw * potenza_motore
    else:
        costo_bollo = fino_a_cento_kw * 100 + oltre_cento_kw * (potenza_motore - 100)

    if potenza_motore > 185:
        costo_superbollo = 20 * (potenza_motore - 185)
    else:
        costo_superbollo = 0

    if eta_auto >= 10:
        costo_superbollo *= 0.6
    elif eta_auto >= 15:
        costo_superbollo *= 0.4
    elif eta_auto >= 20:
        costo_superbollo = 0

    return costo_bollo, costo_superbollo