# Calcolo del bollo e dell'eventuale superbollo di un'auto in base
# - alla classe ambientale
# - alla potenza del motore
# - alla regione di apparteneza
# - all'età dell'auto

from functions.chiedi_classe_ambientale import chiedi_classe_ambientale
from functions.chiedi_potenza_motore import chiedi_potenza_motore
from functions.chiedi_regione import chiedi_regione
from functions.chiedi_eta_auto import chiedi_eta_auto
from functions.calcola import calcola

classe_ambientale = chiedi_classe_ambientale()
potenza_motore = chiedi_potenza_motore()
regione = chiedi_regione()
eta_auto = chiedi_eta_auto()

if classe_ambientale is not None and potenza_motore is not None and regione is not None and eta_auto is not None:
    if regione == "Lazio":
        print(f"\nclasse ambientale: Euro {classe_ambientale}\npotenza motore: {potenza_motore}kw\nregione: {regione}\netà auto: {eta_auto}")
        costo_bollo, costo_superbollo = calcola(classe_ambientale, potenza_motore, regione, eta_auto)
        if costo_superbollo:
            print(f"costo bollo: €{costo_bollo:.2f}\ncosto superbollo: €{costo_superbollo:.2f}\ncosto totale: €{costo_bollo + costo_superbollo:.2f}")
        else:
            print(f"costo bollo: €{costo_bollo:.2f}")
    else:
        print("siamo spiacenti, ma dobbiamo ancora acquisire i dati per questa regione")
