# Geval 12, 13: Koptoeslag - Toeslag per eenheid binnen tolerantie

Het volgende scenario is een voorbeeld van een geconfigureerde mapping en geen aantoonbaar uitgerold standaardsjabloon. De werkelijke uitvoer, bedragen, tekens en documenttypen hangen af van de actieve `conflict_resolution`-regels en -expressies, de exportmapping en de goedkeuringsbesluiten. Elke hieronder beschreven debet- of creditnota is afhankelijk van die configuratie; het voorbeeld garandeert geen automatische uitgifte of wettelijke naleving.

## Scenario:

De headertoeslag per eenheid ligt binnen het aanvaardbare tolerantiebereik vergeleken met de inkooporder.

## Actie:

Het systeem verwerkt de kopheffing zoals gefactureerd en past deze zonder aanpassingen toe.

## Voorbeeld:

* **Purchase Order (PO):**
  * Header Charge Per Unit: $3.50
  * Quantity: 1,200 units
  * Total Header Charge Amount: $4,200.00
* **Invoice Received:**
  * Header Charge Per Unit: $3.55 — 1.43% above the PO value, within the configured ±2% tolerance.
  * Quantity: 1,200 units
  * Total Header Charge Amount: $4,260.00
* **Tolerance Levels:**
  * Header Charge Per Unit Tolerance: ±2%

Omdat de headerkosten per eenheid ($3.55) binnen het aanvaardbare tolerantiebereik van 2% vallen in vergelijking met de inkooporder, zal het systeem:

1. **Accept the Header Charge Per Unit:** Het systeem accepteert het gefactureerde koptoeslag per eenheid van $3.55, aangezien dit binnen de gedefinieerde tolerantielimiet valt.
2. **Process the Header Charge:** Het systeem verwerkt de factuur met het totale bedrag aan kopkosten, gebaseerd op de gefactureerde kosten per eenheid en hoeveelheid:
   * **Total Header Charge Amount = Quantity × Header Charge Per Unit**
   * **Total Header Charge Amount = 1,200 units × $3.55 = $4,260.00**
3. **Finalize the Invoice:** Het systeem verwerkt de transactie zonder enige aanpassingen en accepteert de factuur zoals deze is.

Deze aanpak zorgt voor een soepele en efficiënte verwerking van transacties wanneer de headerkosten binnen het aanvaardbare tolerantiebereik vallen, waardoor onnodige afwijzingen of vertragingen worden vermeden.
