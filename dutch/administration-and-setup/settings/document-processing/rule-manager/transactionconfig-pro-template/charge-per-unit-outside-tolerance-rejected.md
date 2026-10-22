# Geval 15: Regelkosten per eenheid buiten tolerantie (afgewezen)

Het volgende scenario is een voorbeeld van een geconfigureerde mapping en geen aantoonbaar uitgerold standaardsjabloon. De werkelijke uitvoer, bedragen, tekens en documenttypen hangen af van de actieve `conflict_resolution`-regels en -expressies, de exportmapping en de goedkeuringsbesluiten. Elke hieronder beschreven debet- of creditnota is afhankelijk van die configuratie; het voorbeeld garandeert geen automatische uitgifte of wettelijke naleving.

## Scenario

De kosten per eenheid op een kostenregel vallen buiten de tolerantie en de afwijking is niet goedgekeurd. Dit geval betreft regelkosten, geen kosten op kopniveau.

## Voorbeeldactie

Een mapping die na afwijzing de PO-kosten gebruikt, zou de gefactureerde kosten per eenheid vervangen door de PO-waarde. Elke afzonderlijke correctie, debetnota of creditnota hangt af van de exportmapping en goedkeuringsbesluiten.

## Voorbeeld

* **Inkooporder (PO):**
  * Regelkosten per eenheid: $4.00
  * Hoeveelheid: 1,500 eenheden
  * Totale regelkosten: $6,000.00
* **Ontvangen factuur:**
  * Regelkosten per eenheid: $5.00 — 25% boven de PO-waarde, buiten de geconfigureerde tolerantie van ±5%; afgewezen.
  * Hoeveelheid: 1,500 eenheden
  * Totale regelkosten: $7,500.00
* **Geconfigureerde tolerantie:** Kosten per eenheid ±5%.

Voor deze voorbeeldmapping:

1. Wijs de gefactureerde kosten van $5.00 per eenheid af, omdat de afwijking van 25% de tolerantie van ±5% overschrijdt en niet is goedgekeurd.
2. Gebruik de PO-kosten van $4.00 per eenheid.
3. Bereken de totale regelkosten opnieuw: **1,500 eenheden × $4.00 = $6,000.00**.
4. Bereken het te veel gefactureerde bedrag: **$7,500.00 - $6,000.00 = $1,500.00**.
5. Pas de geconfigureerde verwerking van het verschil toe. Een creditnota van $1,500.00 is een mogelijke uitkomst van de mapping en geen gegarandeerde systeemactie. Bedrag, teken, documenttype en uitgifte hangen af van de actieve regels, exportmapping en goedkeuringen.

Valideer de mapping voor regelkosten en de resulterende boekhoudkundige documenten voordat u dit scenario in productie gebruikt.
