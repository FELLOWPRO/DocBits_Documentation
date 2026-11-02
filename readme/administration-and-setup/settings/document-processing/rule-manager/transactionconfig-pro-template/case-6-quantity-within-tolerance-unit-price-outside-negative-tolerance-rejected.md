# Geval 6: Hoeveelheid binnen tolerantie, prijs onder de grens (afgewezen)

Het volgende scenario is een voorbeeld van een geconfigureerde mapping en geen aantoonbaar uitgerold standaardsjabloon. De werkelijke uitvoer, bedragen, tekens en documenttypen hangen af van de actieve `conflict_resolution`-regels en -expressies, de exportmapping en de goedkeuringsbesluiten. Elke hieronder beschreven debet- of creditnota is afhankelijk van die configuratie; het voorbeeld garandeert geen automatische uitgifte of wettelijke naleving.

## Scenario

De hoeveelheid ligt binnen de tolerantie, maar de gefactureerde eenheidsprijs ligt onder het toegestane bereik en de prijsafwijking is niet goedgekeurd.

## Voorbeeldactie

Een mapping die na afwijzing de PO-prijs gebruikt, zou de hoeveelheid behouden en de gefactureerde eenheidsprijs vervangen door de PO-prijs. Of het verschil leidt tot een correctie, debetnota, creditnota of geen afzonderlijk document, hangt af van de actieve mapping en goedkeuringsbesluiten. Extra kosten op kopniveau gelden alleen als deze expliciet zijn geconfigureerd.

## Voorbeeld

* **Inkooporder (PO):**
  * Hoeveelheid: 100 eenheden
  * Eenheidsprijs: $10.00 per eenheid
  * Totaal: $1,000.00
* **Ontvangen factuur:**
  * Hoeveelheid: 100 eenheden — werkelijke afwijking 0%, binnen de geconfigureerde tolerantie van ±2%.
  * Eenheidsprijs: $9.00 — werkelijke prijsafwijking -10%, buiten de geconfigureerde tolerantie van ±1%; afgewezen.
  * Totaal: $900.00
* **Geconfigureerde toleranties:**
  * Hoeveelheid: ±2%
  * Eenheidsprijs: ±1%

Voor deze voorbeeldmapping:

1. Wijs de gefactureerde eenheidsprijs van $9.00 af, omdat de afwijking buiten de tolerantie valt en niet is goedgekeurd.
2. Gebruik de PO-eenheidsprijs van $10.00.
3. Bereken het voorbeeldtotaal opnieuw: **100 eenheden × $10.00 = $1,000.00**.
4. Bereken het verschil met teken als factuurtotaal min herberekend totaal: **$900.00 - $1,000.00 = -$100.00**.
5. Pas de geconfigureerde exportmapping en het goedkeuringsbesluit toe. De waarde -$100.00 is een verschil met teken en geen onvoorwaardelijke opdracht om een creditnota uit te geven. De mapping bepaalt bedrag, teken en documenttype van een eventuele correctie.

Dit voorbeeld betekent niet dat een creditnota automatisch een te laag gefactureerd bedrag herstelt. Controleer vóór gebruik van de regel de gewenste boekhoudkundige verwerking in de actieve exportmapping.
