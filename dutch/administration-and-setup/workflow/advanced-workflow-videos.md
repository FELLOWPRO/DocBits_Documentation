---
description: "Vijf Nederlandstalige hoofdstukken over geavanceerde workflows en logboeken, met ondertiteling en transcripties."
---

# Advanced Workflow-video’s

Alle vijf hoofdstukken hebben Nederlandse gesproken uitleg, een ondertitelbestand en een transcript. Het eerste toont stap voor stap hoe je de voorbeeldworkflow maakt; de andere gaan dieper in op de afzonderlijke onderwerpen.

De eerste drie hoofdstukken tonen de echte DocBits-editor met demonstratieconcepten. De testversie van het zoeken toont echte documentverwerking en logbediening met lege resultaten. Het diagnosehoofdstuk gebruikt nog steeds lesdiagrammen die als illustraties zijn aangeduid.

Elke video heeft WebVTT-ondertiteling en een uitklapbare transcriptie.

1. [Bouwer en canvas](#builder-and-canvas) · 3:21
2. [Knooppunten en routes](#nodes-and-routes) · 1:50
3. [Variabelen, tests en activering](#variables-tests-and-activation) · 1:58
4. [De juiste uitvoering vinden](#find-the-relevant-execution) · 1:49
5. [Knooppunten volgen en onderzoeken](#trace-nodes-and-diagnose) · 1:43

## Bouwer en canvas {#builder-and-canvas}

Maak kennis met Jan en volg zijn uitleg in de echte Nederlandstalige DocBits-interface. Hij controleert het workflowdashboard, de workflowlijst en de licentie en opent daarna een niet-opgeslagen concept in de ontwerper. Stap voor stap geeft hij de workflow een naam, stelt hij de bedragcontrole en twee acties in, plaatst hij de kaarten en verbindt hij beide routes. Daarna laat hij zien hoe je tests voorbereidt met een document of eigen gegevens. Het demoaccount heeft geen Advanced Workflow-abonnement en blokkeert de validatie; het concept blijft niet opgeslagen en inactief.

{% embed url="https://docbits-videos.fra1.cdn.digitaloceanspaces.com/settings-assistant/advanced_workflows_canvas-admin/v7/nl.mp4" %}

[Video openen](https://docbits-videos.fra1.cdn.digitaloceanspaces.com/settings-assistant/advanced_workflows_canvas-admin/v7/nl.mp4) · [Ondertitels (WebVTT)](https://docbits-videos.fra1.cdn.digitaloceanspaces.com/settings-assistant/advanced_workflows_canvas-admin/v7/nl.vtt) · [Transcript (tekst)](https://docbits-videos.fra1.cdn.digitaloceanspaces.com/settings-assistant/advanced_workflows_canvas-admin/v7/nl.txt) · 3:21

| In deze video | Begin |
| --- | --- |
| Maak kennis met de beheerder | [0:00](https://docbits-videos.fra1.cdn.digitaloceanspaces.com/settings-assistant/advanced_workflows_canvas-admin/v7/nl.mp4#t=0) |
| Toegang controleren | [0:03](https://docbits-videos.fra1.cdn.digitaloceanspaces.com/settings-assistant/advanced_workflows_canvas-admin/v7/nl.mp4#t=3) |
| De workflow een naam geven | [0:27](https://docbits-videos.fra1.cdn.digitaloceanspaces.com/settings-assistant/advanced_workflows_canvas-admin/v7/nl.mp4#t=27) |
| De bedragcontrole instellen | [0:41](https://docbits-videos.fra1.cdn.digitaloceanspaces.com/settings-assistant/advanced_workflows_canvas-admin/v7/nl.mp4#t=41) |
| De actie Approval toevoegen | [1:06](https://docbits-videos.fra1.cdn.digitaloceanspaces.com/settings-assistant/advanced_workflows_canvas-admin/v7/nl.mp4#t=66) |
| De actie Standard toevoegen | [1:26](https://docbits-videos.fra1.cdn.digitaloceanspaces.com/settings-assistant/advanced_workflows_canvas-admin/v7/nl.mp4#t=86) |
| Kaarten ordenen | [1:47](https://docbits-videos.fra1.cdn.digitaloceanspaces.com/settings-assistant/advanced_workflows_canvas-admin/v7/nl.mp4#t=107) |
| Routes verbinden | [2:01](https://docbits-videos.fra1.cdn.digitaloceanspaces.com/settings-assistant/advanced_workflows_canvas-admin/v7/nl.mp4#t=121) |
| Tests voorbereiden | [2:26](https://docbits-videos.fra1.cdn.digitaloceanspaces.com/settings-assistant/advanced_workflows_canvas-admin/v7/nl.mp4#t=146) |
| Valideren, opslaan en activeren | [2:51](https://docbits-videos.fra1.cdn.digitaloceanspaces.com/settings-assistant/advanced_workflows_canvas-admin/v7/nl.mp4#t=171) |

<details>
<summary>Transcript</summary>

**Maak kennis met de beheerder**

Ik beheer DocBits. We maken een factuurcontrole.

**Toegang controleren**

Ik begin op het workflowdashboard en open de workflowlijst. Daarna controleer ik de licentie. Workflow en Advanced Workflow hebben allebei actieve toegang nodig. Als beide zijn ingeschakeld, biedt Nieuwe workflow ook Advanced Workflow aan. Dit documentatieaccount heeft geen actieve workflowlicentie. Daarom ga ik verder met een niet opgeslagen voorbeeld in de ontwerper.

**De workflow een naam geven**

Ik werk in de echte DocBits-ontwerper. Eerst geef ik het concept een duidelijke naam. We controleren een factuurbedrag en gebruiken twee eenvoudige acties om de mogelijke routes te tonen. Dit voorbeeld blijft onopgeslagen.

**De bedragcontrole instellen**

Ik open het menu om iets toe te voegen en kies een voorwaardekaart. Onder Documentveld kies ik de Docfield-voorwaarde. Als veld vul ik total_amount in. Dan kies ik de vergelijking groter dan. En voer ik duizend in. Gebruik de veldsleutel van uw eigen document. Precies duizend voldoet niet aan deze vergelijking.

**De actie Approval toevoegen**

Nu voeg ik een actiekaart uit de categorie Documentveld toe. Deze actie stelt een documentveld in. Ik gebruik de voorbeeldsleutel approval_route. En vul de waarde Approval in. Dit geeft de route een herkenbare waarde. Een echt goedkeuringsproces heeft eigen bedrijfsacties nodig.

**De actie Standard toevoegen**

Ik voeg een tweede kaart met dezelfde actie toe. Deze actie stelt een documentveld in. Ik gebruik de voorbeeldsleutel approval_route. Dit keer krijgt het voorbeeldveld de waarde Standard. Beide kaarten zijn ingesteld. Er zijn nog verbindingen nodig om te bepalen welke actie wordt uitgevoerd.

**Kaarten ordenen**

Ik sleep de kaarten naar een leesbare indeling. De twee acties komen rechts. De voorwaarde staat in het midden, met Start links. Verplaatsen verandert alleen de positie. Het maakt geen verbinding.

**Routes verbinden**

Ik sleep van de uitgang van Start naar de ingang van de voorwaarde. De succesroute loopt via een blauwe verbinding naar Approval. De oranje route voor een onjuiste voorwaarde loopt naar Standard. De rode foutuitgang is een aparte uitgang voor evaluatiefouten. Hier blijft die zonder verbinding. Bepaal voor een productieworkflow hoe u zulke fouten afhandelt.

**Tests voorbereiden**

De testknop in de werkbalk opent de keuze van een testdocument. Ik kan een voorbeelddocument kiezen of volledige aangepaste gegevens voorbereiden. Test bedragen boven, onder en precies op duizend. Controleer ook een ontbrekend bedrag. Dit account heeft geen Advanced Workflow-licentie. Ik toon de voorbereiding van een test, geen uitgevoerd resultaat.

**Valideren, opslaan en activeren**

Validatie controleert verbindingen en kaartinstellingen. Bij dit account blokkeert de ontbrekende licentie de validatie. Met een account dat toegang heeft, zou ik uitdrukkelijk op de server opslaan. Daarna controleer ik de activering apart. Vóór de eerste opslag is de schakelaar uitgeschakeld. De aanduiding voor het automatische concept verwijst naar een lokale browserkopie. Die betekent niet dat de workflow opgeslagen of ingeschakeld is.

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
