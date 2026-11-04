# Het dashboard gebruiken

### Filters

| Filter | Wat het doet |
| --- | --- |
| **7D / 30D / 90D** | De periode voor de kerncijfers en de wachtrij. De standaardwaarde is 30 dagen |
| **Documenttype** (Document Type) | Filtert Touchless-metrieken en analyse op type. Geleerde regelvoorstellen hebben momenteel een eigen keuze; zie hieronder. |
| **Segmentveld / Segmentwaarde** (Segment field / Segment value) | Alleen als uw organisatie meerdere processen via één documenttype laat lopen (bijvoorbeeld directe, indirecte en EAM-bestellingen in het veld `order_type`). Kies een veld om de verdeling te zien, kies een waarde om alles daartoe te beperken |
| **Document-ID** (Document ID) | Opent het **Documentspoor** van één document |

De **suborganisatie** die u bovenaan in DocBits hebt gekozen, beperkt de kerncijfers en de leverancierswachtrij. Probleemclusters en de AI-analyse beslaan altijd de hele organisatie.

### Documenttype en geleerde regelvoorstellen

De bovenste keuze en die voor geleerde regels werken in de gecontroleerde implementatie onafhankelijk. De regelsectie laadt eigen typen en kiest eerst het eerste type. **ORDER_CONFIRMATION** bovenaan kan daardoor samengaan met **INVOICE** onderaan: die regels gelden voor facturen. Controleer het lokale type vóór toepassing. Ontbreekt het gewenste type, dan zijn daarvoor geen voorstellen aangetoond. De correctiesteekproef van bijvoorbeeld 60 dagen volgt niet automatisch het tijdvak bovenaan. Dit beschrijft de huidige beperking; synchronisatie is niet geïmplementeerd.

### De vijf kerncijfers

<figure><img src="../.gitbook/assets/touchless-report-kpi-nl-20261104.png" alt="Huidig factuurrapport over 30 dagen: 107 volledig automatische facturen plus 11 met alleen goedkeuring vormen 118 van 201, oftewel 58,7 % AP Touchless. Pure afzonderlijk is 53,2 %. De AP-kaart toont al het gecombineerde aantal 118. Fictieve trainingshistorie; dit bewijst geen uitgevoerde ERP-export."><figcaption><p>Huidig factuurrapport over 30 dagen: 107 volledig automatische facturen plus 11 met alleen goedkeuring vormen 118 van 201, oftewel 58,7 % AP Touchless. Pure afzonderlijk is 53,2 %. De AP-kaart toont al het gecombineerde aantal 118. Fictieve trainingshistorie; dit bewijst geen uitgevoerde ERP-export.</p></figcaption></figure>

| Kaart | Wat telt mee? | Huidige opname |
| --- | --- | --- |
| Pure Touchless | Succesvol afgerond zonder ingreep of goedkeuring | 107 · 53,2 % |
| AP Touchless | Pure plus alleen goedkeuring; gecombineerd percentage en aantal | 118 · 58,7 % |
| AP Assisted | Succesvol afgerond met een handmatige ingreep | 37 · 18,4 % |
| Procesuitzonderingen | Uitkomst die als uitzondering is ingedeeld | 46 · 22,9 % |
| Diagnosedekking | Geblokkeerde gevallen met een bekende oorzaak | 100 % · 0 zonder bekende oorzaak |

* Een kaart toont een streepje (—) in plaats van **0 %** als er niets te meten is. Een streepje betekent "geen gegevens", niet "nul".
* **Diagnosedekking** = documenten met een bekende blokkeringsreden ÷ alle geblokkeerde documenten. Voorbeeld: 50 geblokkeerde documenten, 10 met een onbekende oorzaak → 40 ÷ 50 = **80 %**. Een lage waarde betekent "we begrijpen nog niet waarom documenten stoppen". Verbeter die eerst voordat u afzonderlijke oorzaken probeert op te lossen.
* **Klik op een kaart** om de documentenlijst achter het cijfer in een nieuw tabblad te openen ("View the documents behind this number", de documenten achter dit cijfer bekijken). Kaarten met 0 documenten zijn niet klikbaar.

### Touchless-percentage in de tijd

<figure><img src="../.gitbook/assets/touchless-report-trend-nl-20261104.png" alt="Huidige trend: roze toont Pure Touchless; blauw het gecombineerde percentage inclusief alleen goedkeuring. De stippellijn geeft het doel van 70 % aan. Deze fictieve trainingsgevallen bewijzen geen werkelijke procesverbetering."><figcaption><p>Huidige trend: roze toont Pure Touchless; blauw het gecombineerde percentage inclusief alleen goedkeuring. De stippellijn geeft het doel van 70 % aan. Deze fictieve trainingsgevallen bewijzen geen werkelijke procesverbetering.</p></figcaption></figure>

De huidige grafiek toont Pure, gecombineerd AP en het doel. Blauw omvat Pure en alleen goedkeuring en ligt dus op of boven roze; tel de twee percentages niet op. Elk punt gebruikt zijn eigen aantal afgeronde, meetellende documenten: een dagpercentage is niet automatisch het percentage over de hele periode. Korte perioden tonen dagpunten, lange perioden weekpunten. De afzonderlijke uitkomstcategorie alleen goedkeuring verschilt van deze gecombineerde lijn.

**Voorbeeld.** Pure van 55 naar 68 % na een wijziging toont een verband in de tijd. Vergelijk type, leveranciers en andere wijzigingen; voor/na bewijst op zichzelf geen enkele oorzaak.

### Waar touchless het eerst verloren gaat

<figure><img src="../.gitbook/assets/touchless-blocking-stages-nl.png" alt="Staafdiagram van de geblokkeerde documenten per eerste blokkeringsfase en reden"><figcaption><p>Geblokkeerde documenten naar de fase en reden waar ze het eerst stopten. Hier kost <strong>Veldvalidatie: verplicht veld ontbreekt</strong> de meeste documenten (58), gevolgd door <strong>Exportmapping mislukt</strong> (46) en <strong>PO-regel komt niet overeen</strong> (27). Voorbeeldorganisatie met demogegevens; de namen van leveranciers zijn fictief.</p></figcaption></figure>

Een staafdiagram van **Geblokkeerde documenten** per pipelinefase: de **eerste** fase die een document stopte.

**Voorbeeld.** Bij leverancierherkenning 12, veldvalidatie 41 en orderregelvergelijking 7 onderzoekt u eerst de validatie. Niet uitgelezen waarden zijn slechts één mogelijke oorzaak: vergelijk origineel, regels en brongegevens voordat u de oorzaak bevestigt.

### Leverancierskansen



De wachtrij beantwoordt de vraag **"Welke leverancier pakken we eerst aan?"** Ze is gesorteerd op **Herstelbare** documenten, het hoogste eerst, 25 rijen per pagina.

| Kolom | Betekenis |
| --- | --- |
| **Leveranciersnummer / Leverancier** | De leverancier. Documenten zonder herkende leverancier verschijnen als **No supplier identified (n documents)** (geen leverancier geïdentificeerd) |
| **Volume** | In aanmerking komende documenten van de leverancier in de periode |
| **Puur percentage** (Pure Rate) | Aandeel puur touchless documenten. Groen bij of boven het doel, rood eronder |
| **Verloren documenten** (Lost Documents) | Documenten die eindigden als AP ondersteund of als procesuitzondering. Niet altijd een persoon: een ERP-afwijzing of een document dat zeven dagen bleef steken telt ook mee |
| **Hoofdoorzaak** (Root Cause) | Wie de oplossing in handen heeft: Configuratie, ERP-integratie, Export, Extractie, Stamgegevens, Meting, PO-matching, Gebruikersproces, Validatie of Onbekend |
| **Herstelbaar** (Recoverable) | Verloren documenten waarvan de oorzaak door DocBits kan worden opgelost: configuratie, stamgegevens of leverancierssjabloon |
| **Verwachte stijging** (Expected Lift) | Hoeveel **procentpunten** het percentage van uw organisatie zou stijgen als elk herstelbaar document van deze leverancier touchless zou lopen (**+x pp**) |
| **Betrouwbaarheid** (Confidence) | **Hoog**, **Gemiddeld** of **Laag**: hoe zeker de diagnose is |
| **Status** | Nieuw, Open, In onderzoek, In uitvoering, Bevestigd, Opgelost, Afgewezen. Een leverancier met te weinig documenten toont **NEEDS_DIAGNOSIS** |

**Voorbeeld.** Uw organisatie heeft 1.000 in aanmerking komende documenten in de periode. Leverancier A heeft 40 herstelbare documenten, leverancier B heeft 90 verloren documenten maar slechts 10 herstelbare (hun probleem ligt aan hun kant).

* Leverancier A: 40 ÷ 1.000 = **+4,0 pp verwachte stijging**
* Leverancier B: 10 ÷ 1.000 = **+1,0 pp**, hoewel B meer verloren documenten heeft

De wachtrij plaatst A boven B omdat de **verwachte stijging** wordt afgemeten aan uw hele organisatie, niet aan de leverancier. Een leverancier met vier slechte documenten kan er niet boven komen te staan bij een leverancier met vierhonderd.

Gebruik het zoekvak ("Search supplier number or name", zoek op leveranciersnummer of naam) om een leverancier te vinden. Klik op een rij om de **Leveranciersdiagnose** te openen.

### Leveranciers vergelijken



Klik op **Leveranciers vergelijken** (Compare suppliers), vink **twee tot vijf** leveranciers aan (elk met zijn aantal geblokkeerde documenten) en klik op **Vergelijken** (Compare).

De vergelijking toont de leveranciers naast elkaar: **Puur percentage**, **Verloren documenten**, **Herstelbaar**, **Hoofdoorzaak**, **Verwachte stijging**, een staafdiagram van de uitkomsten en een link naar elke **Leveranciersdiagnose**.

**Voorbeeld.** A en B gebruiken dezelfde indeling; B heeft 80 % Pure en A 35 %. Wijst de diagnose naar stamgegevens, vergelijk dan originelen, extractie en geïmporteerde records. Het verschil bewijst niet dat de indeling correct of A’s stamgegevens onvolledig zijn.

### Analyseren met AI

De knop **Analyseer n clusters met AI** (Analyse n clusters with AI) analyseert de probleemclusters met het hoogste touchless-potentieel (elk met minimaal een bepaald aantal documenten). Het duurt ongeveer 13 seconden per cluster en omvat de **hele organisatie**. Alleen beheerders kunnen het starten.

Terwijl de analyse loopt, ziet u per cluster **Queued** (in de wachtrij), **Running** (bezig), **Done** (klaar), **Already analysed** (al geanalyseerd) of **Error** (fout), met een link **Cluster openen** (Open cluster). Als AI is uitgeschakeld of in de omgeving niet is geconfigureerd, is de knop uitgeschakeld met de reden, en **werkt al het andere op de pagina gewoon door**.

## Werken met Touchless Intelligence: een routine

1. **Wekelijks**: open het tabblad en controleer het **percentage** en de **trend** ten opzichte van het doel.
2. Kijk naar de **Diagnosedekking**. Onder ongeveer 80 % zoekt u eerst uit waarom documenten stoppen.
3. Lees **Waar touchless het eerst verloren gaat** en kies de grootste fase.
4. Open **Leverancierskansen**. Sorteer op **Verwachte stijging** en neem de bovenste leverancier met de status **RECOVERABLE**.
5. Lees de **probleemclusters**, controleer **Ontbrekend bewijs** en volg daarna **Wat te wijzigen**.
6. Herstel een bevestigde oorzaak. Gebruik voorbeeld en historie voor een ondersteund DocBits-voorstel. Leg Infor-bronherstel en import apart vast; dit maakt niet automatisch een instellingswijziging in deze historie.
7. Controleer na twee weken het resultaat **voor/na**.

## Wie het kan zien

* Het tabblad maakt deel uit van het Analyse-dashboard. Uw beheerder schakelt het in voor de organisatie. Als het tabblad ontbreekt, vraag het dan aan uw beheerder.
* **Organisatiebeheerders** zien het altijd.
* Andere gebruikers zien het wanneer een beheerder hun rol het tabblad **Analytics dashboard** (Analyse-dashboard) heeft toegekend (**Instellingen → Rollen**). Zonder toekenning hebben alleen beheerders toegang.
* Sommige acties zijn alleen voor beheerders: **AI-analyse**, **een wijziging toepassen en ongedaan maken**, **voorstellen voor geleerde regels** en het **Adviesrapport**.

Als u geen toegang hebt, toont de pagina *Action not allowed, please contact the administrator* (actie niet toegestaan, neem contact op met de beheerder).

## Gerelateerde pagina’s

* [Touchless Intelligence](touchless-intelligence.md)
* [Metrieken en berekening](touchless-metrics.md)
* [Voorbeelden: prijs en aantal](touchless-examples.md)
* [Touchless Intelligence: Leveranciersdiagnose en probleemclusters](touchless-supplier-diagnosis.md)
* [Touchless Intelligence: PO-matchingdiagnose](touchless-po-matching-diagnosis.md)
* [Touchless Intelligence: Documentspoor](touchless-document-trace.md)
* [Touchless Intelligence: Wijzigingsvoorstellen en rapporten](touchless-change-proposals.md)
* [Touchless uitleggen en verbeteren met MCP](touchless-mcp.md)

<!-- Source notes (not shown): screenshots come from the dev test organisation with synthetic demo data (seed script) and fictional supplier names; the PO matching decision flow has no screenshot yet. facts read from the doc2app code (TouchlessIntelligence pages and components) and the dev UI on 14 Oct 2026; NOVA gates the tab with its own organisation flag, VESTA with the Analytics module. Consulting report export format not verified, so no export is described.

<!-- Alignment 2026-11-04: correct extraction is distinct from process Touchless; KPI numerator and denominator verified. -->
<!-- Completion 2026-11-04: localized MCP examples, AP actions, original-value evidence and owned synthetic PO cards. -->
