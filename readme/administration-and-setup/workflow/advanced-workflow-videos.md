---
description: "Vijf Nederlandstalige hoofdstukken over geavanceerde workflows en logboeken, met ondertiteling en transcripties."
---

# Advanced Workflow-video’s

Leer een geavanceerde workflow bouwen, testen en onderzoeken. Alle vijf hoofdstukken hebben Nederlandse gesproken uitleg.

De eerste drie hoofdstukken tonen de echte DocBits-interface. De twee hoofdstukken over logboeken gebruiken lesdiagrammen die als illustraties zijn aangeduid. De opnamen tonen niet opgeslagen demonstratieconcepten.

Elke video heeft WebVTT-ondertiteling en een uitklapbare transcriptie.

1. [Bouwer en canvas](#builder-and-canvas) · 1:38
2. [Knooppunten en routes](#nodes-and-routes) · 1:50
3. [Variabelen, tests en activering](#variables-tests-and-activation) · 1:58
4. [De juiste uitvoering vinden](#find-the-relevant-execution) · 1:49
5. [Knooppunten volgen en onderzoeken](#trace-nodes-and-diagnose) · 1:43

## Bouwer en canvas {#builder-and-canvas}

{% embed url="https://docbits-videos.fra1.cdn.digitaloceanspaces.com/settings-assistant/advanced_workflows_canvas/v2/nl.mp4" %}

[Ondertiteling (WebVTT)](https://docbits-videos.fra1.cdn.digitaloceanspaces.com/settings-assistant/advanced_workflows_canvas/v2/nl.vtt) · 1:38

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

[Ondertiteling (WebVTT)](https://docbits-videos.fra1.cdn.digitaloceanspaces.com/settings-assistant/advanced_workflows_logic/v2/nl.vtt) · 1:50

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

{% embed url="https://docbits-videos.fra1.cdn.digitaloceanspaces.com/settings-assistant/advanced_workflows_testing/v2/nl.mp4" %}

[Ondertiteling (WebVTT)](https://docbits-videos.fra1.cdn.digitaloceanspaces.com/settings-assistant/advanced_workflows_testing/v2/nl.vtt) · 1:58

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

**Bekijk de resultaten**

Bekijk meldingen en tijden per knooppunt: groen is succes, oranje een onware voorwaarde, rood een fout, grijs overgeslagen. Test opnieuw na correcties. Gebruik Test Manager voor herhaalbare scenario’s: succes, alternatieven, ontbrekende gegevens en fouten.

**Sla op vóór activering**

Automatisch opslaan bewaart ongeveer elke dertig seconden na wijzigingen een lokale browserversie. Sla expliciet op de server op. Activering vereist de eerste opslag. Controleer de ingeschakelde status in de workflowlijst voordat u automatische uitvoering verwacht.

</details>

## De juiste uitvoering vinden {#find-the-relevant-execution}

{% embed url="https://docbits-videos.fra1.cdn.digitaloceanspaces.com/settings-assistant/advanced_workflow_logs_search/v2/nl.mp4" %}

[Ondertiteling (WebVTT)](https://docbits-videos.fra1.cdn.digitaloceanspaces.com/settings-assistant/advanced_workflow_logs_search/v2/nl.vtt) · 1:49

<details>
<summary>Transcriptie</summary>

**Open het documentlogboek**

Kies in het documentdashboard Workflow Logs onder Acties. Workflowtoegang moet ingeschakeld zijn. Deze logboeken horen bij het gekozen document. Ontwerpertests en gebeurtenis- of activiteitenlogboeken van de organisatie staan hier los van.

**Lees de tellers**

Blauw telt uitvoeringen in de huidige resultaten, rood fouten, geel onware voorwaarden en groen successen. De tellers beschrijven uitvoeringen, geen workflowdefinities of knooppunten. Filters kunnen deze aantallen wijzigen.

**Kies de exacte uitvoering**

Elke rij toont workflownaam, aanmaaktijd, duur in seconden en resultaat. Eén workflow kan meermaals voor hetzelfde document draaien. Vergelijk tijdstempels. Een korte uitvoering kan door afronding nul komma nul nul seconden tonen.

**Beperk de resultaten**

Zoek een workflow met Zoeken. Het afstelpictogram opent sorteerrichting, sorteercriterium, status en begin- en einddatum. Sorteer op naam of aanmaaktijd. Voer datums in als jaar, maand, dag en selecteer Toepassen.

**Controleer pagina’s en filters**

Gebruik paginering voor oudere resultaten. Filters wissen laadt de lijst zonder filterkeuzes. Wis de zoektekst afzonderlijk. Controleer bij lege resultaten document, datums en status. Een lege lijst bewijst geen uitvoeringsfout.

**Bijzondere toestanden**

Een banner en blokkeerpictogram tonen de uitvoeringslimiet van het document. Onderzoek herhaalde triggers voordat u limieten wijzigt. Een DocOperator-videodownload verschijnt alleen bij een bestaande opname; die opname hoort bij de uitvoering.

</details>

## Knooppunten volgen en onderzoeken {#trace-nodes-and-diagnose}

{% embed url="https://docbits-videos.fra1.cdn.digitaloceanspaces.com/settings-assistant/advanced_workflow_logs_diagnosis/v2/nl.mp4" %}

[Ondertiteling (WebVTT)](https://docbits-videos.fra1.cdn.digitaloceanspaces.com/settings-assistant/advanced_workflow_logs_diagnosis/v2/nl.vtt) · 1:43

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
