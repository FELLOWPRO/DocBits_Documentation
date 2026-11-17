# Knooppunten

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

{% embed url="https://docbits-videos.fra1.cdn.digitaloceanspaces.com/settings-assistant/workflow-card-version/v1/nl.mp4" %}

**Video:** De versie van een kaart wijzigen · 0:42 · [Ondertitels (WebVTT)](https://docbits-videos.fra1.cdn.digitaloceanspaces.com/settings-assistant/workflow-card-version/v1/nl.vtt)

<details>

<summary>Transcriptie</summary>

**Het label toont de versie van de kaart** · [0:00](https://docbits-videos.fra1.cdn.digitaloceanspaces.com/settings-assistant/workflow-card-version/v1/nl.mp4#t=0.25)

Kaarten kunnen meerdere versies hebben. Het kleine label op een kaart, bijvoorbeeld v1, toont welke versie hij gebruikt. Een nieuwere versie kan meer.

**Klik om de versies te zien** · [0:11](https://docbits-videos.fra1.cdn.digitaloceanspaces.com/settings-assistant/workflow-card-version/v1/nl.mp4#t=11.35)

Klik op het versielabel om de versies van deze kaart te zien.

**Versie 3: Status na export** · [0:16](https://docbits-videos.fra1.cdn.digitaloceanspaces.com/settings-assistant/workflow-card-version/v1/nl.mp4#t=16.916)

Kies de nieuwere versie. Deze kan ook de status van het document na export instellen.

**Stel de waarden opnieuw in** · [0:24](https://docbits-videos.fra1.cdn.digitaloceanspaces.com/settings-assistant/workflow-card-version/v1/nl.mp4#t=24.316)

De waarden worden niet overgenomen. Stel ze opnieuw in, hier de exportconfiguratie en de status.

**Valideren en testen** · [0:33](https://docbits-videos.fra1.cdn.digitaloceanspaces.com/settings-assistant/workflow-card-version/v1/nl.mp4#t=33.083)

Valideer en test de Workflow daarna, zoals na elke wijziging. Sla hem op als hij doet wat je verwacht.

</details>

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

{% embed url="https://docbits-videos.fra1.cdn.digitaloceanspaces.com/settings-assistant/workflow-results/v1/nl.mp4" %}

**Video:** Succes, mislukte conditie en fout in een Workflow-uitvoering · 1:26 · [Ondertitels (WebVTT)](https://docbits-videos.fra1.cdn.digitaloceanspaces.com/settings-assistant/workflow-results/v1/nl.vtt)

<details>

<summary>Transcriptie</summary>

**Wanneer, En, Dan tijdens de uitvoering** · [0:00](https://docbits-videos.fra1.cdn.digitaloceanspaces.com/settings-assistant/workflow-results/v1/nl.mp4#t=0.25)

Loopt een Workflow, dan start de Wanneer-kaart hem. En-kaarten controleren condities, Dan-kaarten handelen. Wat daarna gebeurt, hangt af van het resultaat van elke kaart.

**Succes, mislukte conditie of fout** · [0:13](https://docbits-videos.fra1.cdn.digitaloceanspaces.com/settings-assistant/workflow-results/v1/nl.mp4#t=13.25)

Elke En-kaart eindigt met een van drie resultaten. Succes volgt het blauwe succespad, een mislukte conditie het oranje pad, en een fout het rode foutpad.

**Ontbrekende gegevens zijn een fout** · [0:25](https://docbits-videos.fra1.cdn.digitaloceanspaces.com/settings-assistant/workflow-results/v1/nl.mp4#t=25.183)

Ontbrekende gegevens zijn geen mislukte conditie. Ontbreekt een veld dat de kaart nodig heeft, ontbreekt een variabele of is er geen document, dan meldt de kaart een fout en neemt ze het rode foutpad.

**Mislukte conditie, geen oranje pad: de uitvoering stopt** · [0:38](https://docbits-videos.fra1.cdn.digitaloceanspaces.com/settings-assistant/workflow-results/v1/nl.mp4#t=38.816)

Mislukt een conditie en is haar oranje pad niet verbonden, dan stopt de Workflow bij die kaart. De uitvoering eindigt als mislukte conditie.

**Verbonden: een mislukte conditie is gewoon een vertakking** · [0:49](https://docbits-videos.fra1.cdn.digitaloceanspaces.com/settings-assistant/workflow-results/v1/nl.mp4#t=49.35)

Is het oranje pad wel verbonden, dan is een mislukte conditie gewoon een extra vertakking. De Workflow gaat daar verder en kan toch met succes eindigen.

**Rood foutpad: vang fouten op met een terugvaloptie** · [0:59](https://docbits-videos.fra1.cdn.digitaloceanspaces.com/settings-assistant/workflow-results/v1/nl.mp4#t=59.883)

Verbind het rode foutpad met een terugvaloptie, bijvoorbeeld een taak voor een persoon, zodat fouten niet onopgemerkt blijven. De terugvaloptie loopt, maar de uitvoering telt toch als fout.

**Hoe een uitvoering eindigt** · [1:12](https://docbits-videos.fra1.cdn.digitaloceanspaces.com/settings-assistant/workflow-results/v1/nl.mp4#t=72.416)

Kortom: elke fout maakt de uitvoering tot een fout. Een mislukte conditie zonder verbonden oranje pad maakt er een mislukte conditie van. Al het andere eindigt als succes.

</details>

{% embed url="https://docbits-videos.fra1.cdn.digitaloceanspaces.com/settings-assistant/workflow-merge/v2/nl.mp4" %}

**Video:** EN en OF: voorwaarden combineren · 4:21 · [Ondertitels (WebVTT)](https://docbits-videos.fra1.cdn.digitaloceanspaces.com/settings-assistant/workflow-merge/v2/nl.vtt)

<details>

<summary>Transcriptie</summary>

**EN en OF** · [0:00](https://docbits-videos.fra1.cdn.digitaloceanspaces.com/settings-assistant/workflow-merge/v2/nl.mp4#t=0.25)

Voorwaarden kun je op twee manieren combineren. Kaarten na elkaar werken als EN: ze moeten allemaal waar zijn. Kaarten naast elkaar, verbonden met dezelfde volgende kaart, werken als OF: één ware kaart is genoeg. Verbindingsknooppunten tonen dat op het canvas.

**EN: kaarten na elkaar** · [0:18](https://docbits-videos.fra1.cdn.digitaloceanspaces.com/settings-assistant/workflow-merge/v2/nl.mp4#t=18.616)

Eén kaart na de andere is EN: elke kaart op het pad moet waar zijn voordat de volgende draait. Deze factuur is klaar voor validatie en wacht niet op goedkeuring, dus beide kaarten zijn waar en de actie draait.

**OF: kaarten naast elkaar** · [0:34](https://docbits-videos.fra1.cdn.digitaloceanspaces.com/settings-assistant/workflow-merge/v2/nl.mp4#t=34.916)

OF betekent kaarten naast elkaar. Verbind de groene uitgang van beide En-kaarten direct met de ingang van de volgende kaart. Test het: de eerste kaart is onwaar, de tweede waar, en één waar pad is genoeg om de actie te laten draaien. De testbanner meldt toch een niet vervulde voorwaarde, omdat de oranje uitgang van de onware kaart niet verbonden is, maar de actie draait.

**Hetzelfde met een OF-kaart** · [0:58](https://docbits-videos.fra1.cdn.digitaloceanspaces.com/settings-assistant/workflow-merge/v2/nl.mp4#t=58.416)

Je kunt de paden ook samenvoegen met een OF-kaart. Die doet hetzelfde, maar maakt de OF zichtbaar op het canvas. Klik met rechts op het canvas, kies Toevoegen en dan OF. Verbind beide En-kaarten ermee en de OF-kaart met de actie.

**Voor OF is één waar geval genoeg** · [1:16](https://docbits-videos.fra1.cdn.digitaloceanspaces.com/settings-assistant/workflow-merge/v2/nl.mp4#t=76.55)

De test geeft hetzelfde resultaat: voor de OF-kaart is één waar geval genoeg, dus de actie draait. Ook hier meldt de banner de niet vervulde voorwaarde van de onware kaart.

**Wacht op ÉÉN: hetzelfde als OF** · [1:30](https://docbits-videos.fra1.cdn.digitaloceanspaces.com/settings-assistant/workflow-merge/v2/nl.mp4#t=90.516)

Wacht op ÉÉN werkt precies als OF: de kaart wacht op elke kaart ervoor en gaat verder zodra minstens één pad is genomen. De twee zijn uitwisselbaar, gebruik de naam die in je workflow het best leest.

**EN met Wacht op ALLE** · [1:52](https://docbits-videos.fra1.cdn.digitaloceanspaces.com/settings-assistant/workflow-merge/v2/nl.mp4#t=112.216)

Voor EN met kaarten naast elkaar gebruik je Wacht op ALLE. Klik met rechts op het canvas, kies Toevoegen en dan Wacht op ALLE. Verbind beide En-kaarten ermee en Wacht op ALLE met de actie. Test het: hij wacht op beide kaarten, beide zijn waar, dus de actie draait.

**De volgorde: zoals de verbindingen getekend zijn** · [2:20](https://docbits-videos.fra1.cdn.digitaloceanspaces.com/settings-assistant/workflow-merge/v2/nl.mp4#t=140.516)

In welke volgorde loopt dit? De workflow werkt een lijst af. De kaarten achter een kaart komen erbij in de volgorde waarin hun verbindingen zijn getekend, dus de bovenste voorwaarde loopt eerst, dan de onderste. De OF-kaart wacht tot beide gelopen hebben, en de actie loopt één keer, hoeveel voorwaarden ook waar waren.

**Rechtstreeks naar een actie: geen wachten** · [2:51](https://docbits-videos.fra1.cdn.digitaloceanspaces.com/settings-assistant/workflow-merge/v2/nl.mp4#t=171.883)

Kaarten die rechtstreeks met een actie verbonden zijn, wachten niet. De actie wordt via het korte pad bereikt en loopt voordat de laatste kaart van het lange pad is gecontroleerd, dus die kaart verandert niets meer. Moet de actie op elke controle wachten, zet er dan een OF-, Wacht op ÉÉN- of Wacht op ALLE-kaart voor.

**Elke uitgang kan ergens anders heen** · [3:13](https://docbits-videos.fra1.cdn.digitaloceanspaces.com/settings-assistant/workflow-merge/v2/nl.mp4#t=193.716)

Elke kaart heeft tot drie uitgangen: succes, niet vervulde voorwaarde en fout. Elke uitgang kan naar een eigen volgende kaart leiden.

**Meerdere uitgangen, één ingang: één is genoeg** · [3:25](https://docbits-videos.fra1.cdn.digitaloceanspaces.com/settings-assistant/workflow-merge/v2/nl.mp4#t=205.783)

Je kunt ook meerdere uitgangen van één kaart met dezelfde ingang verbinden. Er kan er maar één genomen worden, omdat een kaart met precies één resultaat eindigt, dus wacht de volgende kaart alleen op die ene. Dat geldt voor elke ingang, niet alleen voor deze verbindingsknooppunten. Test het: de voorwaarde is niet vervuld, en Wacht op ALLE gaat toch verder.

**Verbindingsknooppunten: welke paden genomen zijn** · [3:54](https://docbits-videos.fra1.cdn.digitaloceanspaces.com/settings-assistant/workflow-merge/v2/nl.mp4#t=234.983)

Verbindingsknooppunten maken een Workflow vooral beter leesbaar. OF en Wacht op ÉÉN gaan verder zodra minstens één verbonden pad genomen is. Wacht op ALLE wacht tot alle vorige kaarten klaar zijn en gaat pas verder als alle verbonden paden genomen zijn. Elke uitgang van een kaart kan verbonden worden, niet alleen de groene: eindigt een kaart met een niet vervulde voorwaarde, dan telt haar oranje uitgang als genomen.

</details>

Nodes worden verbonden door **gekleurde verbindingen**. Sleep van een handvat aan de **rechterkant** van een node naar het invoerhandvat aan de **linkerkant** van een andere node om een verbinding te maken. Elke kleur duidt op een andere uitvoeringsuitkomst:

- **Success** (blauw) — het standaardpad dat wordt gevolgd wanneer een node succesvol wordt voltooid. Beschikbaar op alle nodetypes.
- **Failed Condition** (oranje) — gevolgd wanneer een voorwaarde naar onwaar evalueert. Beschikbaar op **And** (voorwaarde) nodes.
- **Error** (rood) — gevolgd wanneer een node tijdens de uitvoering een fout tegenkomt. Beschikbaar op **And** en **Then** (actie) nodes.

## Markeren van het uitvoeringspad

Klik op een node om het uitvoeringspad te zien. Alle nodes die ernaartoe leiden en alle nodes die erop volgen worden gemarkeerd — al het andere wordt gedimd. Voor **Wait ALL** nodes wordt elke binnenkomende vertakking getoond, zodat je precies kunt zien waar de gate op wacht voordat er wordt doorgegaan.

## Volgende stappen

- Geef gegevens door tussen nodes met [Variables](variables.md).
- Controleer en voer je stroom uit met [Validation & Testing](validation-and-testing.md).
