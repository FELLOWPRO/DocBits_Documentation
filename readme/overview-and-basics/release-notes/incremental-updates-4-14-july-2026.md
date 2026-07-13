# DocBits Release-opmerkingen — 4–14 juli 2026

_Een overzicht van wat er voor u verandert met deze DocBits-release. Elke service
hieronder toont de versie die nu wordt uitgerold, gevolgd door wat er nieuw of
opgelost is — in gewone taal, zonder ticketnummers of technisch jargon. Services
die niet zijn vermeld, hadden in dit tijdvenster geen wijzigingen die zichtbaar
zijn voor klanten._

---

## Hoogtepunten

- **Aanmelden met meerdere organisaties.** Gebruikers die tot meerdere
  organisaties behoren, krijgen nu een volwaardige organisatiekeuze bij het
  aanmelden, een organisatiewisselaar in de koptekst en een instelling voor de
  standaardorganisatie. Sessies zijn veilig gekoppeld aan één organisatie
  tegelijk, en de app volgt automatisch de regio van de actieve organisatie.
  Aanmelden in de verkeerde regio probeert nu automatisch de juiste regio
  opnieuw in plaats van te mislukken.
- **Releasekanalen (frozen / latest).** Organisaties kunnen nu worden
  vastgezet op een stabiele ("frozen") release, terwijl andere de nieuwste
  updates ontvangen — voor gecontroleerde uitrol. Het dialoogvenster
  Serviceversies toont een nieuwe kolom *Release*, en beheerders beheren het
  kanaal via Bedrijfsinformatie. Verschillende services tonen in dit
  tijdvenster grotere versiesprongen, puur vanwege de nieuwe
  kanaalversienummering — deze sprongen bevatten geen functionele wijziging.
- **Configureerbare regelsystemen.** Drie nieuwe regelsystemen komen
  beschikbaar in de API (elk standaard uitgeschakeld, per organisatie te
  activeren): **validatieregels** die geëxtraheerde waarden controleren en
  fouten direct op het document markeren, **transformatieregels** die
  geëxtraheerde veld- en tabelwaarden automatisch opschonen of herschrijven,
  en **regelgebaseerde lay-outselectie** die de juiste documentlay-out kiest
  op basis van regels in plaats van op basis van de herkomst van het document.
- **Transparantie bij e-mailimport.** Het e-mailimportlogboek toont nu één
  uitklapbare rij per bijlage, laat zien welke documenten zijn aangemaakt (met
  knoppen die u direct naar het dashboard brengen), markeert overgeslagen en
  gesplitste items, en laat u de originele e-mail downloaden als `.eml`-bestand.
- **AI-tabelextractie.** Een nieuwe gestructureerde AI-extractiemodus voor
  tabellen, met een selectievakje "Use AI" per tabel en per kolom in de
  documenttype-instellingen.
- **Stabiliteit van de Web App.** Een oneindige herlaadlus na een verlopen
  sessie opgelost, de defecte Layout Builder gerepareerd, en extractietabellen
  hebben nu een versleepbare hoogteregelaar.
- **Nieuw: Auth Bridge Service.** Een nieuwe service houdt aanmeldgegevens
  continu synchroon tussen de EU- en US-regio's, met ingebouwde zelfherstel-
  en monitoringfuncties.

---

## API Service — live: `12.57.8`

- **Validatieregels (nieuw, per organisatie):** een door beheerders
  configureerbaar regelsysteem controleert geëxtraheerde waarden (totalen,
  verplichte velden en meer) en markeert fouten direct op het document,
  inclusief welke regel is geactiveerd. Regels kunnen in een proefrun worden
  getest voordat ze worden ingeschakeld, kunnen per documenttype worden
  geactiveerd en worden geleverd met een startcatalogus van standaardregels
  (allemaal uitgeschakeld totdat u ze activeert).
- **Transformatieregels (nieuw, per organisatie):** geëxtraheerde veld- en
  tabelwaarden worden tijdens de verwerking automatisch opgeschoond of
  herschreven — configureerbaar per documenttype of voor de hele organisatie.
- **Regelgebaseerde lay-outselectie (nieuw):** documentlay-outs kunnen nu
  worden gekozen via configureerbare regels in plaats van gekoppeld te zijn
  aan de herkomst van het document. Bestaand herkomstgebaseerd gedrag wordt
  automatisch gemigreerd, lay-outsjablonen kunnen worden hernoemd, en dubbele
  lay-outtitels worden voorkomen.
- **Snellere dashboardexports:** exports die vanuit het dashboard worden
  gestart, worden nu naar een speciale worker gestuurd in plaats van te
  wachten op een pollingcyclus, zodat ze direct beginnen.
- **Exportblokkering bij duplicaatdetectie opgelost:** de exportblokkering
  voor vermoedelijke duplicaten werkt weer.
- **Instellingen die niet bewaard bleven:** opgelost dat opgeslagen voorkeuren
  soms niet werden bewaard wanneer een oudere verwijderde kopie van dezelfde
  instelling bestond.
- **Documenten met ongebruikelijke tekens:** opslagfouten opgelost die werden
  veroorzaakt door onzichtbare NUL-tekens in geëxtraheerde gegevens.
- **Correcte "Bijgewerkt door":** documenten die automatisch als e-documenten
  worden geüpload, tonen niet langer een systeemgebruiker als laatste
  bewerker — het veld blijft leeg totdat een persoon daadwerkelijk iets
  bewerkt.
- **Gescande PDF's met een goede tekstlaag:** een nieuwe optie laat DocBits
  vertrouwen op de tekst die al in een gescande pagina is ingesloten in plaats
  van OCR opnieuw uit te voeren — sneller en vaak nauwkeuriger.
- **E-invoices:** robuustere detectie van ingesloten XML wanneer het originele
  bestand opnieuw moet worden gecontroleerd.
- **Taken:** nieuwe organisatie-instelling waarmee niet-beheerders het filter
  "Alle" in de takenlijst kunnen gebruiken.
- **Regelmatching:** het fuzzy-matching-gedrag is nu per regel configureerbaar.
- **Stabiliteit:** WebSocket-verbindingen worden bij fouten netjes gesloten in
  plaats van serverfouten te veroorzaken; de synchronisatie van de
  permissiecache verifieert en herstelt zichzelf; de serviceversie is nu
  zichtbaar op het health-eindpunt.

## Auth Service — live: `1.71.1`

- **Aanmelden met meerdere organisaties:** bij het aanmelden wordt nu gevraagd
  welke organisatie u wilt openen wanneer een gebruiker tot meerdere behoort,
  sessies zijn aan die organisatie gekoppeld, en nieuwe eindpunten
  ondersteunen het selecteren, wisselen en instellen van een
  standaardorganisatie. Dubbele of conflicterende organisatielidmaatschappen
  zijn opgeschoond en worden nu op databaseniveau voorkomen, met snellere
  lidmaatschapsopzoekingen.
- **Fixes voor de standaardorganisatie:** bij het aanmelden wordt automatisch
  uw standaardorganisatie geselecteerd (niet een willekeurige), en het
  wijzigen van de standaard wordt direct van kracht in plaats van verouderde
  profielgegevens te tonen.
- **Afmelden opgelost:** een serverfout (HTTP 500) bij het afmelden opgelost
  en het eindpunt voor tokenintrekking hersteld.
- **Tokenveiligheid:** tokenverificatie en -caching respecteren nu de
  organisatie waarvoor een token is uitgegeven, en tokenintrekking is
  gecentraliseerd.
- **Releasekanalen:** het releasekanaal van de organisatie wordt hier
  opgeslagen, is beheerbaar door organisatiebeheerders en wordt beschikbaar
  gesteld aan de app en de routeringslaag.

## Auth Bridge Service — live: `0.2.4.2` _(nieuwe service)_

- **Wat het is:** een nieuwe service die authenticatiegegevens continu
  repliceert tussen de EU- en US-regio's, zodat accounts en aanmeldingen
  consistent blijven tussen de regio's.
- **Zelfherstellend:** de service detecteert en herstelt gegevensafwijkingen
  tussen regio's — inclusief het correct doorgeven van verwijderingen — en
  herstelt automatisch van verbindingsverlies in plaats van gegevens te
  verliezen.
- **Veiligheid en monitoring:** een eerdere bidirectionele replicatielus is
  gestopt en wordt nu actief gedetecteerd en afgeschermd; foutregistratie en
  waarschuwingen zijn aangesloten; en de service toont zijn versie in het
  dialoogvenster Serviceversies.

## Docflow Service — live: `2.6.1`

- **Workflowkaarten accepteren lege waarden:** selectievakje- en partnerkaarten
  mislukken niet langer wanneer een veld terecht leeg is; controles op het
  kaarttype zijn strikter en voorspelbaarder.
- **Workflows draaien opnieuw bij echte wijzigingen:** de workflowvergrendeling
  respecteert weer de documentstatus van de trigger en volgt nu ook de
  documentversie — zodat een document waarvan de gegevens daadwerkelijk zijn
  gewijzigd opnieuw door de workflow kan gaan, zelfs met dezelfde status,
  terwijl echte duplicaten geblokkeerd blijven.
- **Grotere geavanceerde workflows:** de limiet op workflowknooppunten is
  verhoogd en is nu per omgeving configureerbaar.
- **Alternatieve export:** door workflows geactiveerde alternatieve exports
  worden nu als zodanig gelabeld, zodat downstream-systemen ze kunnen
  onderscheiden.
- **Veerkracht:** de service maakt automatisch opnieuw verbinding wanneer een
  databaseverbinding tijdens gebruik wegvalt, tolereert een tragere
  berichtenbroker in plaats van te mislukken, en mislukte API-verzoeken worden
  nu gelogd met volledige context en traceerbare uitvoerings-ID's.

## Email Service — live: `1.38.4`

- **Importlogboek, herbouwd voor traceerbaarheid:** elke geïmporteerde e-mail
  registreert nu welke documenten eruit zijn aangemaakt, met detailrijen per
  bijlage.
- **Download van originele e-mail:** het originele bericht kan als
  `.eml`-bestand rechtstreeks vanuit het importlogboek worden gedownload.
- **Bijlageherstel:** het herstelpad voor beschadigde bestanden verwerkt nu
  ook platte-tekstberichten, zodat meer beschadigde inkomende e-mails worden
  hersteld in plaats van overgeslagen.

## Extraction Service — live: `1.51.6`

- **Btw/netto niet langer verwisseld:** een geval op Amerikaanse documenten
  opgelost waarbij het btw-bedrag als groter dan het nettobedrag kon worden
  toegewezen wanneer meerdere kandidaatparen werden gevonden.
- **Meerdere btw-tarieven per leverancier:** de extractie verwerkt nu
  leveranciers waarvan de facturen verschillende btw-tarieven op één document
  bevatten.
- **AI-tabelextractie (nieuw, opt-in):** gestructureerde AI-extractie-eindpunten
  voor tabellen, per organisatie te activeren via een feature flag.
- **Snellere AI-aanroepen:** de configuratie van het AI-model dat tijdens de
  extractie wordt gebruikt is afgestemd om onnodige verwerkingstijd te
  vermijden.
- **Crashfix:** een fout opgelost bij documenten die tijdens de extractie een
  lege kandidatenlijst opleverden.

## Fulltext Service — live: `1.37.2`

- **Migraties van de zoekindex hersteld:** migratiedefinities die waren
  afgeweken zijn hersteld, zodat upgrades van de zoekindex betrouwbaar blijven.
- Interne routeringswerkzaamheden voor de nieuwe releasekanaal-infrastructuur.

## PO Match Service — live: `1.58.2`

- **Tolerantere matching:** PO-matching mislukt niet langer bij ongebruikelijke
  gegevens — niet-tekstuele artikelnummers, ontbrekende hoeveelheden en
  niet-tekstuele bedragwaarden worden nu correct verwerkt in plaats van een
  fout te veroorzaken.

## Web App — live: `10.41.8`

- **Ervaring met meerdere organisaties:** nieuwe organisatiekeuzepagina bij
  het aanmelden, een speciaal organisatiewisselaar-pictogram in de koptekst,
  instellingen voor de standaardorganisatie, en de app volgt de regio van uw
  actieve organisatie. Aanmelden in de verkeerde regio probeert stilzwijgend
  de juiste regio opnieuw en leidt u indien nodig naar de organisatiekeuze.
- **Geen eindeloze herlaadacties meer:** een oneindige herlaadlus opgelost die
  kon optreden wanneer de server een opgeslagen sessietoken weigerde — de app
  forceert nu een echte tokenvernieuwing in plaats van eindeloos te herladen.
- **Layout Builder gerepareerd:** de Layout Builder werkt weer, en de
  lay-outselectie is losgekoppeld van de herkomst van het document (in lijn
  met de nieuwe regelgebaseerde selectie in de API).
- **Extractietabellen:** tabellen met factuurregels hebben nu een versleepbare
  hoogteregelaar, zodat u de tabel meer ruimte kunt geven tijdens het
  valideren.
- **E-mailimportlogboek:** nieuwe badges voor overgeslagen en gesplitste
  items, uitklapbare rijen per bijlage, download van de originele e-mail, en
  document-ID-knoppen die u direct naar het dashboard brengen, gefilterd op
  dat document.
- **Dashboardzoekfunctie:** de vervolgkeuzelijst met querywaarden toont nu het
  gelokaliseerde label voor velden met een waardenlijst, en de voorbeelden in
  de zoekhulp zijn herwerkt.
- **Betrouwbaarheid van instellingen:** gebruikersvoorkeuren worden nu
  betrouwbaar geladen bij het aanmelden via SSO, en de opslagbevestiging wordt
  alleen getoond wanneer het opslaan daadwerkelijk is gelukt.
- **Taken:** het filter "Alle" kan voor niet-beheerders worden hersteld via
  een nieuwe organisatie-instelling.
- **Watchdog-logboeken:** niet langer beperkt tot 10.000 vermeldingen, plus
  algemene verbeteringen in het gebruiksgemak.
- **Supporttickets:** het supportformulier vult uw e-mailadres vooraf in
  vanuit uw profiel.
- **Documenttype-instellingen:** nieuw selectievakje "Use AI" op tabellen en
  kolommen om AI-ondersteunde tabelextractie te beheren.
- **Dialoogvenster Serviceversies:** nieuwe kolom *Release* die het kanaal van
  elke service toont (frozen/latest), zo gerouteerd dat het snel blijft voor
  vastgezette organisaties.
- **Veldvalidatie:** een fout opgelost bij het terugkeren naar Veldvalidatie
  vanuit een ander scherm, en de knop "Scripts" leidt niet langer naar een
  404-pagina.

---

## Alleen hernummering van versies (geen functionele wijzigingen)

**Auto Accounting** (`1.20.1`), **Barcode Service** (`1.17.1`), **OCR
Service** (`1.9.1`), **FTP Service** (`1.31.1`), **Operator Service**
(`1.40.2`) en **Ideas Service** (`0.3.1`) zijn opnieuw geversioneerd als
onderdeel van de nieuwe releasekanaal-infrastructuur. Hun groter ogende
versiesprongen bevatten in dit tijdvenster geen functionele of
gedragswijzigingen. **Docnet Service** (`1.54.6`) is ongewijzigd sinds 19 juni.

<!-- Generated by the docbits-changelog skill (version-boundary mode: exact
     git ranges between the ALT (2026-07-03/04) and NEU (2026-07-09..14)
     version-bump commits supplied by the user, per service). -->
