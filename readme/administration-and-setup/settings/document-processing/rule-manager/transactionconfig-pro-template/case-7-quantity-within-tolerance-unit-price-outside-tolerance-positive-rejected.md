# Geval 7: Hoeveelheid binnen tolerantie, prijsoverschrijding afgewezen

Het volgende scenario is een voorbeeld van een geconfigureerde mapping en geen aantoonbaar uitgerold standaardsjabloon. De werkelijke uitvoer, bedragen, tekens en documenttypen hangen af van de actieve `conflict_resolution`-regels en -expressies, de exportmapping en de goedkeuringsbesluiten. Elke hieronder beschreven debet- of creditnota is afhankelijk van die configuratie; het voorbeeld garandeert geen automatische uitgifte of wettelijke naleving.

## Scenario:

De hoeveelheid valt binnen de tolerantie, maar de eenheidsprijs overschrijdt het aanvaardbare bereik (positieve tolerantie) en wordt niet goedgekeurd.

## Actie:

Het systeem wijst de eenheidsprijs van de factuur af, past deze aan zodat deze overeenkomt met de inkooporder en kan een debetnota genereren om het te veel in rekening gebrachte bedrag te verantwoorden.

## Voorbeeld:

* **Purchase Order (PO):**
  * Quantity: 200 units
  * Eenheidsprijs: $15.00 per eenheid
  * Total Amount: $3,000.00
* **Invoice Received:**
  * Hoeveelheid: 198 eenheden (binnen tolerantie van 1%)
  * Eenheidsprijs: $17.00 per eenheid (buiten de positieve tolerantie van 13.33%)
  * Total Amount: $3,366.00
* **Tolerance Levels:**
  * Quantity Tolerance: ±2%
  * Tolerantie per eenheidsprijs: ±1%

Aangezien de hoeveelheid (198 eenheden) binnen het aanvaardbare tolerantiebereik valt, maar de eenheidsprijs ($17.00) de aanvaardbare tolerantie overschrijdt en niet is goedgekeurd, zal het systeem:

1. **De eenheidsprijs van de factuur afwijzen:** Het systeem accepteert de gefactureerde eenheidsprijs van $17.00 niet.
2. **De eenheidsprijs aanpassen:** Het systeem past de eenheidsprijs aan zodat deze overeenkomt met de oorspronkelijke eenheidsprijs van de inkooporder.
   * Aangepaste eenheidsprijs = $15.00 (vanaf PO)
3. **Bereken het gecorrigeerde totaalbedrag:** Met behulp van de aangepaste eenheidsprijs berekent het systeem het totaalbedrag opnieuw.
   * **Gecorrigeerd totaalbedrag = Aantal × aangepaste eenheidsprijs**
   * **Gecorrigeerd totaalbedrag = 198 eenheden × $15.00 per eenheid = $2,970.00**
4. **Genereer een debetnota:** Het systeem genereert een debetnota om rekening te houden met het verschil als gevolg van de meerkosten.
   * **Bedrag debetnota = Totaal origineel factuur - Gecorrigeerd totaalbedrag**
   * **Bedrag debetnota = $3,366.00 - $2,970.00 = $396.00**
   * Deze debetnota vertegenwoordigt het door de leverancier teveel in rekening gebrachte bedrag.
5. **De factuur verwerken:** Het systeem verwerkt de factuur met het gecorrigeerde totaalbedrag van $2,970.00 en geeft een debetnota uit van $396.00 om de meerkosten te compenseren.

Deze aanpak zorgt ervoor dat eventuele te hoge kosten worden gecorrigeerd, waardoor de transactie wordt afgestemd op de voorwaarden van de inkooporder en de financiële belangen van het bedrijf worden beschermd.
