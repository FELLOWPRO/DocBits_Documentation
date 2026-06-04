# Nodes

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
