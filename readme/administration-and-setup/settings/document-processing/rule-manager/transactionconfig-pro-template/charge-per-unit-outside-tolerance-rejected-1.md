# Toeslag per eenheid buiten tolerantie (Afgewezen)

Het volgende scenario is een voorbeeld van een geconfigureerde mapping en geen aantoonbaar uitgerold standaardsjabloon. De werkelijke uitvoer, bedragen, tekens en documenttypen hangen af van de actieve `conflict_resolution`-regels en -expressies, de exportmapping en de goedkeuringsbesluiten. Elke hieronder beschreven debet- of creditnota is afhankelijk van die configuratie; het voorbeeld garandeert geen automatische uitgifte of wettelijke naleving.

## Scenario:

De toeslag per eenheid valt buiten de tolerantie en is niet goedgekeurd.

## Actie:

Het systeem past de kosten per eenheid aan zodat deze overeenkomen met de inkooporder of goedgekeurde niveaus, en genereert de benodigde debet- of creditnota's.

## Voorbeeld:

* **Purchase Order (PO):**
  * Kosten per eenheid: $6.00
  * Quantity: 800 units
  * Totaal kostenbedrag: $4,800.00
* **Invoice Received:**
  * Kosten per eenheid: $7.00 (buiten de tolerantie van 16.67%, afgewezen)
  * Quantity: 800 units
  * Totaal kostenbedrag: $5,600.00
* **Tolerance Levels:**
  * Tolerantie per eenheid: ±5%

Aangezien de kosten per eenheid ($7.00) het aanvaardbare tolerantiebereik van 5% overschrijden en niet zijn goedgekeurd, zal het systeem:

1. **De gefactureerde kosten per eenheid afwijzen:** Het systeem accepteert de gefactureerde kosten per eenheid van $7.00 niet omdat de afwijking de tolerantielimiet overschrijdt.
2. **De kosten per eenheid aanpassen:** Het systeem past de kosten per eenheid aan zodat deze overeenkomen met de inkooporder of de goedgekeurde kosten per eenheid:
   * Aangepaste kosten per eenheid = $6.00 (vanaf PO)
3. **Herbereken het totale kostenbedrag:** Het systeem herberekent het totale kostenbedrag op basis van de aangepaste kosten per eenheid:
   * **Gecorrigeerd totaalbedrag = Aantal × aangepaste kosten per eenheid**
   * **Gecorrigeerd totaalbedrag = 800 eenheden × $6.00 = $4,800.00**
4. **Een debetnota genereren:** Omdat het oorspronkelijke factuurtotaal hoger was dan het gecorrigeerde totaal, genereert het systeem een debetnota voor het te veel in rekening gebrachte bedrag:
   * **Bedrag debetnota = Totaal origineel factuur - Gecorrigeerd totaalbedrag**
   * **Bedrag debetnota = $5,600.00 - $4,800.00 = $800.00**
5. **De factuur verwerken:** Het systeem verwerkt de factuur met het gecorrigeerde totale bedrag van $4,800.00 en geeft een debetnota uit van $800.00 om het te veel in rekening gebrachte bedrag te verantwoorden.

Deze aanpak zorgt ervoor dat financiële transacties consistent zijn met de voorwaarden van de inkooporder, waarbij niet-goedgekeurde afwijkingen worden afgewezen en nauwkeurige factureringspraktijken worden gehandhaafd.
