# DocBits Release-opmerkingen — 21–25 juni 2026

_Wat deze productie-upgrade heeft opgeleverd, in gewone taal. Elke service toont de
versie die nu live staat op productie. Services die niet zijn vermeld, hadden in dit
tijdvenster geen wijzigingen die zichtbaar zijn voor klanten._

---

## Hoogtepunten

- **Slimmer zoeken in het dashboard.** Zoek documenten betrouwbaar op bedragen en
  nummers — vind facturen boven een bepaalde waarde, of zoek op **aanvraagnummer** —
  met bedragbereiken die echte getallen vergelijken, geen tekst. Factuur-subtypes zijn
  doorzoekbaar op hun vertaalde namen.
- **Betrouwbare e-mailmeldingen.** Meldingen bij statuswijzigingen worden nu voor elke
  status verstuurd (geen stilletjes verdwenen e-mails meer), en ontvangstbevestigingen
  en foutmeldingen van inkomende imports hebben nu de juiste DocBits-huisstijl met
  instellingen per ontvanger.
- **Soepeler aanmelden over regio's heen (EU/US).** Wisselen van regio verloopt nu via
  een kleine banner in plaats van een schermvullende onderbreking, single sign-on komt
  in de juiste regio terecht, en aangemeld blijven over meerdere browsertabbladen is
  betrouwbaarder.
- **Rechtenherstel.** Gebruikers krijgen de toegang die hun groep hun verleent — het
  openen, bewerken, goedkeuren en herstarten van documenten werkt nu correct, ook
  wanneer groepen en rechten op minder gebruikelijke manieren zijn geconfigureerd.
- **Stabielere documentverwerking.** Documenten die eerder na de upload bleven hangen,
  worden automatisch weer opgepakt, en een piek van één klant vertraagt anderen niet
  langer.

---

## Web App — live: `10.32.4`

- **Snelzoeksprong (Cmd/Ctrl + K)** rechtstreeks naar de instelling
  **E-Invoice Validation**.
- **Regio & aanmelden:** het wisselen van regio wordt getoond als een blijvende banner
  in plaats van een blokkerend scherm; single sign-on leidt nu door naar de juiste
  regio (EU/US); aangemeld blijven over meerdere tabbladen is betrouwbaarder.
- **Rechten:** gevallen opgelost waarin gebruikers documenten niet konden **goedkeuren**,
  **bewerken**, **openen** of **herstarten** ondanks dat ze de juiste groepsrechten
  hadden.
- **Instellingen voor inkomende e-mail:** nieuwe schakelaars "Notify sender" en
  "Reply to sender on receipt".
- **Bruikbaarheid:** de waarschuwing voor dubbele documenten moet nu worden weggeklikt
  voordat u verdergaat; de banner "backend niet beschikbaar" verschijnt alleen bij
  echte storingen; taaktellers werken direct bij wanneer taken zijn afgerond; fix voor
  de donkere modus op het validatiescherm van AI-tabellen.
- **Prestaties:** een bevriezing op het e-documentscherm tijdens veldvalidatie en
  PO-matching opgelost.
- **Zoek factuur-subtypes op hun vertaalde namen.**

## API Service — live: `12.41.9`

- **Grondige herziening van het dashboardzoeken:** aanvraagnummer en aanvrager zijn nu
  doorzoekbaar; zoekopdrachten op bedragen en nummers geven correcte resultaten (echte
  numerieke vergelijking); totaal-nettobedrag en berekende kolommen worden correct
  weergegeven.
- **Betrouwbare statusmelding-e-mails** voor elke documentstatus, waarbij
  verzendfouten niet langer verborgen blijven.
- **Rechten:** gebruikers zonder groep kunnen hun eigen documenten openen en goedkeuren;
  documentzichtbaarheid voor gebruikers zonder groep hersteld.
- **Betrouwbaarheid van documentverwerking:** documenten die vastzitten in "new" worden
  automatisch opnieuw in de wachtrij geplaatst; eerlijke verdeling van verwerking zodat
  een grote piek van één organisatie anderen niet uithongert; zelfherstel bij zeldzame
  problemen met databasesequenties.
- **Gescande PDF's met een beschadigde tekstlaag worden naar OCR geleid** in plaats van
  onbetrouwbare tekst te produceren.
- **Nauwkeurigheid van extractie & PO:** leveranciersnaam ingevuld vanuit de gekoppelde
  inkooporder; dubbele kolommen met artikelnummers verwijderd; betere verwerking van
  speciale (niet-afbrekende) spaties.
- **Infor ERP / SAP-export:** authenticatie voor SFTP-export opgelost.
- **E-facturatie:** verfijningen van het ZUGFeRD- / e-document-extractiepad.

## Auth Service — live: `1.66.0`

- **Ontbrekende organisatietoewijzing opgelost** voor sommige gebruikers (leeg org-id).

## Docflow Service — live: `2.3.4`

- **Cooldown voor workflowtriggers** is nu per omgeving instelbaar.

## Email Service — live: `1.35.9`

- **E-mails met huisstijl:** ontvangstbevestigingen en foutmeldingen van inkomende
  imports gebruiken nu het echte DocBits-logo en de echte kleuren.
- **Instellingen per organisatie:** bevestigingsmail bij ontvangst, "notify sender" bij
  een fout, en opties voor reply-to-sender.
- **Betrouwbaarder inkomende import:** importresultaten worden correct vastgelegd,
  gedeeltelijke fouten worden gerapporteerd als fouten (niet als stille successen), en
  probleemtekens in e-mailteksten breken de import niet langer.
- **EU/US-routering:** routering per organisatie naar de juiste regionale API.

## Fulltext Service — live: `1.34.5`

- **Zoeken op bedragen en nummers** werkt nu betrouwbaar, inclusief duizendtalscheiders
  en bedragbereiken (de motor achter de herziening van het dashboardzoeken).
- **Stabielere zoekinfrastructuur:** verweesde achtergrondwachtrijen worden opgeruimd
  zodat ze gedeelde bronnen niet langer bezet houden.

## PO Match Service — live: `1.54.7`

- **Robuustere inkoopordermatching:** tekstgebaseerde verpakkings-/verpakkingseenheids­codes
  blokkeren een match niet langer, en het handmatig matchen van regels gaat veilig om
  met lege resultaten.

---

## Geen wijzigingen zichtbaar voor klanten in dit tijdvenster

Stabiel, geen noemenswaardige productwijzigingen tussen 21–25 juni: Auto Accounting
(`1.18.5`), Barcode (`1.15.6`), Docnet (`1.54.6`), Extraction (`1.48.6`), FTP
(`1.30.0`), OCR (`1.6.8`), Operator (`1.39.5`).

<!-- Generated by the docbits-changelog skill (prod-delta mode). Versions read live
     from prod (do-fra1-polydocs/prod); window 2026-06-21 → 2026-06-25. -->
