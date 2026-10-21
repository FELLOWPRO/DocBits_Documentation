# E-mail verzenden naar groepen

***

Voeg deze kaart toe aan de groep **Dan** van de Workflow Builder — de acties die worden uitgevoerd zodra de When/And-voorwaarden overeenkomen:

<figure><img src="../../../../.gitbook/assets/workflow-card-qa-20261021-canvas-e5e45b3054fa-nl.png" alt="Niet-opgeslagen voorbeeld met Wanneer-, En- en Dan-kaarten. Vul alle velden in vóór uitvoering. Sommige labels van deze versie zijn in de interface nog niet of onjuist vertaald. De uitleg op deze pagina gebruikt de juiste termen; de afbeelding toont de werkelijke interface."><figcaption><p>Niet-opgeslagen voorbeeld met Wanneer-, En- en Dan-kaarten. Vul alle velden in vóór uitvoering. Sommige labels van deze versie zijn in de interface nog niet of onjuist vertaald. De uitleg op deze pagina gebruikt de juiste termen; de afbeelding toont de werkelijke interface.</p></figcaption></figure>

***

## 📌 Versie-informatie

**Status:** ✅ Enkele versie (geen belangrijke wijzigingen) **Nieuwste versie:** v1 (actief) **Opmerking:** Deze kaart maakt gebruik van een enkel versiemodel met meertalige ondersteuning via vertaalsleutels.

📖 [Volledige kaartdatabase](../../cards-overview/export-cards-guide.md)

***

## Doel

Deze kaart verzendt automatisch e-mailmeldingen naar groepen gebruikers. In plaats van werk aan individuele mensen toe te wijzen, verzendt u het bericht naar een groep, en alle leden van die groep ontvangen het.

**Voorbeeld uit de praktijk:** Wanneer een factuur met een hoge waarde binnenkomt, stuurt u automatisch een e-mailmelding naar iedereen in de groep 'Financieel team', zodat ze zich ervan bewust zijn dat de factuur moet worden gecontroleerd.

***

## Wanneer moet u deze kaart gebruiken?

Gebruik deze kaart wanneer u:

* Breng meerdere mensen tegelijk op de hoogte
* Stuur waarschuwingen naar teamgroepen
* Updates naar afdelingen uitzenden
* Breng groepen op de hoogte van wijzigingen in de documentstatus
* Stuur herinneringen naar groepsleden

**Gemeenschappelijke scenario's:**

* Inkoopteam op de hoogte stellen van nieuwe leveranciers
* Waarschuw het financiële team over facturen met een hoge waarde
* Het magazijnteam op de hoogte stellen van zendingen
* Wijzigingen in de documentstatus

***

## Hoe het werkt

1. **Conditiecontrole**: Workflow controleert de voorwaarden "Wanneer" en "En"
2. **E-mail voorbereiden**: het systeem bereidt de e-mail voor met behulp van een sjabloon
3. **Groepsleden verkrijgen**: Systeem vindt alle leden van de opgegeven groep
4. **Verzenden**: e-mail wordt naar elk groepslid verzonden
5. **Log**: het verzenden van e-mails wordt geregistreerd

***

## Parameters uitgelegd

### E-mailsjabloon

Het e-mailbericht dat moet worden verzonden

**Opties:**

* Kies uit bestaande sjablonen
* Elke sjabloon heeft een vooraf gedefinieerd onderwerp, hoofdtekst en opmaak
* Sjablonen kunnen tijdelijke aanduidingen bevatten, zoals {document\_number}, {supplier\_name}

**Voorbeeldsjabloon:**

```
Subject: Document {document_number} requires review

Body:
Dear Team,

A new invoice has arrived and requires review:
- Document: {document_number}
- Supplier: {supplier_name}
- Amount: {amount} {currency}
- Date: {date}

Please login to DocBits to review.

Best regards,
DocBits Automation
```

### Groep

De groep gebruikers waarnaar de e-mail moet worden verzonden

**Voorbeeldgroepen:**

* Het financiële team
* Inkoopteam
* Magazijnteam
* Goedkeuringscommissie
* Beheer Groep

***

## Configuratiestappen

### Stap 1: Kies E-mailsjabloon

1. Klik op ‘Selecteer e-mailsjabloon’
2. Kies een sjabloon uit de lijst
3. Controleer onderwerp en inhoud

### Stap 2: Selecteer Groep

1. Klik op ‘Groep selecteren’
2. Kies de groep die u op de hoogte wilt stellen
3. Groepsleden verifiëren (toont meestal het aantal)

### Stap 3: Stel voorwaarden in

1. Voorwaarde toevoegen: "Als \[voorwaarde] waar is"
2. Voorbeeld: "Als het factuurbedrag groter is dan € 5000"

### Stap 4: Testen

1. Test met voorbeelddocument
2. Controleer of e-mail naar de groep is verzonden
3. Controleer de sjabloonweergave

***

## Voorbeelden van e-mailsjablonen

### Sjabloon 1: Waarschuwing voor hoge facturen

```
Subject: High-Value Invoice Alert - {document_number}

Body:
Team,

An invoice exceeding €10,000 has been received:

Document Number: {document_number}
Supplier: {supplier_name}
Amount: {amount} EUR
Received Date: {date}
Status: {status}

This requires immediate review and approval.

---
Sent automatically by DocBits
```

### Sjabloon 2: Wijziging van de leveranciersstatus

```
Subject: Supplier Status Update - {supplier_name}

Body:
Procurement Team,

The following supplier's status has been updated:

Supplier: {supplier_name}
Supplier Code: {supplier_code}
New Status: {status}
Effective Date: {date}

Please update your systems accordingly.

---
Sent automatically by DocBits
```

### Sjabloon 3: Document gereed voor export

```
Subject: Document Approved for Export - {document_number}

Body:
Export Team,

The following document has been approved and is ready for export:

Document Number: {document_number}
Invoice Number: {invoice_number}
Supplier: {supplier_name}

Please proceed with export to {destination_system}.

---
Sent automatically by DocBits
```

***

## Veelvoorkomende gebruiksscenario's

### Gebruiksscenario 1: Kwaliteitscontrolewaarschuwingen

**Trigger:** Wanneer er een discrepantie wordt gevonden tussen factuur en inkooporder

**E-mailgroep:** Kwaliteitsteam

**Inhoud:**

```
Invoice {number} has quality issues:
- Unit Price variance: 12% (exceeds 5% tolerance)
- Please review and take action
```

### Gebruiksscenario 2: Goedkeuringsmeldingen

**Trigger:** Wanneer het document een bepaalde status bereikt

**E-mailgroep:** Goedkeuringscommissie

**Inhoud:**

```
Document {number} is awaiting approval:
- Amount: {amount}
- Supplier: {supplier_name}
- Please login to approve/reject
```

### Gebruiksscenario 3: Uitzonderingsmeldingen

**Trigger:** Wanneer niet aan de voorwaarden wordt voldaan

**E-mailgroep:** Managers

**Inhoud:**

```
Exception alert for document {number}:
- Supplier code missing
- Delivery date invalid
- Manual review required
```

### Gebruiksscenario 4: Statusupdates

**Trigger:** Wanneer de documentstatus verandert

**E-mailgroep:** Team verantwoordelijk voor de volgende stap

**Inhoud:**

```
Document {number} status changed to: {status}
Assigned to: {assigned_user}
Next steps: {next_steps}
```

***

## Problemen oplossen

### "E-mail niet ontvangen"

**Mogelijke oorzaken:**

* [ ] Gebruikers in de groep hebben geen e-mailadressen
* [ ] E-mail geblokkeerd door spamfilter
* [ ] E-mailadres is onjuist in groep
* [ ] Groep heeft geen leden

**Oplossingen:**

1. Controleer of alle groepsleden een e-mailadres hebben
2. Controleer de spam/ongewenste map
3. Controleer of het groepslidmaatschap correct is
4. Voeg gebruikers toe aan de groep als deze ontbreken
5. Controleer bij IT of de e-mailservice werkt

### "Sjabloon wordt niet correct weergegeven"

**Oorzaak:** Tijdelijke aanduidingsvariabelen niet gevonden

**Oplossing:**

* [ ] Controleer of de veldnamen exact overeenkomen
* [ ] Controleer of het veld een waarde heeft in het document
* [ ] Gebruik het juiste placeholder-formaat: {field\_name}
* [ ] Test met voorbeelddocument dat alle velden bevat

### "Sommige mensen ontvangen e-mail, anderen niet"

**Oorzaak:** Onvolledig groepslidmaatschap of ongeldige e-mails

**Oplossingen:**

* [ ] Controleer of alle leden een geldig e-mailadres hebben
* [ ] Controleer of sommige gebruikers zich hebben afgemeld
* [ ] Controleer of het groepslidmaatschap actueel is
* [ ] Neem contact op met IT om e-mailadressen te valideren

### "Wil mensen toevoegen/verwijderen uit de groep"

**Oplossing:**

* Neem contact op met uw beheerder
* Groepen worden beheerd in de systeeminstellingen
* Kan niet worden gewijzigd vanaf deze kaart
* Wijzigingen in groepslidmaatschap aanvragen in IT

***

## Aanpassing van e-mailsjablonen

### Beschikbare tijdelijke aanduidingen

```
{document_number} - Document ID
{invoice_number} - Invoice ID
{supplier_name} - Supplier name
{supplier_code} - Supplier code
{amount} - Invoice amount
{currency} - Currency (EUR, USD, etc.)
{date} - Document date
{status} - Current status
{assigned_user} - Assigned person
{assigned_group} - Assigned group
{next_steps} - What needs to happen next
{reason} - Reason for exception/alert
{comment} - Comments or notes
```

### Aangepaste tijdelijke aanduidingen maken

Als u aanvullende gegevens in e-mails nodig heeft:

1. Neem contact op met uw beheerder
2. Vraag een nieuwe tijdelijke aanduiding aan
3. Voeg het benodigde veld toe aan het document
4. E-mailsjabloon bijwerken

***

## Beste praktijken

✅ **Doe:**

* Houd de inhoud van e-mails kort en duidelijk
* Neem actiepunten op (wat moeten ontvangers doen?)
* Voeg een link of instructies toe om toegang te krijgen tot het document
* Testsjabloon met voorbeeldgegevens
* Verzenden naar de juiste groep (niet te veel melden)
* Gebruik sjablonen voor consistentie

❌ **Niet doen:**

* Te veel e-mails verzenden (meldingsmoeheid)
* Neem gevoelige gegevens op in e-mails
* Verzend naar groepen die geen informatie nodig hebben
* Gebruik onduidelijke onderwerpregels
* Vergeet te vermelden hoe u actie kunt ondernemen
* Stuur e-mails naar individuen (gebruik in plaats daarvan een groep)

***

## Prestatienotities

* Het verzenden van elke e-mail duurt \~1 seconde
* Grote groepen kunnen enige tijd in beslag nemen (100 personen = \~100 seconden)
* Creëer geen loops die duizenden e-mails versturen
* Bewaak de capaciteit van de e-mailservice
* Overweeg batchverwerking als er veel documenten zijn

***

## Gerelateerde kaarten

* **ACTION\_SEND\_EMAIL** - Verzenden naar individuele persoon
* **ACTION\_ASSIGN\_TASK\_TO\_PROCUREMENT\_GROUP** - Wijs een taak toe in plaats van alleen maar een melding
* **ACTION\_CREATE\_TASK\_FOR\_GROUP\_SEQUENTIAL** - Taak aanmaken en melden
* **STAUS\_CHANGE** - Status wijzigen en op de hoogte stellen

***

## Typisch workflowvoorbeeld

```
Document Arrives
    ↓
Check Condition: "Is amount > €10,000?"
    ↓
YES: Send Email to Finance Team
     "High value invoice alert"
    ↓
Send Email to Procurement Team
     "New invoice from supplier"
    ↓
Workflow Continues
```

***

## Veelgestelde vragen

**V: Kan ik naar meerdere groepen sturen?** A: Maak afzonderlijke kaarten voor elke groep

**V: Wat als iemands e-mail terugkomt?** A: E-mail wordt geregistreerd als mislukt, IT kan problemen oplossen

**V: Kan ik de e-mailsjabloon wijzigen?** A: Neem contact op met uw beheerder om sjablonen te wijzigen

**V: Kan ik verzenden op basis van voorwaarden?** A: Ja! Gebruik de voorwaarden 'Waar' en 'En' om te bepalen wanneer e-mails worden verzonden

**V: Hoe weet ik of e-mail is ontvangen?** A: Controleer e-maillogboeken in DocBits op verzendstatus
