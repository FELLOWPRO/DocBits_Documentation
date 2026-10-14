# AI Workforce

<figure><img src="../../.gitbook/assets/docnet-agents-infographic-en.png" alt="AI Workforce Agents Infographic"><figcaption><p>DocBits Multi-Agent Systeem voor autonome documentverwerking</p></figcaption></figure>

## Overzicht

**AI Workforce** is de orkestratielaag binnen DocBits die inkomend werk omzet in gecoördineerde AI-agenten. In plaats van dat een persoon elke stap handmatig doorloopt, neemt het een eenheid inkomend werk — een e-mail, een chatbericht in Microsoft Teams of Discord, een handmatige actie in de gebruikersinterface of een API-aanroep — en brengt het tot voltooiing: het classificeren van het document, het extraheren en valideren van velden, het matchen met inkooporders en stamgegevens, en het exporteren naar de ERP, met mensen in de lus waar dat belangrijk is.

Zie het als een team dat je aanstuurt in plaats van een tool die je bedient. Elk stuk werk doorloopt dezelfde vaste structuur:

* Een **Orchestrator** ontvangt een **Missie** (één werkeenheid), plant deze en delegeert.
* Het plan wordt opgesplitst in **Problemen** (afzonderlijke taken), die elk worden afgehandeld door een **Specialist-agent** of een **mens**.
* Specialisten rapporteren hun resultaten terug en de Orchestrator brengt het resultaat samen.

De _agenten_ die deze rollen invullen liggen niet vast: DocBits levert een kant-en-klare **DocBits Orchestrator** en twee standaardspecialisten, en je kunt je eigen agenten aanmaken (zie [Agenten](./#agents)).

Een typische uitvoering, van begin tot eind: er komt een factuur binnen per e-mail → er wordt een Missie aangemaakt → de Orchestrator plant deze en verstuurt Problemen naar specialisten (classificeren, extraheren, valideren, PO-matchen) → een gevoelige stap pauzeert in de **Inbox** zodat een mens kan goedkeuren → na goedkeuring wordt het document geëxporteerd en de Missie voltooid. Je volgt het hele proces vanuit het **Dashboard**, houdt gerelateerde uitvoeringen bij elkaar in **Projecten**, en grijpt in via de **Inbox** en **Problemen** wanneer een menselijke beslissing nodig is.

## Hoe activeren

AI Workforce wordt per organisatie ingeschakeld via de hoofdinstellingen.

1. Ga naar **Instellingen → Modules**.
2. Schakel de module **AI Workforce** in.
3. Bevestig het abonnement in het dialoogvenster dat verschijnt.

Zodra AI Workforce is ingeschakeld, verschijnt **AI Workforce** in de hoofdnavigatiebalk en wordt de werkruimte beschikbaar voor je organisatie.

## Dashboard

Het **Dashboard** biedt je een overzicht van de AI Workforce — KPI's, grafieken en activiteitenlijsten in één oogopslag. Je bepaalt zelf welke statistieken worden getoond.

Om de actieve statistieken te configureren, open je de **Instellingen** (tandwielpictogram) en gebruik je het paneel **Dashboard Widgets**. Schakel elke widget in of uit en klik op **Opslaan**; je selectie wordt opgeslagen als persoonlijke voorkeur, zodat elke gebruiker zijn eigen weergave kan aanpassen.

Beschikbare widgets zijn onder meer:

* **Fleet monitoring** — livestatus van al je agenten.
* **KPI-kaarten** — Openstaande Problemen, Actieve Missies, Ingeschakelde Agenten, Uitvoeringen Vandaag, Tokengebruik en Openstaande Goedkeuringen.
* **Grafieken** — problementrend in de tijd, missies per status, e-mailinname, problemen per prioriteit, uitvoeringen per dag en tokengebruik per agent.
* **Lijsten** — actieve missies, recente activiteit, openstaande goedkeuringen, je openstaande problemen, agenten aan het werk en geblokkeerde items.

## Inbox

De **Inbox** is de plek waar werk wacht op **menselijke aandacht**. Wanneer een agent op het punt staat een tool uit te voeren die goedkeuring vereist, pauzeert deze de taak en stelt hier een **goedkeuringsverzoek** in. Dit is Human-in-the-Loop (HITL): de actie wordt niet uitgevoerd totdat een persoon een beslissing neemt. Of een bepaalde tool goedkeuring vereist, wordt bepaald door de **goedkeuringsmodus** van de agent en de **kritisch**-markeringen van zijn tools (zie [Agentinstellingen](./#agent-settings)).

Elk Inbox-item toont de titel van het verzoek, de agent die het heeft ingesteld en een korte beschrijving van waarover een beslissing nodig is. Vanuit het item kun je:

* **Goedkeuren** — de agent laten doorgaan met de actie.
* **Afwijzen** — de actie stopzetten.
* **Opmerking / bericht sturen** — de agent alternatieve instructies geven voordat deze verdergaat.
* **Missie openen** — naar de missie springen waartoe dit item behoort voor volledige context.

Items zijn **In behandeling** totdat iemand actie onderneemt, en worden daarna **Opgelost** (of **Genegeerd** als het item terzijde wordt gelegd zonder beslissing — bijvoorbeeld wanneer de bijbehorende missie wordt geannuleerd). Het navigatie-item Inbox toont een badge met het aantal openstaande goedkeuringen, zodat niets kritisch wordt gemist.

## Missies

Een **Missie** is de bovenliggende werkeenheid en de agentuitvoering die één doel nastreeft. Elke missie kan meerdere taken omvatten en wordt gecoördineerd door een **Orchestrator-agent**, die het werk plant, het als Problemen aan specialisten delegeert, de resultaten in de gaten houdt en het resultaat samenbrengt.

Een missie wordt aangemaakt vanuit haar **bron** — E-mail, Chat (Microsoft Teams of Discord), Mission Control (handmatig) of de API — en draagt die context gedurende haar hele levensduur mee. Je kunt er zelf een starten vanuit **Mission Control** door in gewone taal te beschrijven wat je gedaan wilt hebben; de Orchestrator neemt het vanaf daar over.

Missies doorlopen de volgende statussen:

| Status                    | Betekenis                                                            |
| ------------------------- | ------------------------------------------------------------------- |
| **Planning**              | De Orchestrator analyseert het verzoek en stelt een plan op.        |
| **In Verwerking** _(Actief)_ | Specialist-agenten voeren de geplande problemen uit.             |
| **Wacht op Goedkeuring**  | De missie is gepauzeerd en wacht op een menselijke beslissing in de Inbox. |
| **Voltooid**              | Alle problemen zijn afgehandeld en het doel van de missie is bereikt. |

Missies kunnen ook **Gepauzeerd** of **Geannuleerd** zijn. Vanuit de detailweergave van een missie kun je haar **voortgang** volgen, de gekoppelde **problemen** bekijken, het tijd- en tokengebruik zien, de **tijdlijn** van gebeurtenissen openen en de missie **opnieuw starten**, **bewerken** of **verwijderen**.

## Problemen

Een **Probleem** is een afzonderlijke taak die wordt aangemaakt om een deel van het doel van een missie te bereiken — bijvoorbeeld _een document importeren_, _een antwoord sturen naar de afzender_ of _een stap handmatig goedkeuren_. Problemen worden afgehandeld door **specialist-agenten** en **mensen**, die samen aan dezelfde taak werken.

Elk probleem draagt de context mee die de toegewezene nodig heeft en doorloopt zijn eigen levenscyclus (Te Doen / In Uitvoering → In Beoordeling → Klaar, of Fout / Geannuleerd). Problemen kunnen worden toegewezen aan een agent of een persoon, een prioriteit krijgen (Kritisch, Hoog, Medium, Laag), aan een missie worden gekoppeld en via opmerkingen worden besproken.

Je kunt alle problemen bekijken, ze filteren op status, prioriteit, toegewezene of missie, ze groeperen op status, prioriteit of toegewezene, en **Mijn Problemen** bekijken — de taken die aan jou zijn toegewezen. Door een probleem handmatig aan te maken kun je werk voor een agent of een collega rechtstreeks aan een missie toevoegen.

## Projecten

**Projecten** zijn mappen die gerelateerde **Missies** groeperen — bijvoorbeeld _alle facturen van een specifieke leverancier in Q1_, daarna een ander project voor _Q2_, enzovoort. Ze houden een groot volume aan agentuitvoeringen georganiseerd en gemakkelijk terug te vinden.

Wanneer je een project aanmaakt, geef je het:

* een **Naam** — bijv. _"Acme Facturen Q1"_;
* een optionele **Beschrijving** — waar het project over gaat en welk resultaat je verwacht;
* een optionele **Vervaldatum** — de datum tot waarop het project actief moet blijven.

Een project is **Actief** of **Voltooid**. Een project met een vervaldatum **blijft actief totdat die datum is bereikt** en wordt dan automatisch voltooid — zo sluit een kwartaalverzameling zichzelf af aan het einde van het kwartaal (de controle wordt één keer per dag uitgevoerd). Een project zonder vervaldatum blijft actief totdat je het zelf voltooit. Je kunt een project ook op elk moment handmatig voltooien of heropenen. Vanuit een project kun je zien hoeveel missies het bevat en er verdere missies aan koppelen.

## Agenten

Agenten zijn de werkers. Elke agent heeft een **rol** die bepaalt wat deze doet in de stroom Orchestrator → Missies → Problemen:

* **Orchestrator** — coördineert werk over meerdere agenten. Deze ontvangt een missie, plant deze, delegeert de stappen als problemen en brengt de resultaten samen. Een orchestrator is vereist om missies te laten draaien.
* **Specialist** — voert een specifieke taak uit, zoals het importeren van een document of het versturen van een e-mailantwoord, en rapporteert terug aan zijn orchestrator.

DocBits levert de AI Workforce kant-en-klaar, met deze standaardagenten:

* **DocBits Orchestrator** — de standaard-orchestrator.
* **Document Processor** — importeert en verwerkt geüploade documenten.
* **Email Reply** — stelt antwoorden op en verstuurt deze naar de afzender.

Dit zijn **systeemagenten**: je kunt onderdelen ervan configureren, maar je kunt ze niet verwijderen. Je kunt daarnaast ook je eigen orchestrators en specialisten aanmaken.

### Hiërarchie- en activatieregels

Omdat een orchestrator vereist is om een missie te laten draaien, volgt de activatie een aantal regels:

* **Orchestrators** hebben een schakelaar om ze **in of uit te schakelen**, maar een orchestrator kan **alleen worden uitgeschakeld als er ten minste twee orchestrators bestaan** — het systeem laat je nooit de laatste uitschakelen, omdat er dan niets meer zou zijn om missies te coördineren.
* Wanneer er **meer dan één orchestrator actief is**, wordt de **System Router** automatisch actief. Zijn taak is om naar elke inkomende missie te kijken en deze aan de juiste orchestrator te delegeren. Bij één enkele orchestrator is de router niet nodig en blijft deze op de achtergrond.
* **Specialisten hebben geen in/uit-schakelaar.** In plaats daarvan bepaal je waar ze kunnen werken door ze **aan orchestrators toe te wijzen** (zie _Agent Pool_ hieronder). Een specialist die aan geen enkele orchestrator is toegewezen, is helemaal niet beschikbaar — deze blijft in de directory staan, maar geen enkele orchestrator kan er werk aan delegeren, dus elke specialist moet aan ten minste één orchestrator worden toegewezen om te worden gebruikt.

Je kunt deze relaties bekijken en herschikken in het **Org Chart**, dat Router → Orchestrators → Specialisten toont.

### Agentinstellingen

Elke agent — systeem of aangepast — heeft een instellingenmenu met de volgende secties:

* **Prompt** — de basis-systeemprompt van de agent. _Alleen-lezen bij systeemagenten._
* **Instellingen** — het **model** van de agent en de **redeneerinspanning**. De AI Workforce draait op één enkel redeneervaardig model (**DocBits Pro**), dus in plaats van laag-niveau-instellingen is er één knop — **Redeneerinspanning** — die bepaalt hoe hard de agent nadenkt (en dus hoeveel het kost):
  * **Geen** — snelst en goedkoopst; geen redenering.
  * **Laag** — snelle taken, lichte redenering.
  * **Medium** _(standaard)_ — gebalanceerde kwaliteit en kosten.
  * **Hoog** — diepe redenering voor moeilijkere taken; hogere kosten.
  * **X-Hoog** — maximale redenering; hoogste kosten.
* **Goedkeuringsmodus** — hoeveel van het werk van de agent menselijke goedkeuring nodig heeft in de [Inbox](./#inbox):
  * **Geen** — de agent voert elke tool automatisch uit; er wordt niets ter goedkeuring verzonden.
  * **Kritisch** _(standaard)_ — alleen tools die als **kritisch** zijn gemarkeerd vereisen goedkeuring; al het andere wordt automatisch uitgevoerd. Kritische tools zijn de gevoelige schrijf-/externe acties (bijvoorbeeld _document uploaden/importeren_, _documentvelden bijwerken_, _e-mail beantwoorden_, _melding versturen_). In deze modus stelt een kritische tool **altijd** een goedkeuringsverzoek in de Inbox in. Je kunt individuele tools verfijnen (een normaal veilige tool markeren als goedkeuring vereisend, of een kritische tool vrijgeven) — deze overrides per tool gelden alleen in de Kritisch-modus.
  * **Alle** — elke tool die de agent uitvoert vereist goedkeuring.
*   **Aangepaste instructies** — vrije tekst waarin je de werkgewoonten van de agent beschrijft (dit is ook bij systeemagenten bewerkbaar). Het standaardsjabloon ziet er als volgt uit:

    > **Classificatie:** gebruik de classificator van DocBits op het geüploade document. Vertrouw alleen op het onderwerp/de tekst van de e-mail wanneer er geen document was bijgevoegd.
    >
    > **Veldoverrides:** geen — accepteer extractiewaarden zoals ze zijn.
    >
    > **Goedkeuring:** niet geconfigureerd. (Om menselijke goedkeuring voor specifieke acties te vereisen, noem je de actie en de drempel.)
    >
    > **Projecttoewijzing:** match tegen projectbeschrijvingen; laat een missie liever niet-toegewezen dan een slechte match te forceren. (Om te overschrijven, geef je trefwoorden of afzenderpatronen op: bijv. `supplier@acme.com → Acme Onboarding`.)
* **Vaardigheden** — de tools die de agent mag gebruiken (bijvoorbeeld _documenten uploaden_ of _gebruikers weergeven_). Elke tool is óf **kritisch** (gevoelige schrijf-/externe acties) óf niet-kritisch, wat het hierboven beschreven goedkeuringsgedrag aanstuurt. _Niet bewerkbaar bij systeemagenten._
* **Agent Pool** — _alleen orchestrators._ Een lijst met de beschikbare agenten, waar je selecteert aan welke specialisten deze orchestrator werk mag delegeren. Een specialist moet hier (of aan een andere orchestrator) aan een orchestrator worden toegewezen om enig werk te doen; een specialist die overal niet-toegewezen is, is helemaal niet beschikbaar.

### Aangepaste agenten aanmaken

Naast de standaardagenten kun je je eigen **orchestrators** en **specialisten** aanmaken die passen bij je processen. Open **Agenten → Agent Aanmaken** om de wizard te starten, die je door dezelfde configuratie leidt als hierboven beschreven: kies de **rol** (Orchestrator of Specialist), geef de agent een **naam** en een duidelijke **beschrijving** (een orchestrator wordt op basis van deze tekst gekozen, en een orchestrator kiest zijn specialisten op basis van die van hen), schrijf zijn prompt, kies zijn vaardigheden, stel zijn redeneerinspanning in en — voor orchestrators — kies de specialisten in zijn agent pool. Aangepaste agenten kunnen op elk moment volledig worden bewerkt of verwijderd.
