# Geval 10a: Hoeveelheidstekort afgewezen, eenheidsprijs binnen tolerantie

Het volgende scenario is een voorbeeld van een geconfigureerde mapping en geen aantoonbaar uitgerold standaardsjabloon. De werkelijke uitvoer, bedragen, tekens en documenttypen hangen af van de actieve `conflict_resolution`-regels en -expressies, de exportmapping en de goedkeuringsbesluiten. Elke hieronder beschreven debet- of creditnota is afhankelijk van die configuratie; het voorbeeld garandeert geen automatische uitgifte of wettelijke naleving.

## Scenario:

De hoeveelheid ligt onder het acceptabele bereik (negatieve tolerantie) en is niet goedgekeurd, hoewel de eenheidsprijs binnen de tolerantie valt.

## Actie:

Het systeem past de hoeveelheid aan zodat deze overeenkomt met het goedgekeurde niveau, waardoor de eenheidsprijs consistent blijft. De transactie wordt dienovereenkomstig verwerkt.

## Voorbeeld:

* **Purchase Order (PO):**
  * Quantity: 150 units
  * Unit Price: $20.00 per unit
  * Total Amount: $3,000.00
* **Invoice Received:**
  * Quantity: 140 units — 6.67% below the PO value, outside the configured ±5% tolerance; rejected.
  * Unit Price: $20.00 per unit (within tolerance)
  * Total Amount: $2,800.00
* **Tolerance Levels:**
  * Quantity Tolerance: ±5%
  * Unit Price Tolerance: ±2%

Aangezien de hoeveelheid (140 eenheden) onder de aanvaardbare tolerantielimiet ligt (negatieve variantie van -6.67%) en niet is goedgekeurd, maar de eenheidsprijs ($20.00) binnen de tolerantie valt, zal het systeem:

1. **Reject the Lower Quantity:** Het systeem accepteert de lagere hoeveelheid niet, omdat deze buiten het goedgekeurde tolerantiebereik ligt.
2. **Adjust the Quantity:** Het systeem past de hoeveelheid aan zodat deze overeenkomt met het goedgekeurde niveau dat is opgegeven in de inkooporder.
   * Approved Quantity = 150 units (from PO)
3. **Maintain the Unit Price:** De eenheidsprijs van $20.00 per eenheid valt binnen de tolerantie en blijft ongewijzigd.
4. **Recalculate the Total Amount:** Het systeem berekent het totale bedrag met behulp van de goedgekeurde hoeveelheid en de geaccepteerde eenheidsprijs:
   * **Total Amount = Approved Quantity × Unit Price**
   * **Total Amount = 150 units × $20.00 per unit = $3,000.00**
5. **Process the Invoice:** Het systeem verwerkt de factuur met het aangepaste totaalbedrag van $3,000.00, wat de goedgekeurde hoeveelheid en eenheidsprijs weergeeft. Van de leverancier wordt verwacht dat hij de volledige goedgekeurde hoeveelheid factureert.

Deze aanpak zorgt ervoor dat de financiële transactie in overeenstemming is met de voorwaarden van de inkooporder en voorkomt onderfacturering terwijl de financiële gegevens nauwkeurig worden bijgehouden.
