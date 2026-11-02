# Geval 12, 13: Koptoeslag - Toeslag per eenheid binnen tolerantie

Het volgende scenario is een voorbeeld van een geconfigureerde mapping en geen aantoonbaar uitgerold standaardsjabloon. De werkelijke uitvoer, bedragen, tekens en documenttypen hangen af van de actieve `conflict_resolution`-regels en -expressies, de exportmapping en de goedkeuringsbesluiten. Elke hieronder beschreven debet- of creditnota is afhankelijk van die configuratie; het voorbeeld garandeert geen automatische uitgifte of wettelijke naleving.

## Scenario:

De headertoeslag per eenheid ligt binnen het aanvaardbare tolerantiebereik vergeleken met de inkooporder.

## Actie:

Het systeem verwerkt de kopheffing zoals gefactureerd en past deze zonder aanpassingen toe.

## Voorbeeld:

* **Purchase Order (PO):**
  * Headerkosten per eenheid: $3.50
  * Quantity: 1,200 units
  * Totaal bedrag aan headerkosten: $4,200.00
* **Invoice Received:**
  * Headerkosten per eenheid: $3.55 (binnen tolerantie van 1.43%)
  * Quantity: 1,200 units
  * Totaal bedrag aan headerkosten: $4,260.00
* **Tolerance Levels:**
  * Tolerantie koptekst per eenheid: ±2%

Omdat de headerkosten per eenheid ($3.55) binnen het aanvaardbare tolerantiebereik van 2% vallen in vergelijking met de inkooporder, zal het systeem:

1. **Accepteer het koptoeslag per eenheid:** Het systeem accepteert het gefactureerde koptoeslag per eenheid van $3.55, aangezien dit binnen de gedefinieerde tolerantielimiet valt.
2. **Verwerk de kopkosten:** Het systeem verwerkt de factuur met het totale bedrag aan kopkosten, gebaseerd op de gefactureerde kosten per eenheid en hoeveelheid:
   * **Totaal bedrag kopkosten = Aantal × kopkosten per eenheid**
   * **Totaal bedrag kopkosten = 1,200 eenheden × $3.55 = $4,260.00**
3. **De factuur voltooien:** Het systeem verwerkt de transactie zonder enige aanpassingen en accepteert de factuur zoals deze is.

Deze aanpak zorgt voor een soepele en efficiënte verwerking van transacties wanneer de headerkosten binnen het aanvaardbare tolerantiebereik vallen, waardoor onnodige afwijzingen of vertragingen worden vermeden.
