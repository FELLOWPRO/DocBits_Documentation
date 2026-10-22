# Belastingregels

Het volgende scenario is een voorbeeld van een geconfigureerde mapping en geen aantoonbaar uitgerold standaardsjabloon. De werkelijke uitvoer, bedragen, tekens en documenttypen hangen af van de actieve `conflict_resolution`-regels en -expressies, de exportmapping en de goedkeuringsbesluiten. Elke hieronder beschreven debet- of creditnota is afhankelijk van die configuratie; het voorbeeld garandeert geen automatische uitgifte of wettelijke naleving.

## Scenario:

Verwerkt verschillen in belastingbedragen tussen de factuur en de inkooporder.

## Actie:

Het systeem past de belastingregels aan op basis van de goedgekeurde belastingtarieven en -bedragen, waardoor naleving van de toepasselijke belastingregels wordt gegarandeerd.

## Voorbeeld:

* **Purchase Order (PO):**
  * Subtotal Amount: $10,000.00
  * Tax Rate: 8%
  * Verwacht belastingbedrag: $800.00
  * Totaalbedrag inclusief belasting: $10,800.00
* **Invoice Received:**
  * Subtotal Amount: $10,000.00
  * Belastingtarief: 10% (verschil)
  * Gefactureerd belastingbedrag: $1,000.00
  * Totaalbedrag inclusief belasting: $11,000.00

Omdat het belastingtarief op de factuur (10%) afwijkt van het verwachte belastingtarief (8%) en niet is goedgekeurd, zal het systeem:

1. **Het gefactureerde belastingtarief afwijzen:** Het systeem accepteert het belastingtarief van 10% niet omdat dit niet overeenkomt met het goedgekeurde tarief in de inkooporder.
2. **Het belastingtarief aanpassen:** Het systeem past het belastingtarief aan zodat het overeenkomt met het goedgekeurde tarief uit de inkooporder.
   * Aangepast belastingtarief = 8% (vanaf PO)
3. **Bereken het belastingbedrag opnieuw:** Het systeem berekent het belastingbedrag opnieuw op basis van het aangepaste belastingtarief:
   * **Gecorrigeerd belastingbedrag = Subtotaal × Aangepast belastingtarief**
   * **Gecorrigeerd belastingbedrag = $10,000.00 × 8% = $800.00**
4. **Herbereken het totaalbedrag:** Het systeem herberekent het totaalbedrag inclusief belasting:
   * **Gecorrigeerd totaalbedrag inclusief belasting = Subtotaal + Gecorrigeerd belastingbedrag**
   * **Gecorrigeerd totaalbedrag met belasting = $10,000.00 + $800.00 = $10,800.00**
5. **Een creditnota genereren:** Het systeem genereert een creditnota om de te veel in rekening gebrachte belasting te corrigeren:
   * **Bedrag creditnota = Oorspronkelijk belastingbedrag op factuur - Gecorrigeerd belastingbedrag**
   * **Bedrag creditnota = $1,000.00 - $800.00 = $200.00**
6. **De factuur verwerken:** Het systeem verwerkt de factuur met het gecorrigeerde belastingbedrag van $800.00 en het totale bedrag van $10,800.00, en geeft een creditnota uit voor het belastingverschil van $200.00.

Deze aanpak zorgt ervoor dat de factuurbelasting consistent is met de inkooporder en voldoet aan de toepasselijke belastingregels, waardoor te hoge betalingen worden voorkomen en de nauwkeurigheid van de financiële administratie wordt gewaarborgd.
