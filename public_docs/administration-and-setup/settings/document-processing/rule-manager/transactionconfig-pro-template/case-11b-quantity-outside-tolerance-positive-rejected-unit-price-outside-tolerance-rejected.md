# Geval 11b: Hoeveelheidsoverschot en eenheidsprijs buiten tolerantie, beide afgewezen

Het volgende scenario is een voorbeeld van een geconfigureerde mapping en geen aantoonbaar uitgerold standaardsjabloon. De werkelijke uitvoer, bedragen, tekens en documenttypen hangen af van de actieve `conflict_resolution`-regels en -expressies, de exportmapping en de goedkeuringsbesluiten. Elke hieronder beschreven debet- of creditnota is afhankelijk van die configuratie; het voorbeeld garandeert geen automatische uitgifte of wettelijke naleving.

## Scenario:

De hoeveelheid overschrijdt het aanvaardbare bereik (positief) en wordt afgewezen, en de eenheidsprijs valt ook buiten de tolerantie en wordt afgewezen.

## Actie:

Het systeem past de hoeveelheid en de eenheidsprijs aan zodat deze overeenkomen met de goedgekeurde niveaus van de inkooporder, wijst eventuele excessen af en verwerkt de transactie.

## Voorbeeld:

* **Purchase Order (PO):**
  * Quantity: 200 units
  * Unit Price: $50.00 per unit
  * Total Amount: $10,000.00
* **Invoice Received:**
  * Quantity: 220 units — 10% above the PO value, outside the configured ±5% tolerance; rejected.
  * Unit Price: $55.00 per unit — 10% above the PO value, outside the configured ±2% tolerance; rejected.
  * Total Amount: $12,100.00
* **Tolerance Levels:**
  * Quantity Tolerance: ±5%
  * Unit Price Tolerance: ±2%

Aangezien zowel de hoeveelheid (220 eenheden) als de eenheidsprijs ($55.00) de aanvaardbare tolerantielimieten overschrijden en geen van beide is goedgekeurd, zal het systeem:

1. **Weiger de overtollige hoeveelheid:** Het systeem accepteert de gefactureerde hoeveelheid van 220 eenheden niet en past deze aan zodat deze overeenkomt met de oorspronkelijke inkooporder.
   * Adjusted Quantity = 200 units (from PO)
2. **De eenheidsprijs van de factuur afwijzen:** Het systeem accepteert de gefactureerde eenheidsprijs van $55.00 niet en past deze aan zodat deze overeenkomt met de oorspronkelijke inkooporder.
   * Adjusted Unit Price = $50.00 per unit (from PO)
3. **Herbereken het totaalbedrag:** Het systeem berekent het totaalbedrag met behulp van de aangepaste hoeveelheid en de eenheidsprijs:
   * **Corrected Total Amount = Adjusted Quantity × Adjusted Unit Price**
   * **Corrected Total Amount = 200 units × $50.00 per unit = $10,000.00**
4. **De factuur verwerken:** Het systeem verwerkt de factuur met het gecorrigeerde totaalbedrag van $10,000.00, waarbij de overtollige hoeveelheid en de hogere eenheidsprijs worden afgewezen.

Deze aanpak zorgt ervoor dat de transactie in lijn is met de oorspronkelijke voorwaarden van de inkooporder, waarbij consistente prijs- en hoeveelheidscontroles worden gehandhaafd en niet-goedgekeurde afwijkingen worden afgewezen.
