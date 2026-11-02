# Geval 15: Koptoeslag - Toeslag per eenheid buiten tolerantie (Afgewezen)

Het volgende scenario is een voorbeeld van een geconfigureerde mapping en geen aantoonbaar uitgerold standaardsjabloon. De werkelijke uitvoer, bedragen, tekens en documenttypen hangen af van de actieve `conflict_resolution`-regels en -expressies, de exportmapping en de goedkeuringsbesluiten. Elke hieronder beschreven debet- of creditnota is afhankelijk van die configuratie; het voorbeeld garandeert geen automatische uitgifte of wettelijke naleving.

## Scenario:

De headertoeslag per eenheid valt buiten de tolerantie en is niet goedgekeurd.

## Actie:

Het systeem past de headertoeslag aan zodat deze overeenkomt met de inkooporder, verwerkt de transactie dienovereenkomstig en genereert de benodigde correctiedocumenten.

## Voorbeeld:

* **Purchase Order (PO):**
  * Headerkosten per eenheid: $4.00
  * Quantity: 1,500 units
  * Totaal bedrag aan headerkosten: $6,000.00
* **Invoice Received:**
  * Headerkosten per eenheid: $5.00 (buiten de tolerantie van 25%, afgewezen)
  * Quantity: 1,500 units
  * Totaal bedrag aan headerkosten: $7,500.00
* **Tolerance Levels:**
  * Tolerantie koptekst per eenheid: ±5%

Aangezien de headertoeslag per eenheid ($5.00) het aanvaardbare tolerantiebereik van 5% overschrijdt en niet is goedgekeurd, zal het systeem:

1. **Het gefactureerde koptoeslag per eenheid afwijzen:** Het systeem accepteert het gefactureerde koptoeslag per eenheid van $5.00 niet omdat de afwijking de tolerantielimiet overschrijdt.
2. **Pas de kopkosten per eenheid aan:** Het systeem past de kosten per eenheid aan zodat deze overeenkomen met de oorspronkelijke inkooporder of de goedgekeurde kosten per eenheid:
   * Aangepaste headerkosten per eenheid = $4.00 (vanaf PO)
3. **Het totale bedrag aan kopkosten opnieuw berekenen:** Het systeem herberekent het totale bedrag aan kosten op basis van de aangepaste kosten per eenheid:
   * **Gecorrigeerd totaalbedrag koptekst = Aantal × aangepast koptoeslag per eenheid**
   * **Gecorrigeerd totaalbedrag kopkosten = 1,500 eenheden × $4.00 = $6,000.00**
4. **Een creditnota genereren:** Omdat het oorspronkelijke factuurtotaal hoger was dan het gecorrigeerde totaal, genereert het systeem een creditnota voor het te veel in rekening gebrachte bedrag:
   * **Bedrag creditnota = Totaal origineel factuur - Gecorrigeerd totaal bedrag kopkosten**
   * **Bedrag creditnota = $7,500.00 - $6,000.00 = $1,500.00**
5. **De factuur verwerken:** Het systeem verwerkt de factuur met het gecorrigeerde totale bedrag van $6,000.00 en geeft een creditnota uit van $1,500.00 om het te veel in rekening gebrachte bedrag te verantwoorden.

Deze aanpak zorgt ervoor dat de transactie in overeenstemming is met de oorspronkelijke voorwaarden van de inkooporder, waardoor een nauwkeurige financiële verwerking wordt gehandhaafd en eventuele meerkosten worden gecorrigeerd.
