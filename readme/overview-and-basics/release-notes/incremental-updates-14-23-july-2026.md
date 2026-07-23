# DocBits Release-opmerkingen — 14–23 juli 2026

_Wat er is veranderd met de DocBits-productie-upgrade van 23 juli 2026 (de
update van het Nova-kanaal), inclusief alles sinds de release van 14 juli.
Elke service toont de versie die nu live is, gevolgd door wat er nieuw of
opgelost is — in gewone taal. Services die niet zijn vermeld, hadden geen
wijzigingen die zichtbaar zijn voor klanten._

---

## Hoogtepunten

- **Supporttickets vanuit het foutscherm.** Als er iets misgaat, kunt u nu
  rechtstreeks vanuit de foutmelding een supportticket openen. Het ticket
  bevat de technische context al, zodat u die niet zelf hoeft te beschrijven.
- **E-mailimport in de juiste regio.** Amerikaanse organisaties krijgen
  importadressen in hun eigen regio, en Microsoft 365-postvakken op nationale
  cloudtenants (GCC, 21Vianet en vergelijkbare) kunnen nu worden
  geconfigureerd via een Cloud Instance-selectie.
- **Duidelijkere PO-matchingstatus.** Facturen waarvan de regeltabel niet kon
  worden toegewezen, kregen voorheen het label "inkooporder niet gevonden" —
  waardoor mensen naar het verkeerde probleem zochten. Ze krijgen nu een
  eigen status "tabel onvolledig", met detail op kolomniveau over wat niet
  kon worden toegewezen.
- **Btw-codetoewijzing voor e-documenten.** Een nieuwe instellingenpagina
  wijst uw ERP-btw-codes toe voor elektronische documenten, en exports
  controleren de toewijzing vooraf in plaats van in het ERP te mislukken.
- **Scriptwijzigingen zijn beveiligd met een wachtwoord.** Aangepaste scripts
  kunnen de documentverwerking beïnvloeden; daarom vereist elke
  scriptwijziging nu een wachtwoord dat elk uur wisselt. Vraag uw beheerder
  om het actuele wachtwoord.
- **Turbo AI-niveau uitgefaseerd.** Het Turbo-model heeft het einde van zijn
  levensduur bereikt. Wie het had geselecteerd, is automatisch overgezet naar
  Fast; u hoeft niets te doen.

---

## Web App — live: `10.45.1`

### Werken met documenten

- **Verwijderde documenten:** het openen van een document dat inmiddels is
  verwijderd, toont een nette melding in plaats van scriptfouten.
- **Veldvalidatie:** het invoerveld voor het paginanummer is breder en
  springt bij Enter naar de pagina. Een veld dat door een script
  alleen-lezen is gemaakt, toont nog steeds zijn veldkoppeling.
- **Tabelextractie:** het verwijderen van een kolom maakt de naam weer
  beschikbaar voor hergebruik, en verwijderde koppen duiken niet langer
  opnieuw op in de opgeslagen tabel.
- **Goedkeuringen:** gebruikers kunnen niet langer een Sales Tax-stap
  goedkeuren waarvoor hun groep geen rechten heeft, en de
  goedkeuringshistorie toont weer alle vermeldingen. De historie vermeldt
  bovendien de persoon die daadwerkelijk heeft goedgekeurd, inclusief
  goedkeuringen die een beheerder namens de toegewezen persoon heeft gedaan.
- **Leveranciers:** de pagina Accounting toont niet langer een onterechte
  waarschuwing "Supplier is missing", en het verwijderen van een leverancier
  die alleen uit extractie bestaat, laat het dialoogvenster niet langer
  hangen.
- **Taken en meldingen:** de verwijderoptie is verborgen voor gebruikers
  zonder beheerdersrechten.

### Dashboard en zoeken

- **Export:** exports gebruiken het dashboard dat u hebt geselecteerd, en de
  app waarschuwt voordat u een dashboard met niet-opgeslagen wijzigingen
  exporteert.
- **Zoeken:** Invoice Type is beschikbaar als zoekveld, inclusief de
  bijbehorende waardenlijst.
- **Importlogboek:** gesplitste documenten zijn vindbaar via hun
  bovenliggende document, en de kolom Failed Filenames toont alleen bestanden
  die daadwerkelijk zijn mislukt of overgeslagen.

### Aanmelden

- **Verwijderde accounts:** aanmelden met een verwijderd account meldt dat
  nu duidelijk, in plaats van te mislukken met een algemene fout.
- **SSO:** een fout opgelost bij het aanmelden terwijl een andere regio was
  geselecteerd.

### Instellingen en beheer

- **Supporttickets:** maak een ticket rechtstreeks vanuit een foutmelding.
  Tickets bevatten de omgeving en het releasekanaal, en het vastleggen van
  de schermafbeelding blijft niet langer hangen.
- **Workflow Builder:** nieuw aangemaakte of hernoemde kaarten,
  e-mailsjablonen en andere keuzelijstitems verschijnen direct, zonder de
  pagina te herladen.
- **Documenttypen:** nieuwe instelling Structured Extraction in de
  extractiesectie.
- **E-Doc-btw-codes:** nieuwe instellingenpagina om uw ERP-btw-codes toe te
  wijzen voor elektronische documenten (zie Hoogtepunten).
- **AI-modelselectie:** het uitgefaseerde Turbo-niveau is uit de keuzelijst
  verdwenen; bestaande selecties tonen Fast.
- **Dialoogvenster Serviceversies:** is nu scrollbaar, bevat de Auth
  Bridge-service en toont de releasekanaalnamen Vesta en Nova.
- **Importpagina:** crasht niet langer voor organisaties met een leeg
  abonnementsrecord.

### Kleinere fixes

Lege meldingen worden onderdrukt, het dialoogvenster voor het aanmaken en
bewerken van ideeën scrolt, scheef uitgelijnde selectievakjes in de
veldinstellingen staan weer recht, geblokkeerde documentverwijderingen
leggen uit waarom, en de E-Document-instellingen verwerken het wisselen van
Default naar Custom netjes.

## API Service — live: `12.64.3`

- **Scriptbeveiliging:** scriptwijzigingen vereisen een tijdgebonden
  wachtwoord (zie Hoogtepunten).
- **E-Doc-btw-codes:** ERP-btw-codetoewijzing voor elektronische documenten,
  met een centrale controle vóór de export zodat ontbrekende codes vroeg aan
  het licht komen.
- **Toegangsbeheer:** beheerders kunnen niet-beheerders inzage geven in
  niet-geclassificeerde documenten.
- **Persoonlijke dashboards:** deelinstellingen die niet werden opgeslagen
  zijn gerepareerd.
- **Dashboardzoekfunctie:** Invoice Type is toegevoegd aan de uitgebreide
  zoekvelden, en documenten die door een barcode- of QR-splitsing zijn
  ontstaan, zijn vindbaar via hun bovenliggende document.
- **Uploads:** herhaalde uploads van hetzelfde bestand tijdens een
  netwerkretry maken niet langer dubbele documenten aan.
- **Leveranciersopzoeking:** resultaten komen binnen zodra de gegevens klaar
  zijn, in plaats van na een vaste wachttijd.
- **Infor-export:** eenheidsprijzen behouden vier decimalen. M3-exports
  kunnen regeltoeslagen met een nulbedrag bevatten, en negatieve
  LN-kostenregels worden als positieve creditregels verzonden.
- **Goedkeuringen:** een goedkeuring wordt alleen aan een
  goedkeuringsverzoek gekoppeld wanneer de goedkeurder de toegewezen persoon
  is.
- **Aanmeldstabiliteit:** een tijdelijke fout in de tokenvalidatie logt
  gebruikers niet langer uit; de app probeert het opnieuw.
- **Classificatie:** bronregels matchen nu op elk documentbronveld, niet op
  vaste posities.
- **Validatiestabiliteit:** een veld zonder naam laat de documentvalidatie
  niet langer crashen.
- **AI-modellen:** het (uitgefaseerde) Turbo-niveau wordt overal omgezet
  naar Fast, inclusief fijn afgestemde varianten, met een beveiliging zodat
  een uitgefaseerd model nooit kan draaien.

## Auth Service — live: `1.72.8`

- **Aanmeldhistorie:** aanmeldingen via SSO/SAML verschijnen nu in de
  aanmeldhistorie, en het tijdstip van de laatste aanmelding wordt bij elk
  aanmeldtype betrouwbaar vastgelegd. Het bekijken van de aanmeldhistorie
  van een andere gebruiker vereist het passende beheerdersniveau.
- **Legacy-accounts:** het verwijderen van een legacy-gebruikersaccount werkt
  weer, in plaats van stilzwijgend niets te doen.
- **Gebruikersbeheer in bulk:** voeg bestaande gebruikers in bulk via CSV toe
  aan suborganisaties en groepen, gematcht op e-mailadres. Ook opgelost: een
  crash bij ongelijk gevulde CSV-rijen en een serverfout bij het tegelijk
  toevoegen van twee of meer nieuwe gebruikers.
- **Ledenlijsten:** verwijderde gebruikers verschijnen niet langer in de
  ledenlijsten van suborganisaties.
- **Single sign-on:** een reeks verstevigingen. Verlopen tokens geven nu een
  duidelijke "verlopen"-melding, organisaties zonder SAML-configuratie
  krijgen een correct niet-gevonden-antwoord in plaats van een verkeerde
  aanmeldflow, afmelden wordt altijd voltooid — ook wanneer het
  afmeldverzoek niet kan worden geverifieerd — en diverse crashes rond
  ontbrekende identityprovider-configuratie zijn verholpen.
- **Sessietokens:** opgelost dat kortlopende sessietokens als ongeldig
  werden geweigerd terwijl ze niet verlopen waren.
- **Beheertooling:** de regio van een organisatie is zichtbaar in de
  beheer-API, de systeemgebruiker van een organisatie kan opnieuw worden
  toegewezen, en het beheer van abonnementen en verbruik heeft eigen
  eindpunten gekregen. Deze wijzigingen betreffen de interne tooling van
  DocBits, niet de klantapp.

## Email Service — live: `1.39.9`

- **Import in de juiste regio:** inkomende e-maildomeinen bestaan per regio,
  en e-mails die in de verkeerde regio aankomen, worden doorgestuurd naar de
  juiste. Amerikaanse organisaties zijn niet langer afhankelijk van het
  Europese importpad.
- **Microsoft 365:** nationale cloudtenants worden geconfigureerd via een
  Cloud Instance-selectie, wat O365-imports voor Amerikaanse klanten
  herstelt. Een ongeldige tenant geeft nu een duidelijke aanmeldfout in
  plaats van een serverfout, en onvolledige tenantgegevens mislukken direct
  met een melding in plaats van stilzwijgend.
- **Opgeruimde inbox:** e-mails zonder bijlagen worden uit de inbox
  verplaatst in plaats van zich op te stapelen.
- **Geen duplicaten bij een retry:** uploads naar de document-API dragen een
  idempotentiesleutel, zodat een opnieuw afgeleverde e-mail niet twee keer
  hetzelfde document kan aanmaken.
- **Bronnamen:** O365-bronnen met een geconfigureerde map nemen het
  e-mailadres van het account op in hun naam, zodat vergelijkbare bronnen te
  onderscheiden zijn.
- **Opschoning van het importlogboek:** vermeldingen in het importlogboek
  worden 90 dagen bewaard en daarna automatisch opgeruimd.

## PO Match Service — live: `1.59.1`

- **Status "tabel onvolledig":** facturen waarvan de regeltabel niet kon
  worden toegewezen, krijgen een eigen status in plaats van het misleidende
  "inkooporder niet gevonden" (zie Hoogtepunten). Het dashboard toont de
  status met het niet-gematcht-pictogram.
- **Betere foutdetails:** fouten bij het toewijzen van tabellen benoemen de
  specifieke kolom die niet kon worden toegewezen.
- **Netter API-gedrag:** verzoeken om PO-regels die niet bestaan, geven een
  correct niet-gevonden-antwoord, en corrupte cache-items worden verwijderd
  in plaats van herhaalde fouten te veroorzaken.
- **Matchen op totaal:** een fout opgelost in het matchen tegen het
  totaalbedrag van de inkooporder.

## Fulltext Service — live: `1.38.3`

- **Europese getalnotaties:** bedragen met een decimale komma (`1.234,56`)
  worden vóór het indexeren genormaliseerd, zodat zoeken en filteren op
  bedragen werkt ongeacht de getalnotatie.
- **ERP-tellingen:** een tokenfout opgelost die de live tellingenstroom op
  het dashboard kon onderbreken.
- **Robuuster indexeren:** het indexeren doorstaat nu tijdelijke haperingen
  van de database en de Auth Service (automatische retry, terugvallen op de
  primaire database) en verwijdert misvormde wachtrijberichten in plaats van
  ze eindeloos opnieuw te proberen.

## OCR Service — live: `1.9.9`

- **Grote documenten:** het OCR-tijdbudget schaalt mee met de
  documentgrootte, zodat zeer grote bestanden niet langer mislukken met een
  time-out.
- **Ongebruikelijke tekens:** een sanitizer verwijdert tekens die de
  OCR-engine niet kan weergeven, wat fouten oplost bij documenten met
  exotische symbolen.
- **Minder tijdelijke fouten:** tijdelijke verbindingsfouten met de opslag
  worden automatisch opnieuw geprobeerd.

## Extraction Service — live: `1.52.0`

- **Amerikaanse facturen zonder btw:** een geval opgelost waarbij het juiste
  netto/btw-paar werd weggegooid wanneer het btw-bedrag nul is.
- **Tabelextractie:** tabellen blijven bewerkbaar wanneer de geconfigureerde
  toewijzing meer kolommen verwacht dan het document bevat, en een crash bij
  ongebruikelijke rijgegevens is opgelost.
- **AI-modellen:** uitfasering van het Turbo-niveau, overgenomen van de API
  Service.

## Docflow Service — live: `2.7.2`

- **PO-matching in workflows:** ontbrekende vergelijkingswaarden worden
  behandeld als ontbrekende gegevens in plaats van als een mismatch.
- **Orderbevestigingskaarten:** koper en verantwoordelijke worden
  betrouwbaar bepaald.
- **Vrachtkosten:** wanneer geen van beide kanten kosten heeft, wordt het
  geval afgehandeld door de operatorkaart in plaats van te blijven hangen.
- **Beveiliging:** workflow-API-tokens worden gevalideerd tegen de
  organisatie waartoe ze behoren.
- **Sneller activeren:** de controle op actieve workflows wordt gecachet, en
  de achtergrondworkers herstarten netjes in plaats van vastgelopen
  processen achter te laten.

## Barcode Service — live: `1.17.4`

- **Langlopende splitsingen:** de verbinding met de taakwachtrij blijft
  actief tijdens lange barcodetaken, zodat het splitsen van grote batches
  niet langer tegen het einde vastloopt.

## FTP Service — live: `1.31.2`

- **Opschoning van het importlogboek:** dezelfde 90-daagse bewaartermijn en
  automatische opruiming als bij de Email Service.

---

## Ongewijzigd in deze release

**Auth Bridge** (`0.3.6`), **Auto Accounting** (`1.20.1`), **Docnet**
(`1.55.1`), **Operator** (`1.40.2`) en **Ideas** (`0.3.1`) bevatten in dit
tijdvenster geen wijzigingen.

<!-- Generated by the docbits-changelog skill (version-boundary mode), then
     reconciled on 23 Jul 2026 against the Nova versions actually deployed
     (Web App 10.45.1, API 12.64.3, Auth 1.72.8, Email 1.39.9, PO Match
     1.59.1, OCR 1.9.9, Docflow 2.7.2, FTP 1.31.2). Manage Layouts and
     Custom Validation Rules were removed from this page: DOCB-13719 gated
     both behind a beta query parameter, so they are not generally available
     in 10.45.1. -->
