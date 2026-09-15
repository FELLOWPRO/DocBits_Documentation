# DocBits Release-opmerkingen — 15 september 2026

_Wat er verandert met de DocBits-productiehotfix van 15 september 2026 (release
R1.0.13), inclusief alles sinds de release van 1 september. Elke service
vermeldt de versie die wordt uitgerold, gevolgd door wat er nieuw of opgelost
is — in gewone taal. Services die niet zijn vermeld, hadden geen wijzigingen
die zichtbaar zijn voor klanten._

---

## Hoogtepunten

- **Eén set regels voor de dashboardzoekfunctie.** `field=value` betekent nu op
  elke zoekmachine exact deze waarde, `field:value` betekent bevat (met
  `value*` en `*value` voor begint-met en eindigt-op), en `field!=value` geeft
  ook documenten terug die helemaal geen waarde hebben. Een zoekopdracht zonder
  chip is een substring-zoekopdracht over elk veld, inclusief zakelijke
  identifiers. Het aantal resultaten en de resultatenlijst beschrijven dezelfde
  set documenten, en een zoekopdracht die tegen het resultatenvenster aanliep
  of zonder de volledige-tekstindex draaide, meldt dat in plaats van "compleet"
  te rapporteren. De eigen zoekverbinding van het dashboard (WebSocket)
  bereikte de volledige-tekstindex voorheen nooit; nu wel.
- **Leveranciers worden vaker herkend.** Wanneer één opzoekveld (btw-nummer,
  IBAN, leveranciersnummer) precies één leverancier oplevert, wordt die
  leverancier gebruikt, ook als een breed veld zoals de naam met meerdere
  overeenkomt. XRechnung CII- en Facturae-documenten leveren hun
  leveranciersvelden weer. Waar stamgegevens een geëxtraheerde waarde hebben
  vervangen, meldt het validatiescherm dat en kunt u het origineel herstellen.
- **Purchase order matching legt zichzelf uit.** Het scherm geeft aan waarom
  er geen match is en waarom een match niet is behouden, de matching
  geschiedenis vermeldt de transformatieregels die zijn uitgevoerd, en PO
  eenheidsprijzen worden afgeleid van het nettobedrag. Handmatige matches
  werken weer voor organisaties zonder fallback regel, en een afgebroken
  matchingtaak markeert het document als mislukt in plaats van het eindeloos in
  "Queue" te parkeren.
- **Vastgelopen documenten en onterechte fouten.** Bij organisaties die continu
  uploaden werden documenten teruggezet naar een wachtrijprioriteit die tijdens
  kantooruren nooit werd bediend (866 documenten vast in "new" bij één klant).
  Een retry-sweeper kon een succesvol geëxporteerd document uren later
  overschrijven met "error" en daarvoor de exportfout-mail versturen. Dat pad
  is gesloten.
- **Touchless Intelligence.** Het Analytics-tabblad dat meet hoeveel documenten
  DocBits doorlopen zonder menselijke tussenkomst, krijgt zijn volledige eerste
  release: issue-clusters met AI-advies, bulkanalyse, wijzigingsvoorstellen met
  voorbeeld, toepassen en ongedaan maken, een AI-diagnose per leverancier en
  een pijplijnstroomdiagram per document.
- **Sneller waar de gegevens groot zijn.** De accounting-keuzelijst werkt voor
  organisaties met meer dan 2.000 rekeningen, de E-Documents-regelpagina
  pagineert haar 1.600 regels op de server in plaats van de browser te
  bevriezen, en Refresh op het purchase order dashboard geeft verse gegevens
  terug in plaats van een gecachte lijst.
- **Beveiliging.** Frontend source maps worden niet langer met elke deploy
  uitgeleverd, filters van de stamgegevens-lookup worden als SQL-parameters
  gebonden in plaats van geïnterpoleerd, een verlopen token wordt ook bij een
  cachehit geweigerd, en de organisatiecontrole op het verwerkingstoken wordt
  onafhankelijk van de laag ervoor afgedwongen.

---

## Web App — `10.66.3`

### Aanmelden en accounts

- De overlay "Updating DocBits v10.59.3.1 → v10.59.3.1" die op sandbox
  eindeloos bleef herladen, is opgelost. Een herlaad naar dezelfde versie toont
  de overlay niet meer, de lus is per tabblad begrensd, en een banner biedt
  handmatig herstel als het toch nog eens gebeurt.
- Het selectievakje System Admin kan worden aangevinkt bij een bestaande
  gebruiker. Een systeembeheerder aanmaken vanuit de frontend heeft nu effect;
  een synchronisatietaak zette de vlag voorheen bij elke run terug.

### Dashboard en zoeken

- Nieuwe operatorregels, ook beschreven in de zoekhulp-popup: `=` is exact deze
  waarde (hoofdletterongevoelig), `:` is bevat, `: value*` begint met,
  `: *value` eindigt op, `!=` is alles wat niet exact deze waarde is, inclusief
  documenten zonder waarde. Aanhalingstekens groeperen alleen een waarde met
  spaties.
- Een zin tussen aanhalingstekens zoals `"Johnson and Johnson"` wordt als één
  zin gezocht. "and" en "or" binnen aanhalingstekens worden niet langer als
  verbindingswoorden gelezen.
- Wanneer een kale zoekopdracht niets vindt, legt het dashboard de regel uit en
  biedt het chips met één klik aan (`Invoice number : <term>`,
  `Purchase order : <term>`, `Supplier ID : <term>`).
- Een zoekopdracht met nul resultaten zet de paginering terug. Voorheen hield
  de paginering het aantal van de vorige zoekopdracht vast.
- Aanvraagnummers en aanvragers (requisition number, requisitioner) worden
  gevonden met een gewone zoekopdracht, zonder chip.

### Validatiescherm

- Waarden die door stamgegevens zijn vervangen, worden gemarkeerd. Een
  amberkleurige badge toont de oorspronkelijke en de huidige waarde, de dataset
  en hoe die is gematcht, en een knop herstelt de geëxtraheerde waarde. Waarden
  die door stamgegevens zijn bevestigd of vanuit de purchase order zijn
  ingevuld, krijgen hun eigen labels. Voorheen droegen ze allemaal de badge
  "Extracted using saved rules".
- De goedkeuringsstempel wordt ook opgeslagen wanneer de pagina al een andere
  annotatie bevat. Gedownloade geannoteerde documenten misten in dat geval de
  stempel.
- "Hide non mapped columns" behoudt kolommen die u handmatig hebt getraind
  (bijvoorbeeld Item Number en Purchase Order).
- Extractieregels opslaan werkt nadat u een paginanummer typt en daarna een
  kader voor een veld tekent. Die volgorde liet het opslaan voorheen crashen.
- Train Model draait op de achtergrond. Het scherm toont "training started",
  vraagt het resultaat periodiek op en meldt succes of mislukking. Grote
  organisaties kregen voorheen een gateway-fout terwijl de training server-side
  gewoon doorliep.
- Donkere modus: de schaarcursor op het splitsscherm en de modusschakelaar op
  het Auto Accounting-scherm zijn weer leesbaar.

### Purchase order matching

De wijzigingen die zijn aangekondigd in [Hotfixes 8 september 2026](incremental-updates-8-september-2026.md)
bereiken productie met deze release: de match blijft behouden na opslaan,
matching wordt opnieuw uitgevoerd wanneer het PO nummer wordt gecorrigeerd, het
scherm geeft aan waarom er geen match is en waarom een match niet is behouden,
de matching geschiedenis toont de transformatieregels, en de PO eenheidsprijs
wordt berekend uit het nettobedrag. Daarnaast:

- De knop Auto Match exporteert het document ook wanneer "PO Auto Match and
  Export" is ingeschakeld. Voorheen vond de export alleen plaats wanneer het
  document vanuit het dashboard via "PO Match" werd geopend.
- De pop-up voor de tolerantie op hoeveelheid/eenheidsprijs blijft open
  wanneer de server het opslaan weigert, zodat de ingevoerde waarden niet
  verloren gaan.
- De knop Refresh op het purchase order dashboard wist de server-side cache
  voordat de lijst opnieuw wordt geladen. Een purchase order die vanuit het ERP
  was geïmporteerd, verscheen pas na zeven à acht minuten.

### Auto Accounting

- Organisaties met meer dan 2.000 rekeningen doorzoeken de rekeninglijst op de
  server. De keuzelijst was op sandbox leeg voor zulke organisaties, en het
  laden van de pagina duurde vijf seconden.
- Rekeningen waarnaar een document verwijst, worden in batches opgehaald: een
  document met 100 regels en twee splitsingen per regel heeft 4 verzoeken nodig
  in plaats van 403.
- De koppen van de Auto Accounting- en PO-tabellen volgen het label dat in de
  Layout Builder is ingesteld in plaats van een vaste tekst.

### Instellingen

- Instellingen → E-Documents → Rules pagineert, doorzoekt en sorteert de
  catalogus van 1.600 regels op de server. Het tabblad renderde voorheen elke
  regel tegelijk en bevroor de browser. "Reset all" is één aanroep in plaats
  van één per regel.
- De Advanced Settings van een documenttype tonen de opgeslagen stand van elke
  schakelaar. Een opgeslagen `false`, een tolerantie van `0` of een lege
  keuzelijst werden vervangen door de standaardwaarde, en bij het wisselen van
  documenttype bleven de waarden van het vorige type staan.
- Transformatieregels: een actie "Set value" wordt opgeslagen. De editor
  verstuurde die onder een naam die de server weigert.
- De link naar documentsubtypen wordt getoond bij standaard documenttypen.
- De JPL-mapping van de SMB-export wordt gedownload als `.properties`, zodat
  het bestand opnieuw kan worden geüpload. Het heette `.xml` en werd bij het
  terugladen geweigerd.

### Workflows

- Het hernoemen van een workflow behoudt de kaartwijzigingen die in dezelfde
  sessie zijn gemaakt. Nieuwe workflows worden in één opslagverzoek aangemaakt,
  en hernoemingen van sjablonen worden bewaard.
- Een geëxporteerd workflowbestand bevat de volledige exportenvelop (versie,
  naam, beschrijving). Geavanceerde workflows kunnen weer worden geïmporteerd;
  voorheen verloor het bestand zijn versie, werd het teruggelezen als
  standaardworkflow en geweigerd.
- Kolomfilters in de workflowlijst worden gecombineerd met AND. Met een naam-
  en een datumfilter actief slopen rijen die alleen op de naam overeenkwamen in
  het resultaat.
- Taakdeadlines gebruiken het datumformaat uit uw gebruikersinstellingen in de
  lijst, het bord en de detailweergave.

### Analytics: Touchless Intelligence

Het tabblad Touchless (Analytics → Touchless) meet hoeveel documenten DocBits
doorlopen zonder dat iemand ze aanraakt, en waarom de andere dat niet deden.
Deze release maakt het compleet:

- **Issue-clusters met bewijs.** Documenten die een handeling nodig hadden,
  worden gegroepeerd op oorzaak. Elke clusterkaart benoemt de velden,
  validatiecodes en foutmeldingen waarop het misgaat, en de leverancier, of
  meldt dat er geen is. Clusters die DocBits kan oplossen (een regel, een
  veldinstelling) worden gescheiden van clusters die alleen de leverancier kan
  oplossen, en het AI-analysebudget gaat eerst naar de oplosbare.
- **AI-analyse, als zodanig gelabeld.** Een clusterkaart geeft aan of een
  taalmodel het advies schreef of een regel, wat de analyse heeft geteld en
  wanneer die niet meer klopte, en of een klik een gecachte analyse hergebruikt.
  Als de AI-adviseur in deze omgeving niet kan draaien, meldt het tabblad
  waarom.
- **Bulkanalyse.** Analyseer veel clusters in één run, zie cluster voor cluster
  wat de run doet, en vind de resultaten achteraf terug. De resultatenlijst
  overleeft navigatie en herladen, en de run blijft niet langer hangen op
  "Running · 0/6 done" in een suborganisatieweergave.
- **Wijzigingsvoorstellen.** Een aanbeveling wordt iets waarop u kunt handelen:
  een voorstel dat het veld aanpakt dat de documenten blokkeert, een voorbeeld
  dat toont wat het zou doen (er wordt niets opgeslagen), toepassen, gemeten
  effect en ongedaan maken. Agents bereiken dezelfde stappen via MCP-tools.
  Oplossingsstappen linken rechtstreeks naar de instellingenpagina die ze
  noemen, voorgefilterd op documenttype, veld of regel.
- **Leveranciersdiagnose.** De leverancierspagina legt een lege toestand uit in
  plaats van nullen te tonen, en biedt een AI-diagnose per leverancier. Tot
  vijf leveranciers kunnen worden geselecteerd en naast elkaar vergeleken.
- **Pijplijnstroom.** Een diagram per document en per cluster toont het pad
  door intake, classificatie, e-documentcontrole, leverancier, OCR, extractie,
  validatie, PO matching, goedkeuring en export, met de fase waar het is
  gestopt.
- **Redenen bij purchase order matching.** De matchingbeslissing wordt per
  document getraceerd (fase, doorgang, regel, kolom) en samengevat in het
  Touchless-resultaat. Redencodes maken onderscheid tussen "purchase order niet
  gevonden", "regel komt niet overeen" en "verplicht veld ontbreekt", en de
  tolerantievoorstellen van de adviseur richten zich op de rule engine die
  beslist.
- **Correcte cijfers.** KPI-tegels respecteren het suborganisatiefilter en
  tellen alleen documenten die de drill-down kan tonen.

### DocNet

- De Activities-feed, de widget Recent Activity en de missietijdlijn zijn
  vertaald. Auditsamenvattingen waren in alle 22 talen Engels.
- Agents zien velden die het documenttype definieert maar die de extractie leeg
  liet. Ze concludeerden voorheen dat zulke velden niet bestonden en sloegen
  verplichte updates over zonder een schrijfpoging te doen.

### Beveiliging

- Frontend source maps worden uit elke deploy verwijderd. Elke omgeving
  serveerde ze, productie inbegrepen.

---

## API Service — `12.83.156`

### Leveranciersherkenning en stamgegevens

- Een leverancier wordt geïdentificeerd wanneer één opzoekveld uniek is. Met
  meerdere doorzoekbare velden werden de resultaten als een unie gecombineerd,
  zodat een brede naammatch met vier leveranciers een btw-nummer dat precies
  één leverancier opleverde, overstemde. Velden die nergens mee overeenkomen,
  blokkeren niet langer de velden die dat wel deden. Zie
  [Mastergegevensinstellingen](../../administration-and-setup/settings/global-settings/document-types/fields/master-data-settings.md)
  voor hoe de velden samenwerken.
- Vervangingen door stamgegevens worden vastgelegd met hun herkomst: dataset,
  configuratie, bronveld, operator en soort match. Het validatiescherm toont
  dit en kan de geëxtraheerde waarde herstellen.
- Cash Discount Term wordt geïmporteerd uit de leveranciers-BOD; bij
  leveranciers die via het ERP zijn gesynchroniseerd was het leeg. Een Discount
  Term Overwrite die als volledige code is ingevoerd ("143", "012", "X08")
  wordt toegepast; voorheen werd alleen het procentvoorvoegsel geraadpleegd.
- Stamgegevens-lookups zijn begrensd op 1.000 rijen per pagina en pivoteren in
  SQL. Een lookup van 19.000 records kostte vijf seconden per aanroep en
  blokkeerde de API.
- Filtereigenschapsnamen en gegevenstypen in de stamgegevens-lookup worden als
  SQL-parameters gebonden. Ze werden in de query geïnterpoleerd.

### Documentverwerking

- Documenten van een organisatie die continu uploadt, werden teruggezet naar
  prioriteit 9, die de wachtrij alleen bedient wanneer elke hogere prioriteit
  leeg is. De verlaging is nu begrensd op 3. De reconciler die vastgelopen
  documenten opnieuw in de wachtrij moet zetten, had in productie geen werkende
  credentials; nu wel.
- Een afgerond, geëxporteerd document wordt nooit overschreven met "error". Een
  workflowvlag die nooit werd gewist, liet de retry-sweeper een succesvol
  geëxporteerd document elke minuut oppakken totdat de retry-limiet het als
  "error" stempelde en de exportfout-mail van de klant verstuurde, 2 u 17 min
  na de export.
- Samenvoegen en toevoegen accepteert `.PDF`- en `.Pdf`-bestanden.
  Scanneruitvoer met de naam `SCAN0001.PDF` werd geweigerd met "Only PDF files
  are allowed."
- Cache-invalidatie doorloopt de sleutelruimte één keer in plaats van twee keer
  en wist alleen de lookup-gegevenstypen die een BOD heeft gewijzigd. Elke BOD
  wiste voorheen de hele lookup-cache van de organisatie en blokkeerde de API
  terwijl die ieders sleutels doorliep.
- Het opnieuw trainen van een model draait als achtergrondtaak en geeft direct
  een status terug die de UI periodiek opvraagt.
- Een verwerkingstoken van een andere organisatie wordt geweigerd, onafhankelijk
  van de controle op suborganisatielidmaatschap ervoor.
- De gebruikerssynchronisatie laat de systeemgebruikersvlag met rust in plaats
  van die bij elke run terug te zetten.

### Export

- M3-ontvangstregels koppelen de geëxporteerde eenheidsprijs aan de eigen
  prijsbasis van de factuurregel. De prijs reisde mee met de deler van de PO
  regel en het ERP herprijsde de regel op 1.000 keer het gefactureerde bedrag.
- Een tabelexport overleeft een regel waarvan de purchase order is verwijderd;
  de regel wordt zonder prijsbasis geëxporteerd.

### E-documenten

- XRechnung CII-facturen waarvan het te betalen bedrag 0,00 is omdat een
  vooruitbetaald bedrag het totaal compenseert, tonen het eindtotaal (BT-112)
  als totaalbedrag. De klant zag "total amount 0,00".
- XRechnung CII- en Facturae-documenten leveren hun leveranciersvelden weer.
  Verouderde overschrijvingen op organisatieniveau overschaduwden de juiste
  standaardmapping, waardoor leveranciersherkenning nooit kon matchen.
- De catalogus met validatieregels wordt op de server gepagineerd, doorzocht en
  gesorteerd, met facetten voor de filterbalk.

### Classificatie

- Zwitserse documenten worden op basis van hun inhoud (CHF-bedragen,
  CHE-btw-nummers, CH-IBAN) geclassificeerd als `de_CH`, `fr_CH` of `it_CH`.
  De landinstelling werd overgenomen van de organisatiestandaard en Zwitserse
  documenten kregen `de_DE`.

### Dashboardzoekfunctie

- Eén operatorsemantiek op Postgres en ClickHouse: `=` exact, `:` bevat met
  wildcards aan de randen, `!=` complement inclusief lege waarden. Op Postgres
  was `=` voorheen een prefixmatch, zodat `invoice_id=911892112` ook
  911892112333 teruggaf.
- Een kale zoekopdracht is een substring-zoekopdracht over elk veld, inclusief
  zakelijke identifiers. Een identifier met koppelteken zoals `2026-003` is één
  letterlijke waarde, en het clausuletype verandert niet meer na het vijfde
  teken.
- De factuurnummer-chip is exact op Postgres, zoals die op de index al was.
  Voorloopnullen, float-vormen en hoofdletters worden in vrije tekst en in
  chips hetzelfde behandeld.
- De WebSocket-zoekopdracht van het dashboard geeft de credential van de
  aanroeper door aan de volledige-tekstservice. Elke delegatie werd voorheen
  geweigerd, zodat het dashboard stilzwijgend alleen Postgres doorzocht en het
  antwoord als compleet presenteerde.
- Het aantal resultaten en de resultatenlijst draaien op één set predicaten.
  Het aantal was voorheen een Postgres-benadering terwijl de lijst uit de index
  kwam.
- Vectorzoeken is begrensd op het werkelijke resultatenvenster en meldt die
  grens in plaats van "(50)" als exact totaal te tonen.
- Een zoekopdracht die zonder de volledige-tekstindex draaide (index minuten
  achter, capability-lookup mislukt, verminderde veldresolutie) meldt haar
  vensterstatus in plaats van "compleet".
- Documentscripts die de volledige-tekstzoekfunctie aanroepen, authenticeren
  correct en tonen fouten in plaats van een leeg resultaat terug te geven.

### Purchase order matching (in-process matcher)

Voor organisaties die in de API matchen in plaats van in de PO Match Service:
een gecorrigeerd PO nummer wordt gematcht in de opslag die het corrigeert.

### Analytics

- Touchless: alle backend-wijzigingen achter de Web App-sectie hierboven,
  inclusief fasebewijs dat elke pijplijnfase vastlegt, de PO-match-trace,
  wijzigingsvoorstellen met voorbeeld, toepassen en terugdraaien, en bulkstatus
  in één aanroep per tik.

---

## PO Match Service — `1.59.34`

- De eenheidsprijs van een PO regel wordt afgeleid van het nettobedrag, niet
  van het totaal inclusief belasting, en de PO-snapshot van een document leidt
  zijn eenheidsprijzen opnieuw af op het moment van matchen.
- De service registreert waar elke PO nummer-kandidaat vandaan kwam en welke
  nummers een run heeft opgezocht. Het eigen factuurnummer van een document is
  nooit een PO kandidaat. Een gevallen match laat zijn reden achter op het
  document voor het scherm.
- Handmatig matchen werkt voor organisaties waarvan de regels geen
  `is_fallback`-vlag dragen. Gebruikers selecteerden regels, drukten op match,
  en er kwam niets terug.
- Geen documenten meer verweesd in "Queue": database statement timeouts,
  keepalives en een expliciete soft-time-limit-handler markeren de taak als
  mislukt in plaats van te vertrouwen op een kill die geen spoor achterliet.
- Tolerantiewijzigingen worden per matchingverzoek gelezen, zodat een zojuist
  opgeslagen tolerantie door de volgende match wordt gebruikt.
- De beslissingstrace in vijf fasen wordt per document bewaard voor Touchless.

---

## Auth Service — `1.78.27`

- Tokenverloop wordt afgedwongen bij cachehits. Een gecachte vermelding kon tot
  negen uur na het verlopen van het token nog authenticeren.
- Tokenverificatie schrijft niet langer bij elk verzoek een ongewijzigd
  `org_id` terug naar de gebruikersrij, wat een UPDATE per aanroep opleverde.
- Een geheugenlek dat de autoscaler naar het maximale aantal replica's dreef,
  is opgelost, en de service draait weer met twee workers.
- De systeemgebruikersvlag kan worden gewijzigd bij een bestaande gebruiker
  wanneer geen ander lid die heeft.

---

## Auth Bridge Service — `0.5.7`

- Wanneer de EU ↔ VS-replicatiestroom wegvalt, wordt het replicatieslot ter
  plekke opnieuw gekoppeld in plaats van de bridge te herbouwen en de volledige
  opstart-reconciliatie opnieuw uit te voeren, waarbij het slot inactief bleef.

---

## Extraction Service — `1.55.33`

- AI-tabelextractie: bedragkolommen worden getypeerd als getallen met een
  beschrijving, en verzonnen niet-numerieke waarden in bedragkolommen (een
  "St." die vanuit de naastgelegen cel naar eenheidsprijs per is gekopieerd)
  worden verwijderd in plaats van opgeslagen.
- Amerikaanse facturen: float-ruis onder de cent bepaalt niet langer de keuze
  tussen kandidaat-paren netto/belasting (268.28 + 22.13 verloor van netto =
  totaal, belasting = 0).

---

## Fulltext Service — `1.42.35`

- De zoekresultatencache staat in elke omgeving aan; productie, sandbox en
  stage draaiden er zonder sinds de actieve env-bestanden zijn aangemaakt.
  Uploaden en verwijderen maken de cache ongeldig, zodat een zoekopdracht na
  een upload het nieuwe document ziet.
- Een gewone zoekopdracht op een kaal factuurnummer geeft de exact
  overeenkomende factuur terug. Uitgeschreven valutawaarden, verouderde
  boolean-mappings, datums en belastingvlaggen overleven de rebuild van de
  slanke index, en indexvermeldingen zonder velden worden gedetecteerd en
  hersteld vanuit de extractie.
- Exact `=` op een dynamisch tekstveld vergelijkt alleen de volledige waarde.
  Een wildcard op het geanalyseerde pad liet `note_field=53173` overeenkomen
  met "PO 53173 / 2024".
- Een kale identifier met koppelteken zoals `2026-003` is één letterlijke
  waarde, geen verzameling tokens.
- Leespaden maken niet langer de index aan die ze lezen, en elk antwoord zonder
  treffers draagt een vensterstatus en een reden.
- De service-side limiet van 50 bij vectorzoeken is verdwenen.

---

## Docflow Service — `2.10.11`

- Imports van geavanceerde workflows worden gecontroleerd tegen de rechten van
  de organisatie, en een batch wordt gecontroleerd voordat er iets wordt
  geschreven. Een organisatie zonder de geavanceerde module kon een
  geavanceerde workflow importeren die ze vervolgens niet kon openen.
- Een workflowhernoeming gaat mee met de opslag, en hernoemingen van sjablonen
  worden bewaard.

---

## Docnet Service — `1.56.12`

- Velddetectie geeft elk headerveld terug dat de layout definieert, gevuld of
  niet, en komt overeen met wat de schrijfbeveiliging controleert. Agents
  sloegen verplichte veldupdates over omdat lege velden afwezig leken.
- Identiteiten worden gecachet onder dezelfde organisatiegebonden sleutel die
  de API gebruikt, zodat de API-sleutelgrens van de organisatie over beide
  services standhoudt.

---

## Email Service — `1.41.6`

- Gedeelde Office 365-mailboxen met meer dan tien submappen herleiden elke map.
  Microsoft Graph pagineert mappen per tien; de 11e en latere configuraties
  mislukten bij elke poll met "unable to find the selected Folder".

---

## FTP Service — `1.32.18`

- De SFTP-planner start in elk workerproces in plaats van vóór de fork.
  Periodieke SFTP-imports mislukten stilzwijgend met een beschadigde
  plannerstatus, terwijl een vers proces prima werkte.

---

## Auto Accounting `1.21.7`, Barcode `1.18.14`, OCR `1.10.11`, Operator `1.42.12`, Ideas `0.3.6`

Alleen build- en deploymentwijzigingen (update van de basisimage,
CI-credentials). Geen gedragswijziging.

<!-- Release R1.0.13. Announced: tickets with Jira "Release No." = R1.0.13 and a
     status on sandbox or beyond, plus DOCB-14454, DOCB-14450, DOCB-14415,
     DOCB-14419, DOCB-14431, DOCB-14045/46 (no Release No., on sandbox).
     Held back (Release No. R1.1): DRFS-778, DRFS-712, MEF-165, MEF-166, DOCB-14389.
     Labelled R1.0.12 but code ships now: DRFS-746/748/749/750/751, DOCB-14282. -->
