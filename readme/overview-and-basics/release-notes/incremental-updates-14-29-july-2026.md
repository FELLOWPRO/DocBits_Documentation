# DocBits Release-opmerkingen — 14–29 juli 2026

_Wat er is veranderd met de DocBits-productie-upgrade van 29 juli 2026 (de
update van het Nova-kanaal), inclusief alles sinds de release van 14 juli.
Elke service toont de versie die nu live is, gevolgd door wat er nieuw of
opgelost is — in gewone taal. Services die niet zijn vermeld, hadden geen
wijzigingen die zichtbaar zijn voor klanten._

---

## Hoogtepunten

- **Twee-factor-authenticatie.** DocBits-accounts kunnen nu worden beveiligd
  met een tweede factor: een authenticator-app (TOTP), een eenmalige code per
  e-mail, of een passkey via Touch ID, Windows Hello, YubiKey en vergelijkbare
  methoden. Back-upcodes dekken het geval van een verloren apparaat, en op een
  vertrouwd apparaat kan de tweede factor een tijdlang worden overgeslagen.
  Elke gebruiker kan 2FA voor zichzelf inschakelen; beheerders kunnen het voor
  de hele organisatie verplicht stellen. Zie de
  [handleiding Twee-factor-authenticatie](../two-factor-authentication.md).
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
- **Turbo AI-niveau uitgefaseerd.** Het Turbo-model heeft het einde van zijn
  levensduur bereikt. Wie het had geselecteerd, is automatisch overgezet naar
  Fast; u hoeft niets te doen.

---

## Web App — live: `10.46.2`

### Aanmelden

- **Twee-factor-authenticatie:** stel onder uw profiel een authenticator-app,
  e-mailcodes of een passkey in, print uw back-upcodes en markeer een apparaat
  als vertrouwd zodat er niet elke keer om wordt gevraagd. Gebruikers met een
  passkey kunnen volledig zonder wachtwoord inloggen. Organisatiebeheerders
  krijgen een schakelaar om 2FA verplicht te stellen en een adoptieoverzicht
  waarin te zien is wie zich al heeft geregistreerd.
- **Verwijderde accounts:** aanmelden met een verwijderd account meldt dat
  nu duidelijk, in plaats van te mislukken met een algemene fout.
- **SSO:** een fout opgelost bij het aanmelden terwijl een andere regio was
  geselecteerd. SSO-sessies verlopen nu op het moment dat de
  identityprovider aangeeft, en niet meer volgens een vaste lokale timer.

### Werken met documenten

- **Verwijderde documenten:** het openen van een document dat inmiddels is
  verwijderd, toont een nette melding in plaats van scriptfouten.
- **Veldvalidatie:** het invoerveld voor het paginanummer is breder en
  springt bij Enter naar de pagina. Een veld dat door een script
  alleen-lezen is gemaakt, toont nog steeds zijn veldkoppeling. Een
  waarschuwingsvenster dat ruwe JavaScript weergaf, toont nu de
  daadwerkelijke melding, en het scherm loopt niet langer vast bij documenten
  met lange regeltabellen van e-documenten.
- **Tabelextractie:** het verwijderen van een kolom maakt de naam weer
  beschikbaar voor hergebruik, en verwijderde koppen duiken niet langer
  opnieuw op in de opgeslagen tabel.
- **Goedkeuringen:** het openen van een document dat net in behandeling is
  genomen, komt uit op het juiste goedkeuringsscherm. Gebruikers kunnen niet
  langer een Sales Tax-stap goedkeuren waarvoor hun groep geen rechten heeft,
  en de goedkeuringshistorie toont weer alle vermeldingen. De historie
  vermeldt bovendien de persoon die daadwerkelijk heeft goedgekeurd,
  inclusief goedkeuringen die een beheerder namens de toegewezen persoon
  heeft gedaan.
- **Leveranciers:** de pagina Accounting toont niet langer een onterechte
  waarschuwing "Supplier is missing", en het verwijderen van een leverancier
  die alleen uit extractie bestaat, laat het dialoogvenster niet langer
  hangen.
- **Stamgegevens:** tabellen op de pagina met stamgegevens scrollen weer.
- **Taken en meldingen:** het verwijderen van een taak is niet langer
  voorbehouden aan beheerders. Of niet-beheerders hun eigen taken mogen
  verwijderen, is nu een organisatie-instelling, en gebruikers die een taak
  hebben op een document dat ze niet kunnen openen, krijgen een weergave met
  alleen de taak in plaats van een foutmelding.

### Dashboard en zoeken

- **Export:** exports gebruiken het dashboard dat u hebt geselecteerd, en de
  app waarschuwt voordat u een dashboard met niet-opgeslagen wijzigingen
  exporteert.
- **Zoeken:** Invoice Type is beschikbaar als zoekveld, inclusief de
  bijbehorende waardenlijst. Wanneer een resultatenset groter is dan het
  venster dat het Dashboard kan tonen, geeft de teller dat nu aan in plaats
  van de lijst stilzwijgend af te kappen.
- **Importlogboek:** gesplitste documenten zijn vindbaar via hun
  bovenliggende document, en de kolom Failed Filenames toont alleen bestanden
  die daadwerkelijk zijn mislukt of overgeslagen.

### Instellingen en beheer

- **Supporttickets:** maak een ticket rechtstreeks vanuit een foutmelding.
  Tickets bevatten de omgeving en het releasekanaal, en het vastleggen van
  de schermafbeelding blijft niet langer hangen.
- **Groepen en rechten:** niet-geclassificeerde documenten kunnen als recht
  worden toegekend, net als elk ander documenttype.
- **Workflow Builder:** nieuw aangemaakte of hernoemde kaarten,
  e-mailsjablonen en andere keuzelijstitems verschijnen direct, zonder de
  pagina te herladen.
- **Decision Trees:** de labels van documentvelden in de designer volgen de
  interfacetaal in plaats van altijd de Engelse naam te tonen.
- **Documenttypen:** nieuwe instelling Structured Extraction in de
  extractiesectie.
- **E-Doc-btw-codes:** nieuwe instellingenpagina om uw ERP-btw-codes toe te
  wijzen voor elektronische documenten (zie Hoogtepunten).
- **Auto Accounting:** dimensies worden nu betrouwbaar getoond in plaats van
  met tussenpozen.
- **AI-modelselectie:** het uitgefaseerde Turbo-niveau is uit de keuzelijst
  verdwenen; bestaande selecties tonen Fast.
- **Dialoogvenster Serviceversies:** is nu scrollbaar, bevat de Auth Bridge
  Service en toont de releasekanaalnamen Vesta en Nova.
- **Importpagina:** crasht niet langer voor organisaties met een leeg
  abonnementsrecord.

### Kleinere fixes

Lege meldingen worden onderdrukt, het dialoogvenster voor het aanmaken en
bewerken van ideeën scrolt, scheef uitgelijnde selectievakjes in de
veldinstellingen staan weer recht, geblokkeerde documentverwijderingen
leggen uit waarom, en de E-Document-instellingen verwerken het wisselen van
Default naar Custom netjes.

## API Service — live: `12.68.1`

- **Twee-factor-authenticatie:** alle aanmeldpaden met een wachtwoord lopen
  via de controle op de tweede factor, zodat geen enkele integratieroute die
  kan omzeilen.
- **E-Doc-btw-codes:** ERP-btw-codetoewijzing voor elektronische documenten,
  met een centrale controle vóór de export zodat ontbrekende codes vroeg aan
  het licht komen.
- **Toegangsbeheer:** beheerders kunnen niet-beheerders inzage geven in
  niet-geclassificeerde documenten.
- **Audittrail bij verwijderen:** documenten leggen vast wie ze heeft
  verwijderd en wanneer.
- **Persoonlijke dashboards:** deelinstellingen die niet werden opgeslagen
  zijn gerepareerd.
- **Dashboardzoekfunctie:** Invoice Type is toegevoegd aan de uitgebreide
  zoekvelden, en documenten die door een barcode- of QR-splitsing zijn
  ontstaan, zijn vindbaar via hun bovenliggende document.
- **Actuele dashboardgegevens:** het vernieuwen van een tabel of het opnieuw
  verwerken van een document wist de dashboardcache, zodat de lijst niet
  langer de waarden van vóór de wijziging toont.
- **Uploads:** herhaalde uploads van hetzelfde bestand tijdens een
  netwerkretry maken niet langer dubbele documenten aan.
- **Leveranciersopzoeking:** resultaten komen binnen zodra de gegevens klaar
  zijn, in plaats van na een vaste wachttijd.
- **Infor-export:** eenheidsprijzen behouden vier decimalen. M3-exports
  kunnen regeltoeslagen met een nulbedrag bevatten, en negatieve
  LN-kostenregels worden als positieve creditregels verzonden. De export
  wacht bovendien tot een lopende workflow is afgerond in plaats van midden
  in de workflow te draaien.
- **Goedkeuringen:** een goedkeuring wordt alleen aan een
  goedkeuringsverzoek gekoppeld wanneer de goedkeurder de toegewezen persoon
  is. Wijzigingen die een workflow zelf doorvoert, worden toegeschreven aan
  de systeemgebruiker in plaats van aan de laatste persoon die het document
  heeft bewerkt.
- **Aanmeldstabiliteit:** een tijdelijke fout in de tokenvalidatie logt
  gebruikers niet langer uit; de app probeert het opnieuw. Documenten krijgen
  dezelfde behandeling en mislukken niet langer meteen bij een korte hapering
  in de authenticatie.
- **Classificatie:** bronregels matchen nu op elk documentbronveld, niet op
  vaste posities.
- **Validatiestabiliteit:** een veld zonder naam laat de documentvalidatie
  niet langer crashen.
- **AI-modellen:** het (uitgefaseerde) Turbo-niveau wordt overal omgezet
  naar Fast, inclusief fijn afgestemde varianten, met een beveiliging zodat
  een uitgefaseerd model nooit kan draaien.
- **Achtergrondtaken:** een vastgelopen scheduler wordt gedetecteerd en
  herstart, zodat terugkerende taken niet stilzwijgend kunnen stoppen.

## Auth Service — live: `1.75.3`

- **Twee-factor-authenticatie:** de backend achter het hoogtepunt hierboven.
  Authenticator-apps, eenmalige codes per e-mail, passkeys en vertrouwde
  apparaten, plus back-upcodes, verplichtstelling per organisatie en
  aanmelden zonder wachtwoord met een passkey. Bij het registreren worden uw
  andere sessies afgemeld, bij het wijzigen van uw wachtwoord worden
  vertrouwde apparaten ingetrokken, en de verificatie-eindpunten kennen een
  snelheidsbegrenzing met vergrendeling en een beveiliging tegen hergebruik
  van codes.
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
  ontbrekende identityprovider-configuratie zijn verholpen. De
  tokenlevensduur die de provider teruggeeft, wordt doorgegeven aan de app.
- **Sessietokens:** opgelost dat kortlopende sessietokens als ongeldig
  werden geweigerd terwijl ze niet verlopen waren.
- **Beheertooling:** de regio van een organisatie is zichtbaar in de
  beheer-API, de systeemgebruiker van een organisatie kan opnieuw worden
  toegewezen, en het beheer van abonnementen en verbruik heeft eigen
  eindpunten gekregen. Deze wijzigingen betreffen de interne tooling van
  DocBits, niet de klantapp.

## Email Service — live: `1.40.2`

- **Import in de juiste regio:** inkomende e-maildomeinen bestaan per regio,
  en e-mails die in de verkeerde regio aankomen, worden doorgestuurd naar de
  juiste. Amerikaanse organisaties zijn niet langer afhankelijk van het
  Europese importpad.
- **Microsoft 365:** nationale cloudtenants worden geconfigureerd via een
  Cloud Instance-selectie, wat O365-imports voor Amerikaanse klanten
  herstelt. Een ongeldige tenant geeft nu een duidelijke aanmeldfout in
  plaats van een serverfout, en onvolledige tenantgegevens mislukken direct
  met een melding in plaats van stilzwijgend.
- **Verbindingstest:** het testen van een IMAP-postvak dat niet antwoordt,
  mislukt na enkele seconden met een time-outmelding in plaats van tegen een
  gateway-time-out aan te lopen.
- **Opgeruimde inbox:** e-mails zonder bijlagen worden uit de inbox
  verplaatst in plaats van zich op te stapelen.
- **Geen duplicaten bij een retry:** uploads naar de document-API dragen een
  idempotentiesleutel, zodat een opnieuw afgeleverde e-mail niet twee keer
  hetzelfde document kan aanmaken.
- **Bronnamen:** O365-bronnen met een geconfigureerde map nemen het
  e-mailadres van het account op in hun naam, zodat vergelijkbare bronnen te
  onderscheiden zijn. Het postvakadres wordt uitgelezen uit het
  geauthenticeerde account in plaats van uit een ingetypt veld.
- **Opschoning van het importlogboek:** vermeldingen in het importlogboek
  worden 90 dagen bewaard en daarna automatisch opgeruimd.

## PO Match Service — live: `1.59.3`

- **Status "tabel onvolledig":** facturen waarvan de regeltabel niet kon
  worden toegewezen, krijgen een eigen status in plaats van het misleidende
  "inkooporder niet gevonden" (zie Hoogtepunten). Het dashboard toont de
  status met het niet-gematcht-pictogram.
- **Betere foutdetails:** fouten bij het toewijzen van tabellen benoemen de
  specifieke kolom die niet kon worden toegewezen.
- **Sneller bij grote facturen:** de op regels gebaseerde matching groepeert
  kandidaten op artikelnummer en leest de tolerantie-instellingen één keer
  per organisatie in plaats van één keer per regel.
- **Netter API-gedrag:** verzoeken om PO-regels die niet bestaan, geven een
  correct niet-gevonden-antwoord, en corrupte cache-items worden verwijderd
  in plaats van herhaalde fouten te veroorzaken.
- **Matchen op totaal:** een fout opgelost in het matchen tegen het
  totaalbedrag van de inkooporder.

## Fulltext Service — live: `1.39.1`

- **Europese getalnotaties:** bedragen met een decimale komma (`1.234,56`)
  worden vóór het indexeren genormaliseerd, zodat zoeken en filteren op
  bedragen werkt ongeacht de getalnotatie.
- **Eerlijke resultaataantallen:** wanneer een zoekopdracht meer documenten
  vindt dan het dashboardvenster teruggeeft, meldt het antwoord dat, in
  plaats van een afgekapte lijst als volledig te presenteren.
- **ERP-tellingen:** een tokenfout opgelost die de live tellingenstroom op
  het dashboard kon onderbreken.
- **Robuuster indexeren:** het indexeren doorstaat nu tijdelijke haperingen
  van de database en de Auth Service (automatische retry, terugvallen op de
  primaire database) en verwijdert misvormde wachtrijberichten in plaats van
  ze eindeloos opnieuw te proberen.

## OCR Service — live: `1.10.3`

- **Stabiele leesvolgorde:** tekst wordt in een vaste volgorde gelezen,
  zodat hetzelfde document elke keer op dezelfde manier wordt geëxtraheerd.
- **Grote documenten:** het OCR-tijdbudget schaalt mee met de
  documentgrootte, zodat zeer grote bestanden niet langer mislukken met een
  time-out.
- **Ongebruikelijke tekens:** een sanitizer verwijdert tekens die de
  OCR-engine niet kan weergeven, wat fouten oplost bij documenten met
  exotische symbolen.
- **Minder tijdelijke fouten:** tijdelijke verbindingsfouten met de opslag
  worden automatisch opnieuw geprobeerd, en een vastgelopen worker wordt
  herkend aan de vraag of hij daadwerkelijk werk verwerkt.

## Extraction Service — live: `1.53.3`

- **Amerikaanse facturen zonder btw:** een geval opgelost waarbij het juiste
  netto/btw-paar werd weggegooid wanneer het btw-bedrag nul is.
- **Tabelextractie:** tabellen blijven bewerkbaar wanneer de geconfigureerde
  toewijzing meer kolommen verwacht dan het document bevat, en een crash bij
  ongebruikelijke rijgegevens is opgelost.
- **Stabiele leesvolgorde:** een weerspiegeling van de OCR-wijziging
  hierboven, zodat de extractie dezelfde tokenvolgorde ziet als de OCR heeft
  geproduceerd.
- **AI-modellen:** uitfasering van het Turbo-niveau, overgenomen van de API
  Service.

## Docflow Service — live: `2.7.3`

- **PO-matching in workflows:** ontbrekende vergelijkingswaarden worden
  behandeld als ontbrekende gegevens in plaats van als een mismatch.
- **Orderbevestigingskaarten:** koper en verantwoordelijke worden
  betrouwbaar bepaald.
- **Offertekaarten:** het logboek legt nu vast wanneer er wel een
  geoffreerde prijs bestaat maar die buiten het toegestane datumbereik valt —
  voorheen leek dat op ontbrekende gegevens.
- **Vrachtkosten:** wanneer geen van beide kanten kosten heeft, wordt het
  geval afgehandeld door de operatorkaart in plaats van te blijven hangen.
- **Beveiliging:** workflow-API-tokens worden gevalideerd tegen de
  organisatie waartoe ze behoren.
- **Sneller activeren:** de controle op actieve workflows wordt gecachet, en
  de achtergrondworkers herstarten netjes in plaats van vastgelopen
  processen achter te laten.

## Barcode Service — live: `1.18.1`

- **Langlopende splitsingen:** de verbinding met de taakwachtrij blijft
  actief tijdens lange barcodetaken, zodat het splitsen van grote batches
  niet langer tegen het einde vastloopt.

## FTP Service — live: `1.31.2`

- **Opschoning van het importlogboek:** dezelfde 90-daagse bewaartermijn en
  automatische opruiming als bij de Email Service.

## Auth Bridge Service — live: `0.4.1`

- **Nauwkeurige replicatiemeldingen:** de replicatiebrug voor accounts tussen
  EU en VS meet een stilstand vanaf de laatste echte voortgang in plaats van
  vanaf de eerste fout, en telt alleen daadwerkelijke replicatiebeweging als
  voortgang. De nachtelijke valse meldingen "bridge stalled" zijn verdwenen.
  In de app verandert er niets.

## Operator Service — live: `1.42.1`

- **Stabielere workers:** een vastgelopen worker wordt herkend aan de vraag
  of hij werk verwerkt, en het overbodige onderlinge verkeer tussen workers
  is uitgeschakeld.

---

## Ongewijzigd in deze release

**Auto Accounting** (`1.21.1`) is opnieuw gebouwd zonder wijzigingen die
zichtbaar zijn voor klanten. **Docnet** (`1.55.1`) en **Ideas** (`0.3.1`)
bevatten in dit tijdvenster geen wijzigingen.

<!-- Generated by the docbits-changelog skill. Boundary: versions live in the
     prod namespace on 28 Jul 2026 (Web App 10.41.8, API 12.57.8, Auth 1.71.1)
     up to the versions live in the sandbox namespace the same day, which is
     what the 29 July upgrade promotes. Re-check the version headers on the
     morning of the upgrade in case anything else lands on sandbox first.
     Manage Layouts and Custom Validation Rules stay excluded: DOCB-13719 gates
     both behind a beta query parameter, so they are not generally available in
     10.46.2. The hourly password for script changes (DOCB-13673) was added and
     then reverted inside this window, so it must not be announced. -->
