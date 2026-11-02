# TransactionConfig Pro Template

## Verwerking van financiële documenten configureren

_TransactionConfig Pro Template_ beschrijft voorbeeldmappings voor facturen, debetnota’s en creditnota’s. Regelbeheer kan geconfigureerde `conflict_resolution`-regels en -expressies gebruiken om verwerkingsacties te bepalen. Deze documentatie toont niet aan dat een vooraf gedefinieerd sjabloon in uw omgeving is uitgerold.

Veldmappings, transactietypen en procesbesluiten moeten voor de betreffende Infor M3/LN-integratie worden geconfigureerd. De voorbeelden lichten die configuratie toe; ze garanderen geen juiste resultaten, integratie zonder aanpassingen of naleving van internationale financiële normen.

### Configuratiegebieden

* **Mapping:** Definieer bron- en doelvelden per transactietype en controleer de resulterende gegevens.
* **Aanpassing:** Configureer de regels voor het bedrijfsproces en de goedkeuringen.
* **Automatisering:** Automatiseer alleen besluiten die expliciet door actieve regels en expressies worden gedekt.
* **Integratie:** Controleer de exportmapping en de vereisten van het Infor M3/LN-doelsysteem.
* **Naleving:** Beoordeel boekhoudkundige en fiscale vereisten afzonderlijk; configuratie alleen garandeert geen wettelijke naleving.

## Voorbeelden van conflictoplossing

Het volgende scenario is een voorbeeld van een geconfigureerde mapping en geen aantoonbaar uitgerold standaardsjabloon. De werkelijke uitvoer, bedragen, tekens en documenttypen hangen af van de actieve `conflict_resolution`-regels en -expressies, de exportmapping en de goedkeuringsbesluiten. Elke hieronder beschreven debet- of creditnota is afhankelijk van die configuratie; het voorbeeld garandeert geen automatische uitgifte of wettelijke naleving.

### [Gevallen 1, 2, 3: Hoeveelheid en eenheidsprijs binnen tolerantie](case-1-2-3-quantity-and-unit-price-within-tolerance.md)

**Scenario:** De hoeveelheid en prijs op de factuur vallen binnen de geconfigureerde PO-toleranties.

**Voorbeeldactie:** De voorbeeldmapping accepteert de factuurwaarden en berekent hoeveelheid × eenheidsprijs.

### [Gevallen 4, 5: Hoeveelheid binnen, prijs buiten tolerantie (goedgekeurd)](case-4-5-quantity-within-tolerance-unit-price-outside-tolerance-approved.md)

**Scenario:** De hoeveelheid valt binnen de tolerantie; de prijsafwijking valt erbuiten en is goedgekeurd.

**Voorbeeldactie:** De voorbeeldmapping gebruikt de PO-prijs en boekt het goedgekeurde verschil als regelkosten als dit zo is geconfigureerd.

### [Geval 6: Hoeveelheid binnen tolerantie, prijs onder de grens (afgewezen)](case-6-quantity-within-tolerance-unit-price-outside-negative-tolerance-rejected.md)

**Scenario:** De hoeveelheid valt binnen de tolerantie; de prijs ligt onder het toegestane bereik en is afgewezen.

**Voorbeeldactie:** De voorbeeldmapping gebruikt de PO-prijs. Het verschil met teken is niet automatisch een creditnota; type en teken van de correctie hangen af van de mapping.

### [Geval 7: Hoeveelheid binnen tolerantie, prijs boven de grens (afgewezen)](case-7-quantity-within-tolerance-unit-price-outside-tolerance-positive-rejected.md)

**Scenario:** De hoeveelheid valt binnen de tolerantie; de positieve prijsafwijking is afgewezen.

**Voorbeeldactie:** De voorbeeldmapping gebruikt de PO-prijs. Een eventuele nota of correctie voor het verschil hangt af van de exportmapping.

### [Gevallen 8a, 9a: Hoeveelheid buiten tolerantie (goedgekeurd), prijs binnen](case-8a-9a-quantity-outside-tolerance-approved-unit-price-within-tolerance.md)

**Scenario:** De hoeveelheidafwijking is goedgekeurd en de prijs blijft binnen de tolerantie.

**Voorbeeldactie:** De voorbeeldmapping gebruikt de goedgekeurde factuurhoeveelheid en de gefactureerde eenheidsprijs.

### [Geval 11a: Hoeveelheid boven de grens (afgewezen), prijs binnen tolerantie](case-11a-quantity-outside-tolerance-positive-rejected-unit-price-within-tolerance.md)

**Scenario:** De hoeveelheid overschrijdt de tolerantie en is afgewezen; de prijs valt binnen de tolerantie.

**Voorbeeldactie:** De voorbeeldmapping gebruikt de goedgekeurde hoeveelheid en behoudt de prijs. De verwerking van het overschot hangt af van de geconfigureerde regels.

### [Geval 10a: Hoeveelheid onder de grens (afgewezen), prijs binnen tolerantie](case-10a-quantity-outside-tolerance-negative-rejected-unit-price-within-tolerance.md)

**Scenario:** De hoeveelheid ligt onder de tolerantie en is afgewezen; de prijs valt binnen de tolerantie.

**Voorbeeldactie:** De voorbeeldmapping gebruikt de goedgekeurde hoeveelheid en behoudt de eenheidsprijs.

### [Gevallen 8b, 9b: Hoeveelheid en prijs buiten tolerantie (goedgekeurd)](case-8b-9b-quantity-outside-tolerance-approved-unit-price-outside-tolerance-approved.md)

**Scenario:** Zowel de hoeveelheidafwijking als de prijsafwijking is goedgekeurd.

**Voorbeeldactie:** De voorbeeldmapping gebruikt goedgekeurde factuurwaarden en expliciet geconfigureerde regelkosten of correcties.

### [Geval 10b: Hoeveelheid onder de grens en prijs buiten tolerantie (afgewezen)](case-10b-quantity-outside-tolerance-negative-rejected-unit-price-outside-tolerance-rejected.md)

**Scenario:** De negatieve hoeveelheidafwijking en de prijsafwijking zijn niet goedgekeurd.

**Voorbeeldactie:** De voorbeeldmapping gebruikt PO-waarden of goedgekeurde waarden. Debet- of creditnota’s vereisen de bijbehorende mapping en het bijbehorende goedkeuringsbesluit.

### [Geval 11b: Hoeveelheid boven de grens en prijs buiten tolerantie (afgewezen)](case-11b-quantity-outside-tolerance-positive-rejected-unit-price-outside-tolerance-rejected.md)

**Scenario:** De positieve hoeveelheidafwijking en de prijsafwijking zijn afgewezen.

**Voorbeeldactie:** De voorbeeldmapping gebruikt goedgekeurde PO-waarden; de verwerking van overschotten hangt af van de actieve configuratie.

### [Gevallen 12, 13: Regelkosten per eenheid binnen tolerantie](charge-per-unit-within-tolerance.md)

**Scenario:** De regelkosten per eenheid vallen binnen de geconfigureerde PO-tolerantie.

**Voorbeeldactie:** De voorbeeldmapping accepteert de gefactureerde regelkosten zonder correctie.

### [Geval 14: Regelkosten per eenheid buiten tolerantie (goedgekeurd)](charge-per-unit-outside-tolerance-approved-1.md)

**Scenario:** De regelkosten per eenheid vallen buiten de tolerantie en zijn goedgekeurd.

**Voorbeeldactie:** De voorbeeldmapping past de goedgekeurde regelkosten toe.

### [Geval 15: Regelkosten per eenheid buiten tolerantie (afgewezen)](charge-per-unit-outside-tolerance-rejected.md)

**Scenario:** De regelkosten per eenheid vallen buiten de tolerantie en zijn afgewezen.

**Voorbeeldactie:** De voorbeeldmapping gebruikt de PO-regelkosten of goedgekeurde regelkosten. Een eventuele nota voor het verschil hangt af van de exportmapping.

### [Gevallen 12, 13: Kosten op kopniveau per eenheid binnen tolerantie](case-12-13-header-charge-charge-per-unit-within-tolerance.md)

**Scenario:** De kosten op kopniveau per eenheid vallen binnen de geconfigureerde PO-tolerantie.

**Voorbeeldactie:** De voorbeeldmapping past de gefactureerde kosten op kopniveau zonder correctie toe.

### [Geval 14: Kosten op kopniveau per eenheid buiten tolerantie (goedgekeurd)](charge-per-unit-outside-tolerance-approved.md)

**Scenario:** De kosten op kopniveau per eenheid vallen buiten de tolerantie en zijn goedgekeurd.

**Voorbeeldactie:** De voorbeeldmapping past de goedgekeurde kosten op kopniveau toe.

### [Geval 15: Kosten op kopniveau per eenheid buiten tolerantie (afgewezen)](case-15-header-charge-charge-per-unit-outside-tolerance-rejected.md)

**Scenario:** De kosten op kopniveau per eenheid vallen buiten de tolerantie en zijn afgewezen.

**Voorbeeldactie:** De voorbeeldmapping gebruikt PO-kosten op kopniveau of goedgekeurde waarden. Een eventuele afzonderlijke nota hangt af van de geconfigureerde verwerking.

### [Belastingregels](tax-lines.md "mention")

**Scenario:** De belastingbedragen op de factuur en PO verschillen.

**Voorbeeldactie:** De voorbeeldmapping gebruikt goedgekeurde belastingtarieven en bedragen. De configuratie moet aan de toepasselijke belastingvereisten worden getoetst; het voorbeeld garandeert geen wettelijke naleving.
