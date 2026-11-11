# Geval 7: hoeveelheid binnen tolerantie, eenheidsprijs buiten tolerantie (positieve afwijking afgewezen)

Het volgende scenario is een voorbeeld van een geconfigureerde mapping en geen aantoonbaar uitgerold standaardsjabloon. De werkelijke uitvoer, bedragen, tekens en documenttypen hangen af van de actieve regels en expressies voor `conflict_resolution`, de exportmapping en de goedkeuringsbesluiten. Elke hieronder beschreven debet- of creditnota is afhankelijk van die configuratie; het voorbeeld garandeert geen automatische uitgifte of wettelijke naleving.

## Scenario:

De hoeveelheid valt binnen de tolerantie, maar de eenheidsprijs overschrijdt het aanvaardbare bereik (positieve tolerantie) en wordt niet goedgekeurd.

## Actie:

Het systeem wijst de eenheidsprijs van de factuur af, past deze aan zodat deze overeenkomt met de inkooporder, en kan een debetnota genereren om het te veel gefactureerde bedrag te verwerken.

## Voorbeeld:

* **Purchase Order (PO):**
  * Quantity: 200 units
  * Unit Price: $15.00 per unit
  * Total Amount: $3,000.00
* **Invoice Received:**
  * Quantity: 198 units — 1% below the PO value, within the configured ±2% tolerance.
  * Unit Price: $17.00 per unit — 13.33% above the PO value, outside the configured ±1% tolerance; rejected.
  * Total Amount: $3,366.00
* **Tolerance Levels:**
  * Quantity Tolerance: ±2%
  * Unit Price Tolerance: ±1%

Omdat de hoeveelheid (198 eenheden) binnen het aanvaardbare tolerantiebereik valt, maar de eenheidsprijs ($17.00) de aanvaardbare tolerantie overschrijdt en niet is goedgekeurd, zal het systeem:

1. **De gefactureerde eenheidsprijs afwijzen:** Het systeem accepteert de gefactureerde eenheidsprijs van $17.00 niet.
2. **De eenheidsprijs aanpassen:** Het systeem past de eenheidsprijs aan zodat deze overeenkomt met de oorspronkelijke eenheidsprijs van de inkooporder.
   * Adjusted Unit Price = $15.00 (from PO)
3. **Het gecorrigeerde totaalbedrag berekenen:** Met de aangepaste eenheidsprijs berekent het systeem het totaalbedrag opnieuw.
   * **Corrected Total Amount = Quantity × Adjusted Unit Price**
   * **Corrected Total Amount = 198 units × $15.00 per unit = $2,970.00**
4. **Een debetnota genereren:** Het systeem genereert een debetnota om het verschil als gevolg van de te hoge facturering te verwerken.
   * **Debit Note Amount = Original Invoice Total - Corrected Total Amount**
   * **Debit Note Amount = $3,366.00 - $2,970.00 = $396.00**
   * Deze debetnota vertegenwoordigt het bedrag dat de leverancier te veel in rekening heeft gebracht.
5. **De factuur verwerken:** Het systeem verwerkt de factuur met het gecorrigeerde totaalbedrag van $2,970.00 en geeft een debetnota van $396.00 uit om de te hoge facturering te compenseren.

Deze aanpak zorgt ervoor dat eventuele te hoge facturering wordt gecorrigeerd, zodat de transactie aansluit bij de voorwaarden van de inkooporder en de financiële belangen van het bedrijf worden beschermd.
