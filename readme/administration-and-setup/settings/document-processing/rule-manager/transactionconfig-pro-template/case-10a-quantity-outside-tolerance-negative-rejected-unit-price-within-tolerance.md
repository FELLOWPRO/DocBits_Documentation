# Geval 10a: Hoeveelheidstekort afgewezen, eenheidsprijs binnen tolerantie

Het volgende scenario is een voorbeeld van een geconfigureerde mapping en geen aantoonbaar uitgerold standaardsjabloon. De werkelijke uitvoer, bedragen, tekens en documenttypen hangen af van de actieve `conflict_resolution`-regels en -expressies, de exportmapping en de goedkeuringsbesluiten. Elke hieronder beschreven debet- of creditnota is afhankelijk van die configuratie; het voorbeeld garandeert geen automatische uitgifte of wettelijke naleving.

## Scenario:

De hoeveelheid ligt onder het acceptabele bereik (negatieve tolerantie) en is niet goedgekeurd, hoewel de eenheidsprijs binnen de tolerantie valt.

## Actie:

Het systeem past de hoeveelheid aan zodat deze overeenkomt met het goedgekeurde niveau, waardoor de eenheidsprijs consistent blijft. De transactie wordt dienovereenkomstig verwerkt.

## Voorbeeld:

* **Purchase Order (PO):**
  * Quantity: 150 units
  * Eenheidsprijs: $20.00 per eenheid
  * Total Amount: $3,000.00
* **Invoice Received:**
  * Hoeveelheid: 140 eenheden (buiten tolerantie van -6.67%, afgekeurd)
  * Eenheidsprijs: $20.00 per eenheid (binnen tolerantie)
  * Total Amount: $2,800.00
* **Tolerance Levels:**
  * Quantity Tolerance: ±5%
  * Tolerantie per eenheidsprijs: ±2%

Aangezien de hoeveelheid (140 eenheden) onder de aanvaardbare tolerantielimiet ligt (negatieve variantie van -6.67%) en niet is goedgekeurd, maar de eenheidsprijs ($20.00) binnen de tolerantie valt, zal het systeem:

1. **Weiger de lagere hoeveelheid:** Het systeem accepteert de lagere hoeveelheid niet, omdat deze buiten het goedgekeurde tolerantiebereik ligt.
2. **De hoeveelheid aanpassen:** Het systeem past de hoeveelheid aan zodat deze overeenkomt met het goedgekeurde niveau dat is opgegeven in de inkooporder.
   * Goedgekeurde hoeveelheid = 150 eenheden (vanaf PO)
3. **Handhaaf de eenheidsprijs:** De eenheidsprijs van $20.00 per eenheid valt binnen de tolerantie en blijft ongewijzigd.
4. **Het totale bedrag opnieuw berekenen:** Het systeem berekent het totale bedrag met behulp van de goedgekeurde hoeveelheid en de geaccepteerde eenheidsprijs:
   * **Totaalbedrag = goedgekeurde hoeveelheid × eenheidsprijs**
   * **Totaalbedrag = 150 eenheden × $20.00 per eenheid = $3,000.00**
5. **De factuur verwerken:** Het systeem verwerkt de factuur met het aangepaste totaalbedrag van $3,000.00, wat de goedgekeurde hoeveelheid en eenheidsprijs weergeeft. Van de leverancier wordt verwacht dat hij de volledige goedgekeurde hoeveelheid factureert.

Deze aanpak zorgt ervoor dat de financiële transactie in overeenstemming is met de voorwaarden van de inkooporder en voorkomt onderfacturering terwijl de financiële gegevens nauwkeurig worden bijgehouden.
