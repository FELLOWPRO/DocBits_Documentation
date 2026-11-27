# Geval 14: Koptoeslag - Toeslag per eenheid buiten tolerantie (Goedgekeurd)

Het volgende scenario is een voorbeeld van een geconfigureerde mapping en geen aantoonbaar uitgerold standaardsjabloon. De werkelijke uitvoer, bedragen, tekens en documenttypen hangen af van de actieve `conflict_resolution`-regels en -expressies, de exportmapping en de goedkeuringsbesluiten. Elke hieronder beschreven debet- of creditnota is afhankelijk van die configuratie; het voorbeeld garandeert geen automatische uitgifte of wettelijke naleving.

## Scenario:

De headertoeslag per eenheid valt buiten de tolerantie, maar is goedgekeurd.

## Actie:

Het systeem verwerkt de goedgekeurde kosten per eenheid en past deze toe op de transactie.

## Voorbeeld:

* **Purchase Order (PO):**
  * Header Charge Per Unit: $2.50
  * Quantity: 2,000 units
  * Total Header Charge Amount: $5,000.00
* **Invoice Received:**
  * Header Charge Per Unit: $3.00 — 20% above the PO value, outside the configured ±5% tolerance; approved.
  * Quantity: 2,000 units
  * Total Header Charge Amount: $6,000.00
* **Tolerance Levels:**
  * Header Charge Per Unit Tolerance: ±5%

Aangezien de headertoeslag per eenheid ($3.00) het aanvaardbare tolerantiebereik van 5% overschrijdt, maar is goedgekeurd, zal het systeem:

1. **Accept the Approved Header Charge Per Unit:** Het systeem accepteert het gefactureerde koptoeslag per eenheid van $3.00, aangezien dit is goedgekeurd ondanks het overschrijden van de tolerantielimiet.
2. **Process the Header Charge:** Het systeem verwerkt de factuur met behulp van de goedgekeurde toeslag per eenheid en de hoeveelheid:
   * **Total Header Charge Amount = Quantity × Approved Header Charge Per Unit**
   * **Total Header Charge Amount = 2,000 units × $3.00 = $6,000.00**
3. **Finalize the Invoice:** Het systeem verwerkt de transactie met de goedgekeurde kosten, die het totale bedrag van $6,000.00 weerspiegelen.

Dankzij deze aanpak kan het systeem rekening houden met goedgekeurde afwijkingen in de header-toeslagen, waardoor wordt gegarandeerd dat de transactie wordt verwerkt in overeenstemming met de goedkeuring, terwijl nauwkeurige financiële gegevens worden bijgehouden.
