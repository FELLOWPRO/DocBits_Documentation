# Toeslag per eenheid binnen tolerantie

Het volgende scenario is een voorbeeld van een geconfigureerde mapping en geen aantoonbaar uitgerold standaardsjabloon. De werkelijke uitvoer, bedragen, tekens en documenttypen hangen af van de actieve `conflict_resolution`-regels en -expressies, de exportmapping en de goedkeuringsbesluiten. Elke hieronder beschreven debet- of creditnota is afhankelijk van die configuratie; het voorbeeld garandeert geen automatische uitgifte of wettelijke naleving.

## Scenario:

Charge Per Unit op de factuur ligt binnen het aanvaardbare tolerantiebereik vergeleken met de inkooporder.

## Actie:

Het systeem accepteert Charge Per Unit zoals gefactureerd en verwerkt de transactie zonder aanpassingen.

## Voorbeeld:

* **Purchase Order (PO):**
  * Charge Per Unit: $5.00
  * Quantity: 500 units
  * Total Charge Amount: $2,500.00
* **Invoice Received:**
  * Charge Per Unit: $5.10 (afwijking 2%, binnen de tolerantie van ±3%)
  * Quantity: 500 units
  * Total Charge Amount: $2,550.00
* **Tolerance Levels:**
  * Charge Per Unit Tolerance: ±3%

Aangezien Charge Per Unit ($5.10) binnen het aanvaardbare tolerantiebereik van 3% valt in vergelijking met de inkooporder, zal het systeem:

1. **Accept the Charge Per Unit:** Het systeem accepteert de gefactureerde Charge Per Unit van $5.10, aangezien deze binnen de gedefinieerde tolerantielimiet valt.
2. **Process the Transaction:** Het systeem verwerkt de factuur met het Total Charge Amount op basis van de gefactureerde Charge Per Unit en Quantity:
   * **Total Charge Amount = Quantity × Charge Per Unit**
   * **Total Charge Amount = 500 units × $5.10 = $2,550.00**
3. **Finalize the Invoice:** Het systeem verwerkt de transactie zonder enige aanpassingen en accepteert de factuur zoals deze is.

Dankzij deze aanpak kan het systeem kleine aanvaardbare verschillen in kosten opvangen, waardoor een soepele en efficiënte verwerking van transacties wordt gegarandeerd zonder onnodige afwijzingen of vertragingen.
