# Geval 14: Toeslagregel - Toeslag per eenheid buiten tolerantie (Goedgekeurd)

Het volgende scenario is een voorbeeld van een geconfigureerde mapping en geen aantoonbaar uitgerold standaardsjabloon. De werkelijke uitvoer, bedragen, tekens en documenttypen hangen af van de actieve `conflict_resolution`-regels en -expressies, de exportmapping en de goedkeuringsbesluiten. Elke hieronder beschreven debet- of creditnota is afhankelijk van die configuratie; het voorbeeld garandeert geen automatische uitgifte of wettelijke naleving.

## Scenario:

De toeslag per eenheid valt buiten de tolerantie, maar is goedgekeurd.

## Actie:

Het systeem accepteert de kosten per eenheid en past de goedgekeurde kosten toe, waarbij de transactie dienovereenkomstig wordt verwerkt.

## Voorbeeld:

* **Purchase Order (PO):**
  * Kosten per eenheid: $4.50
  * Quantity: 1,000 units
  * Totaal kostenbedrag: $4,500.00
* **Invoice Received:**
  * Kosten per eenheid: $5.00 (buiten de tolerantie van 11.11%, goedgekeurd)
  * Quantity: 1,000 units
  * Totaal kostenbedrag: $5,000.00
* **Tolerance Levels:**
  * Tolerantie per eenheid: ±5%

Aangezien de kosten per eenheid ($5.00) buiten het aanvaardbare tolerantiebereik van 5% vallen, maar wel zijn goedgekeurd, zal het systeem:

1. **Accepteer de goedgekeurde kosten per eenheid:** Het systeem accepteert de gefactureerde kosten per eenheid van $5.00, aangezien deze zijn goedgekeurd ondanks het overschrijden van de tolerantielimiet.
2. **De transactie verwerken:** Het systeem verwerkt de factuur met behulp van de goedgekeurde kosten per eenheid en de hoeveelheid:
   * **Totaal bedrag aan kosten = Aantal × goedgekeurde kosten per eenheid**
   * **Totaal bedrag van de kosten = 1,000 eenheden × $5.00 = $5,000.00**
3. **De factuur afronden:** Het systeem verwerkt de transactie met de goedgekeurde kosten, die het totale bedrag van $5,000.00 weerspiegelen.

Deze aanpak zorgt ervoor dat het systeem goedgekeurde afwijkingen in de kosten kan opvangen, waardoor flexibiliteit mogelijk is en tegelijkertijd nauwkeurige financiële gegevens worden bijgehouden.
