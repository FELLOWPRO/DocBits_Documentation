# Geval 1, 2, 3: Hoeveelheid en eenheidsprijs binnen tolerantie

Het volgende scenario is een voorbeeld van een geconfigureerde mapping en geen aantoonbaar uitgerold standaardsjabloon. De werkelijke uitvoer, bedragen, tekens en documenttypen hangen af van de actieve `conflict_resolution`-regels en -expressies, de exportmapping en de goedkeuringsbesluiten. Elke hieronder beschreven debet- of creditnota is afhankelijk van die configuratie; het voorbeeld garandeert geen automatische uitgifte of wettelijke naleving.

## Scenario:

Zowel de hoeveelheid als de eenheidsprijs op de factuur liggen binnen een acceptabel tolerantiebereik vergeleken met de inkooporder.

## Actie:

Het systeem accepteert de factuurwaarden en berekent het totaalbedrag op basis van de opgegeven hoeveelheid en eenheidsprijs.

## Voorbeeld:

**Purchase Order (PO):**

Quantity: 100 units

Eenheidsprijs: $10.00 per eenheid

Total Amount: $1,000.00

**Invoice Received:**

Hoeveelheid: 101 eenheden (binnen tolerantie van 1%)

Eenheidsprijs: $10.05 per eenheid (binnen tolerantie van 0.5%)

Total Amount: $1,015.05

**Tolerance Levels:**

Quantity Tolerance: ±2%

Tolerantie per eenheidsprijs: ±1%\


Omdat de hoeveelheid (101 eenheden) en de eenheidsprijs ($10.05) beide binnen de aanvaardbare tolerantieniveaus vallen in vergelijking met de inkooporder, zal het systeem:\


1\. **Accepteer de factuurwaarden:** De hoeveelheid en eenheidsprijs op de factuur worden als geldig geaccepteerd omdat ze binnen de gedefinieerde tolerantiegrenzen vallen.

2\. **Bereken het totale bedrag:** Het totale bedrag wordt berekend met behulp van de geaccepteerde waarden:

• Totaalbedrag = Aantal × eenheidsprijs

• Totaalbedrag = 101 eenheden × $10.05 per eenheid = $1,015.05

3\. **De factuur verwerken:** De factuur wordt verwerkt met een totaalbedrag van $1,015.05 en de financiële gegevens worden dienovereenkomstig bijgewerkt.

Deze aanpak zorgt ervoor dat kleine afwijkingen die binnen aanvaardbare tolerantieniveaus vallen, niet leiden tot factuurafwijzingen of vertragingen in de betaling, waardoor het financiële proces wordt gestroomlijnd.
