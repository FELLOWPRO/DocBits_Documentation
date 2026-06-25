# DocBits Release-opmerkingen — 21–25 juni 2026

_Wat deze prod-upgrade heeft opgeleverd, in begrijpelijke taal. Bij elke service
staat de versie die nu live is in productie. Services die niet worden vermeld,
hadden in deze periode geen wijzigingen die voor klanten merkbaar zijn._

---

## Hoogtepunten

- **Slimmer zoeken in het dashboard.** Zoek documenten betrouwbaar op bedragen en
  nummers — vind facturen boven een bepaalde waarde, of zoek op
  **aanvraagnummer** — met bedragbereiken die echte getallen vergelijken in plaats
  van tekst. Factuursubtypen zijn doorzoekbaar op hun vertaalde namen.
- **Betrouwbare e-mailmeldingen.** Meldingen bij statuswijzigingen worden nu voor
  elke status verzonden (geen stilzwijgend weggevallen e-mails meer), en
  ontvangstbevestigingen en foutmeldingen van inkomende import zijn nu correct
  voorzien van de DocBits-huisstijl, met instellingen per ontvanger.
- **Soepeler aanmelden over regio's heen (EU/US).** Het wisselen van regio is nu
  een kleine banner in plaats van een schermvullende onderbreking, single sign-on
  komt in de juiste regio uit, en aangemeld blijven over meerdere browsertabbladen
  is betrouwbaarder geworden.
- **Verbeteringen aan machtigingen.** Gebruikers krijgen de toegang die hun groep
  hun verleent — documenten openen, bewerken, goedkeuren en opnieuw starten werkt
  nu correct, ook wanneer groepen en machtigingen op minder gangbare manieren zijn
  geconfigureerd.
- **Stabielere documentverwerking.** Documenten die eerder na het uploaden bleven
  hangen, worden automatisch opnieuw opgepakt, en een piek van één klant
  vertraagt de anderen niet langer.

---

## Web App — live: `10.32.4`

- **Snelzoek-sprong (Cmd/Ctrl + K)** rechtstreeks naar de instelling
  **E-Invoice Validation**.
- **Regio & aanmelden:** het wisselen van regio wordt nu als een blijvende banner
  getoond in plaats van een blokkerend scherm; single sign-on leidt nu door naar
  de juiste regio (EU/US); aangemeld blijven over meerdere tabbladen is
  betrouwbaarder.
- **Machtigingen:** opgelost dat gebruikers documenten niet konden **goedkeuren**,
  **bewerken**, **openen** of **opnieuw starten** ondanks de juiste
  groepsmachtigingen.
- **Instellingen voor inkomende e-mail:** nieuwe schakelaars "Afzender op de
  hoogte stellen" en "Antwoorden naar afzender bij ontvangst".
- **Gebruiksgemak:** de waarschuwing voor dubbele documenten moet nu worden
  weggeklikt voordat je verdergaat; de banner "backend niet beschikbaar"
  verschijnt alleen bij echte storingen; taaktellers worden direct bijgewerkt
  wanneer taken zijn afgerond; oplossing voor de donkere modus op het
  validatiescherm voor AI-tabellen.
- **Prestaties:** een vastloper op het scherm voor e-documenten tijdens
  veldvalidatie en PO-matching opgelost.
- **Zoek factuursubtypen op hun vertaalde namen.**

## API Service — live: `12.41.9`

- **Grondige vernieuwing van het dashboardzoeken:** aanvraagnummer en aanvrager
  zijn nu doorzoekbaar; zoekopdrachten op bedragen en nummers geven correcte
  resultaten (echte numerieke vergelijking); totaal nettobedrag en berekende
  kolommen worden correct weergegeven.
- **Betrouwbare e-mails met statusmeldingen** voor elke documentstatus, waarbij
  verzendfouten niet langer verborgen blijven.
- **Machtigingen:** gebruikers zonder groep kunnen hun eigen documenten openen en
  goedkeuren; de documentzichtbaarheid voor gebruikers zonder groep is hersteld.
- **Betrouwbaarheid van documentverwerking:** documenten die vastzitten op "nieuw"
  worden automatisch opnieuw in de wachtrij geplaatst; eerlijke verdeling van de
  verwerking zodat een grote piek van één organisatie de anderen niet uithongert;
  zelfherstel bij zeldzame problemen met databasesequenties.
- **Gescande PDF's met een defecte tekstlaag worden naar OCR geleid** in plaats
  van onbetrouwbare tekst te produceren.
- **Nauwkeurigheid van extractie & PO:** leveranciersnaam ingevuld vanuit de
  gekoppelde inkooporder; dubbele kolommen met artikelnummers verwijderd; betere
  verwerking van speciale (vaste) spaties.
- **Infor ERP / SAP-export:** authenticatie van de SFTP-export opgelost.
- **E-facturering:** verfijningen aan het ZUGFeRD-/e-document-extractiepad.

## Auth Service — live: `1.66.0`

- **Ontbrekende organisatietoewijzing opgelost** voor sommige gebruikers (lege
  org-id).

## Docflow Service — live: `2.3.4`

- **Afkoelperiode voor workflowtriggers** is nu per omgeving instelbaar.

## Email Service — live: `1.35.9`

- **E-mails met huisstijl:** ontvangstbevestigingen en foutmeldingen van inkomende
  import gebruiken nu het echte DocBits-logo en de DocBits-kleuren.
- **Instellingen per organisatie:** bevestigingsmail bij ontvangst, "afzender op
  de hoogte stellen" bij een fout, en opties om naar de afzender te antwoorden.
- **Betrouwbaardere inkomende import:** importresultaten worden correct
  vastgelegd, gedeeltelijke mislukkingen worden als mislukkingen gerapporteerd
  (niet als stilzwijgende successen), en probleemtekens in e-mailteksten breken de
  import niet langer.
- **EU/US-routing:** routing per organisatie naar de juiste regionale API.

## Fulltext Service — live: `1.34.5`

- **Zoeken op bedragen en nummers** werkt nu betrouwbaar, inclusief
  duizendtalscheidingstekens en bedragbereiken (de motor achter de grondige
  vernieuwing van het dashboardzoeken).
- **Stabielere zoekinfrastructuur:** verweesde achtergrondwachtrijen worden
  opgeruimd zodat ze geen gedeelde resources meer bezet houden.

## PO Match Service — live: `1.54.7`

- **Robuustere matching van inkooporders:** op tekst gebaseerde codes voor
  verpakkings-/verpakkingseenheden blokkeren een match niet langer, en het
  handmatig matchen van regels gaat veilig om met lege resultaten.

---

## Geen wijzigingen die voor klanten merkbaar zijn in deze periode

Stabiel, geen noemenswaardige productwijzigingen tussen 21–25 juni: Auto
Accounting (`1.18.5`), Barcode (`1.15.6`), Docnet (`1.54.6`), Extraction
(`1.48.6`), FTP (`1.30.0`), OCR (`1.6.8`), Operator (`1.39.5`).

<!-- Generated by the docbits-changelog skill (prod-delta mode). Versions read live
     from prod (do-fra1-polydocs/prod); window 2026-06-21 → 2026-06-25. -->
