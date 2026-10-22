# Geval 11a: Hoeveelheidsoverschot afgewezen, eenheidsprijs binnen tolerantie

Het volgende scenario is een voorbeeld van een geconfigureerde mapping en geen aantoonbaar uitgerold standaardsjabloon. De werkelijke uitvoer, bedragen, tekens en documenttypen hangen af van de actieve `conflict_resolution`-regels en -expressies, de exportmapping en de goedkeuringsbesluiten. Elke hieronder beschreven debet- of creditnota is afhankelijk van die configuratie; het voorbeeld garandeert geen automatische uitgifte of wettelijke naleving.

## Scenario:

Het aantal op de factuur overschrijdt het aanvaardbare bereik (positief) en wordt afgewezen, maar de eenheidsprijs valt binnen de tolerantie.

## Actie:

Het systeem past de hoeveelheid aan tot het goedgekeurde niveau, handhaaft de eenheidsprijs en verwerkt de transactie. Elke overtollige hoeveelheid wordt afgewezen en niet gefactureerd.

## Voorbeeld:

* **Purchase Order (PO):**
  * Quantity: 100 units
  * Eenheidsprijs: $8.00 per eenheid
  * Total Amount: $800.00
* **Invoice Received:**
  * Aantal: 110 stuks (buiten tolerantie van 10%, afgekeurd)
  * Eenheidsprijs: $8.00 per eenheid (binnen tolerantie)
  * Total Amount: $880.00
* **Tolerance Levels:**
  * Quantity Tolerance: ±5%
  * Tolerantie per eenheidsprijs: ±2%

Aangezien de hoeveelheid (110 eenheden) de aanvaardbare tolerantielimiet overschrijdt (positieve variantie van 10%) en niet is goedgekeurd, maar de eenheidsprijs ($8.00) binnen de tolerantie valt, zal het systeem:

1. **De overtollige hoeveelheid afwijzen:** Het systeem wijst de hoeveelheid af die het goedgekeurde tolerantieniveau overschrijdt.
2. **De hoeveelheid aanpassen:** Het systeem past de hoeveelheid aan zodat deze overeenkomt met het goedgekeurde niveau dat is opgegeven in de inkooporder.
   * Goedgekeurde hoeveelheid = 100 eenheden (vanaf PO)
3. **Handhaaf de eenheidsprijs:** De eenheidsprijs van $8.00 per eenheid valt binnen de tolerantie en blijft ongewijzigd.
4. **Het totale bedrag opnieuw berekenen:** Het systeem berekent het totale bedrag met behulp van de goedgekeurde hoeveelheid en de geaccepteerde eenheidsprijs:
   * **Totaalbedrag = goedgekeurde hoeveelheid × eenheidsprijs**
   * **Totaalbedrag = 100 eenheden × $8.00 per eenheid = $800.00**
5. **De factuur verwerken:** Het systeem verwerkt de factuur met het aangepaste totaalbedrag van $800.00, waarbij alleen de goedgekeurde hoeveelheid en eenheidsprijs worden weergegeven. De overtollige hoeveelheid van 10 eenheden wordt afgewezen en niet gefactureerd.

Deze aanpak zorgt ervoor dat het gefactureerde bedrag in overeenstemming is met de overeengekomen voorwaarden in de inkooporder, zelfs wanneer de leverancier probeert een overtollige hoeveelheid te factureren.
