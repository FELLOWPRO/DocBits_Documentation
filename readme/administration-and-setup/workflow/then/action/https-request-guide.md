# HTTPS-verzoek verzenden

***

Voeg deze kaart toe aan de groep **Dan** van de Workflow Builder — de acties die worden uitgevoerd zodra de When/And-voorwaarden overeenkomen:

<figure><img src="../../../../.gitbook/assets/workflow-card-qa-20261021-canvas-e5e45b3054fa-nl.png" alt="Niet-opgeslagen voorbeeld met Wanneer-, En- en Dan-kaarten. Vul alle velden in vóór uitvoering. Sommige labels van deze versie zijn in de interface nog niet of onjuist vertaald. De uitleg op deze pagina gebruikt de juiste termen; de afbeelding toont de werkelijke interface."><figcaption><p>Niet-opgeslagen voorbeeld met Wanneer-, En- en Dan-kaarten. Vul alle velden in vóór uitvoering. Sommige labels van deze versie zijn in de interface nog niet of onjuist vertaald. De uitleg op deze pagina gebruikt de juiste termen; de afbeelding toont de werkelijke interface.</p></figcaption></figure>

***

## 📌 Versie-informatie

**Huidige versie:** v2 (nieuwste en aanbevolen) **Status:** ✅ Actief

**Versiegeschiedenis:**

* v1 → Eenvoudig HTTP-verzoek (niet langer aanbevolen)
* **v2 → CURRENT** (meertalige ondersteuning toegevoegd)

**Wat is er veranderd:** v2 heeft ondersteuning voor internationalisering (i18n) toegevoegd. De kernfunctionaliteit voor webhook/verzoek blijft ongewijzigd.

📖 [Versiegeschiedenis en wijzigingen](../../release.md) | [Volledige kaartdatabase](../../cards-overview/export-cards-guide.md)

***

## Doel

De HTTPS-aanvraagkaart gebruikt een ingestelde HTTPS-URL en eigen headers. `call_api` gebruikt een relatief DocBits-API-pad en de context van de huidige gebruiker; het resultaat komt uit de antwoordtekst. Kies op basis van endpoint en antwoordcontract, niet op basis van een eenvoudige of complexe API.

## Wanneer moet u deze kaart gebruiken?

Gebruik deze kaart wanneer u:

* Stuur webhookmeldingen naar externe services
* Activeer acties in andere systemen
* Vraag een eenvoudige webservice op
* Verzend statusupdates naar andere applicaties
* Voer eenvoudige integraties uit zonder complexe API-vereisten

***

## Hoe het werkt

1. **Trigger Check**: het systeem controleert of aan de voorwaarden 'Waar' en 'En' is voldaan
2. **Bouwverzoek**: het systeem bereidt het HTTPS-verzoek voor met uw parameters
3. **Veilig verzenden**: gegevens worden verzonden via een beveiligde HTTPS-verbinding
4. **Respons ontvangen**: Externe service reageert
5. **Continue**: Workflow gaat verder met de antwoordgegevens

***

## Parameters

### URL

Het websiteadres waarnaar het verzoek moet worden verzonden

**Voorbeeld:** `https://webhook.company.com/process`

### Kopteksten

Speciale instructies voor de ontvanger

**Voorbeeld:**

```
Content-Type: application/json
Authorization: Bearer token123
```

### Methode

* **GET**: Informatie opvragen
* **POST**: gegevens verzenden
* **PUT**: gegevens bijwerken

### Parameters (querytekenreeks)

Gegevens toegevoegd aan de URL

**Voorbeeld:** `?action=approve&user_id=123`

### Gegevens opvragen

De daadwerkelijke informatie die wordt verzonden (in JSON-indeling)

**Voorbeeld:**

```json
{
  "invoice_number": "INV-2025-001",
  "amount": 5000,
  "currency": "EUR"
}
```

***

## Stapsgewijs voorbeeld

### Scenario: factuur naar boekhoudsysteem verzenden

**Kaartconfiguratie:**

* **URL:** `https://accounting.company.com/invoices/create`
* **Methode:** POST
* **Kopteksten:** `Authorization: Bearer YOUR-TOKEN`
* **Gegevens opvragen:**

```json
{
  "supplier_id": "SUPP001",
  "invoice_number": "12345",
  "amount": 1500.00,
  "currency": "EUR",
  "date": "2025-10-23"
}
```

**Verwachte reactie:**

```json
{
  "status": "success",
  "accounting_id": "ACC-98765",
  "message": "Invoice recorded in accounting system"
}
```

***

## Veelvoorkomende gebruiksscenario's

### 1. Webhook-meldingen

Stuur realtime notificaties naar andere systemen wanneer er iets gebeurt in DocFlow

**Voorbeeld:**

* Document goedgekeurd → Melding verzenden naar uitvoeringssysteem
* Leverancier gewijzigd → Inkoopteam op de hoogte stellen via Slack/Teams-webhook

### 2. Externe systeemintegratie

Verbind DocFlow met andere bedrijfssystemen voor automatische gegevensuitwisseling

**Voorbeeld:**

* Nadat het document is verwerkt → Synchroniseren met ERP-systeem
* Nieuwe leverancier toegevoegd → Leveranciersrecord aanmaken in masterdatasysteem

### 3. Goedkeuringsworkflows

Stuur het document naar een extern goedkeuringssysteem en ontvang een beslissing

**Voorbeeld:**

* Factuur met hoge waarde → Ter goedkeuring naar Financiën sturen
* Document met beslissing terugsturen naar extern systeem

***

## Configuratiegids

### Stap 1: eindpuntinformatie ophalen

Vraag het ontvangstsysteem naar:

* [ ] HTTPS-URL
* [ ] Vereiste headers
* [ ] Authenticatiemethode
* [ ] Verwacht verzoekformaat
* [ ] Verwacht antwoordformaat

### Stap 2: Configureer de kaart

1. Voer de HTTPS-URL in
2. HTTP-methode instellen (meestal POST)
3. Voeg indien nodig authenticatie toe
4. Formatteer aanvraaggegevens als JSON
5. Voeg eventuele aangepaste headers toe

### Stap 3: Testen

Verzend een testverzoek en verifieer het antwoord

***

## Reactieafhandeling

Uw HTTPS-verzoek krijgt een reactie. Veel voorkomende reacties:

### Succes (200, 201)

```json
{
  "success": true,
  "id": "REC-12345",
  "status": "processed"
}
```

### Slecht verzoek (400)

```json
{
  "error": "Missing required field: invoice_number"
}
```

### Ongeautoriseerd (401)

```json
{
  "error": "Invalid authentication token"
}
```

### Serverfout (500)

Het ontvangende systeem heeft een intern probleem

***

## Problemen oplossen

### "Certificaatfout"

**Oorzaak:** Probleem met HTTPS-beveiligingscertificaat

**Oplossing:**

* Controleer of de URL correct is
* Controleer of het certificaat van de website geldig is
* Zorg ervoor dat u HTTPS gebruikt (niet HTTP)

### "Verbinding geweigerd"

**Oorzaak:** Kan geen verbinding maken met de server

**Oplossing:**

* Controleer of het URL/IP-adres correct is
* Controleer of de service actief is
* Controleer firewallregels
* Controleer de internetverbinding

### "Geen reactie / time-out"

**Oorzaak:** Server reageert niet binnen de tijdslimiet

**Oplossing:**

* Controleer of de dienst beschikbaar is
* Controleer de eindpunt-URL
* Controleer of er tarieflimieten zijn
* Neem contact op met de systeembeheerder

### "Ongeldige JSON"

**Oorzaak:** De aanvraaggegevens hebben een onjuiste indeling

**Oplossing:**

* Controleer op ontbrekende komma's in JSON
* Controleer of alle offertes correct zijn
* Valideer het JSON-formaat (gebruik online JSON-validator)
* Controleer op speciale tekens

***

## Voorbeelden

### Voorbeeld 1: Verzenden naar Webhook Service

```
URL: https://webhook.site/your-unique-id
Method: POST
Data:
{
  "document_id": "DOC-123",
  "status": "approved",
  "amount": 5000
}
```

### Voorbeeld 2: Extern systeem bijwerken

```
URL: https://api.company.com/update
Method: PUT
Data:
{
  "record_id": "REC-456",
  "status": "completed",
  "timestamp": "2025-10-23T10:30:00"
}
```

### Voorbeeld 3: Externe service opvragen

```
URL: https://lookup.company.com/validate?id=SUP-789
Method: GET
Headers: Authorization: Bearer token
```

***

## Verschil met de "Call API"-kaart

De HTTPS-aanvraagkaart gebruikt een ingestelde HTTPS-URL en eigen headers. `call_api` gebruikt een relatief DocBits-API-pad en de context van de huidige gebruiker; het resultaat komt uit de antwoordtekst. Kies op basis van endpoint en antwoordcontract, niet op basis van een eenvoudige of complexe API.

***

## Beveiligingsoverwegingen

✅ **Gebruik altijd HTTPS** (beveiligde verbinding)

⚠️ **Nooit:**

* Zet wachtwoorden in de URL
* Maak API-sleutels zichtbaar in logboeken
* Neem persoonlijke gegevens op in parameters
* Gebruik HTTP voor gevoelige gegevens

***

## Beste praktijken

✅ **Doe:**

* Test eerst met kleine hoeveelheden gegevens
* Inclusief foutafhandeling
* Registreer belangrijke verzoeken
* Documenteer de integratie
* Controleer op fouten

❌ **Niet doen:**

* Roep herhaaldelijk hetzelfde eindpunt aan als dit niet nodig is
* Negeer reactiefouten
* Neem gevoelige gegevens op in platte tekst
* Overschrijd de limieten voor servicetarieven

***

## Gerelateerde kaarten

* **CALL\_API** - Meer geavanceerde API-integratie
* **CONDITION\_HTTPS\_REQUEST\_STATUS** - Controleer of het verzoek is geslaagd
* **ACTION\_SEND\_EMAIL** - Verzend in plaats daarvan via e-mail
* **ACTION\_RUN\_DOCOPERATOR\_SCRIPT** - Geautomatiseerde scripts

<!-- workflow-card-complete-example-20261021 action_https_request -->

### Voorbeeld van HTTPS-actie

**Configuratie:** Selecteer methode `POST`, vervang `DEMO_WEBHOOK_URL` door uw geautoriseerde testeindpunt, voeg header `Content-Type: application/json` en body `{"document_number":"DEMO-001"}` toe. Configureer authenticatie alleen zoals vereist door dat eindpunt; Kopieer nooit een echt geheim in documentatie.

**Verwacht resultaat en tegenvoorbeeld:** De actie verzendt het geconfigureerde verzoek wanneer de werkstroomroute wordt uitgevoerd. Inspecteer het HTTP-antwoord en de ontvangende testservice. Een time-out is geen bewijs dat de service niets heeft gedaan, en deze Then-actie staat los van de And-kaart die een HTTP-status controleert. Dit illustratieve verzoek is niet verzonden.

Dit is een illustratieve testconfiguratie en verwachte uitkomst; het werd niet uitgevoerd. Gebruik gegevens en ontvangers die in uw testorganisatie zijn geconfigureerd.
