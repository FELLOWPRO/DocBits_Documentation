# DocBits Release-opmerkingen — 12–25 augustus 2026

_Wat er verandert met de DocBits-productie-upgrade van 25 augustus 2026,
inclusief alles sinds de release van 12 augustus. Elke service vermeldt de
versie die wordt uitgerold, gevolgd door wat er nieuw of opgelost is — in
gewone taal. Services die niet zijn vermeld, hadden geen wijzigingen die
zichtbaar zijn voor klanten._

---

## Hoogtepunten

- **Strengere organisatie-isolatie.** Een beveiligingsronde sloot
  verschillende plekken waar gegevens van de ene organisatie vanuit een andere
  konden worden gelezen of geschreven: documentscripts, gebruikerslijsten van
  suborganisaties, groepslidmaatschappen en het verwerkingstoken dat een
  document door de pijplijn draagt, worden nu allemaal gecontroleerd tegen de
  organisatie van de aanroeper. Goedkeuringen dwingen bovendien het
  vier-ogen-principe correct af: de tweede goedkeurder moet een andere persoon
  zijn dan de eerste.
- **Documenten blijven niet meer hangen.** Vier afzonderlijke oorzaken van
  documenten die eindeloos bleven hangen zijn opgelost: exports die na een
  afwijzing in "Exporting" bleven staan, herstarts die bevroren wanneer een
  verwerkingsstap crashte, barcodesplitsingen die nooit terugmeldden, en het
  accountingscherm dat bleef hangen op "Preparing…". In elk geval wordt het
  document nu óf afgerond, óf toont het een echte fout waarop u kunt handelen.
- **Creditnota's worden herkend als creditnota's.** XRechnung 3.0-, 3.0.1- en
  3.0.2-creditnota's in CII-syntaxis, pure CII-creditnota's en ZUGFeRD 2.4- /
  Factur-X 1.08-documenten worden nu allemaal correct geclassificeerd, met het
  totaal uit het juiste veld. Bij gescande documenten die zowel "factuur" als
  "creditnota" vermelden, wint het trefwoord dat het dichtst bij het
  documenttype staat, en bedragen worden weer positief wanneer u een
  creditnota terugzet naar factuur.
- **PO-matching rekent zoals u verwacht.** Toleranties worden vergeleken als
  exacte decimalen in plaats van floating-point-waarden, zijn gebaseerd op de
  waarde van de inkooporder, en facturen die naar meerdere inkooporders
  verwijzen, worden tegen al die orders gematcht. Kolommen die u nooit hebt
  toegewezen, vertekenen de controle op het regelbedrag niet langer, en
  wanneer verplichte kolommen ontbreken, benoemt de foutmelding ze.
- **Workflowruns behouden hun werk.** Een workflow die een veldwaarde
  schrijft, schrijft die nu zó op het document dat een latere export dat niet
  stilzwijgend kan terugdraaien. Opnieuw geprobeerde triggers gooien niet
  langer weg wat de run al had gedaan, en twee triggers op hetzelfde document
  sluiten netjes aan in de rij in plaats van elkaars vergrendeling af te
  pakken.
- **Wachtwoordreset-e-mails worden weer verzonden.** Ze verlieten de server
  stilzwijgend nooit. Het resetformulier toont bovendien echte feedback na het
  versturen, en het antwoord onthult niet langer of een account bestaat.

---

## Web App — `10.55.0`

### Aanmelden en accounts

- Wachtwoordreset werkt weer van begin tot eind: de mail komt aan, het
  formulier bevestigt de verzending, en het antwoord is hetzelfde ongeacht of
  het adres een account heeft.
- Afmelden in het ene browsertabblad meldt de andere tabbladen ook af, zonder
  de fout-toasts die verschenen wanneer tabbladen het oneens waren over de
  sessie.
- Als uw organisatie registratie voor twee-factor-authenticatie verplicht
  stelt, meldt het aanmeldscherm dat nu in plaats van zonder melding te
  mislukken. Aanmelden met een passkey over regio's heen toont vertaalde
  foutmeldingen, en de verzendknop is zichtbaar.
- Beheerders kunnen organisatiebrede MFA-verplichting niet langer inschakelen
  voordat registratie bij het aanmelden beschikbaar is, wat mensen voorheen
  kon buitensluiten.

### Validatiescherm

- De zoomschuif gaat nu tot 150% (voorheen stopte hij bij 80%), en inzoomen op
  een tabel werkt voorbij de containerbreedte in plaats van niets te doen.
- Lege bedragvelden tellen als 0 in plaats van een fout-toast te veroorzaken,
  en een dubbelklik op de documentafbeelding wordt genegeerd wanneer geen veld
  is geselecteerd.
- De banner die verschijnt wanneer een andere sessie de documentvergrendeling
  vasthoudt, had geen tekst; hij legt zichzelf nu uit. Het taggen van een
  tabel veroorzaakt niet langer een onterechte waarschuwing "document extern
  gewijzigd" over uw eigen wijziging.
- In de AI-tabel vraagt een kolomhertoewijzing die een andere kolom zou
  loskoppelen eerst om bevestiging, en waarden die geen getallen zijn, worden
  gemarkeerd in AMOUNT- en NUMBER-kolommen.
- Het tabblad "Extracted table" linkt weer naar handmatige tabeltraining
  wanneer het leeg is, en blijft niet langer eindeloos draaien wanneer er al
  een AI-tabel bestaat.
- Artikelnummers in de regelitemtabel van Compare worden getoond als
  identifiers, niet afgerond zoals bedragen.
- Goedkeurdervelden herleiden gebruikers- en groeps-id's tot namen, zodat ze
  nooit een ruwe id tonen of leeg blijven. Taakdeadlines worden via één
  UTC-bewust pad geconverteerd, zodat elke kijker dezelfde datum ziet.
- Documenten die terug naar validatie zijn gestuurd, tonen een laadindicator
  in plaats van een dood scherm terwijl ze worden voorbereid.
- Grote leveranciersfacturen openen merkbaar sneller.

### Accounting

- Gesplitste regelitems behouden hun %-teken na het indrukken van Enter, en
  0 % wordt als waarde geaccepteerd.
- In het rekeningfilter bevestigt Enter de eerste overeenkomende rekening in
  plaats van niets te doen.
- Flexdimensie-tekens worden toegewezen op dimensie-id, zodat dimensies in de
  juiste kolom terechtkomen, ook wanneer de volgorde verschilt.
- Een mislukte accountingvoorbereiding herstelt met een foutmelding in plaats
  van eindeloos op "Preparing…" te blijven hangen, en het heropenen van een
  document serveert niet langer verouderde gegevens van het vorige document.

### PO-matching

- PO Matching openen zonder dat elke verplichte kolom is toegewezen kan weer;
  wanneer er iets nodigs ontbreekt, benoemt de melding de exacte kolommen.
- Kolommen die nergens aan zijn toegewezen, worden bij het openen van het
  scherm verborgen — na één keer vragen — en stromen niet langer mee in de
  berekening van het regelbedrag.
- De gematchte hoeveelheid wordt ververst na het opslaan, en de pop-up over
  ontbrekende kolommen leidt u naar Veldvalidatie, waar u het kunt oplossen.

### Dashboard en zoeken

- Kolommen op basis van keuzelijsten (factuurtype, status en vergelijkbare)
  tonen hun label in uw interfacetaal in plaats van de ruwe opgeslagen waarde.
- Vrijetekstzoeken accepteert haakjes als gewone tekst; voorheen werd de
  zoekopdracht geweigerd. De filteroperator "niet gelijk aan" blijft
  geselecteerd, en het handmatig bewerken van een filter beschadigt de
  veldnaam niet meer.
- Het selecteren van een suborganisatie in het snelzoeken voegt de naam in,
  niet de uuid, en de autocomplete voor suborganisaties toont geen duplicaten
  meer.
- Het dashboard kan nu tot 10.000 documenten per zoekvenster ophalen, zodat
  grote resultatensets correct pagineren.
- Het paneel met dubbele documenten toont dezelfde herleide kolommen als de
  hoofdlijst, en leveranciersfilterwaarden van meerdere woorden overleven het
  indrukken van Enter.
- De teller voor openstaande taken in de zijbalk telt taken in uw
  suborganisatiecontext, niet in de context van het document dat toevallig
  openstaat.

### Taken

- Kanban-kolommen pagineren terwijl u scrolt, zodat borden met veel taken snel
  laden.
- De toewijzings-e-mail gaat uit wanneer een taak wordt toegewezen — één keer.
  Een taak bewerken of afronden verzendt hem niet opnieuw, en de datum
  "toegewezen op" blijft de datum van toewijzing. Taak-e-mails worden
  bovendien correct weergegeven in Outlook.

### Workflow Builder

- De workflowlijst onthoudt uw zoekopdracht, sorteervolgorde, pagina en
  paginagrootte wanneer u een workflow opent en terugkeert, ook via het
  kruimelpad. De pagina opent standaard op het tabblad List.
- De schakelaar "run workflow on change" in de layoutbuilder bepaalt nu
  daadwerkelijk of de workflow wordt uitgevoerd, en inschakelen vereist dat u
  een workflow kiest.

### Instellingen en beheer

- De WatchDog-downloadlink en het installatiecommando verwijzen naar de
  omgeving waarin u zich bevindt, niet altijd naar productie.
- Decision Trees: het geselecteerde documentveld blijft gemarkeerd wanneer de
  kiezer opnieuw opent, afgekapte labels krijgen een tooltip, en bij het
  toevoegen van een regel worden gebruikersnamen getoond (geen ruwe id's).
- Het selectievakje System Admin is bewerkbaar bij het bewerken van een
  gebruiker.
- De pagina met stamgegevens komt niet langer leeg op door een race in de
  sortering, en sorteren op badges laat de pagina niet meer crashen.
- Een abonnement in de status "cancelling" kan worden hervat.
- De XSLT-detailpagina meldt laadfouten in plaats van niets te tonen, en de
  instellingen voor e-mailmeldingen gebruiken de volledige paginabreedte, met
  een werkend logvenster.
- De organisatiekiezer voor gebruikers met meerdere organisaties heeft een
  correcte rij-indeling, formaat en themakleuren.
- Analytics: Core Web Vitals worden weergegeven op basis van de echte
  meetgegevens, de logs-serviceweergave werkt, en een mislukt metrics-verzoek
  toont een fouttoestand in plaats van nullen weer te geven.
- "Use Default Template" in de layoutmanager kopieert de standaardlayout
  zoals bedoeld; voorheen crashte de functie of beweerde die dat er geen
  standaard bestaat.
- Labels van aangepaste velden overschrijven niet langer de meegeleverde
  vertalingen van standaardvelden, en de DocNet-schermen (AI Workforce),
  inclusief de Agent Wizard, zijn vertaald.
- Offertes in het leveranciersportaal: het indienen van een offerte met een
  REF1-waarde buiten de toegestane lijst wordt geblokkeerd, beheerde
  maateenheden verschijnen in de regelitemtabel, en de goedkeuringsopmaak
  geldt alleen voor contractoffertes.
- MediOrder krijgt detectie van dubbele documenten op het validatiescherm.

## API Service — `12.82.3`

### Beveiliging en organisatie-isolatie

- Het wisselen van de actieve organisatie wordt gevalideerd tegen uw
  daadwerkelijke lidmaatschap en wordt bij twijfel geweigerd, en een intern
  testeindpunt dat kon worden misbruikt om organisatiegrenzen te passeren, is
  gesloten.
- Documentscripts kunnen niet langer over organisatiegrenzen heen worden
  gelezen of overschreven, noch via de aanroep die een script op een document
  toepast, noch via een vreemd versie-id bij het opslaan.
- Gebruikerslijsten van suborganisaties en groepsledenlijsten geven alleen
  personen uit de organisatie van de aanroeper terug, en het in één keer
  toevoegen van meerdere gebruikers aan een groep laat niet langer alle
  gebruikers behalve de eerste vallen.
- Een credential uit de verkeerde organisatie wordt geweigerd voordat die het
  verwerkingstoken van een document kan worden, en
  volledige-tekstzoekopdrachten draaien als de aanroepende gebruiker in plaats
  van als een service-identiteit.
- Het vier-ogen-principe wordt afgedwongen bij goedkeuringen: de tweede
  goedkeurder moet iemand anders zijn dan degene die als eerste goedkeurde.
- De live PO Dashboard-lijst is beperkt tot de suborganisaties van de
  gebruiker.

### Documentpijplijn

- Documenten waarvan de export is afgewezen, blijven niet langer eindeloos in
  "Exporting" staan, en exportfouten bevatten altijd een melding in plaats van
  een lege.
- Wanneer een verwerkingsstap crasht, gaat het document naar een fouttoestand
  in plaats van vast te zitten in "restart in progress" zonder uitweg.
- Een barcodesplitsing die mislukt of een time-out bereikt, markeert het
  document als Error in plaats van stilzwijgend "Running" te tonen, en een
  splitsing die geen onderliggende documenten oplevert, behoudt het
  bovenliggende document en markeert het, in plaats van alles te verwijderen.
- Een mislukte nieuwe poging kan niet langer een document overschrijven dat
  ondertussen klaar was met verwerken.
- Documenten die zonder gebruikersinteractie zijn herstart en gesplitste
  onderliggende documenten draaien nu onder een duurzaam organisatietoken,
  zodat langdurige verwerking niet strandt op een verlopen sessie.
- Een leeg antwoord voor layoutsjablonen wordt niet langer zes uur gecachet,
  wat layouts voorheen liet verdwijnen tot de cache verliep.

### Extractie en e-documenten

- Bedragen met een minteken aan het einde ("100,00-") worden als negatief
  geparseerd in plaats van te worden weggelaten.
- Zwitserse documenten worden herkend als Zwitsers (CHF, CHE-btw-nummers,
  CH-IBAN's) in plaats van terug te vallen op Duitse conventies, en datums met
  typografische streepjes worden correct geparseerd.
- XRechnung 3.0-, 3.0.1- en 3.0.2-creditnota's in CII-syntaxis worden
  geclassificeerd als creditnota's, met het totaal uit het eindtotaalveld;
  hetzelfde geldt voor pure CII-creditnota's. Een gedeclareerde ZUGFeRD 2.4- /
  Factur-X 1.08-versie wint van de generieke profielidentifier, en kale
  XRechnung-typen worden herleid tot hun UBL- of CII-tegenhanger in plaats van
  te mislukken.
- Keuzelijstvelden (list-of-values) zoals Tax Country en Tax Code behouden hun
  waarde tijdens veldtransformatie; ze werden voorheen leeggemaakt.
- Tabelextractie: een fout in een kolom met alleen getallen blijft beperkt tot
  die kolom in plaats van de hele tabel onbruikbaar te maken, AI-tabelextractie
  krijgt een time-out die runs met meerdere batches overleeft, en twee crashes
  bij ongebruikelijke tabelvormen (rijen zonder paginaposities, ongelijke
  kolomaantallen) zijn opgelost.
- Bronregelpatronen matchen hoofdletterongevoelig.

### Export

- Een btw-controle die tijdens het exportvoorbeeld mislukt, geeft een leesbare
  fout terug in plaats van een serverfout, op beide voorbeeld-eindpunten.
- SFTP-export kan het originele document meesturen naast het geconverteerde.
- Wanneer exportconfiguraties op meerdere niveaus bestaan, wint consequent de
  meest specifieke.
- BOD-exports kunnen kolomtype-attributen meegeven via mapping.

### Import en stamgegevens

- Het e-mailimportlogboek is compleet: geweigerde en mislukte inkomende
  e-mails krijgen altijd een logregel met een accurate reden. Geen
  stilzwijgende drops meer.
- BOD-imports van inkooporders houden subregels aan de juiste regel gekoppeld;
  een meegenomen vlag koppelde ze voorheen aan de verkeerde.
- Het importeren van een CSV met meerdere nieuwe leveranciers werkt (hun
  gegenereerde id's botsen niet meer), aliassen voor betalingskortingstermijnen
  worden geïmporteerd en respecteren de "on conflict"-instelling, en de
  on-conflict-keuze IGNORE geldt ook buiten leveranciers.
- De leverancierssuggestie (TF-IDF) behoudt haar leveranciers-id wanneer een
  voorkeur wordt bijgewerkt, zodat suggesties niet langer nergens naar
  verwijzen.

### Overige fixes

- Dashboardrijen vertalen keuzelijstlabels naar de taal van de gebruiker,
  zonder het verzoek te blokkeren.
- Na het bewerken van velden wordt de PO-matchstatus bijgewerkt in plaats van
  de toestand van vóór de bewerking te tonen.
- Purchase Order Change-documenten krijgen vijf velden die gelijk oplopen met
  Purchase Order en een standaardlayout voor veldvalidatie.
- Foutantwoorden op 152 eindpunten geven leesbare meldingen terug in plaats
  van ruwe exception-objecten, en de analysepagina voor logs antwoordt niet
  langer met 502 voor organisaties zonder logindex.

## Auth Service — `1.77.9`

- Wachtwoordreset-e-mails werden stilzwijgend nooit verzonden; opgelost, samen
  met het onderliggende thread-safety-probleem.
- Een opnieuw afgespeeld refresh-token wordt geweigerd: de gezaghebbende
  databasecontrole draait nu elke keer in plaats van te worden overgeslagen
  bij een cachehit.
- Twee-factor-authenticatie: een authenticator-app kan worden geregistreerd
  naast e-mailcodes, en het verwijderen van de laatste passkey of het opnieuw
  genereren van back-upcodes vereist eerst een verse tweede factor.
- Een geldig suborganisatie-id wordt niet langer geweigerd met "Organization
  not found", en een API-sleutel die in een suborganisatie is aangemaakt,
  bepaalt zijn technische gebruiker vanuit die suborganisatie.
- Het bewerken van een organisatie valideert het partner-id en zet niet langer
  als bijeffect het organisatietype terug.
- "Remaining tokens" in de abonnementsweergave is verankerd aan het
  contractjaar, niet aan het kalenderjaar.

## Auth Bridge Service — `0.5.7`

- Accountreplicatie tussen de EU- en VS-regio's herstelt zichzelf. Een
  weggevallen replicatiestroom koppelt zichzelf ter plekke opnieuw aan,
  replicatie blijft doorlopen terwijl een reconciliatie draait, en het
  geheugengebruik van de reconciliatie is begrensd, zodat de service niet
  langer in een crashlus raakt bij grote tabellen.

## Barcode Service — `1.18.7`

- Het lezen van barcodes draait onder een tijdslimiet en meldt een time-out in
  plaats van te blijven hangen, wat het document voorheen vast liet zitten in
  de verwerking.

## Docflow Service — `2.9.8`

- Veldwaarden die door een workflowkaart worden geschreven, landen in beide
  opgeslagen representaties op het document, zodat een latere export ze niet
  langer terugdraait.
- Een opnieuw geprobeerde trigger behoudt het werk dat de run al had gedaan,
  concurrerende triggers op hetzelfde document sluiten aan in de rij in plaats
  van de vergrendeling af te pakken, en een geëscaleerde nieuwe poging krijgt
  voorrang in de wachtrij.
- Kaarten voor inkoopordervergelijking: toleranties worden vergeleken als
  exacte decimalen en zijn gebaseerd op de waarde van de inkooporder,
  omgekeerde vergelijkingsrichtingen zijn beschikbaar als optie, een
  toegewezen groep wordt gerapporteerd als groep in plaats van te stranden op
  een vergelijking met een gebruikers-id, toewijzings-id's worden correct als
  UUID's vergeleken, regels met lege numerieke waarden worden overgeslagen, en
  een "received"-vergelijking zonder ontvangstgegevens meldt ontbrekende
  gegevens in plaats van te doen alsof er een match is.
- De kaart Apply Decision Table is uitgefaseerd.

## Email Service — `1.41.0`

- Gmail-imports halen elke bijlage precies één keer op; duplicaten door
  overlappende ophaalrondes zijn verdwenen.
- De leescursor van de import schuift pas op nadat een import is bevestigd,
  zodat een crash midden in een import geen e-mails meer kan overslaan.
- Wanneer een importconfiguratie wordt gedeactiveerd omdat er een
  vergelijkbare bestaat, is die deactivering zichtbaar en wordt die gemeld in
  plaats van stilzwijgend te gebeuren.

## Extraction Service — `1.54.5`

- Of een document een creditnota of een factuur is, wordt bepaald door welk
  trefwoord het dichtst bij de documenttypevermelding staat, in plaats van dat
  de eerste treffer wint.
- Wanneer meerdere btw-interpretaties binnen de tolerantie vallen, krijgt de
  exacte aansluiting de voorkeur boven een benadering.
- Na een geforceerde nieuwe OCR worden het documenttype en de landinstelling
  hersteld, zodat tabelextractie en -training weer werken op opnieuw
  ge-OCR'de documenten.
- Documenten zonder documenttype laten het opzoeken van tabelregels niet
  langer crashen.

## FTP Service — `1.32.8`

- Het scannen van mappen doet één listingronde per map met een begrensde
  diepte, waardoor imports uit grote FTP-directory's veel sneller zijn en niet
  langer een time-out bereiken.

## Fulltext Service — `1.42.3`

- Documenten waarvan de opgeslagen zoekpayload geen geëxtraheerde velden
  bevatte, worden opnieuw geïndexeerd vanuit de database, zodat ze weer
  verschijnen in de dashboardzoekfunctie.
- Het zoekvenster van het dashboard ondersteunt tot 10.000 documenten.
- Facetzoekopdrachten mislukken niet langer wanneer semantisch zoeken actief
  is.

## OCR Service — `1.10.7`

- Het OCR-tijdbudget wordt bemeten op de werkelijke kosten per pagina, zodat
  lange documenten worden afgerond in plaats van tegen de pijplijnlimiet aan
  te lopen.

## PO Match Service — `1.59.8`

- Tabelregels met hoeveelheid nul worden overgeslagen in de
  mismatch-controles in plaats van onterechte mismatches op te leveren.
- Wanneer verplichte PO-matchkolommen ontbreken, benoemt het resultaat ze.
