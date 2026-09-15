# DocBits Roadmap

_Planningsstand per 15 september 2026. Elke release vermeldt de geplande
sandbox-datum (wanneer klanten de release kunnen testen) en de geplande
productiedatum. De thema's beschrijven wat voor de release is gepland, niet wat
al is uitgeleverd; omvang en data kunnen verschuiven. Hotfixes tussen releases
worden gedocumenteerd in de [Release-opmerkingen](release-notes/README.md)._

| Release | Sandbox | Productie |
|---|---|---|
| R1.1 | 16 september 2026 | 23 september 2026 |
| R1.2 | 21 oktober 2026 | 28 oktober 2026 |
| R1.3 | 25 november 2026 | 2 december 2026 |
| R1.4 | 27 januari 2027 | 3 februari 2027 |
| R1.5 | 10 maart 2027 | 17 maart 2027 |

---

## R1.1 — Sandbox 16 september 2026 · Productie 23 september 2026

**Transformatieregels en layouts**

- Een regelengine voor geëxtraheerde veld- en kolomwaarden: waarden instellen,
  vervangen of afleiden met geneste conditiegroepen, met een instellingenscherm
  om de regels te beheren. Layoutselectieregels krijgen dezelfde geneste
  condities.
- Layoutselectie werkt onafhankelijk van de herkomst van een document.
- Duidelijke voorrangsregels voor veldlabels op kopvelden en tabelkolommen.

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

- Een knop "New workflow", logs voor geavanceerde workflows, en workflowstappen
  die een veld of selectievakje wijzigen, worden betrouwbaar toegepast.
- Goedkeurings-e-mails bereiken de toegewezen goedkeurders in
  inkoopfactuurworkflows.
- Elke statuswijziging van een document wordt gelogd.

**Import**

- E-mailimport verplaatst een mail pas uit het postvak nadat de upload is
  bevestigd, behandelt een opnieuw bezorgde doorgestuurde mail als één
  bezorging, registreert wie het laatst heeft opgeslagen, en accepteert met
  S/MIME ondertekende mails.
- FTP-import krijgt een echte optie "verwijderen na import" naast verplaatsen
  en archiveren.
- De upload vanuit de scanner-app werkt weer.

**Documentverwerking en extractie**

- Wanneer de barcodeservice blijft hangen, toont het document de fout in plaats
  van eindeloos in "Processing" te blijven staan.
- "Restrict to pages" beperkt alleen OCR en het tellen van pagina's; het knipt
  geen pagina's meer van het document af.
- Een document opslaan laat niet-gerelateerde gegevens ongemoeid.
- Een nieuw, goedkoper AI-modelniveau ("Eco") voor extractie, en tabeltags
  toepassen op de AI-tabel werkt weer.
- Het samenvoegen van een ZUGFeRD-PDF met een andere PDF behoudt de
  e-factuurgegevens; UBL e-documentsjablonen zijn aangepast; extractiecorrecties
  voor bedragen, btw-tarieven en purchase order nummers op specifieke
  leverancierslayouts.
- Extra datumformaten worden herkend.

**Purchase order matching**

- Matching vereist een hoeveelheidskolom, gebruikt de prijs per hoeveelheid in
  de basiseenheid, en de fallback op de laatste regel kan per klant worden in-
  of uitgeschakeld.
- Het e-documentscherm bevriest niet meer bij facturen met meer dan 250 regels.
- Diagnostiek meet de hoeveelheid ook wanneer een PO regel geen prijs heeft.

**Touchless Intelligence**

- Meer detail in het Touchless-rapport, en een blokkade door de purchase order
  wordt als zodanig gemeld in plaats van als een mislukte veldvalidatie.

**Dashboard**

- Het dashboard kan tot 10.000 documenten per zoekopdracht tonen.
- Kortingsvervaldatum en factuurvervaldatum zijn beschikbaar als layoutvelden en
  worden bij import ingevuld.
- Gebruikers waarmee een dashboard is gedeeld, blijven behouden wanneer het
  dashboard wordt opgeslagen; "Assigned to" en "Updated by" tonen de juiste
  persoon.
- Documentrechten gelden ook voor de volledige-tekstindex.

**Export en EDI**

- BOD-export behoudt tabelkolomwaarden die langer zijn dan 30 tekens.
- Een extra Infor M3-exportstap voor aanvullende factuurinformatie, en
  eenheidsprijzen in exports van regeltype 5.
- Het opnieuw importeren van een receive delivery mislukt niet langer op een
  dubbele sleutel.
- EDI X12-mappings voor factuur (810), purchase order (850), orderbevestiging
  (855), verzendbericht (856, inclusief WMS-export) en orderwijziging (860)
  zijn bijgewerkt.

**Beveiliging**

- Rekeningschema-mappings van leveranciers worden opgeslagen met gebonden
  SQL-parameters, en de organisatiecontrole voor API-sleutels wordt in elke
  omgeving afgedwongen.

---

## R1.2 — Sandbox 21 oktober 2026 · Productie 28 oktober 2026

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
- Een flow voor PO-wijzigingsverzoeken en de documenteigenaar in de
  Infor-exportmapping.

**Export**

- De exportgeschiedenis toont geëxporteerde documenten weer.
- Vrachtfacturen worden naar Infor LN geëxporteerd.

---

## R1.3 — Sandbox 25 november 2026 · Productie 2 december 2026

**Auto Accounting Rule Manager**

- Regels wijzen automatisch rekeningen en dimensies toe, afgebakend per
  suborganisatie en documenttype, met een auditscherm dat toont welke regel is
  toegepast.
- Een regel kan een waarde vullen vanuit een kolom van een tabelregel.
- Velden en dimensies kunnen afzonderlijk worden gewist, tabelregels zonder
  bedrag kunnen worden verwijderd, en de regels blijven werken op velden die
  van tekst naar keuzelijst zijn gewijzigd.

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

## R1.4 — Sandbox 27 januari 2027 · Productie 3 februari 2027

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
- Meerdere magazijnboekingen kunnen met één factuurregel matchen, en
  meeteenheden worden tijdens het matchen van de factuur geconverteerd.

**Overig**

- Feedbackronde over de Rule Manager.
- Het supportticketformulier accepteert bijlagen en koppelt de organisatie
  automatisch.
- Uitgebreide Vertex-belastingintegratie.

---

## R1.5 — Sandbox 10 maart 2027 · Productie 17 maart 2027

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

<!-- Generated from Jira "Release No." (customfield_10392) on 2026-09-15 by the
     docbits-roadmap skill. Themes only; ticket keys, customer names and
     internal work are deliberately left out. Rerun the skill to refresh. -->
