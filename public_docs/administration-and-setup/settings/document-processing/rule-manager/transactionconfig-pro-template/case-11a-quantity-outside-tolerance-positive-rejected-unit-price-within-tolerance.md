# Geval 11a: Hoeveelheidsoverschot afgewezen, eenheidsprijs binnen tolerantie

Het volgende scenario is een voorbeeld van een geconfigureerde mapping en geen aantoonbaar uitgerold standaardsjabloon. De werkelijke uitvoer, bedragen, tekens en documenttypen hangen af van de actieve `conflict_resolution`-regels en -expressies, de exportmapping en de goedkeuringsbesluiten. Elke hieronder beschreven debet- of creditnota is afhankelijk van die configuratie; het voorbeeld garandeert geen automatische uitgifte of wettelijke naleving.

## Scenario:

Het aantal op de factuur overschrijdt het aanvaardbare bereik (positief) en wordt afgewezen, maar de eenheidsprijs valt binnen de tolerantie.

## Actie:

Het systeem past de hoeveelheid aan tot het goedgekeurde niveau, handhaaft de eenheidsprijs en verwerkt de transactie. Elke overtollige hoeveelheid wordt afgewezen en niet gefactureerd.

## Voorbeeld:

* **Purchase Order (PO):**
  * Quantity: 100 units
  * Unit Price: $8.00 per unit
  * Total Amount: $800.00
* **Invoice Received:**
  * Quantity: 110 units — 10% above the PO value, outside the configured ±5% tolerance; rejected.
  * Unit Price: $8.00 per unit (within tolerance)
  * Total Amount: $880.00
* **Tolerance Levels:**
  * Quantity Tolerance: ±5%
  * Unit Price Tolerance: ±2%

Aangezien de hoeveelheid (110 eenheden) de aanvaardbare tolerantielimiet overschrijdt (positieve variantie van 10%) en niet is goedgekeurd, maar de eenheidsprijs ($8.00) binnen de tolerantie valt, zal het systeem:

1. **Reject the Excess Quantity:** Het systeem wijst de hoeveelheid af die het goedgekeurde tolerantieniveau overschrijdt.
2. **Adjust the Quantity:** Het systeem past de hoeveelheid aan zodat deze overeenkomt met het goedgekeurde niveau dat is opgegeven in de inkooporder.
   * Approved Quantity = 100 units (from PO)
3. **Maintain the Unit Price:** De eenheidsprijs van $8.00 per eenheid valt binnen de tolerantie en blijft ongewijzigd.
4. **Recalculate the Total Amount:** Het systeem berekent het totale bedrag met behulp van de goedgekeurde hoeveelheid en de geaccepteerde eenheidsprijs:
   * **Total Amount = Approved Quantity × Unit Price**
   * **Total Amount = 100 units × $8.00 per unit = $800.00**
5. **Process the Invoice:** Het systeem verwerkt de factuur met het aangepaste totaalbedrag van $800.00, waarbij alleen de goedgekeurde hoeveelheid en eenheidsprijs worden weergegeven. De overtollige hoeveelheid van 10 eenheden wordt afgewezen en niet gefactureerd.

Deze aanpak zorgt ervoor dat het gefactureerde bedrag in overeenstemming is met de overeengekomen voorwaarden in de inkooporder, zelfs wanneer de leverancier probeert een overtollige hoeveelheid te factureren.
