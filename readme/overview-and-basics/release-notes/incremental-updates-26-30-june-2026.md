# DocBits Release-opmerkingen — 26–30 juni 2026

_Wat deze productie-upgrade heeft opgeleverd, in gewone taal. Elke service toont de
versie die nu live staat op productie. Services die niet zijn vermeld, hadden in dit
tijdvenster geen wijzigingen die zichtbaar zijn voor klanten._

---

## Hoogtepunten

- **Eén verbinding voor AI-assistenten (DocBits MCP).** Eén enkele, geïntegreerde
  gateway bedient nu alle DocBits-tools — inclusief DocFlow — via de hoofd-API, zodat
  AI-assistenten (Claude, Gemini CLI, Codex) verbinding maken via één betrouwbaar
  eindpunt in plaats van meerdere.
- **Slimmer meertalig zoeken in het dashboard.** Zoekverbindingswoorden
  (**AND / OR**) verschijnen nu in uw taal met kleurmarkering, factuur-subtypes bieden
  een keuzelijst met waarden, en meldingen over de zoeksyntaxis worden gelokaliseerd —
  met over de hele linie soepelere toetsenbordafhandeling.
- **Soepeler goedkeuringen & rechten.** Goedkeuring wordt niet langer geactiveerd
  wanneer de verpakkingseenheid uit een orderbevestiging leeg is, normale gebruikers
  kunnen na de migratie van de toegangscontrole weer kostenelementen goedkeuren, en
  rechten op documentniveau worden correct toegepast, ook wanneer een tabelkolom al
  bestaat.
- **De app werkt zichzelf bij.** Wanneer een nieuwe versie wordt uitgebracht, ververst
  DocBits nu automatisch in plaats van u te onderbreken met een "Refresh Now"-pop-up.
- **Robuustere inkoopordermatching.** Kolomwaardetransformaties, crashbeveiligingen
  voor regels zonder prijs of hoeveelheid, en automatisch opnieuw proberen bij
  verbroken databaseverbindingen maken het matchen stabieler.
- **Minder fouten over de hele linie.** Veel zeldzame serverfouten op dashboards,
  leveranciersfacturen, PO-records en OCR-taken zijn opgespoord en opgelost.

---

## Web App — live: `10.34.4`

- **Snelzoeken in het dashboard:** gelokaliseerde **AND / OR**-verbindingswoorden
  (de/fr) met kleurgecodeerde syntaxismarkering; keuzelijst met waarden voor
  factuur-subtypes; gelokaliseerde foutmeldingen over de zoeksyntaxis; soepelere
  toetsenbordervaring; de waarschuwing "full-text vereist" wordt nu inline weergegeven
  zodat de lay-out niet langer verspringt.
- **Goedkeuringen & rechten:** opgelost dat goedkeuring ten onrechte werd geactiveerd
  wanneer de verpakkingseenheid uit een orderbevestiging leeg is; normale gebruikers
  kunnen na de migratie van de toegangscontrole weer kostenelementen goedkeuren; rechten
  op documentniveau worden nu toegepast wanneer een tabelkolom al bestaat.
- **Automatisch bijwerken:** de app ververst automatisch bij een nieuwe versie in plaats
  van een "Refresh Now"-pop-up te tonen; het oude dialoogvenster met versie-informatie
  is verwijderd.
- **Instellingen voor inkomende e-mail:** nieuwe schakelaar en veld voor ontvangers van
  foutmeldingen; het importlogboek toont nu uitgaande activiteit en de foutreden; het
  inkomende adres wordt betrouwbaar gekopieerd.
- **Document Split:** het scherm Document Split kan nu scrollen.
- **Donkere modus:** fixes voor tabelextractie, de taakteller en de markeringen voor
  gesloten documenten op het dashboard.
- **Bruikbaarheid & stabiliteit:** fixes voor de export-UI van het dashboard; vaste
  tabelkoppen komen niet langer door dialoogvensters heen; het DocNet-dashboard crasht
  niet langer bij een mislukt statistiekverzoek; veldscripts zetten geleegde velden niet
  langer terug naar hun oude waarden; fixes voor de checkboxes en lay-out van
  PO-instellingen; fixes voor de weergave van de classify-lijst.
- **Leveranciers:** leveranciersorganisaties kunnen zich nu registreren via een
  magic link.

## API Service — live: `12.46.8`

- **DocBits MCP-gateway:** een geïntegreerde gateway proxyt nu DocFlow-tools via de
  hoofd-API, zodat AI-assistenten elke DocBits-tool via één eindpunt bereiken; het
  MCP-eindpunt wordt aangeboden zonder een redirect die verbindingen zou kunnen
  verbreken.
- **Boekhouding:** validatie van de kostenplaats toegevoegd voor het boekhoud-ID.
- **OCR-routering:** documenten worden voor een volledige re-OCR verzonden wanneer de
  e-text van de leverancier is uitgeschakeld, zodat de tekst betrouwbaar blijft.
- **Infor ERP / SAP:** aanvullende kosten worden correct gerouteerd wanneer het ERP de
  kosten al met een bedrag van nul bevat.
- **Betrouwbaarheid (minder serverfouten):** queries voor dashboard, leveranciersfactuur,
  PO-record en taakbeheer gehard zodat ze niet langer zeldzame 500-fouten retourneren;
  veerkrachtigere synchronisatie van de organisatiecache en opschoning van opgeslagen
  bestanden.
- **Schonere dashboardfilters:** het overbodige filterveld voor factuurnummer
  verwijderd; PO-gematchte hoeveelheid gecorrigeerd.
- **API-documentatie voor ontwikkelaars:** de Swagger UI biedt nu een keuzelijst voor de
  spec (OpenAPI 3.0 plus de Infor Swagger 2.0-weergave) met DocBits-huisstijl.

## Auth Service — live: `1.68.0`

- **Sneller afmelden / token-intrekking:** het bulksgewijs intrekken van tokens duurt
  niet langer minuten en verbreekt de verbinding niet meer.
- **E-mails voor wachtwoord instellen opgelost** zodat ze correct worden weergegeven.
- **Leveranciers:** leveranciersorganisaties kunnen zich registreren met een magic link.
- **Stabiliteit bij aanmelden:** een lid wordt niet langer buitengesloten bij een
  tijdelijke misser in de organisatie-opzoeking, en een ongeldig organisatie-id
  retourneert nu een nette melding in plaats van een fout.

## Docflow Service — live: `2.4.1`

- **Betrouwbare AI-gateway:** hang- en time-outproblemen op het DocFlow MCP-eindpunt
  opgelost (handshake, verbroken clients, dubbele antwoorden) — de DocFlow-kant van de
  geïntegreerde DocBits MCP-gateway.

## OCR Service — live: `1.7.1`

- **Stabielere OCR-verwerking:** achtergrondwachtrijen voor antwoorden verlopen
  automatisch en tijdelijke verbindingsfouten worden opnieuw geprobeerd, zodat er minder
  OCR-taken blijven hangen.

## PO Match Service — live: `1.55.7`

- **Waardetransformaties** worden nu toegepast op de kolommen artikel-id, eenheidscode
  en statische waarde tijdens het matchen op basis van regels.
- **Crashbeveiligingen:** een regel zonder prijs of hoeveelheid, een ongebruikelijke
  gewogen-sleutelcombinatie of een onmogelijke deling laten het matchen niet langer
  crashen.
- **Betrouwbaarheid:** databaseschrijfacties worden automatisch opnieuw geprobeerd bij
  verbroken of via SSL gesloten verbindingen.
- **Infor ERP / SAP:** aanvullende kosten worden correct gerouteerd wanneer het ERP de
  kosten met een bedrag van nul bevat.

## Fulltext Service — live: `1.35.6`

- **Sneller herindexeren:** alle synchronisatiefasen worden nu uitgewaaierd zodat
  autoscaling in werking treedt, wat traag serieel herindexeren en een vastgelopen
  voortgangswidget op 0% oplost.
- **Stabielere statistieken:** cross-region-verzoeken voor documentstatistieken worden
  begrensd zodat ze niet langer een time-out krijgen.

---

## Geen wijzigingen zichtbaar voor klanten in dit tijdvenster

Stabiel, geen noemenswaardige productwijzigingen tussen 26–30 juni: Auto Accounting
(`1.18.6`), Barcode (`1.15.6`), Docnet (`1.54.6`), Email (`1.36.4`), Extraction
(`1.48.7`), FTP (`1.30.1`), Operator (`1.39.5`). Auto Accounting en FTP kregen alleen
intern onderhoud.

<!-- Generated by the docbits-changelog skill (prod-delta mode). Versions read live
     from prod (do-fra1-polydocs/prod); window 2026-06-26 → 2026-06-30. -->
