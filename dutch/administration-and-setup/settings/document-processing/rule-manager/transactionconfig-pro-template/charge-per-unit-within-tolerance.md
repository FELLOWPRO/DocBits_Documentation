# Toeslag per eenheid binnen tolerantie

Het volgende scenario is een voorbeeld van een geconfigureerde mapping en geen aantoonbaar uitgerold standaardsjabloon. De werkelijke uitvoer, bedragen, tekens en documenttypen hangen af van de actieve `conflict_resolution`-regels en -expressies, de exportmapping en de goedkeuringsbesluiten. Elke hieronder beschreven debet- of creditnota is afhankelijk van die configuratie; het voorbeeld garandeert geen automatische uitgifte of wettelijke naleving.

## Scenario:

De kosten per eenheid op de factuur liggen binnen het aanvaardbare tolerantiebereik vergeleken met de inkooporder.

## Actie:

Het systeem accepteert de kosten per eenheid zoals gefactureerd en verwerkt de transactie zonder aanpassingen.

## Voorbeeld:

* **Purchase Order (PO):**
  * Kosten per eenheid: $5.00
  * Quantity: 500 units
  * Totaal kostenbedrag: $2,500.00
* **Invoice Received:**
  * Kosten per eenheid: $5.10 (binnen tolerantie van 2%)
  * Quantity: 500 units
  * Totaal kostenbedrag: $2,550.00
* **Tolerance Levels:**
  * Tolerantie per eenheid: ±3%

Aangezien de kosten per eenheid ($5.10) binnen het aanvaardbare tolerantiebereik van 3% vallen in vergelijking met de inkooporder, zal het systeem:

1. **Accepteer de kosten per eenheid:** Het systeem accepteert de gefactureerde kosten per eenheid van $5.10, aangezien deze binnen de gedefinieerde tolerantielimiet vallen.
2. **De transactie verwerken:** Het systeem verwerkt de factuur met het totale kostenbedrag op basis van de gefactureerde kosten per eenheid en hoeveelheid:
   * **Totaal bedrag aan kosten = Aantal × kosten per eenheid**
   * **Totaal bedrag = 500 eenheden × $5.10 = $2,550.00**
3. **De factuur voltooien:** Het systeem verwerkt de transactie zonder enige aanpassingen en accepteert de factuur zoals deze is.

Dankzij deze aanpak kan het systeem kleine aanvaardbare verschillen in kosten opvangen, waardoor een soepele en efficiënte verwerking van transacties wordt gegarandeerd zonder onnodige afwijzingen of vertragingen.
