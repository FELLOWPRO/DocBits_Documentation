# Infrastructuur

De pagina **Infrastructure** geeft beheerders een actueel overzicht van waar elk onderdeel van het platform draait (EU of US) en of de verwerking gezond is. De pagina is alleen-lezen, er wordt hier dus niets geconfigureerd.

> **Access:** Infrastructure is een pagina die alleen voor beheerders toegankelijk is. Open **Settings → Organization & Access → Infrastructure**.

De pagina heeft drie tabs. Elk tabblad laadt zijn gegevens de eerste keer dat u het opent, heen en weer schakelen haalt dus niet alles opnieuw op.

| Tab | Answers |
|-----|---------|
| **Topology** | Waar draait elke component, en hoe reist een document door DocBits? |
| **Processing** | Draaien de stappen van de documentverwerking, en loopt het werk achterop? |
| **Scheduled Tasks** | Worden de terugkerende achtergrondtaken volgens schema uitgevoerd? |

## Topology

**Topology** opent standaard. De weergave toont het platform in twee aanzichten: **Architecture** en **Process**. Met de schakelaar boven het diagram wisselt u tussen beide; de indicator ernaast toont **live** zolang de weergave zijn status streamt.

Een banner boven het diagram vat de regiocontrole samen:

* **Green**: alle componenten draaien in de regio van uw organisatie, en de banner noemt die regio (bijvoorbeeld **EU**).
* **Red**: een component die als kritiek is gemarkeerd, draait buiten de regio van uw organisatie.
* **Amber**: de melding noemt componenten die in een andere regio staan, terwijl de totale controle slaagt. Dat is een regioafwijking, geen fout.

### Architectuurweergave

De architectuurweergave tekent het platform als rijbanen met componentkaarten, bijvoorbeeld Edge / Web, Core API, Import, Background Services en Modules. Pijlen tonen de verbindingen tussen de kaarten.

Elke kaart toont de naam van de component, een regiobadge en, bij kritieke componenten, een statusstip die groen wordt wanneer de component antwoordt en de latentie in milliseconden toont wanneer een waarde wordt gemeld.

| Badge | Meaning |
|-------|---------|
| **EU ✓** / **US ✓** | De component draait in de regio van uw organisatie. |
| **SHARED** | Een globale component zoals de CDN, zonder eigen regio. Dat is normaal. |
| **EU ⓘ** / **US ⓘ** | De component draait in een andere regio en wordt als melding gerapporteerd. |
| **EU ⚠** / **US ⚠** | De component draait in een andere regio en wordt als fout gerapporteerd. Meld dit bij de support. |
| Grijze badge, geen teken | De regio van deze component is niet bekend. |

### Procesweergave

De procesweergave animeert één document door de pipeline: de invoerbronnen **Email**, **FTP** en **Web** komen samen op **API** en gaan daarna door **OCR**, **Extraction**, **PO matching**, **Auto Accounting** en **Export**. Elke fase is verbonden met een balk voor de gegevensopslag met **Postgres** en bestandsopslag. Een bijschrift noemt de stap die op dat moment wordt geanimeerd, en de afspeelknop pauzeert of hervat de animatie.

PO matching en Auto Accounting zijn optioneel. Wanneer een ervan voor uw organisatie is uitgeschakeld, is de bijbehorende fase grijs en slaat de animatie die over.

### Optionele modules

Optionele modules (Full-Text Search, DocFlow, Auto-Accounting, DocNet en PO Matching) dragen een badge **active** of **inactive** op hun kaart. Een gedeactiveerde module biedt een knop **Activate** die u naar de pagina brengt waar u hem inschakelt: de instellingen van Modules voor de meeste modules, of **Document Types** voor PO Matching, dat per documenttype wordt ingeschakeld.

## Processing

Het tabblad **Processing** vermeldt de stappen van de documentverwerking voor uw organisatie en geeft aan of het werk doorstroomt of achteroploopt.

| Column | Description |
|--------|-------------|
| **Process** | De verwerkingsstap: Document Processing, OCR, TR-OCR, Barcode Split, Barcode Extraction, Extraction en PO Match. |
| **Last run** | Hoe lang geleden de stap voor het laatst liep. Beweeg de muis erover voor de exacte tijdstempel. **Never run** betekent dat er nog geen document bij deze stap is aangekomen. |
| **Status** | Een of meer badges (zie hieronder). |

De statusbadges zijn onafhankelijke signalen:

* Rode badge **Errors (N)**: `N` documenten zijn bij deze stap onlangs mislukt.
* Gele badge met een aantal: `N` documenten worden op dit moment door deze stap verwerkt.
* Groene badge **OK**: geen recente fouten en niets in de wachtrij.

Omdat fouten en lopend werk apart worden geteld, kan een stap beide tegelijk tonen; een fout blijft dus zichtbaar terwijl andere documenten nog lopen.

## Scheduled Tasks

Het tabblad **Scheduled Tasks** vermeldt de terugkerende achtergrondtaken die DocBits draaiende houden, bijvoorbeeld cacheverversingen, statuswaarschuwingen, documenttime-outs en uitgaande synchronisaties. Elke rij toont of de taak op tijd wordt uitgevoerd.

| Column | Description |
|--------|-------------|
| **Task** | De naam van de geplande taak, waarbij scheidingstekens door spaties zijn vervangen. |
| **Last run** | Hoe lang geleden de taak voor het laatst liep. Beweeg de muis erover voor de exacte tijdstempel. **Never run** betekent dat de taak nog niet is uitgevoerd. |
| **Status** | Gezondheid van het schema (zie hieronder). |

| Status | Meaning |
|--------|---------|
| **On schedule** (groen) | De taak loopt volgens het verwachte interval. |
| **Delayed** (rood) | De taak is niet op het verwachte moment gelopen. Onderzoek dit of meld het bij de support. |
| **Unknown** (grijs) | De status van het schema kon niet worden vastgesteld. |

Beide tabellen hebben een knop **Refresh** die de actuele cijfers op verzoek opnieuw laadt.
