# DocBits Release-opmerkingen — 30 juni – 3 juli 2026

_Wat deze productie-upgrade heeft opgeleverd, in gewone taal. Elke service toont de
versie die nu live staat op productie. Services die niet zijn vermeld, hadden in dit
tijdvenster geen wijzigingen die zichtbaar zijn voor klanten._

---

## Hoogtepunten

- **AI-chat op Activiteitenlogboeken.** Een nieuw AI-chatpaneel op de pagina
  Activiteitenlogboeken laat u rechtstreeks vragen stellen over logactiviteit, zonder
  te hoeven graven in ruwe vermeldingen.
- **Registratie van uitgaande e-mailimport.** Het importlogboek registreert nu
  uitgaande e-mail naast inkomende, met snelfilterchips voor Fouten / Inkomend /
  Uitgaand — postbussen die blijven falen worden automatisch gedeactiveerd na
  herhaalde fouten, beheerders kunnen per e-mail worden geïnformeerd bij een
  importfout, en pogingen worden nu tot 15 keer herhaald over ongeveer 5 uur voordat
  wordt opgegeven.
- **Duidelijkere foutmeldingen bij e-mailimport.** Aanmeldfouten tonen nu de echte
  onderliggende reden, met specifieke meldingen voor een ongeldig certificaat of een
  onjuist Gmail-app-wachtwoord.
- **Aanmeldlus opgelost.** Sommige gebruikers konden vast komen te zitten in een
  herhaalde aanmeldlus tijdens het vernieuwen van het token — opgelost.
- **Stabielere documentverwerking.** Een crash tijdens data-extractie door niet-
  afgeronde coördinaatwaarden is opgelost, barcodeherkenning probeert nu automatisch
  opnieuw bij herstelbare fouten in plaats van stilzwijgend op te geven, en een
  zeldzaam geval waarbij een document tegelijk twee keer kon worden geëxporteerd is
  verholpen.
- **Verbeteringen in het validatiescherm.** U kunt nu verder inzoomen op documenten,
  velden worden niet langer geleegd door scripts wanneer hun waarde in werkelijkheid
  niet is gewijzigd, en het dashboard onthoudt uw paginapositie wanneer u terugnavigeert.

---

## Web App — live: `10.35.7`

- **AI-chatpaneel** toegevoegd aan de pagina Activiteitenlogboeken (#15512).
- **Importlogboek:** nieuwe snelfilterchips voor Fouten / Inkomend / Uitgaand;
  schakelaar en veld voor ontvangers van foutmeldingen bij instellingen voor
  inkomende e-mail.
- **Validatiescherm:** het inzoomen op documenten gaat nu verder dan de vorige
  standaardgrootte; velden die door validatiescripts werden geleegd behouden nu
  correct hun waarde wanneer het script dezelfde waarde teruggeeft.
- **Dashboard:** de paginapositie blijft behouden bij het terugnavigeren naar de
  tabel; de sleepgreep voor kolombreedte loopt niet langer buiten de tabelkop.
- **Scherm Auto Accounting:** een validatiefout opgelost.
- **DocBits Tasks:** een rechtenprobleem opgelost.
- **Watchdog-logboeken:** een tijdsbereikfilter en een instelbare selectie voor
  rijen per pagina toegevoegd.
- **Fixes:** een grafiekfout ("Element not found") op de pagina Boards; een kapotte
  link voor het verwijderen van exports op Activiteitenlogboeken; lay-outfixes op
  het scherm Layout Builder; een ontbrekende vertaling bij het tijdsbereikfilter van
  Activiteitenlogboeken.
- **Auto-update:** verdere versteviging van het automatische app-updatemechanisme
  (snellere opstartopschoning, betrouwbaardere versiedetectie, cache wissen vóór een
  herstelherlaad).

## API Service — live: `12.48.1`

- **Snellere laadtijd voor documentscripts:** validatiescripts worden nu
  server-side gecachet (6 uur cache) in plaats van telkens opnieuw opgehaald.
- **Nauwkeurigere betrouwbaarheidsscore voor bedragen:** de betrouwbaarheidsscore
  houdt nu rekening met documenten die verschillende decimaalscheiding-conventies
  gebruiken.
- **Betrouwbaarheid:** documentvalidatie voert altijd de enige actieve scriptversie
  uit, en welke versie is uitgevoerd wordt nu gelogd; een zeldzaam geval waarbij een
  document tegelijk twee keer kon worden geëxporteerd is verholpen;
  leveranciersspecifieke extractieregels worden weer correct toegepast na een
  geforceerde re-OCR.
- **E-mailimport:** backend-ondersteuning toegevoegd voor het loggen van uitgaande
  e-mail en foutmeldings-e-mails (zie Email Service, hieronder).

## Auth Service — live: `1.68.5`

- **Aanmeldlus opgelost** die sommige gebruikers konden tegenkomen tijdens het
  vernieuwen van hun sessietoken.
- **Snellere schermen voor organisatiebeheer:** gebruikers- en abonnementsgegevens
  worden nu in bulk geladen in plaats van record voor record.
- **Zeldzaam databaseconflict opgelost** bij het koppelen van een gebruiker aan een
  organisatie.

## Email Service — live: `1.37.4`

- **Het importlogboek registreert nu ook uitgaande e-mail** naast inkomende, met
  een filter om alleen inkomende, uitgaande of mislukte imports te tonen.
- **Postbussen die blijven falen worden nu automatisch gedeactiveerd** na herhaalde
  fouten, en beheerders kunnen per e-mail worden geïnformeerd wanneer een import
  mislukt; pogingen worden nu tot 15 keer herhaald over ongeveer 5 uur voordat wordt
  opgegeven.
- **Duidelijkere foutmeldingen bij aanmeldfouten:** toont de echte onderliggende
  reden, een specifieke melding voor een ongeldig certificaat, en een specifieke
  melding voor een onjuist Gmail-app-wachtwoord.
- **Inkomende routering opgelost** die serveradressen voor accounts in de
  EU-regio onterecht herschreef.
- Veerkrachtiger tegen korte onderbrekingen van de Redis-verbinding.

## Extraction Service — live: `1.49.0`

- **Een crash tijdens extractie opgelost**, veroorzaakt door niet-afgeronde
  coördinaatwaarden.
- **Nauwkeurigere betrouwbaarheidsscore voor bedragen** bij documenten met gemengde
  decimaalscheiding-formaten; kleine afrondingsverschillen in het belastingtotaal
  blokkeren een match niet langer.

## Docflow Service — live: `2.4.2`

- **Authenticatie voor geavanceerde (Celery-gebaseerde) workflows herzien**, met
  beveiligingen zodat een mislukte authenticatiecontrole een workflowuitvoering niet
  langer kan laten crashen.
- **Duidelijkere respons** wanneer een workflowstap probeert te draaien tegen een
  workflow die niet meer bestaat.

## Barcode Service — live: `1.15.7`

- **Barcodeherkenning probeert nu automatisch opnieuw** bij herstelbare fouten in
  plaats van stilzwijgend op te geven.

## OCR Service — live: `1.7.3`

- **Een OCR-fout opgelost**, veroorzaakt door een probleem met het opzoeken van de
  Redis-hostnaam.
- Verbroken Redis-verbindingen bij een health-check worden niet langer als fout
  gelogd, wat het aantal valse meldingen vermindert.

## PO Match Service — live: `1.55.8`

- **Opgelost dat notities niet verschenen** bij PO Match-records.

---

## Geen wijzigingen zichtbaar voor klanten in dit tijdvenster

Stabiel, geen noemenswaardige productwijzigingen tussen 30 juni – 3 juli: Auto
Accounting (`1.18.7`), Docnet (`1.54.6`), FTP (`1.30.2`), Fulltext (`1.35.7`),
Operator (`1.39.5`). Auto Accounting kreeg alleen intern
deploymentconfiguratie-onderhoud. Ideas Service kon tijdens dit tijdvenster niet
worden bereikt voor een versiecontrole.

<!-- Generated by the docbits-changelog skill (version-boundary mode, resolved
     from the prod version table supplied by the user). Window 2026-06-30 →
     2026-07-03. -->
