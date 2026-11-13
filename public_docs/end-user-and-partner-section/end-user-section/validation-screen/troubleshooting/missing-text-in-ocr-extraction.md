# Ontbrekende tekst in OCR-extractie

Als tekst zichtbaar is op een document maar een veld kan niet worden geëxtraheerd, controleer dan eerst of DocBits die tekst heeft herkend. Een gescande afbeelding en de ingebedde tekst van een PDF kunnen verschillende resultaten opleveren. Wijzig een extractieregel pas als u weet welke tekst beschikbaar is.

## De OCR-weergave controleren

1. Open het document in **Veldvalidatie**.
2. Selecteer in de werkbalk aan de rechterkant het pictogram **OCR-weergave**. De OCR-weergave opent in een nieuw browsertabblad.
3. Zoek het ontbrekende woord of getal in de herkende tekst die over de pagina heen wordt weergegeven. Ontbreekt het daar, dan kan de veldextractie het niet uit die tekstlaag halen. Staat het er wel, controleer dan in plaats daarvan de veldtoewijzing.

<figure><img src="../../../../.gitbook/assets/dbdc-1238-ocr-view-nl-20261113.png" alt="OCR-weergave van een fictieve factuur in het Nederlands, met de herkende woorden over de pagina heen weergegeven"><figcaption><p>Vergelijk de tekst op het document met de woorden in de OCR-weergave: hier zijn de leverancier Musterfirma GmbH, de titel Factuur, het factuurnummer INV-2026-0412 en de datum 14-09-2026 als tekst herkend. Dit voorbeeld toont herkende tekst, geen mislukte extractie.</p></figcaption></figure>

## OCR proberen in plaats van ingebedde E-tekst voor één leverancier

Als **Gebruik E-tekst indien beschikbaar** is ingeschakeld, kan DocBits de tekst gebruiken die al in de PDF is ingebed. Tekst die alleen in een afbeelding staat, kan in die laag ontbreken. Voor een leverancier bij wie dit probleem optreedt:

1. Open een document van die leverancier in **Veldvalidatie**.
2. Selecteer **Meer opties** (drie puntjes) in de werkbalk aan de rechterkant.
3. Schakel **Gebruik E-tekst indien beschikbaar** uit.
4. Lees de melding over opnieuw opstarten en selecteer **Bevestigen** om de wijziging op te slaan en het document opnieuw te verwerken. Selecteer **Annuleren** om de instelling ongewijzigd te laten.
5. Open **OCR-weergave** opnieuw nadat het document is verwerkt en controleer of de ontbrekende tekst verschijnt.

<figure><img src="../../../../.gitbook/assets/dbdc-1238-supplier-etext-nl-20261113.png" alt="Menu Meer opties in de veldvalidatie met de schakelaar Gebruik E-tekst indien beschikbaar van de leverancier, hier nog ingeschakeld"><figcaption><p>De E-tekstschakelaar van de leverancier staat in Meer opties van het validatiescherm en is hier nog ingeschakeld; in stap 3 schakelt u hem uit.</p></figcaption></figure>

<figure><img src="../../../../.gitbook/assets/dbdc-1238-restart-confirm-nl-20261113.png" alt="Bevestigingsvenster dat meldt dat het document opnieuw moet worden opgestart, met de knoppen Annuleren en Bevestigen"><figcaption><p>Bevestigen start de verwerking van het geopende document opnieuw, zodat de leveranciersinstelling van kracht wordt.</p></figcaption></figure>

Het menu **Meer opties** bevat ook ingangen voor andere taken: **Gebruik gestructureerde extractie (AI)** en **AI-model (kopvelden en tabel)** worden beschreven in [Een leveranciersspecifiek AI-model kiezen voor veld- en tabelextractie](../supplier-specific-ai-model-for-field-and-table-extraction.md). Wat **Documentstroom** toont, staat uitgelegd in [Documentstroom](../../dashboard/document-flow.md); **Lay-outbouwer** opent de [Lay-outeditor](../../../../administration-and-setup/setup/document-types/layout-builder.md).

## De standaardinstelling van de organisatie wijzigen

Een beheerder kan **Instellingen → Documentverwerking → OCR-instellingen → Algemene OCR-instellingen** openen en **Gebruik E-tekst indien beschikbaar** voor de organisatie uitschakelen. Dit wijzigt de standaard voor latere verwerkingen; controleer en verwerk reeds getroffen documenten apart. Zie [OCR-instellingen](../../../../administration-and-setup/settings/document-processing/ocr-settings.md) voor de andere OCR-instellingen.

<figure><img src="../../../../.gitbook/assets/dbdc-1238-org-ocr-settings-nl-20261113.png" alt="Kaart Algemene OCR-instellingen met de schakelaar Gebruik E-tekst indien beschikbaar voor de hele organisatie"><figcaption><p>De organisatie-instelling helpt wanneer het probleem documenten van meerdere leveranciers treft. Dezelfde kaart toont ook de optie Gebruik DESKEW indien beschikbaar en de AI OCR-versie.</p></figcaption></figure>

Als de tekst na opnieuw verwerken nog steeds ontbreekt, controleer dan de kwaliteit van de scan en neem contact op met uw DocBits-beheerder of de support met het document-ID en het paginanummer. Stuur geen vertrouwelijk document mee in een openbare supportaanvraag.
