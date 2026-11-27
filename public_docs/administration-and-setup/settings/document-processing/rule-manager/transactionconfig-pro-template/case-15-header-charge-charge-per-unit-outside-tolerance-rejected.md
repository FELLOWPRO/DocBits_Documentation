# Geval 15: Koptoeslag - Toeslag per eenheid buiten tolerantie (Afgewezen)

Het volgende scenario is een voorbeeld van een geconfigureerde mapping en geen aantoonbaar uitgerold standaardsjabloon. De werkelijke uitvoer, bedragen, tekens en documenttypen hangen af van de actieve `conflict_resolution`-regels en -expressies, de exportmapping en de goedkeuringsbesluiten. Elke hieronder beschreven debet- of creditnota is afhankelijk van die configuratie; het voorbeeld garandeert geen automatische uitgifte of wettelijke naleving.

## Scenario:

De headertoeslag per eenheid valt buiten de tolerantie en is niet goedgekeurd.

## Actie:

Het systeem past de headertoeslag aan zodat deze overeenkomt met de inkooporder, verwerkt de transactie dienovereenkomstig en genereert de benodigde correctiedocumenten.

## Voorbeeld:

* **Purchase Order (PO):**
  * Header Charge Per Unit: $4.00
  * Quantity: 1,500 units
  * Total Header Charge Amount: $6,000.00
* **Invoice Received:**
  * Header Charge Per Unit: $5.00 — 25% above the PO value, outside the configured ±5% tolerance; rejected.
  * Quantity: 1,500 units
  * Total Header Charge Amount: $7,500.00
* **Tolerance Levels:**
  * Header Charge Per Unit Tolerance: ±5%

Aangezien de headertoeslag per eenheid ($5.00) het aanvaardbare tolerantiebereik van 5% overschrijdt en niet is goedgekeurd, zal het systeem:

1. **Het gefactureerde koptoeslag per eenheid afwijzen:** Het systeem accepteert het gefactureerde koptoeslag per eenheid van $5.00 niet omdat de afwijking de tolerantielimiet overschrijdt.
2. **Pas de kopkosten per eenheid aan:** Het systeem past de kosten per eenheid aan zodat deze overeenkomen met de oorspronkelijke inkooporder of de goedgekeurde kosten per eenheid:
   * Adjusted Header Charge Per Unit = $4.00 (from PO)
3. **Het totale bedrag aan kopkosten opnieuw berekenen:** Het systeem herberekent het totale bedrag aan kosten op basis van de aangepaste kosten per eenheid:
   * **Corrected Total Header Charge Amount = Quantity × Adjusted Header Charge Per Unit**
   * **Corrected Total Header Charge Amount = 1,500 units × $4.00 = $6,000.00**
4. **Een creditnota genereren:** Omdat het oorspronkelijke factuurtotaal hoger was dan het gecorrigeerde totaal, genereert het systeem een creditnota voor het te veel in rekening gebrachte bedrag:
   * **Credit Note Amount = Original Invoice Total - Corrected Total Header Charge Amount**
   * **Credit Note Amount = $7,500.00 - $6,000.00 = $1,500.00**
5. **De factuur verwerken:** Het systeem verwerkt de factuur met het gecorrigeerde totale bedrag van $6,000.00 en geeft een creditnota uit van $1,500.00 om het te veel in rekening gebrachte bedrag te verantwoorden.

Deze aanpak zorgt ervoor dat de transactie in overeenstemming is met de oorspronkelijke voorwaarden van de inkooporder, waardoor een nauwkeurige financiële verwerking wordt gehandhaafd en eventuele meerkosten worden gecorrigeerd.
