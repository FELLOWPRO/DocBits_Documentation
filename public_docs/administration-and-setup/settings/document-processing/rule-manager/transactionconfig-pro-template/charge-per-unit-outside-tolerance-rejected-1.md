# Toeslag per eenheid buiten tolerantie (Afgewezen)

Het volgende scenario is een voorbeeld van een geconfigureerde mapping en geen aantoonbaar uitgerold standaardsjabloon. De werkelijke uitvoer, bedragen, tekens en documenttypen hangen af van de actieve `conflict_resolution`-regels en -expressies, de exportmapping en de goedkeuringsbesluiten. Elke hieronder beschreven debet- of creditnota is afhankelijk van die configuratie; het voorbeeld garandeert geen automatische uitgifte of wettelijke naleving.

## Scenario:

Charge Per Unit valt buiten de tolerantie en is niet goedgekeurd.

## Actie:

Het systeem past Charge Per Unit aan zodat deze overeenkomt met de inkooporder of goedgekeurde niveaus, en genereert de benodigde debet- of creditnota's.

## Voorbeeld:

* **Purchase Order (PO):**
  * Charge Per Unit: $6.00
  * Quantity: 800 units
  * Total Charge Amount: $4,800.00
* **Invoice Received:**
  * Charge Per Unit: $7.00 (afwijking 16.67%, buiten de tolerantie van ±5%, afgewezen)
  * Quantity: 800 units
  * Total Charge Amount: $5,600.00
* **Tolerance Levels:**
  * Charge Per Unit Tolerance: ±5%

Aangezien Charge Per Unit ($7.00) het aanvaardbare tolerantiebereik van 5% overschrijdt en niet is goedgekeurd, zal het systeem:

1. **Reject the Invoiced Charge Per Unit:** Het systeem accepteert de gefactureerde Charge Per Unit van $7.00 niet omdat de afwijking de tolerantielimiet overschrijdt.
2. **Adjust the Charge Per Unit:** Het systeem past Charge Per Unit aan zodat deze overeenkomt met de inkooporder of de goedgekeurde Charge Per Unit:
   * Adjusted Charge Per Unit = $6.00 (vanaf PO)
3. **Recalculate the Total Charge Amount:** Het systeem herberekent het Total Charge Amount op basis van de aangepaste Charge Per Unit:
   * **Corrected Total Charge Amount = Quantity × Adjusted Charge Per Unit**
   * **Corrected Total Charge Amount = 800 units × $6.00 = $4,800.00**
4. **Generate a Debit Note:** Omdat het oorspronkelijke factuurtotaal hoger was dan het gecorrigeerde totaal, genereert het systeem een debetnota voor het te veel in rekening gebrachte bedrag:
   * **Debit Note Amount = Original Invoice Total - Corrected Total Charge Amount**
   * **Debit Note Amount = $5,600.00 - $4,800.00 = $800.00**
5. **Process the Invoice:** Het systeem verwerkt de factuur met het gecorrigeerde Total Charge Amount van $4,800.00 en geeft een debetnota uit van $800.00 om het te veel in rekening gebrachte bedrag te verantwoorden.

Deze aanpak zorgt ervoor dat financiële transacties consistent zijn met de voorwaarden van de inkooporder, waarbij niet-goedgekeurde afwijkingen worden afgewezen en nauwkeurige factureringspraktijken worden gehandhaafd.
