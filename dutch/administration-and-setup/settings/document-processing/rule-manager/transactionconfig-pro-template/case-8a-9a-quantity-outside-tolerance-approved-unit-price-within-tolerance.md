# Geval 8a, 9a: Hoeveelheid buiten tolerantie (Goedgekeurd), Eenheidsprijs binnen tolerantie

Het volgende scenario is een voorbeeld van een geconfigureerde mapping en geen aantoonbaar uitgerold standaardsjabloon. De werkelijke uitvoer, bedragen, tekens en documenttypen hangen af van de actieve `conflict_resolution`-regels en -expressies, de exportmapping en de goedkeuringsbesluiten. Elke hieronder beschreven debet- of creditnota is afhankelijk van die configuratie; het voorbeeld garandeert geen automatische uitgifte of wettelijke naleving.

## Scenario:

Het aantal op de factuur valt buiten de aanvaardbare tolerantie maar is goedgekeurd, terwijl de eenheidsprijs binnen de tolerantie blijft.

## Actie:

Het systeem accepteert de goedgekeurde hoeveelheid en de eenheidsprijs volgens de factuur en verwerkt de transactie dienovereenkomstig.

## Voorbeeld:

* **Purchase Order (PO):**
  * Quantity: 150 units
  * Eenheidsprijs: $12.00 per eenheid
  * Total Amount: $1,800.00
* **Invoice Received:**
  * Hoeveelheid: 160 eenheden (buiten tolerantie van 6.67% maar goedgekeurd)
  * Eenheidsprijs: $12.00 per eenheid (binnen tolerantie)
  * Total Amount: $1,920.00
* **Tolerance Levels:**
  * Quantity Tolerance: ±5%
  * Tolerantie per eenheidsprijs: ±2%

Aangezien de hoeveelheid (160 eenheden) de aanvaardbare tolerantielimiet overschrijdt, maar is goedgekeurd, en de eenheidsprijs ($12.00) binnen het aanvaardbare bereik ligt, zal het systeem:

1. **Accepteer de goedgekeurde hoeveelheid:** Het systeem bevestigt dat de hoeveelheid is goedgekeurd ondanks dat deze buiten het normale tolerantiebereik ligt.
2. **Accepteer de eenheidsprijs:** De eenheidsprijs van $12.00 per eenheid valt binnen de aanvaardbare tolerantie en wordt daarom geaccepteerd als gefactureerd.
3. **Verwerk de transactie:** Het systeem berekent het totaalbedrag met behulp van de goedgekeurde hoeveelheid en eenheidsprijs:
   * **Totaalbedrag = Aantal × eenheidsprijs**
   * **Totaalbedrag = 160 eenheden × $12.00 per eenheid = $1,920.00**
4. **De factuur voltooien:** Het systeem verwerkt de factuur met een totaalbedrag van $1,920.00, wat de goedgekeurde hoeveelheid en de geaccepteerde eenheidsprijs weergeeft.

Dankzij deze aanpak kan het systeem rekening houden met goedgekeurde variaties in de hoeveelheid en tegelijkertijd ervoor zorgen dat de eenheidsprijs binnen het verwachte bereik blijft, wat een soepele transactieverwerking mogelijk maakt.
