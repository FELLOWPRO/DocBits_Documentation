# API Integratie Patroon

**Patroontype:** Integratie
**Complexiteit:** Gemiddeld
**Geschatte Insteltijd:** 45-60 minuten
**Veelvoorkomende Gebruiksscenario's:** Externe gegevens ophalen, prijsvalidatie, masterdata opzoeken

---

U bouwt dit patroon in de **Workflow Builder** (Workflow Dashboard → Workflowlijst → Workflow Toevoegen). Klik op **Add Card** om de kaartbibliotheek te openen en kies de kaarten die dit patroon gebruikt — `CALL_API`, `CONDITION_HTTPS_REQUEST_STATUS`, `ACTION_SET_FIELD_TO_TEXT` en `CONDITION_COMPARE_TWO_DOCFIELD_VALUES`:

<figure><img src="../../.gitbook/assets/workflow_add_card_picker.png" alt="Add Card-bibliotheek in de Workflow Builder, gegroepeerd per categorie"><figcaption><p>De <strong>Add Card</strong>-bibliotheek — kies de API-, voorwaarde- en veldkaarten die door dit patroon worden gebruikt uit deze categorieën.</p></figcaption></figure>

---

## Patroonoverzicht

Dit patroon demonstreert hoe u DocBits kunt integreren met externe API's om gegevens uit externe systemen op te halen, te valideren en op te slaan. Het is een van de meest voorkomende workflowpatronen voor het verbinden van DocBits met prijssystemen, validatiediensten, ERP-systemen en andere externe gegevensbronnen.

**Wat Dit Patroon Doet:**
1. Roept een externe API aan om gegevens op te halen
2. Valideert de API-respons
3. Slaat responsgegevens op in documentvelden
4. Neemt beslissingen op basis van opgehaalde gegevens
5. Routeert documenten dienovereenkomstig

---

## Wanneer Dit Patroon Te Gebruiken

Gebruik dit patroon wanneer u het volgende moet doen:
- ✅ Real-time prijzen ophalen uit externe systemen
- ✅ Leveranciersinformatie valideren tegen masterdatabase
- ✅ Productdetails opzoeken uit catalogussystemen
- ✅ Wisselkoersen ophalen van valutadiensten
- ✅ Adressen verifiëren met geocodingdiensten
- ✅ Voorraadniveaus controleren uit magazijnsystemen
- ✅ Belastingtarieven valideren van belastingdiensten

**Gebruik dit patroon niet wanneer:**
- ❌ Gegevens al in DocBits masterdata staan (gebruik in plaats daarvan masterdata lookup)
- ❌ Extern systeem geen API heeft (gebruik in plaats daarvan DocOperator Script patroon)
- ❌ Gegevens niet vaak veranderen (overweeg handmatige import)

---

## Compleet Workflowvoorbeeld

### Scenario: Valideer Factuurprijs Tegen Huidige Prijs-API

**Bedrijfsvereiste:**
- Leverancier stuurt factuur
- Factuur toont eenheidsprijs van €52,00
- We moeten verifiëren of dit overeenkomt met de huidige leveranciersprijzen
- Als de prijs meer dan 5% afwijkt, escaleren voor beoordeling

**Gebruikte Workflowkaarten:**
1. CALL_API - Haal huidige prijs op van leveranciers-API
2. CONDITION_HTTPS_REQUEST_STATUS - Controleer of API-aanroep is gelukt
3. ACTION_SET_FIELD_TO_TEXT - Sla API-prijs op in documentveld
4. CONDITION_COMPARE_TWO_DOCFIELD_VALUES - Vergelijk factuurprijs vs API-prijs
5. ACTION_ASSIGN_TO_USER - Routeer op basis van vergelijkingsresultaat
6. tasks_create - Maak beoordelingstaak indien nodig

---

## Stap-voor-Stap Implementatie

### Stap 1: Roep Externe API Aan

**Kaart:** CALL_API of ACTION_CALL_EXTERNAL_API

**Configuratie:**
```json
{
  "api_endpoint": "https://api.supplier-system.com/v1/pricing",
  "method": "POST",
  "headers": {
    "Authorization": "Bearer YOUR_API_KEY",
    "Content-Type": "application/json"
  },
  "request_body": {
    "product_id": "{{DOCUMENT_FIELD:Product_Code}}",
    "supplier_id": "{{DOCUMENT_FIELD:Supplier_Code}}",
    "quantity": "{{DOCUMENT_FIELD:Quantity}}",
    "currency": "EUR"
  }
}
```

**Verwachte Respons:**
```json
{
  "success": true,
  "data": {
    "product_id": "ABC123",
    "unit_price": 50.00,
    "currency": "EUR",
    "valid_until": "2025-12-31",
    "discount_applicable": true
  }
}
```

**Gidsreferentie:** [Call API Gids](../then/action/call-api-guide.md)

---

### Stap 2: Valideer API-respons

**Kaart:** CONDITION_HTTPS_REQUEST_STATUS

**Configuratie:**
```
Operator: IS EQUAL TO
Status Code: 200
```

**Logica:**
```
ALS API 200 retourneert (succes):
  → Ga door met gegevens opslaan
ANDERS:
  → Routeer naar "API Fout" afhandelingsworkflow
  → Stuur e-mailmelding
  → Maak handmatige beoordelingstaak
```

**Gidsreferentie:** [Gids Conditiekaarten - HTTP Status](../and/condition-cards-complete-guide.md#condition-https-request-status)

---

### Stap 3: Sla API-respons op in Documentvelden

**Kaart:** ACTION_SET_FIELD_TO_TEXT (of gelijkwaardige veldinsteller)

**Configuratie:**

**Veld 1: Current_API_Price**
```
Veldnaam: Current_API_Price
Veldwaarde: {{API_RESPONSE:data.unit_price}}
Veldtype: Nummer
```

**Veld 2: API_Price_Valid_Until**
```
Veldnaam: API_Price_Valid_Until
Veldwaarde: {{API_RESPONSE:data.valid_until}}
Veldtype: Datum
```

**Veld 3: API_Discount_Available**
```
Veldnaam: API_Discount_Available
Veldwaarde: {{API_RESPONSE:data.discount_applicable}}
Veldtype: Booleaans
```

**Resultaat:** Gegevens van API zijn nu opgeslagen in documentvelden voor later gebruik

**Gidsreferentie:** [Gids Veldmanipulatie - API-gegevens Opslaan](../then/document-field/field-manipulation-guide.md#storing-api-data)

---

### Stap 4: Vergelijk Factuurprijs met API-prijs

**Kaart:** CONDITION_COMPARE_TWO_DOCFIELD_VALUES

**Configuratie:**
```
Veld 1: Invoice_Unit_Price (uit OCR-extractie)
Veld 2: Current_API_Price (uit API-respons)
Operator: Bereken variantiepercentage
Tolerantie: 5%
```

**Berekening:**
```
Variantie % = |(Factuurprijs - API-prijs)| / API-prijs × 100

Voorbeeld:
  Factuurprijs: €52,00
  API-prijs: €50,00
  Variantie = |52 - 50| / 50 × 100 = 4%

  Is 4% ≤ 5% tolerantie? JA ✅
  Resultaat: PASS
```

**Gidsreferentie:** [Gids Conditiekaarten - Veldvergelijking](../and/condition-cards-complete-guide.md#field-comparison)

---

### Stap 5: Routeer op Basis van Validatieresultaat

**Scenario A: Prijs Binnen Tolerantie (Pass)**

**Kaarten:**
- ACTION_SET_FIELD_TO_TEXT
  - Stel veld "Price_Validation_Status" in op "PASS"
  - Stel veld "Price_Variance_Percent" in op "4%"
- ACTION_APPROVE_DOCUMENT
  - Document automatisch goedkeuren

**Scenario B: Prijs Buiten Tolerantie (Fail)**

**Kaarten:**
- ACTION_SET_FIELD_TO_TEXT
  - Stel veld "Price_Validation_Status" in op "FAIL"
  - Stel veld "Price_Variance_Percent" in op "12%" (voorbeeld)
- tasks_create
  - Taaktitel: "Review Price Variance - {{DOCUMENT_NUMBER}}"
  - Taakbeschrijving: "Invoice price (€{{Invoice_Unit_Price}}) exceeds API price (€{{Current_API_Price}}) by {{Price_Variance_Percent}}"
  - Prioriteit: Hoog
- ACTION_ASSIGN_TO_USER
  - Toewijzen aan: Inkoopmanager
- ACTION_SEND_EMAIL_TO_GROUPS
  - Stuur melding naar Inkoopteam

**Gidsreferenties:**
- [Toewijzingsgids](../then/assignee/assignment-user-guide.md)
- [Taaktoewijzingsgids](../then/task/task-assignment-guide.md)
- [Gids E-mail Verzenden](../then/action/send-email-groups-guide.md)

---

## Compleet Workflow Diagram

```
DOCUMENT KOMT AAN (Factuur met Product ABC123, Prijs €52)
│
├─ STAP 1: Roep Prijs-API Aan
│  Kaart: CALL_API
│  Verzoek: Haal huidige prijs op voor ABC123
│  │
│  ├─ SUCCES (200) ✅
│  │  Respons: {"unit_price": 50.00}
│  │  │
│  │  ├─ STAP 2: Controleer API-status
│  │  │  Kaart: CONDITION_HTTPS_REQUEST_STATUS
│  │  │  Resultaat: 200 = Succes
│  │  │  │
│  │  │  ├─ STAP 3: Sla API-gegevens op
│  │  │  │  Kaart: ACTION_SET_FIELD_TO_TEXT
│  │  │  │  Actie: Sla €50 op in "Current_API_Price" veld
│  │  │  │  │
│  │  │  │  ├─ STAP 4: Vergelijk Prijzen
│  │  │  │  │  Kaart: CONDITION_COMPARE_TWO_DOCFIELD_VALUES
│  │  │  │  │  Bereken: Variantie = |52-50|/50 = 4%
│  │  │  │  │  │
│  │  │  │  │  ├─ ALS Variantie ≤ 5% (PASS) ✅
│  │  │  │  │  │  │
│  │  │  │  │  │  ├─ Stel Statusveld in: "PASS"
│  │  │  │  │  │  └─ Document Automatisch Goedkeuren
│  │  │  │  │  │     → EINDE (Document Goedgekeurd)
│  │  │  │  │  │
│  │  │  │  │  └─ ALS Variantie > 5% (FAIL) ❌
│  │  │  │  │     │
│  │  │  │  │     ├─ Stel Statusveld in: "FAIL"
│  │  │  │  │     ├─ Maak Beoordelingstaak
│  │  │  │  │     ├─ Toewijzen aan Inkoopmanager
│  │  │  │  │     └─ Stuur E-mailmelding
│  │  │  │  │        → EINDE (In Afwachting van Beoordeling)
│  │  │  │  │
│  │  │  │  └─ [Veldopslag voltooid]
│  │  │  │
│  │  │  └─ [Statuscontrole voltooid]
│  │  │
│  │  └─ [API-gegevens opgehaald]
│  │
│  └─ FOUT (Niet-200) ❌
│     │
│     ├─ Stel Foutstatus in
│     ├─ Maak "API Fout" Taak
│     ├─ Toewijzen aan IT-ondersteuning
│     └─ Stuur E-mail naar Admin
│        → EINDE (API Fout - Handmatige Beoordeling)
```

---

## Configuratiesjablonen

### Sjabloon 1: Eenvoudig GET-verzoek (Opzoeken)

```json
{
  "card": "CALL_API",
  "endpoint": "https://api.example.com/lookup",
  "method": "GET",
  "headers": {
    "Authorization": "Bearer {{API_KEY}}"
  },
  "parameters": {
    "id": "{{DOCUMENT_FIELD:Lookup_ID}}"
  }
}
```

**Gebruik:** Eenvoudig gegevens opzoeken op ID

---

### Sjabloon 2: POST-verzoek met Body (Validatie)

```json
{
  "card": "CALL_API",
  "endpoint": "https://api.example.com/validate",
  "method": "POST",
  "headers": {
    "Authorization": "Bearer {{API_KEY}}",
    "Content-Type": "application/json"
  },
  "body": {
    "document_number": "{{DOCUMENT_NUMBER}}",
    "supplier_id": "{{DOCUMENT_FIELD:Supplier_Code}}",
    "total_amount": "{{DOCUMENT_FIELD:Total_Amount}}",
    "currency": "{{DOCUMENT_FIELD:Currency}}"
  }
}
```

**Gebruik:** Documentgegevens verzenden voor validatie

---

### Sjabloon 3: Complex Verzoek met Geneste Gegevens

```json
{
  "card": "CALL_API",
  "endpoint": "https://api.example.com/process",
  "method": "POST",
  "headers": {
    "Authorization": "Bearer {{API_KEY}}",
    "Content-Type": "application/json"
  },
  "body": {
    "document": {
      "type": "{{DOCUMENT_TYPE}}",
      "number": "{{DOCUMENT_NUMBER}}",
      "date": "{{DOCUMENT_FIELD:Invoice_Date}}"
    },
    "vendor": {
      "code": "{{DOCUMENT_FIELD:Supplier_Code}}",
      "name": "{{DOCUMENT_FIELD:Supplier_Name}}"
    },
    "items": [
      {
        "product": "{{TABLE_FIELD:Product_Code}}",
        "quantity": "{{TABLE_FIELD:Quantity}}",
        "unit_price": "{{TABLE_FIELD:Unit_Price}}"
      }
    ]
  }
}
```

**Gebruik:** Complexe documentverwerking met tabelgegevens

---

## Foutafhandeling

### Veelvoorkomende Fouten en Oplossingen

#### Fout 1: Verbindingstime-out

**Symptomen:**
- API reageert niet
- Workflow blijft wachten

**Oplossing:**
```
1. Controleer URL API-eindpunt (typfout?)
2. Verifieer netwerkconnectiviteit
3. Controleer status API-service
4. Implementeer time-outafhandeling:

   ALS CONDITION_HTTPS_REQUEST_STATUS = TIMEOUT:
     → Maak "API Time-out" taak
     → Toewijzen aan IT-ondersteuning
     → Stuur e-mailmelding
     → Gebruik fallback-waarde (indien beschikbaar)
```

#### Fout 2: 401 Ongeautoriseerd

**Symptomen:**
- API retourneert 401 status
- Authenticatie mislukt

**Oplossing:**
```
1. Verifieer of API-sleutel correct is
2. Controleer of API-sleutel is verlopen
3. Zorg ervoor dat Authorization-header correct is opgemaakt
4. Implementeer auth-foutafhandeling:

   ALS CONDITION_HTTPS_REQUEST_STATUS = 401:
     → Maak "API Auth Mislukt" taak
     → Toewijzen aan Admin
     → Log foutdetails
     → Stop workflowuitvoering
```

#### Fout 3: Ongeldig Responsformaat

**Symptomen:**
- Respons ontvangen maar kan niet parsen
- Ontbrekende verwachte velden

**Oplossing:**
```
1. Verifieer API-documentatie
2. Controleer of responsstructuur overeenkomt met verwachtingen
3. Implementeer responsvalidatie:

   ALS API_RESPONSE:data.unit_price IS NULL:
     → Stel standaardwaarde in
     → Maak "Ongeldige Respons" taak
     → Log respons voor debugging
```

**Gidsreferentie:** [Call API Probleemoplossing](../then/action/call-api-guide.md#troubleshooting)

---

## Geavanceerde Variaties

### Variatie 1: Multi-API Koppeling

**Scenario:** Gegevens nodig van meerdere API's

```
Stap 1: Roep Leveranciers-API Aan → Haal Leveranciersdetails Op
Stap 2: Roep Product-API Aan → Haal Productinfo Op (met Leveranciers-ID uit Stap 1)
Stap 3: Roep Prijs-API Aan → Haal Prijs Op (met Product-ID uit Stap 2)
Stap 4: Valideer & Sla alle gegevens op
```

---

### Variatie 2: Voorwaardelijke API-aanroepen

**Scenario:** Roep API alleen aan onder bepaalde voorwaarden

```
ALS DOCUMENT_TYPE = "Invoice" EN AMOUNT > 10000:
  → Roep Prijsvalidatie-API Aan
  → Verifieer prijzen
ANDERS:
  → Sla API-aanroep over (niet nodig voor kleine bedragen)
```

---

### Variatie 3: API-responscaching

**Scenario:** Verminder API-aanroepen door responsen te cachen

```
1. Controleer of "API_Last_Called" datum vandaag is
2. ALS Ja:
     → Gebruik gecachete waarde uit "Cached_API_Price" veld
3. ALS Nee:
     → Roep API aan
     → Sla respons op in "Cached_API_Price"
     → Stel "API_Last_Called" in op vandaag
```

---

## Prestatieoverwegingen

### Beste Praktijken

✅ **Doen:**
- Cache API-responsen waar mogelijk
- Gebruik time-outinstellingen (30-60 seconden)
- Implementeer retry-logica voor tijdelijke storingen
- Log API-aanroepen voor debugging
- Monitor API-gebruik/kosten
- Test eerst met voorbeelddocumenten

❌ **Niet Doen:**
- API's synchroon aanroepen voor elk document (overweeg batchverwerking)
- Responsfouten negeren
- Inloggegevens hardcoderen in workflow
- Onnodige API-aanroepen maken
- Vergeten time-outs af te handelen

---

## Testchecklist

Voordat u dit patroon implementeert:

- [ ] Test API-aanroep met geldige gegevens
- [ ] Test API-aanroep met ongeldige gegevens
- [ ] Test time-outscenario (wat gebeurt er als API traag is?)
- [ ] Test authenticatiefout
- [ ] Test ongeldig responsformaat
- [ ] Test veldopslag (gegevens correct opgeslagen?)
- [ ] Test vergelijkingslogica (correcte berekening?)
- [ ] Test routering (documenten gaan naar juiste plaats?)
- [ ] Test foutafhandeling (fouten netjes afgehandeld?)
- [ ] Test met hoog volume (prestaties acceptabel?)

---

## Praktijkvoorbeelden

### Voorbeeld 1: Wisselkoers Opzoeken

**API:** https://api.exchangerate-api.com/v4/latest/USD

**Workflow:**
1. Extraheer factuurvaluta: "GBP"
2. Roep wisselkoers-API aan
3. Haal GBP→EUR wisselkoers op
4. Bereken EUR-equivalent
5. Sla op in "Amount_EUR" veld
6. Ga door met verwerking met EUR-bedrag

---

### Voorbeeld 2: Leverancierskredietcontrole

**API:** Interne kredietcontroledienst

**Workflow:**
1. Extraheer leverancierscode
2. Roep kredietcontrole-API aan
3. Haal kredietstatus op: "APPROVED" of "BLOCKED"
4. ALS BLOCKED:
   - Stop verwerking
   - Maak urgente taak
   - Meld financiële team
5. ALS APPROVED:
   - Ga door met normale workflow

---

### Voorbeeld 3: Product Master Data Verrijking

**API:** Productcatalogusdienst

**Workflow:**
1. Extraheer productcode uit factuur
2. Roep product-API aan
3. Haal op: Productnaam, categorie, GL-rekening
4. Sla op in documentvelden
5. Gebruik voor automatische boekhouding

---

## Gerelateerde Patronen

### Dit Patroon Werkt Goed Samen Met:

- **[Gegevenstransformatie Patroon](data-transformation-pattern.md)** - Transformeer API-responsgegevens
- **[Beslissingslogica Patroon](decision-logic-pattern.md)** - Routeer op basis van API-gegevens
- **[Taakbeheer Patroon](task-management-pattern.md)** - Maak taken voor API-fouten
- **[PO Matching Patroon](po-matching-pattern.md)** - Combineer API-prijzen met PO-validatie

---

## Gerelateerde Gidsen

### Vereisten
- [Call API Gids](../then/action/call-api-guide.md) - API-kaartdocumentatie
- [Gids Conditiekaarten](../and/condition-cards-complete-guide.md) - Conditielogica
- [Gids Veldmanipulatie](../then/document-field/field-manipulation-guide.md) - Veldoperaties

### Gerelateerde Kaarten
- **CALL_API** - [Call API Gids](../then/action/call-api-guide.md)
- **ACTION_HTTPS_REQUEST** - [HTTPS Request Gids](../then/action/https-request-guide.md)
- **CONDITION_HTTPS_REQUEST_STATUS** - [Gids Conditiekaarten](../and/condition-cards-complete-guide.md#condition-https-request-status)
- **ACTION_SET_FIELD_TO_TEXT** - [Gids Veldmanipulatie](../then/document-field/field-manipulation-guide.md#set-field)
- **CONDITION_COMPARE_TWO_DOCFIELD_VALUES** - [Gids Conditiekaarten](../and/condition-cards-complete-guide.md#field-comparison)

### Volgende Stappen
- Implementeer foutafhandeling: [Foutafhandeling Patroon](error-handling-pattern.md)
- Voeg taakcreatie toe: [Taakbeheer Patroon](task-management-pattern.md)
- Transformeer gegevens: [Gegevenstransformatie Patroon](data-transformation-pattern.md)

---

## Ondersteuning & Bronnen

**Hulp Nodig?**
- Bekijk [Call API Probleemoplossing](../then/action/call-api-guide.md#troubleshooting)
- Controleer [API Responscodes](../then/action/call-api-guide.md#response-scenarios)
- Test API eerst met Postman
- Neem contact op met ondersteuning van API-provider

**Feedback:**
- Meld patroonproblemen aan: docs@docbits.com
- Suggesteer verbeteringen
- Deel uw gebruiksscenario's

---

**Patroonversie:** 1.0
**Laatst Bijgewerkt:** 23 oktober 2025
**Moeilijkheidsgraad:** Gemiddeld
**Geschatte Tijd:** 45-60 minuten
**Succespercentage:** Hoog (wanneer API stabiel is)
