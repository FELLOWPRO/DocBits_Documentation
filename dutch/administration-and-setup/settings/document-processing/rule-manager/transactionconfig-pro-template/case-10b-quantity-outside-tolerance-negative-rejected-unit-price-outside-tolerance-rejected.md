# Geval 10b: Hoeveelheidstekort en eenheidsprijs buiten tolerantie, beide afgewezen

Het volgende scenario is een voorbeeld van een geconfigureerde mapping en geen aantoonbaar uitgerold standaardsjabloon. De werkelijke uitvoer, bedragen, tekens en documenttypen hangen af van de actieve `conflict_resolution`-regels en -expressies, de exportmapping en de goedkeuringsbesluiten. Elke hieronder beschreven debet- of creditnota is afhankelijk van die configuratie; het voorbeeld garandeert geen automatische uitgifte of wettelijke naleving.

## Scenario:

Zowel de hoeveelheid als de eenheidsprijs vallen buiten de tolerantie en geen van beide is goedgekeurd.

## Actie:

Het systeem wijst de factuurgegevens af, past de waarden aan zodat deze overeenkomen met de inkooporder en genereert de benodigde debet- of creditnota's.

## Voorbeeld:

* **Purchase Order (PO):**
  * Quantity: 150 units
  * Eenheidsprijs: $30.00 per eenheid
  * Total Amount: $4,500.00
* **Invoice Received:**
  * Hoeveelheid: 140 eenheden (buiten tolerantie van -6.67%, afgekeurd)
  * Eenheidsprijs: $33.00 per eenheid (buiten tolerantie van 10%, afgewezen)
  * Total Amount: $4,620.00
* **Tolerance Levels:**
  * Quantity Tolerance: ±5%
  * Tolerantie per eenheidsprijs: ±2%

Aangezien zowel de hoeveelheid (140 eenheden) als de eenheidsprijs ($33.00) buiten de aanvaardbare tolerantiegrenzen vallen en geen van beide is goedgekeurd, zal het systeem:

1. **Weiger de factuurgegevens:** Het systeem accepteert de gefactureerde hoeveelheid of eenheidsprijs niet omdat deze afwijkt van de tolerantielimieten.
2. **De hoeveelheid aanpassen:** Het systeem past de hoeveelheid aan zodat deze overeenkomt met de oorspronkelijke inkooporderhoeveelheid.
   * Aangepaste hoeveelheid = 150 eenheden (vanaf PO)
3. **De eenheidsprijs aanpassen:** Het systeem past de eenheidsprijs aan zodat deze overeenkomt met de oorspronkelijke eenheidsprijs van de inkooporder.
   * Aangepaste eenheidsprijs = $30.00 per eenheid (vanaf PO)
4. **Herbereken het totaalbedrag:** Het systeem herberekent het totaalbedrag met behulp van de aangepaste hoeveelheid en eenheidsprijs:
   * **Gecorrigeerd totaalbedrag = Aangepaste hoeveelheid × Aangepaste eenheidsprijs**
   * **Gecorrigeerd totaalbedrag = 150 eenheden × $30.00 per eenheid = $4,500.00**
5. **Een debetnota genereren:** Omdat het oorspronkelijke factuurtotaal hoger was dan het gecorrigeerde totaal, genereert het systeem een debetnota voor het te veel in rekening gebrachte bedrag.
   * **Bedrag debetnota = Totaal origineel factuur - Gecorrigeerd totaalbedrag**
   * **Bedrag debetnota = $4,620.00 - $4,500.00 = $120.00**
6. **De factuur verwerken:** Het systeem verwerkt de factuur met het gecorrigeerde totaalbedrag van $4,500.00 en geeft een debetnota uit van $120.00 om het te veel in rekening gebrachte bedrag te compenseren.

Deze aanpak zorgt ervoor dat de financiële transactie wordt gecorrigeerd zodat deze overeenkomt met de voorwaarden van de inkooporder, waardoor nauwkeurige en eerlijke factureringspraktijken worden gehandhaafd.
