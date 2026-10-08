# DocBits Roadmap

_Planningsstand per 7 oktober 2026. Elke release vermeldt de geplande
sandbox-datum (wanneer klanten de release kunnen testen) en de geplande
productiedatum. De thema's beschrijven wat voor de release is gepland, niet wat
al is uitgeleverd; omvang en data kunnen verschuiven. Hotfixes tussen releases
worden gedocumenteerd in de [Release-opmerkingen](release-notes/README.md)._

| Release | Sandbox | Productie |
|---|---|---|
| R1.1 | 16 oktober 2026 | 4 november 2026 |
| R1.2 | 16 februari 2027 | 3 maart 2027 |
| R1.3 | 1 juni 2027 | 16 juni 2027 |
| R1.4 | 5 oktober 2027 | 20 oktober 2027 |

---

## R1.1 — Sandbox 16 oktober 2026 · Productie 4 november 2026

**Transformatieregels en layouts**

- Een regelengine voor geëxtraheerde veld- en kolomwaarden: waarden instellen,
  vervangen of afleiden met geneste conditiegroepen, met een instellingenscherm
  om de regels te beheren. De conditie "is one of" accepteert meerdere waarden,
  de regellijst kan op regel-ID worden doorzocht, en regels worden ook na de
  opzoeking van stamgegevens uitgevoerd.
- Layoutselectieregels krijgen dezelfde geneste condities en een optioneel
  uitvoeringslog. Layoutselectie werkt onafhankelijk van de herkomst van een
  document.
- Manage Layouts, Custom Validation Rules en Transformation Rules hebben de
  betaschakelaar niet meer nodig.
- Duidelijke voorrangsregels voor veldlabels op kopvelden en tabelkolommen.
  Gebruikers kunnen eigen vertaalsleutels aanmaken voor veldinstellingen en
  tabelkolommen.
- Een tabelkolom kan opnieuw worden toegewezen nadat deze is verwijderd, en de
  prijstabel voor leveranciersartikelen toont al haar kolommen.

**Goedkeurings- en validatieschermen**

- De drie regelitemtabellen op het goedkeuringsscherm (factuurregels,
  vergelijkingsregels, PO matching) delen één stijl.
- Het laatst geopende zijpaneel (activiteitenstroom of
  goedkeuringsgeschiedenis) wordt per gebruiker onthouden.
- Documenten samenvoegen vanuit het goedkeuringsscherm met de documentuploader.
- Aangepaste validatieregels behandelen verzendkosten generiek, tonen een
  veldmelding in plaats van een algemene fout wanneer een verplicht veld leeg
  is, en regels die ten onrechte geen fout meldden, zijn gecorrigeerd.
  Standaardregels van het systeem kunnen worden gedupliceerd.
- Een afwijking tussen hoeveelheid en nettobedrag in een met AI geëxtraheerde
  tabel wordt gemeld, een factuur met een gematcht purchase order wordt niet meer
  als kostenfactuur geclassificeerd, en een datum die door een regel is
  herformatteerd, wordt geaccepteerd.
- Een goedkeuringsscherm dat na goedkeuren of afwijzen bleef hangen op de
  laadoverlay, is opgelost. Een laadbalk vervangt het eenvoudige laadicoon, en
  pagina-URL's zijn vriendelijker.
- Het openen van een documentlink nadat de sessie is verlopen leidt naar de
  inlogpagina in plaats van naar een 404.

**Duplicaatdetectie**

- Aangepaste velden verschijnen in het resultaat van de duplicaatdetectie, en de
  duplicaatinstellingen kunnen worden doorzocht.
- "Block Duplicate Document Export" blokkeert de export van een gedetecteerd
  duplicaat.

**Workflows en taken**

- Een knop "New workflow", logs voor geavanceerde workflows, een
  overzichtelijker watchdog-logscherm, en workflowstappen die een veld of
  selectievakje wijzigen, worden betrouwbaar toegepast.
- Bij het toevoegen van een regel in een beslisboom blijven de gebruikersnamen
  behouden in plaats van dat er ID's worden getoond.
- Elke statuswijziging van een document wordt gelogd.
- Het aanmaken van een nieuwe e-mailsjabloon werkt weer.
- De takenlijst toont zijn taken bij de eerste keer laden.

**Import**

- E-mailimport verplaatst een mail pas uit het postvak nadat de upload is
  bevestigd, behandelt een opnieuw bezorgde doorgestuurde mail als één
  bezorging, registreert wie het laatst heeft opgeslagen, en vermeldt een bijlage
  één keer met de reden wanneer deze mislukt.
- FTP- en SFTP-import krijgen een echte optie "verwijderen na import" naast
  verplaatsen en archiveren. Wachtwoorden worden niet meer beschadigd wanneer een
  configuratie wordt bewerkt, de verbindingstest werkt voor nieuwe
  SFTP-verbindingen, en een mislukte SFTP-verbinding of verkeerde login toont een
  specifieke melding in plaats van een algemene fout.
- Beheerders worden in de Settings Assistant geïnformeerd wanneer een
  geconfigureerde FTP- of e-mailimport niet meer werkt.
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
- Een kostenfactuur met twee btw-tarieven behoudt beide boekingsregels.

**Purchase order matching**

- Matching vereist een hoeveelheidskolom, gebruikt de prijs per hoeveelheid in
  de basiseenheid, en de fallback op de laatste regel kan per klant worden in-
  of uitgeschakeld.
- Leveringsbonregels kunnen afzonderlijk worden geselecteerd.
- Het e-documentscherm bevriest niet meer bij facturen met meer dan 250 regels.

**Touchless Intelligence**

- Meer detail in het Touchless-rapport, en het Touchless-selectievakje
  weerspiegelt de opgeslagen instelling.

**Dashboard, accounts en abonnement**

- Het dashboard kan tot 10.000 documenten per zoekopdracht bevatten, en een
  aangepast datumfilter wordt correct toegepast.
- Kortingsvervaldatum en factuurvervaldatum zijn beschikbaar als layoutvelden en
  worden bij import ingevuld.
- Gebruikers waarmee een dashboard is gedeeld, blijven behouden wanneer het
  dashboard wordt opgeslagen, en "Updated by" toont de juiste persoon.
- Gearchiveerde documenten kunnen weer uit de status "Archived" worden
  gehaald.
- Gebruikers kunnen na een wachtwoordreset weer inloggen.
- De pagina van het abonnement toont het gebruik voor het abonnement en de
  bijbehorende functies.

**Export en EDI**

- Een extra Infor M3-exportstap voor aanvullende factuurinformatie.
- Een paklijst met meerdere containernummers wordt geëxporteerd als één record
  per container.
- Het opnieuw importeren van een receive delivery mislukt niet langer op een
  dubbele sleutel, en receive delivery BOD's worden in de juiste volgorde
  toegepast.
- EDI-mappings voor factuur, purchase order en orderbevestiging zijn
  bijgewerkt.
- Het testen van de verbinding van een nieuwe Infor IDM- of Infor LN-
  exportconfiguratie werkt.

**Beveiliging**

- De organisatiecontrole voor API-sleutels wordt in elke omgeving afgedwongen.

---

## R1.2 — Sandbox 16 februari 2027 · Productie 3 maart 2027

**Goedkeuring en purchase order matching**

- Een status "Pending input" pauzeert een document totdat iemand antwoordt,
  zonder de workflow of de auditgeschiedenis te verstoren, en goedkeurders
  kunnen vragen stellen zonder de goedkeuringsflow te onderbreken.
- Een document kan aan een andere gebruiker worden toegewezen (eerste fase).
- Vooruitbetalingsfacturen kunnen vóór de goederenontvangst worden gematcht
  terwijl "Match on received quantity" actief blijft.
- Het matchingscherm biedt alleen geschikte PO regels aan, en matches over
  meerdere regels die de prijsvergelijking overslaan, tonen nog steeds de
  eenheidsprijs op het goedkeuringsscherm.
- Een vlag voor ontvangstbeschikbaarheid vergelijkt gefactureerde en ontvangen
  hoeveelheden.
- Orderbevestigingen: kostenelementen worden getoond terwijl de goedkeuring in
  behandeling is, kleurgecodeerde toeslagposities in PO matching, en de
  artikelnummerkolom in de factuurregelitems.
- RMA-regels van leveranciers worden afgehandeld.

**Import en classificatie**

- Het leverancierstype wordt afgeleid uit de regelitems.
- Het supportticketformulier accepteert bijlagen en koppelt de organisatie
  automatisch.

**Instellingen en automatisering**

- Het script "Set sub-organisation" wordt een transformatieregel.
- Standaardkolommen kunnen uit een documenttype worden verwijderd.

**Export**

- De exportgeschiedenis toont geëxporteerde documenten weer.
- Vrachtfacturen worden naar Infor LN geëxporteerd.
- Exportbestandsnamen zijn configureerbaar.
- Uitgebreide Vertex-belastingintegratie.

---

## R1.3 — Sandbox 1 juni 2027 · Productie 16 juni 2027

**Auto Accounting Rule Manager**

- Regels wijzen automatisch rekeningen en dimensies toe, afgebakend per
  suborganisatie en documenttype, met een auditscherm dat toont welke regel is
  toegepast.
- Een regel kan stamgegevens opzoeken en meerdere velden tegelijk toewijzen, of
  een waarde vullen vanuit een kolom van een tabelregel.
- Velden en dimensies kunnen afzonderlijk worden gewist, regelitems kunnen
  worden verwijderd (ook regels zonder bedrag), en de regels blijven werken op
  velden die van tekst naar keuzelijst zijn gewijzigd.
- Voorspellingen ondersteunen meerdere btw-codes en dimensies, vouchers en
  boekingsreferenties. De Auto Accounting-schermen zijn beschikbaar in meerdere
  talen.

**Purchase order matching**

- Het match-icoon navigeert, scrolt en markeert over tabbladen heen, inclusief
  een-op-veel-matches.
- Eenheidsconversie met aliassen (bijvoorbeeld KG en TO), een configureerbare
  afrondingsvariantie met een afrondingsrekening, en berekeningen met vier
  decimalen die als drie worden getoond.

**Gebruiksgemak**

- De uitvoeringsvolgorde van documentscripts is zichtbaar in de frontend.
- Met Enter en Tab navigeert u via het toetsenbord door de velden.

**Export**

- Een onvolledig document in Infor LN wordt na een mislukte export verwijderd.
- De databaseconnector bevat alle relevante tabellen.

---

## R1.4 — Sandbox 5 oktober 2027 · Productie 20 oktober 2027

**Auto Accounting op het goedkeuringsscherm**

- Goedkeurders kunnen rechtstreeks op het goedkeuringsscherm met Auto
  Accounting werken.
- De goedkeuring kan afhankelijk worden gemaakt van boekhoudvelden zoals
  grootboekrekening of land, met een crediteurencorrectie wanneer een document
  wordt teruggestuurd.
- Een keuzelijst voor btw-codes in Auto Accounting zonder meerdere btw-regels
  in te stellen.
- Dimensies worden in een nieuwe structuur opgeslagen, zodat grote
  dimensiesets sneller laden, en de Rule Manager krijgt een feedbackronde.

**Goedkeuring**

- Een verbeterde goedkeuringsflow, delegatie aan een andere gebruiker tijdens de
  goedkeuring, en een knop "Export & Next".

**Purchase order matching en exportbewaking**

- Overgematchte facturen, waarbij de gefactureerde hoeveelheid de ontvangen
  hoeveelheid overschrijdt, worden op het matchingscherm herkend, en
  meeteenheden worden tijdens het matchen van de factuur geconverteerd.
- Toeslagcodes (tol, transport, energie) worden herkend en hun kosten verdeeld.
- De export wordt met een waarschuwing geblokkeerd wanneer de gematchte
  hoeveelheid de ontvangen hoeveelheid overschrijdt of er te veel van afwijkt,
  of wanneer de boekingsdatum vóór de magazijnboekingsdatum ligt.

**Import en instellingen**

- Een retry-mechanisme voor FTP-, e-mail- en inbound-e-mailimport met
  automatische en handmatige herverwerking, en het afzenderadres is beschikbaar
  vanuit e-mailimport.
- Instellingen kunnen worden doorzocht over alle schakelaars en subpagina's
  heen.
- In de e-mailserverinstellingen kunt u een verlopen OAuth- of client secret
  vervangen zonder het postvak opnieuw te hoeven instellen.
- De mapping van leveranciersartikelnummers (conversietabel voor
  artikelnummers) kan vanuit een CSV-import worden gevuld.
- De goedkeuringsgeschiedenis kan via SFTP-export worden geëxporteerd.

**DocNet Agents**

- Orderintake: een klantorder wordt een verkooporder in Infor M3 of Infor
  LN (eerste versie, tekstdocumenten).

<!-- Generated from Jira "Release No." (customfield_10392) on 2026-10-07 by the
     docbits-roadmap skill. Releases up to R1.4 only; R1.5 and later are not
     published yet. Themes only; ticket keys, customer names and internal work
     are deliberately left out. Rerun the skill to refresh. -->
