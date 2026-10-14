# DocBits Release-opmerkingen — 29 juli – 12 augustus 2026

_Wat er veranderde met de DocBits-productie-upgrade die op 10–12 augustus 2026
is uitgerold, inclusief alles sinds de release van 29 juli. Elke service
vermeldt de versie die live is gegaan, gevolgd door wat er nieuw of opgelost
is — in gewone taal. Services die niet zijn vermeld (Auto Accounting `1.21.1`,
Ideas `0.3.1`, OCR `1.10.3`, Operator `1.42.1`, PO Match `1.59.3`, FTP
`1.32.4`), hadden geen wijzigingen die zichtbaar zijn voor klanten._

---

## Hoogtepunten

- **Ondersteuning voor FacturaE.** Spaanse FacturaE 3.1-e-facturen worden
  standaard geclassificeerd en geëxtraheerd, met volledige veldtoewijzingen.
  In dezelfde ronde werden de ebInterface-toewijzingen (Oostenrijk)
  versiegetrouw, kregen de standaardinstellingen van Factur-X en ZUGFeRD het
  pad voor de bedrijfsnaam, en werden verschillende foutieve
  standaardtoewijzingen voor kortingen, btw en stukprijzen gecorrigeerd.
- **Dashboardzoeken en sorteren gerepareerd.** Sorteren hangt niet langer af
  van welke kolommen toevallig zichtbaar zijn, een OR-filter in combinatie met
  een bereik- of gelijkheidsconditie wist de zoektermen niet langer,
  leveranciersnamen verschijnen weer in het snelzoeken, en ISO-geformatteerde
  datums worden correct gelezen.
- **AI-extractie corrigeert zichzelf.** Een aantoonbare verwisseling van
  netto- en totaalbedrag door de AI wordt automatisch teruggedraaid,
  AI-gescande velden komen na een documentherstart niet langer verkeerd terug,
  en AI-tabelextractie verwerkt documenten in paginabatches, zodat lange
  tabellen compleet aankomen.
- **Workflows overleven een auth-hapering.** Een kort onbereikbare
  auth-service wordt opnieuw geprobeerd in plaats van de run te laten
  mislukken, en een workflowtrigger die niet kan authenticeren, meldt de fout
  in plaats van het document vast te laten zitten.
- **Moeilijk leesbare pdf's worden weer geëxtraheerd.** Wanneer de
  standaard-pdf-tekstdecoder een pagina niet kan lezen (gebruikelijk bij met
  Ghostscript geproduceerde bestanden), valt de extractie terug op een tweede
  engine in plaats van niets terug te geven.
- **MFA werkt over regio's heen.** Registratiegegevens voor
  twee-factor-authenticatie worden gerepliceerd tussen de EU- en VS-regio's,
  zodat een tweede factor die in de ene regio is ingesteld, in de andere wordt
  gehonoreerd.

---

## Web App — `10.49.4`

### Aanmelden en accounts

- Afmelden in het ene browsertabblad meldt de andere tabbladen ook af, zonder
  de fout-toasts die verschenen wanneer tabbladen het oneens waren over de
  sessie.
- Het wijzigen van uw eigen wachtwoord in het profiel loopt via het speciale
  selfservice-eindpunt, zodat het werkt zonder beheerdersrechten.
- Aanmelden met een passkey vanuit de niet-thuisregio toont vertaalde
  foutmeldingen, en de verzendknop is zichtbaar.

### Validatiescherm

- Het tabblad "Extracted table" blijft niet langer eindeloos draaien wanneer
  er al een AI-tabel bestaat.
- Documenten waarvan de barcodegegevens ontbreken, breken de weergave voor
  barcodetoewijzing niet langer.
- M3-regels met meerdere belastingen bieden de belastingcode aan als een
  keuzelijst gevoed vanuit de list of values, in plaats van als vrij
  tekstveld.
- Grote leveranciersfacturen openen merkbaar sneller.

### Taken

- Kanban-kolommen pagineren terwijl u scrolt, zodat borden met veel taken snel
  laden.
- De teller voor openstaande taken in de zijbalk telt taken in uw
  suborganisatiecontext, niet in de context van het document dat toevallig
  openstaat.

### Workflow Builder

- De workflowlijst onthoudt uw zoekopdracht, sorteervolgorde, pagina en
  paginagrootte wanneer u een workflow opent en terugkeert, ook via het
  kruimelpad, en de pagina opent standaard op het tabblad List.

### Instellingen en beheer

- De pagina met stamgegevens komt niet langer leeg op door een race in de
  sortering, en sorteren op badges laat de pagina niet meer crashen.
- Een abonnement in de status "cancelling" kan worden hervat.
- De XSLT-detailpagina meldt laadfouten in plaats van niets te tonen, en de
  instellingen voor e-mailmeldingen gebruiken de volledige paginabreedte, met
  een werkend logvenster.
- De organisatiekiezer voor gebruikers met meerdere organisaties heeft een
  correcte rij-indeling, formaat en themakleuren, scrolt naar behoren en biedt
  een filter voor accounts met veel organisaties.
- Analytics: een mislukt metrics-verzoek toont een fouttoestand in plaats van
  nullen weer te geven, en de gebruikswidgets rapporteren eerlijk wanneer er
  geen meetgegevens beschikbaar zijn.
- Verouderde cache-opties zijn verwijderd van de pagina voor cachebeheer, en
  de pagina's Gebruikers en Groepen zijn verlost van hun geneste dubbele
  schuifbalken.
- "Use Default Template" in de layoutmanager crasht niet langer en blijft niet
  langer dood staan; de functie beweert ook niet meer dat er geen
  standaardlayout bestaat.
- Selectieregels behouden hun operatoren voor tekstovereenkomst, aanwezigheid
  en regex wanneer een regel opnieuw wordt geopend.
- Documenttypen ondersteunen transformatieregels per type, en de regellijst
  kreeg een actie om een vaste waarde in te stellen.
- Statusbadges van inkooporders worden correct toegewezen voor statuswaarden
  in ERP-schrijfwijze.
- De DocNet-schermen (AI Workforce), inclusief de Agent Wizard, zijn vertaald,
  en de dialoog voor het aanmaken/bewerken van ideeën scrolt horizontaal.
- Offertes in het leveranciersportaal: beheerde maateenheden verschijnen in de
  regelitemtabel, de goedkeuringsopmaak geldt alleen voor contractoffertes, en
  de vergelijkingsregel verschijnt niet langer wanneer beide waarden identiek
  zijn.
- De JSON-terugval van de foutpagina is leesbaar in donkere modus, en
  rapporten gebruiken een correct label "laatste 7 dagen" in plaats van een
  losse "7".

## API Service — `12.74.0`

### Dashboard en zoeken

- Sorteren werkt ongeacht welke kolommen zichtbaar zijn, en een trefwoord dat
  het zoeken doorgeeft aan de volledige-tekstzoekfunctie laat niet langer een
  kapot SQL-fragment achter.
- Leveranciersnamen verschijnen weer in het snelzoeken voor organisaties
  zonder volledige-tekstindexering.
- ISO-geformatteerde datums (2026-08-12) worden niet langer verkeerd gelezen
  door de dag-eerst-datumnormalisatie.
- Dashboardexports leiden kale tekstwaarden zoals factuurnummers naar de
  juiste kolom.

### E-facturen

- FacturaE 3.1 (Spanje): classificatieregel en volledige veldtoewijzingen.
- XRechnung-classificatieregels zijn verankerd aan hun syntaxisfamilie, zodat
  een UBL-document niet langer door CII-regels wordt gematcht en omgekeerd.
- De geaccepteerde versie "3.0" dekt haar hele patchfamilie (3.0.1, 3.0.2).
- CII-facturen nemen de juridische naam van de leverancier over en gebruiken
  de handelsnaam alleen als terugvaloptie.
- De ebInterface-toewijzingen (Oostenrijk) zijn versiegetrouw, met een
  gecorrigeerde catch-all en opnieuw opgebouwde fixtures.
- De standaardinstellingen van Factur-X en ZUGFeRD kregen het extractiepad
  voor de bedrijfsnaam, en standaard-headertransformaties voor btw-tarief,
  factuurtype en tier-3-velden zijn gerepareerd, samen met familiebrede
  semantiek voor kortingen, btw en stukprijzen.
- Belastingcategoriecodes uit de bron worden niet langer blind toegewezen aan
  uw ERP-codes.
- Documenten die zowel "factuur" als "creditnota" vermelden, krijgen bij
  voorkeur de classificatie creditnota.

### Documenten en extractie

- Wanneer de standaard-pdf-decoder de ingebedde tekst van een pagina niet kan
  lezen, valt de extractie terug op een tweede engine, zodat getroffen pdf's
  worden geëxtraheerd in plaats van leeg terug te komen.
- De hoofdschakelaar voor barcodes heet nu `BARCODE_EXTRACTION`; de oude
  QR-code-instelling blijft werken als alias.
- Een geheugenlek in de achtergrondplanner is gedicht; het liet de verwerking
  over dagen van uptime langzaam achteruitgaan.
- Leveranciers die zonder land worden geïmporteerd, blijven leeg in plaats van
  standaard op Duitsland te worden gezet.

### Export en stamgegevens

- Save Rules meldt een mislukking wanneer er niets wordt weggeschreven, in
  plaats van succes te claimen.
- Regels met bedrag nul worden niet langer weggelaten uit
  auto-accounting-exports, en een filter dat elke bucket matchte, is
  gerepareerd.
- M3-exports ondersteunen post-hooks voor aanvullende informatie.
- Eén mislukte datasetcontrole maakt niet langer het hele stamgegevensscherm
  leeg.
- PO-caches worden ongeldig gemaakt wanneer het ERP de status van een
  inkooporder bijwerkt, zodat het dashboard niet langer de verouderde status
  toont.

### Beheer

- Elke voorkeur toont welke gebruiker haar het laatst heeft gewijzigd.
- Extractieregels kunnen per leverancier worden verwijderd en via nieuwe
  eindpunten worden gekloond.
- Ontvangers van status-alert-e-mails worden NULL-veilig vergeleken, wat een
  crash in de meldingsbezorging verhelpt.

## Auth Service — `1.75.9`

- Een organisatie-API-sleutel die tegen een niet-gerelateerde organisatie
  wordt gebruikt, wordt geweigerd.
- Het aanmaken van een organisatie gaf een fout terug terwijl de rij wél werd
  opgeslagen; het antwoord is nu correct.
- Aanmelden met een passkey terwijl er geen is geregistreerd, geeft een eigen
  foutcode terug, zodat het aanmeldscherm kan zeggen wat er mis is.

## Auth Bridge Service — `0.4.2`

- Registratietabellen voor twee-factor-authenticatie worden gerepliceerd
  tussen de EU- en VS-regio's, en rijen worden geïdentificeerd op hun echte
  primaire sleutel.

## Docflow Service — `2.8.7`

- Een workflowtrigger die niet kan authenticeren, meldt de mislukking in
  plaats van het document vast te laten zitten, en een kort onbereikbare
  auth-service wordt opnieuw geprobeerd in plaats van als een ongeldig token
  te worden behandeld.
- Kaarten voor offertevergelijking: artikelnummers worden alleen vergeleken
  voor regels die de artikelprijsmatrix beschrijft; regels zonder maateenheid
  of zonder prijs worden overgeslagen in plaats van de vergelijking te laten
  mislukken.
- De vergelijkingskaart voor contractprijzen kreeg een any/all-operatoroptie,
  en kaartcaches worden correct ongeldig gemaakt na migraties en code-updates.
- Weggevallen SSL-verbindingen worden behandeld als tijdelijk en opnieuw
  geprobeerd in plaats van de run te laten mislukken.

## Docnet Service — `1.56.4`

- Health- en versie-eindpunten blokkeren niet langer op live controles, wat de
  dialoog Service Versions voorheen liet hangen.

## Email Service — `1.40.6`

- Wanneer een inkomende e-mail wordt overgeslagen, wordt de reden getoond in
  de importgebeurtenisrij in plaats van te worden verzwegen.
- Bijgevoegde `.eml`-containerbestanden worden niet langer als documenten
  geïmporteerd.
- Een mislukte Microsoft Office-aanmelding levert een leesbare foutmelding op,
  en een transportfout van de AI-service telt als "onduidelijk" in plaats van
  als afwijzing.

## Extraction Service — `1.53.8`

- Een aantoonbare verwisseling van netto- en totaalbedrag door de AI wordt na
  de veldextractie teruggedraaid, en guard-fouten worden gelogd in plaats van
  stilzwijgend te passeren.
- AI-gescande velden komen na een documentherstart niet langer verkeerd terug.
- AI-tabelextractie werkt in paginabatches en voegt alle batches samen, zodat
  lange tabellen compleet aankomen.
- Documenten die zowel "factuur" als "creditnota" vermelden, krijgen bij
  voorkeur de classificatie creditnota.
- Herhaald opschonen van kop- en voetteksten wordt gecachet, wat de extractie
  op meerpaginadocumenten versnelt.

## Fulltext Service — `1.41.7`

- Een OR-filter in combinatie met een bereik- of gelijkheidsconditie wist de
  zoektermen niet langer.
- Sorteren gebruikt de juiste indexpaden en toont de echte reden wanneer de
  zoekbackend een query weigert; een sorteerregressie die het zoeken met ruwe
  query's volledig brak, is opgelost in dezelfde week waarin hij ontstond.
- Documentopzoekingen werken op oudere indexen met tekst-mapping.
- De tokencache is beperkt tot het paar van token en organisatie, zodat het
  wisselen van organisatie geen resultaten meer kan opleveren onder de vorige
  context.
