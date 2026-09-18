# DocBits Roadmap

_Planningsstand per 18 september 2026. Elke release vermeldt de geplande
sandbox-datum (wanneer klanten de release kunnen testen) en de geplande
productiedatum. De thema's beschrijven wat voor de release is gepland, niet wat
al is uitgeleverd; omvang en data kunnen verschuiven. Hotfixes tussen releases
worden gedocumenteerd in de [Release-opmerkingen](release-notes/README.md)._

| Release | Sandbox | Productie |
|---|---|---|
| R1.1 | 5 oktober 2026 | 14 oktober 2026 |
| R1.2 | 23 november 2026 | 2 december 2026 |
| R1.3 | 8 februari 2027 | 17 februari 2027 |
| R1.4 | 7 april 2027 | 15 april 2027 |
| R1.5 | 18 mei 2027 | 27 mei 2027 |
| R1.6 | 6 juli 2027 | 15 juli 2027 |
| R1.7 | 21 september 2027 | 30 september 2027 |
| R2.0 | nog aan te kondigen | nog aan te kondigen |

---

## R1.1 — Sandbox 5 oktober 2026 · Productie 14 oktober 2026

**Transformatieregels en layouts**

- Een regelengine voor geëxtraheerde veld- en kolomwaarden: waarden instellen,
  vervangen of afleiden met geneste conditiegroepen, met een instellingenscherm
  om de regels te beheren. Layoutselectieregels krijgen dezelfde geneste
  condities.
- Layoutselectie werkt onafhankelijk van de herkomst van een document.
- Duidelijke voorrangsregels voor veldlabels op kopvelden en tabelkolommen.
- Een tabelkolom kan opnieuw worden toegewezen nadat deze is verwijderd, en de
  prijstabel voor leveranciersartikelen toont al haar kolommen.

**Goedkeurings- en validatieschermen**

- De drie regelitemtabellen op het goedkeuringsscherm (factuurregels,
  vergelijkingsregels, PO matching) delen één stijl, en de vergelijkingsweergave
  toont het artikelnummer dat bij de regel hoort.
- Het laatst geopende zijpaneel (activiteitenstroom of
  goedkeuringsgeschiedenis) wordt per gebruiker onthouden.
- Documenten samenvoegen vanuit het goedkeuringsscherm met de documentuploader.
- Aangepaste validatieregels behandelen verzendkosten generiek, en regels die
  ten onrechte geen fout meldden, zijn gecorrigeerd.
- Een laadbalk vervangt het eenvoudige laadicoon; vriendelijkere pagina-URL's.

**Duplicaatdetectie**

- Aangepaste velden verschijnen in het resultaat van de duplicaatdetectie, en de
  duplicaatinstellingen kunnen worden doorzocht.

**Workflows en taken**

- Een knop "New workflow", logs voor geavanceerde workflows, een
  overzichtelijker watchdog-logscherm, en workflowstappen die een veld of
  selectievakje wijzigen, worden betrouwbaar toegepast.
- Bij het toevoegen van een regel in een beslisboom blijven de gebruikersnamen
  behouden in plaats van dat er ID's worden getoond.
- Elke statuswijziging van een document wordt gelogd.
- Het aanmaken van een nieuwe e-mailsjabloon werkt weer.

**Import**

- E-mailimport verplaatst een mail pas uit het postvak nadat de upload is
  bevestigd, behandelt een opnieuw bezorgde doorgestuurde mail als één
  bezorging, registreert wie het laatst heeft opgeslagen, en accepteert met
  S/MIME ondertekende mails.
- FTP-import krijgt een echte optie "verwijderen na import" naast verplaatsen
  en archiveren.
- De upload vanuit de scanner-app werkt weer.
- Purchase order BOD-bestanden die in de US-regio worden geüpload, blijven in
  de US-regio.

**Documentverwerking en extractie**

- Wanneer de barcodeservice blijft hangen, toont het document de fout in plaats
  van eindeloos in "Processing" te blijven staan.
- Een nieuw, goedkoper AI-modelniveau ("Eco") voor extractie.
- Bij gestructureerde AI-extractie blijven getrainde leveranciersartikelnummers
  getraind, en artikelnummer en leveranciersartikelnummer worden niet meer
  verwisseld.
- UBL e-documentsjablonen zijn aangepast; extractiecorrecties voor bedragen,
  btw-tarieven, eenheidsprijzen en purchase order nummers op specifieke
  leverancierslayouts.
- Extra datumformaten worden herkend.

**Purchase order matching**

- Matching vereist een hoeveelheidskolom, gebruikt de prijs per hoeveelheid in
  de basiseenheid, en de fallback op de laatste regel kan per klant worden in-
  of uitgeschakeld.
- Leveringsbonregels kunnen afzonderlijk worden geselecteerd.
- Het e-documentscherm bevriest niet meer bij facturen met meer dan 250 regels.

**Touchless Intelligence**

- Meer detail in het Touchless-rapport, en het Touchless-selectievakje
  weerspiegelt de opgeslagen instelling.

**Dashboard**

- Het dashboard kan tot 10.000 documenten per zoekopdracht tonen.
- Kortingsvervaldatum en factuurvervaldatum zijn beschikbaar als layoutvelden en
  worden bij import ingevuld.
- Gebruikers waarmee een dashboard is gedeeld, blijven behouden wanneer het
  dashboard wordt opgeslagen, en "Updated by" toont de juiste persoon.
- Gearchiveerde documenten kunnen weer uit de status "Archived" worden
  gehaald.

**Export en EDI**

- Een extra Infor M3-exportstap voor aanvullende factuurinformatie.
- Een paklijst met meerdere containernummers wordt geëxporteerd als één record
  per container.
- Het opnieuw importeren van een receive delivery mislukt niet langer op een
  dubbele sleutel, en receive delivery BOD's worden in de juiste volgorde
  toegepast.
- EDI-mappings voor factuur, purchase order en orderbevestiging zijn
  bijgewerkt.

**Beveiliging**

- De organisatiecontrole voor API-sleutels wordt in elke omgeving afgedwongen.

---

## R1.2 — Sandbox 23 november 2026 · Productie 2 december 2026

**Goedkeuring en purchase order matching**

- Een status "Pending input" pauzeert een document totdat iemand antwoordt,
  zonder de workflow of de auditgeschiedenis te verstoren, en goedkeurders
  kunnen vragen stellen zonder de goedkeuringsflow te onderbreken.
- Vooruitbetalingsfacturen kunnen vóór de goederenontvangst worden gematcht
  terwijl "Match on received quantity" actief blijft.
- Een vlag voor ontvangstbeschikbaarheid vergelijkt gefactureerde en ontvangen
  hoeveelheden.
- Orderbevestigingen: kostenelementen worden getoond terwijl de goedkeuring in
  behandeling is, kleurgecodeerde toeslagposities in PO matching, en de
  artikelnummerkolom in de factuurregelitems.
- Niet-gemapte kolommen tellen niet langer mee in de berekening van het
  tabelbedrag.
- RMA-regels van leveranciers worden afgehandeld.

**Import en classificatie**

- Het afzenderadres is beschikbaar vanuit e-mailimport.
- Het leverancierstype wordt afgeleid uit de regelitems.

**Instellingen en automatisering**

- Het script "Set sub-organisation" wordt een transformatieregel.
- Standaardkolommen kunnen uit een documenttype worden verwijderd.

**Export**

- De exportgeschiedenis toont geëxporteerde documenten weer.
- Vrachtfacturen worden naar Infor LN geëxporteerd.

---

## R1.3 — Sandbox 8 februari 2027 · Productie 17 februari 2027

**Auto Accounting Rule Manager**

- Regels wijzen automatisch rekeningen en dimensies toe, afgebakend per
  suborganisatie en documenttype, met een auditscherm dat toont welke regel is
  toegepast.
- Een regel kan een waarde vullen vanuit een kolom van een tabelregel.
- Velden en dimensies kunnen afzonderlijk worden gewist, regelitems kunnen
  worden verwijderd (ook regels zonder bedrag), en de regels blijven werken op
  velden die van tekst naar keuzelijst zijn gewijzigd.

**Purchase order matching**

- Het match-icoon navigeert, scrolt en markeert over tabbladen heen, inclusief
  een-op-veel-matches.
- Eenheidsconversie met aliassen (bijvoorbeeld KG en TO), een configureerbare
  afrondingsvariantie met een afrondingsrekening, en berekeningen met vier
  decimalen die als drie worden getoond.

**Export**

- Configureerbare exportbestandsnamen.
- Een onvolledig document in Infor LN wordt na een mislukte export verwijderd.
- De databaseconnector bevat alle relevante tabellen.

---

## R1.4 — Sandbox 7 april 2027 · Productie 15 april 2027

**Import**

- Een retry-mechanisme voor FTP-, e-mail- en inbound-e-mailimport met
  automatische en handmatige herverwerking.

**DocNet Agents**

- Orderintake: een klantorder wordt een verkooporder in Infor M3 of Infor LN
  (eerste versie, tekstdocumenten).

**Goedkeuring**

- Een verbeterde goedkeuringsflow, delegatie aan een andere gebruiker tijdens de
  goedkeuring, en een knop "Export & Next".

**Purchase order matching**

- Alleen geschikte PO regels worden op het matchingscherm aangeboden.
- Overgematchte facturen, waarbij de gefactureerde hoeveelheid de ontvangen
  hoeveelheid overschrijdt, worden op het matchingscherm herkend, en
  meeteenheden worden tijdens het matchen van de factuur geconverteerd.

**Overig**

- Feedbackronde over de Rule Manager.
- Het supportticketformulier accepteert bijlagen en koppelt de organisatie
  automatisch.
- Uitgebreide Vertex-belastingintegratie.

---

## R1.5 — Sandbox 18 mei 2027 · Productie 27 mei 2027

**Auto Accounting**

- Lookup-actie in de Rule Manager: stamgegevens matchen en meerdere velden
  tegelijk toewijzen.
- Voorspellingen ondersteunen meerdere btw-codes en dimensies, vouchers en
  boekingsreferenties.
- Auto Accounting-schermen in meerdere talen.

**Goedkeuring en purchase order matching**

- Een document opnieuw toewijzen aan een andere gebruiker.
- De kolomvolgorde op het PO matching scherm wordt per gebruiker opgeslagen.
- Toeslagcodes (tol, transport, energie) worden herkend en hun kosten verdeeld.

**Exportbewaking**

- De export wordt met een waarschuwing geblokkeerd wanneer de gematchte
  hoeveelheid de ontvangen hoeveelheid overschrijdt of er te veel van afwijkt,
  of wanneer de boekingsdatum vóór de magazijnboekingsdatum ligt.

**Gebruiksgemak**

- De uitvoeringsvolgorde van documentscripts is zichtbaar in de frontend.
- Met Enter en Tab navigeert u via het toetsenbord door de velden.

---

## R1.6 — Sandbox 6 juli 2027 · Productie 15 juli 2027

**Instellingen**

- Instellingen kunnen worden doorzocht over alle schakelaars en subpagina's
  heen.
- In de e-mailserverinstellingen kunt u een verlopen OAuth- of client secret
  vervangen zonder het postvak opnieuw te hoeven instellen.
- De mapping van leveranciersartikelnummers (conversietabel voor
  artikelnummers) kan vanuit een CSV-import worden gevuld.

**Auto Accounting**

- Dimensies worden in een nieuwe structuur opgeslagen, zodat grote
  dimensiesets sneller laden.

---

## R1.7 — Sandbox 21 september 2027 · Productie 30 september 2027

**Auto Accounting op het goedkeuringsscherm**

- Goedkeurders kunnen rechtstreeks op het goedkeuringsscherm met Auto
  Accounting werken.
- De goedkeuring kan afhankelijk worden gemaakt van boekhoudvelden zoals
  grootboekrekening of land, met een crediteurencorrectie wanneer een document
  wordt teruggestuurd.
- Een keuzelijst voor btw-codes in Auto Accounting zonder meerdere btw-regels
  in te stellen.

---

## R2.0 — Sandbox nog aan te kondigen · Productie nog aan te kondigen

**Auto Accounting**

- Velden die op een lijst zijn gebaseerd, accepteren ook vrije tekst.
- Verplichte velden worden gevalideerd.
- Modelvoorspellingen vullen boekhoudvelden automatisch in (hybride modus met
  het getrainde voorspellingsmodel), met een audittrail van wat het model heeft
  ingevuld.

<!-- Generated from Jira "Release No." (customfield_10392) on 2026-09-18 by the
     docbits-roadmap skill. Themes only; ticket keys, customer names and
     internal work are deliberately left out. Rerun the skill to refresh. -->
