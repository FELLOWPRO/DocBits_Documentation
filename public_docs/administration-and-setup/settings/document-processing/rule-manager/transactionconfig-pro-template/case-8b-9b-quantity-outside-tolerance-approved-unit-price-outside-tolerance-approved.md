# Geval 8b, 9b: Hoeveelheid en eenheidsprijs buiten tolerantie, beide goedgekeurd

Het volgende scenario is een voorbeeld van een geconfigureerde mapping en geen aantoonbaar uitgerold standaardsjabloon. De werkelijke uitvoer, bedragen, tekens en documenttypen hangen af van de actieve `conflict_resolution`-regels en -expressies, de exportmapping en de goedkeuringsbesluiten. Elke hieronder beschreven debet- of creditnota is afhankelijk van die configuratie; het voorbeeld garandeert geen automatische uitgifte of wettelijke naleving.

## Scenario:

Zowel de hoeveelheid als de eenheidsprijs vallen buiten het tolerantiebereik, maar zijn goedgekeurd.

## Actie:

Het systeem verwerkt de transactie met behulp van de factuurwaarden voor zowel de hoeveelheid als de eenheidsprijs, waarbij eventuele noodzakelijke aanpassingen of regelkosten worden toegepast.

## Voorbeeld:

* **Purchase Order (PO):**
  * Quantity: 200 units
  * Unit Price: $25.00 per unit
  * Total Amount: $5,000.00
* **Invoice Received:**
  * Quantity: 220 units — 10% above the PO value, outside the configured ±5% tolerance; approved.
  * Unit Price: $27.00 per unit — 8% above the PO value, outside the configured ±2% tolerance; approved.
  * Total Amount: $5,940.00
* **Tolerance Levels:**
  * Quantity Tolerance: ±5%
  * Unit Price Tolerance: ±2%

Aangezien zowel de hoeveelheid (220 eenheden) als de eenheidsprijs ($27.00) buiten de aanvaardbare tolerantiegrenzen vallen, maar wel zijn goedgekeurd, zal het systeem:

1. **Accept the Approved Quantity:** Het systeem accepteert de gefactureerde hoeveelheid van 220 eenheden zoals deze is goedgekeurd, ondanks dat deze buiten het tolerantiebereik ligt.
2. **Accept the Approved Unit Price:** Het systeem accepteert de gefactureerde eenheidsprijs van $27.00 per eenheid zoals deze is goedgekeurd, ondanks dat deze buiten het tolerantiebereik ligt.
3. **Calculate the Total Amount:** Het systeem berekent het totaalbedrag op basis van de goedgekeurde factuurwaarden:
   * **Total Amount = Quantity × Unit Price**
   * **Total Amount = 220 units × $27.00 per unit = $5,940.00**
4. **Apply Necessary Adjustments or Line Charges:** Indien van toepassing kan het systeem eventuele extra regeltoeslagen of aanpassingen toepassen op basis van het beleid van de organisatie voor het verwerken van goedgekeurde afwijkingen.
5. **Process the Invoice:** Het systeem verwerkt de factuur met behulp van de goedgekeurde waarden voor zowel de hoeveelheid als de eenheidsprijs, en voltooit de transactie voor een totaalbedrag van $5,940.00.

Deze aanpak zorgt ervoor dat de transactie wordt verwerkt in overeenstemming met de goedgekeurde afwijkingen, waardoor flexibiliteit mogelijk is en tegelijkertijd nauwkeurige financiële gegevens worden bijgehouden.
