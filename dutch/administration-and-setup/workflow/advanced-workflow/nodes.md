# Nodes

## Video: Knooppunten en routes

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

[Bekijk alle vijf hoofdstukken](../advanced-workflow-videos.md)

Een Advanced Workflow is een graaf van **nodes** die met elkaar verbonden zijn door verbindingen. Je voegt nodes toe via het **+ Add**-menu (of door met de rechtermuisknop op het canvas te klikken) en verbindt ze om de uitvoeringsstroom te definiëren.

<figure><img src="../../../.gitbook/assets/workflow_advanced_add_menu.png" alt="Menu Node toevoegen met de beschikbare nodetypes"><figcaption><p>Het <strong>+ Add</strong>-nodemenu — de beschikbare nodetypes.</p></figcaption></figure>

## Nodetypes

- **Start** — het beginpunt van de workflow. Wordt automatisch toegevoegd; elke stroom begint hier.
- **When** — een triggerkaart, hetzelfde als in de Standard-builder.
- **And** — een voorwaardekaart. Deze evalueert naar waar of onwaar en kan de stroom vertakken.
- **Then** — een actiekaart die werk uitvoert (velden instellen, taken aanmaken, API's aanroepen, …).
- **Wait ALL** — wacht totdat *alle* binnenkomende vertakkingen klaar zijn voordat er wordt doorgegaan.
- **Wait ANY** — gaat verder zodra *een* binnenkomende vertakking klaar is.
- **OR** — vertakt de stroom langs alternatieve paden.
- **Note** — een vrije-tekst-annotatie op het canvas; deze heeft geen invloed op de uitvoering.

De **When / And / Then** nodes gebruiken precies dezelfde kaarten die worden beschreven in het gedeelte [Kaarten](../cards-overview.md).

## Nodes verbinden

Nodes worden verbonden door **gekleurde verbindingen**. Sleep van een handvat aan de **rechterkant** van een node naar het invoerhandvat aan de **linkerkant** van een andere node om een verbinding te maken. Elke kleur duidt op een andere uitvoeringsuitkomst:

- **Success** (blauw) — het standaardpad dat wordt gevolgd wanneer een node succesvol wordt voltooid. Beschikbaar op alle nodetypes.
- **Failed Condition** (oranje) — gevolgd wanneer een voorwaarde naar onwaar evalueert. Beschikbaar op **And** (voorwaarde) nodes.
- **Error** (rood) — gevolgd wanneer een node tijdens de uitvoering een fout tegenkomt. Beschikbaar op **And** en **Then** (actie) nodes.

## Markeren van het uitvoeringspad

Klik op een node om het uitvoeringspad te zien. Alle nodes die ernaartoe leiden en alle nodes die erop volgen worden gemarkeerd — al het andere wordt gedimd. Voor **Wait ALL** nodes wordt elke binnenkomende vertakking getoond, zodat je precies kunt zien waar de gate op wacht voordat er wordt doorgegaan.

## Volgende stappen

- Geef gegevens door tussen nodes met [Variables](variables.md).
- Controleer en voer je stroom uit met [Validation & Testing](validation-and-testing.md).
