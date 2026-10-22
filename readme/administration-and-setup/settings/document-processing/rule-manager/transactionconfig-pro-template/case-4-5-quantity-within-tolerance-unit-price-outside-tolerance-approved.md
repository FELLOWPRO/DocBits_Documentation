# Geval 4, 5: Hoeveelheid binnen tolerantie, Eenheidsprijs buiten tolerantie (Goedgekeurd)

Het volgende scenario is een voorbeeld van een geconfigureerde mapping en geen aantoonbaar uitgerold standaardsjabloon. De werkelijke uitvoer, bedragen, tekens en documenttypen hangen af van de actieve `conflict_resolution`-regels en -expressies, de exportmapping en de goedkeuringsbesluiten. Elke hieronder beschreven debet- of creditnota is afhankelijk van die configuratie; het voorbeeld garandeert geen automatische uitgifte of wettelijke naleving.

## Scenario:

Het aantal op de factuur valt binnen de tolerantie, maar de eenheidsprijs ligt buiten het aanvaardbare tolerantiebereik. Dit verschil in de eenheidsprijs is echter beoordeeld en goedgekeurd door de bevoegde autoriteiten.

## Actie:

Het systeem past de eenheidsprijs aan zodat deze overeenkomt met de inkooporder en past eventuele noodzakelijke regelkosten toe om het verschil te compenseren.

## Voorbeeld:

**Purchase Order (PO):**

Quantity: <mark style="color:green;">100</mark> units

Eenheidsprijs: $10.00 per eenheid

Total Amount: <mark style="color:purple;">$1,000.00</mark>

**Invoice Received:**

Aantal: <mark style="color:green;">100</mark> eenheden (binnen tolerantie)

Eenheidsprijs: <mark style="color:red;">$11.00</mark> per eenheid (buiten tolerantie van ±5%)

Total Amount: <mark style="color:red;">$1,100.00</mark>

**Tolerance Levels:**

Quantity Tolerance: ±2%

Tolerantie per eenheidsprijs: ±5% (verwacht bereik: $9.50 tot $10.50)

**Approval:**

• De eenheidsprijs van $11.00 valt buiten het tolerantiebereik, maar is handmatig goedgekeurd door de betreffende afdeling.

Aangezien de hoeveelheid binnen de tolerantie valt, maar de eenheidsprijs buiten de tolerantie valt (toch goedgekeurd), zal het systeem:

1\. **Pas de eenheidsprijs aan**: Het systeem past de eenheidsprijs terug aan de eenheidsprijs van PO aan, omdat de afwijking is goedgekeurd:

• **Aangepaste eenheidsprijs = $10.00 per eenheid**

• **Aangepast totaalbedrag = 100 eenheden × $10.00 per eenheid = $1,000.00**

2\. **Pas regeltoeslagen toe voor het verschil**: Omdat de goedgekeurde eenheidsprijs van $11.00 hoger is dan de PO eenheidsprijs van $10.00, past het systeem regeltoeslagen toe om rekening te houden met dit verschil:

• **Bedrag regelkosten = (goedgekeurde eenheidsprijs factuur - PO eenheidsprijs) × hoeveelheid**

• **Bedrag regeltoeslagen = ($11.00 - $10.00) × 100 eenheden = $100.00**

3\. **De factuur verwerken**: Het systeem verwerkt de factuur met:

• **Base Amount:** $1,000.00

• **Line Charge:** $100.00

• **Totaal verwerkt bedrag:** $1,100.00

Dit zorgt ervoor dat, hoewel de basis-PO-waarden behouden blijven voor consistentie, de goedgekeurde variantie in de eenheidsprijs wordt verantwoord via een extra regeltoeslag, wat resulteert in een nauwkeurige financiële verwerking en administratie.
