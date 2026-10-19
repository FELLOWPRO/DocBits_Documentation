---
description: "Vijf Nederlandstalige hoofdstukken over geavanceerde workflows en logboeken, met ondertiteling en transcripties."
---

# Advanced Workflow-video’s

Leer een geavanceerde workflow bouwen, testen en onderzoeken. Alle vijf hoofdstukken hebben Nederlandse gesproken uitleg.

De eerste drie hoofdstukken tonen de echte DocBits-editor met demonstratieconcepten. De testversie van het zoeken toont echte documentverwerking en logbediening met lege resultaten. Het diagnosehoofdstuk gebruikt nog steeds lesdiagrammen die als illustraties zijn aangeduid.

Elke video heeft WebVTT-ondertiteling en een uitklapbare transcriptie.

1. [Bouwer en canvas](#builder-and-canvas) · 1:38
2. [Knooppunten en routes](#nodes-and-routes) · 1:50
3. [Variabelen, tests en activering](#variables-tests-and-activation) · 1:58
4. [De juiste uitvoering vinden](#find-the-relevant-execution) · 1:49
5. [Knooppunten volgen en onderzoeken](#trace-nodes-and-diagnose) · 1:43

## Bouwer en canvas {#builder-and-canvas}

{% embed url="https://docbits-videos.fra1.cdn.digitaloceanspaces.com/settings-assistant/advanced_workflows_canvas/v2/nl.mp4" %}

[Video openen](https://docbits-videos.fra1.cdn.digitaloceanspaces.com/settings-assistant/advanced_workflows_canvas/v2/nl.mp4) · [Ondertiteling (WebVTT)](https://docbits-videos.fra1.cdn.digitaloceanspaces.com/settings-assistant/advanced_workflows_canvas/v2/nl.vtt) · 1:38

<details>
<summary>Transcriptie</summary>

**Een factuur met twee routes**

Dit is een echte geavanceerde workflow in DocBits. Een controle van het factuurbedrag leidt naar twee acties. De verbindingen bepalen welke actie wordt uitgevoerd. Het voorbeeld gebruikt een niet-opgeslagen concept en demonstratievelden.

**De bedragcontrole instellen**

Open Toevoegen, kies And en selecteer een voorwaarde voor een documentveld. Stel het bedragveld in, kies Groter dan en voer duizend in. Gebruik de exacte veldsleutel uit uw documentconfiguratie.

**De acties instellen**

Voeg twee Then-kaarten toe. Beide stellen het demonstratieveld approval route in. De ene schrijft Approval, de andere Standard. Deze waarden geven de route aan. Stel voor een productieworkflow uw bedrijfsacties in.

**De resultaatuitgangen verbinden**

Verbind Start met de ingang van de voorwaarde. Verbind de blauwe succesuitgang met Approval en de oranje uitgang voor een onware voorwaarde met Standard. De rode uitgang behandelt evaluatiefouten afzonderlijk. Alleen de positie van een kaart vormt geen route.

**De testgevallen voorbereiden**

Open Testen in de werkbalk. Kies een testdocument of voer de volledige documentgegevens in als JSON. Controleer bedragen boven, onder en precies op duizend, en ontbrekende waarden. Bekijk na de uitvoering de resultaten van de knooppunten.

**Valideren, opslaan en activeren**

Valideer de verbindingen en kaartinstellingen. Sla de workflow expliciet op de server op en controleer de activering afzonderlijk. Automatische browserconcepten vervangen Opslaan niet. Voor uitvoering en logboeken zijn de juiste module en het juiste abonnement nodig.

</details>

## Knooppunten en routes {#nodes-and-routes}

{% embed url="https://docbits-videos.fra1.cdn.digitaloceanspaces.com/settings-assistant/advanced_workflows_logic/v2/nl.mp4" %}

[Video openen](https://docbits-videos.fra1.cdn.digitaloceanspaces.com/settings-assistant/advanced_workflows_logic/v2/nl.mp4) · [Ondertiteling (WebVTT)](https://docbits-videos.fra1.cdn.digitaloceanspaces.com/settings-assistant/advanced_workflows_logic/v2/nl.vtt) · 1:50

<details>
<summary>Transcriptie</summary>

**De rol van elk knooppunt**

Start begint handmatig. When definieert een gebeurtenis. Beide accepteren geen inkomende verbindingen. And controleert een voorwaarde. Then voert een actie uit. Beide bouwers delen de kaartcatalogus. Notities lichten het ontwerp toe zonder te worden uitgevoerd.

**Drie verschillende uitkomsten**

Sleep een uitgang naar de volgende ingang. In de ontwerper betekent blauw succes, oranje een onware voorwaarde en rood een fout. And heeft drie uitkomsten; Then succes en fout. Uitvoeringsweergaven tonen succes in groen.

**Bouw een alternatief**

Controleer of een factuur de drempel overschrijdt. Verbind blauw met goedkeuring, oranje met normale verwerking en rood met foutafhandeling. Een onware voorwaarde kan via de verbonden route doorgaan en stopt niet alle takken.

**Samenvoegen met Wait ALL**

Wait ALL voegt takken samen. Elk bronknooppunt moet een route naar de samenvoeging hebben gevolgd. Verbind beide vereiste controles en de volgende actie. Een niet gekozen route levert het vereiste resultaat niet.

**Alternatieven met ANY en OR**

Wait ANY en OR voegen takken samen als minstens één bron een verbonden route volgt. OR vereist twee verschillende bronknooppunten. Deze samenvoegingen maken keuzes niet exclusief en annuleren geen andere acties. Test de hele graaf.

**Houd de graaf uitvoerbaar**

Maak knooppunten bereikbaar vanaf een ingang. Vermijd cycli en inkomende verbindingen naar Start of When. Voeg een Then-actie toe en valideer routes. Geïmporteerde Delay-knooppunten vereisen een positieve duur; Toevoegen biedt geen Delay.

</details>

## Variabelen, tests en activering {#variables-tests-and-activation}

Volg de verbonden factuurworkflow in de echte DocBits-editor. Open Variabelen, vergelijk de typen en de documentverwijzing, zoek Valideren, bereid tests met documenten of aangepaste gegevens voor en bekijk Opslaan en activering. De testscènes tonen de configuratie van voorbeeldgegevens; ze tonen geen uitgevoerd testresultaat.

{% embed url="https://docbits-videos.fra1.cdn.digitaloceanspaces.com/settings-assistant/advanced_workflows_testing/v3/nl.mp4" %}

[Video openen](https://docbits-videos.fra1.cdn.digitaloceanspaces.com/settings-assistant/advanced_workflows_testing/v3/nl.mp4) · [Ondertiteling (WebVTT)](https://docbits-videos.fra1.cdn.digitaloceanspaces.com/settings-assistant/advanced_workflows_testing/v3/nl.vtt) · 2:00

<details>
<summary>Transcriptie</summary>

**Kies het variabeletype**

Open Variabelen met het accoladesymbool. Kies tekst, getal, ja of nee, of document. Zoek op naam. Een Document-variabele bevat een verwijzing die een specifieke workflowactie instelt; dit formulier accepteert geen documentwaarden.

**Variabelen van de organisatie**

Kies een unieke naam, type en beginwaarde. Aanmaken, wijzigen en verwijderen wordt direct voor de organisatie opgeslagen. Andere workflows kunnen deze waarden delen. Het canvas opslaan of verwerpen maakt variabelewijzigingen niet ongedaan.

**Valideer eerst de structuur**

Selecteer Valideren. Bekijk fouten en waarschuwingen boven het canvas. Klik op een melding om het knooppunt te vinden. Controleer acties, ingangen, uitgangen, cycli en samenvoegingen. Structurele validatie garandeert geen juiste uitvoeringsgegevens.

**Kies de testcontext**

Afspelen op de werkbalk opent de documentkeuze. Kies een document, aangepaste gegevens of een test zonder document voor onafhankelijke kaarten. Afspelen op Start begint direct. Tests gebruiken het huidige canvas, inclusief niet opgeslagen wijzigingen, en simuleren destructieve acties.

**Testscenario’s voorbereiden en controleren**

Maak aparte tests boven, onder en precies op duizend, plus ontbrekende gegevens. Controleer na uitvoering berichten en looptijden: groen betekent geslaagd, oranje onwaar, rood fout en grijs overgeslagen. Test correcties opnieuw. Gebruik Testbeheer voor herhaalbare scenario’s.

**Sla op vóór activering**

Automatisch opslaan bewaart ongeveer elke dertig seconden na wijzigingen een lokale browserversie. Sla expliciet op de server op. Activering vereist de eerste opslag. Controleer de ingeschakelde status in de workflowlijst voordat u automatische uitvoering verwacht.

</details>

## De juiste uitvoering vinden {#find-the-relevant-execution}

{% hint style="info" %}
Testversie: echte DocBits-schermen met documentacties, de documentstroom, staptijden, lege workflowlogs en status- en datumfilters. Het document heeft geen opgeslagen Advanced Workflow-uitvoering. Uitvoeringsrijen, paginering en nodediagnose zijn nog niet opgenomen in deze testversie.
{% endhint %}

{% embed url="https://docbits-videos.fra1.cdn.digitaloceanspaces.com/settings-assistant/advanced_workflow_logs_search/v3/nl.mp4" %}

[Video openen](https://docbits-videos.fra1.cdn.digitaloceanspaces.com/settings-assistant/advanced_workflow_logs_search/v3/nl.mp4) · [Ondertiteling (WebVTT)](https://docbits-videos.fra1.cdn.digitaloceanspaces.com/settings-assistant/advanced_workflow_logs_search/v3/nl.vtt) · 1:52

<details>
<summary>Transcriptie</summary>

**Begin bij het document**

Open op het documentdashboard het actiemenu en kies Documentstroom. De echte verwerkingsgeschiedenis toont import en OCR. Open een stap om de wachttijd en verwerkingstijd te bekijken. Deze verwerkingsstappen staan los van Advanced Workflow-nodes.

**Lees de echte tellers**

Hier staan de workflowlogs van hetzelfde document. Blauw is het totaal, rood zijn fouten, geel zijn niet-vervulde voorwaarden en groen zijn successen. Dit demonstratiedocument heeft geen opgeslagen workflowuitvoeringen. Daarom tonen alle vier de tellers nul.

**Controleer de uitvoeringskolommen**

De tabel bevat kolommen voor workflownaam, aanmaaktijd, looptijd en resultaat. Gebruik de tijdstempel om herhaalde uitvoeringen te onderscheiden. Deze testversie heeft geen uitvoeringsrij om te openen. Een lege lijst bewijst op zichzelf geen uitvoeringsfout.

**Open de statusfilters**

Het filterpictogram opent het echte menu. Sorteer op naam of aanmaaktijd, oplopend of aflopend. Status biedt succes, een niet-vervulde voorwaarde en een fout. Je ziet hier de echte DocBits-interface.

**Kies datums en wis filters**

Kies een periode met de start- en einddatum of de kalender. De volgorde is jaar, maand en dag. Toepassen vraagt de resultaten op. Filters wissen herstelt de selectie. Wis de zoekopdracht afzonderlijk. In deze versie blijven de maandnamen in de kalender Engels.

**Testversie: een opgeslagen uitvoering ontbreekt nog**

Met deze testversie controleer je de documenttoegang, verwerkingsdetails en logbediening. Een opgeslagen Advanced Workflow-uitvoering ontbreekt nog om echte rijen, paginering, routes en nodeberichten te tonen. Deze resultaten worden niet nagebootst in de video.

</details>

## Knooppunten volgen en onderzoeken {#trace-nodes-and-diagnose}

{% embed url="https://docbits-videos.fra1.cdn.digitaloceanspaces.com/settings-assistant/advanced_workflow_logs_diagnosis/v2/nl.mp4" %}

[Video openen](https://docbits-videos.fra1.cdn.digitaloceanspaces.com/settings-assistant/advanced_workflow_logs_diagnosis/v2/nl.mp4) · [Ondertiteling (WebVTT)](https://docbits-videos.fra1.cdn.digitaloceanspaces.com/settings-assistant/advanced_workflow_logs_diagnosis/v2/nl.vtt) · 1:43

<details>
<summary>Transcriptie</summary>

**Vouw een uitvoering uit**

Vouw de workflowrij uit. Een geavanceerde uitvoering toont de graaf links en meldingen rechts; een standaardworkflow toont een reeks kaarten. De gegevens beschrijven die uitvoering en kunnen afwijken van de huidige ontwerper.

**Selecteer een knooppunt**

Verschuif of vergroot de graaf en klik op een knooppunt. Card Logs toont de meldingen. Wait ALL en Wait ANY kunnen ook knooppuntmeldingen hebben. Lees de melding samen met het gekozen knooppunt en tijdstempel.

**Onderscheid de uitkomsten**

Groen betekent succes, oranje een onware voorwaarde, rood een fout, grijs overgeslagen. Een overgeslagen knooppunt is niet uitgevoerd. Controleer eerst of een andere tak werd gekozen of een vereiste ingang van de samenvoeging ontbreekt.

**Volg de eerste afwijking**

Volg de werkelijke route vanaf de ingang. Bekijk oranje bij een onware bedragcontrole. Lees bij een fout de melding en volg rood. Foutafhandeling kan slagen terwijl de gehele uitvoering de oorspronkelijke fout blijft melden.

**Onderzoek samenvoegingen**

Controleer bij Wait ALL elke bron en verbonden uitkomst. Zoek bij ANY of OR een passende bron. Twee uitgangen van één knooppunt zijn geen onafhankelijke goedkeuringen. Een oranje voorwaarderesultaat kan bedoeld zijn.

**Corrigeer en controleer**

Noteer workflownaam, documentverwijzing, tijdstempel, knooppunt en exacte melding. Corrigeer instellingen of gegevens en test een herhaalbaar scenario. Sla op en controleer activering. Vergelijk een nieuwe uitvoering met de oude; eerdere logboeken beschrijven eerder gedrag.

</details>
