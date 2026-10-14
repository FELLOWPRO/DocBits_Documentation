# Tabel Extractie Probleemoplossing

## **Stap 1: Open OCR-weergave voor Slechte Extractieresultaten**

Als de resultaten van de tabel extractietraining niet goed zijn:

1. Open de **OCR-weergave** door te klikken op het vergrootglaspictogram met **OCR** erop geschreven.
2. Bekijk de extractieresultaten en zie of het OCR-proces de gegevensvastlegging kan verbeteren.
3. Als de resultaten er nog steeds slecht uitzien, probeer dan een ander document om te controleren of het probleem documentspecifiek is.
4. Als het probleem documentspecifiek is, gebruik dan een ander document voor extractie.
   * Als het probleem aanhoudt, volg dan de volgende stappen.

## **Stap 2: Controleer de Beschikbaarheid van E-tekst**

1. Controleer of het document **e-tekst** beschikbaar heeft.
   * U kunt dit controleren met een tool zoals **Adobe Acrobat**.
   * Als het document e-tekst bevat, volg dan **Stap 3.**
   * Als het document geen e-tekst bevat, volg dan **Stap 4.**

## **Stap 3: Schakel E-tekst Extractie In**

Als het document e-tekst bevat, heeft u twee opties:

1. **Schakel e-tekst extractie in voor alleen deze leverancier**:
   * Ga terug naar de **Documenten Veldvalidatie**.
   * Klik op het vierkantje met de drie puntjes in de linkerwerkbalk.
   * Activeer hier de optie **Gebruik E-tekst indien beschikbaar** om het in te schakelen voor alleen deze leverancier.
2. **Schakel e-tekst extractie in voor alle leveranciers**:
   * Ga naar **Instellingen** > **Documentverwerking** > **OCR-instellingen**.
   * In dit gedeelte vindt u de optie **Gebruik E-tekst indien beschikbaar** en kunt u het inschakelen voor alle leveranciers.
3. Na het inschakelen van e-tekst extractie, probeer de **tabel extractietraining** opnieuw.
   * Als de resultaten verbeteren, is het probleem opgelost.
   * Als de resultaten nog steeds niet goed zijn, ga verder naar **Stap 4**.

## **Stap 4: Geen E-tekst Beschikbaar - Verander AI OCR Versie**

Als het document geen e-tekst heeft:

1. Ga naar **Instellingen** > **Documentverwerking** > **OCR-instellingen**.
2. Verander de **AI OCR Versie** naar een andere versie.
3. Ga terug naar de **Tabel Extractie Training** en probeer opnieuw.
4. Als het resultaat beter is:
   * Controleer andere documenten van verschillende leveranciers om ervoor te zorgen dat de extractieresultaten voor die leveranciers niet worden beïnvloed door deze verandering.
   * **Wees voorzichtig, aangezien deze verandering de extractieresultaten van andere leveranciers kan beïnvloeden.**
   * Deze verandering kan andere leveranciers beïnvloeden, dus zorg ervoor dat u de resultaten grondig controleert om ervoor te zorgen dat het de documentextracties van andere leveranciers niet negatief beïnvloedt.
5. Als het resultaat niet verbeterde na het veranderen van de AI OCR versie, neem dan **contact met ons op** voor verdere assistentie.

## Meldingen op de tabel

De extractie kan er goed uitzien en toch weigert het document om goedgekeurd te worden. Dit zijn de meldingen die DocBits op of onder de regelitemtabel toont, wat ze veroorzaakt en hoe u ze oplost.

| Melding | Oorzaak | Oplossing |
|---|---|---|
| **Verplichte kolom leeg** (cel rood gemarkeerd, kolomnaam in de tooltip) | Een kolom die in de tabelkolominstellingen als *Verplicht* is gemarkeerd, heeft in deze rij geen waarde. | Vul de cel in. Als de waarde voor dit documenttype nooit bestaat, schakelt een beheerder *Verplicht* uit onder Instellingen → Documenttypen → Tabelkolommen en start u het document opnieuw. |
| **Line total does not match quantity x unit price (expected …, got …)** | DocBits controleert elke rij: `TOTAL_AMOUNT = QUANTITY × UNIT_PRICE + CHARGES`, min `DISCOUNT`, of × (100 − `DISCOUNT_PERCENT`) / 100, of min `DISCOUNT_PER_UNIT × QUANTITY`, afhankelijk van welke kortingskolom is gevuld. Een verschil groter dan 0,02 geeft de melding. De controle draait alleen wanneer hoeveelheid, eenheidsprijs en totaal alle drie zijn gevuld. | Vergelijk de vier waarden met het document. Meestal is een ervan in de verkeerde kolom gelezen; een kosten- of kortingswaarde in de verkeerde cel is het meest voorkomende geval. Corrigeer de cel; de melding verdwijnt bij het opslaan. |
| **Line total does not match quantity x unit price minus discount / minus percentage discount / minus per-unit discount** | Dezelfde controle, met de kortingskolom die is gevuld. | Zoals hierboven; controleer eerst de kortingscel. |
| **Line items add up to … but the net total is …** (waarschuwing) | De som van alle `TOTAL_AMOUNT`-cellen wijkt af van het nettobedrag in de koptekst. | Zoek naar een ontbrekende rij, een dubbele rij of een verkeerd gelezen nettobedrag in de koptekst. Een waarschuwing blokkeert de goedkeuring niet. |
| **Total does not add up: expected …, got …** (koptekst) | Netto + belasting (+ verzendkosten in Amerikaanse lay-outs) wijkt af van het totaal in de koptekst. | Koptekstcontrole, geen tabelprobleem: corrigeer de kopbedragen. |
| **Line Item Table is missing Mandatory column for PO like (Item Number, Unit Price, Quantity and Total amount)** | PO-matching heeft die vier standaardkolommen nodig en een ervan is verborgen of vervangen door een eigen kolom. | Beheerder: maak de standaardkolom weer zichtbaar onder Tabelkolommen, of koppel de waarde eraan in de tabeltraining. |
| **Table is already extracted by AI. Do you want to train manually?** | U hebt de tabeltraining geopend voor een leverancier van wie de tabel uit de AI komt. | Bevestig om te trainen; de opgeslagen regels vervangen dan de AI-tabel voor deze leverancier. Annuleer om de AI-tabel te behouden. |
| **AI Table will display here. Enable in …** | AI-tabelextractie is voor de organisatie uitgeschakeld. | Beheerder: Instellingen → Documentverwerking → Classificatie en extractie → *AI-tabel extractie*. |
| **No line items yet** | Er is niets geëxtraheerd: geen regels voor deze leverancier en de AI heeft geen tabel gevonden, of het document heeft geen leesbare tekst. | Volg Stap 1–4 hierboven (OCR-weergave, E-tekst). Train daarna de tabel eenmalig, of voeg handmatig rijen toe met *Nieuwe tabelrij toevoegen*. |

### De AI blijft een kolom met de verkeerde waarde vullen

Voorbeeld uit de praktijk: de AI schrijft het regeltotaal in `CHARGES`. Elke rij haalt dan de regeltotaalcontrole niet, omdat kosten worden opgeteld bij hoeveelheid × eenheidsprijs.

1. Als de leverancier opgeslagen regels heeft, schakel dan *AI gebruiken* voor die kolom uit (Instellingen → Documenttypen → Tabelkolommen), zodat de regels de kolom vullen.
2. Als de leverancier geen regels heeft, train de tabel dan eenmalig zodat de kolom aan de positie op de pagina is gebonden, of verberg de kolom als de leverancier die waarde nooit afdrukt.
3. Voeg een [AI-tabeltag](../../../end-user-and-partner-section/end-user-section/ai-table/ai-table-tags.md) toe zoals *"charges column is empty on this supplier"*; tags worden per leverancier opgeslagen.

### De tabelcontroles uitschakelen

Instellingen → Documenttypen → *uw type* → Meer instellingen → **Tabelvalidatie overslaan** markeert de tabel van elk document van dat type als geldig: regeltotaalafwijkingen en lege verplichte kolommen worden niet meer gemeld. De koptekstcontroles (totaal = netto + belasting) blijven bestaan. Gebruik dit alleen voor documenttypen waarvan de tabellen informatief zijn en niet naar het ERP worden geëxporteerd.
