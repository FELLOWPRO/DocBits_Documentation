# API Integration Pattern

**Tip obrasca:** Integracija
**Složenost:** Srednja
**Procenjeno podešavanje:** 45-60 minuta
**Uobičajeni slučajevi upotrebe:** Preuzimanje eksternih podataka, validacija cena, pretraga glavnih podataka

---

Ovaj obrazac gradite u **Workflow Builder**-u (Workflow Dashboard → Workflow List → Add Workflow). Kliknite na **Add Card** da otvorite biblioteku kartica i izaberete kartice koje ovaj obrazac koristi — `CALL_API`, `CONDITION_HTTPS_REQUEST_STATUS`, `ACTION_SET_FIELD_TO_TEXT` i `CONDITION_COMPARE_TWO_DOCFIELD_VALUES`:

<figure><img src="../../../.gitbook/assets/workflow_add_card_picker.png" alt="Biblioteka Add Card u Workflow Builder-u, grupisana po kategoriji"><figcaption><p>Biblioteka <strong>Add Card</strong> — izaberite API, uslovne i kartice polja koje ovaj obrazac koristi iz ovih kategorija.</p></figcaption></figure>

---

## Pregled obrasca

Ovaj obrazac pokazuje kako da integrišete DocBits sa eksternim API-jima radi preuzimanja, validacije i čuvanja podataka iz eksternih sistema. To je jedan od najčešćih obrazaca toka rada za povezivanje DocBits-a sa sistemima za cene, servisima za validaciju, ERP sistemima i drugim eksternim izvorima podataka.

**Šta ovaj obrazac radi:**
1. Poziva eksterni API radi preuzimanja podataka
2. Validira API odgovor
3. Čuva podatke odgovora u poljima dokumenta
4. Donosi odluke na osnovu preuzetih podataka
5. Rutira dokumente u skladu sa tim

---

## Kada koristiti ovaj obrazac

Koristite ovaj obrazac kada treba da:
- ✅ Preuzmete cene u realnom vremenu iz eksternih sistema
- ✅ Validirate informacije o dobavljaču u odnosu na glavnu bazu podataka
- ✅ Pretražite detalje o proizvodu iz katalog sistema
- ✅ Dobijete kurseve valuta iz servisa za valute
- ✅ Verifikujete adrese pomoću servisa za geokodiranje
- ✅ Proverite nivoe zaliha iz sistema skladišta
- ✅ Validirate poreske stope iz poreskih servisa

**Nemojte koristiti ovaj obrazac kada:**
- ❌ Podaci su već u DocBits glavnim podacima (umesto toga koristite pretragu glavnih podataka)
- ❌ Eksterni sistem nema API (umesto toga koristite DocOperator Script obrazac)
- ❌ Podaci se ne menjaju često (razmotrite ručni uvoz)

---

## Kompletan primer toka rada

### Scenario: Validacija cene fakture u odnosu na API trenutnih cena

**Poslovni zahtev:**
- Dobavljač šalje fakturu
- Faktura prikazuje jediničnu cenu od €52,00
- Treba da proverimo da li se ovo poklapa sa trenutnim cenama dobavljača
- Ako cena varira više od 5%, eskalirati za pregled

**Korišćene kartice toka rada:**
1. CALL_API - Preuzimanje trenutne cene iz API-ja dobavljača
2. CONDITION_HTTPS_REQUEST_STATUS - Provera da li je API poziv uspeo
3. ACTION_SET_FIELD_TO_TEXT - Čuvanje API cene u polju dokumenta
4. CONDITION_COMPARE_TWO_DOCFIELD_VALUES - Poređenje cene fakture sa API cenom
5. ACTION_ASSIGN_TO_USER - Rutiranje na osnovu rezultata poređenja
6. tasks_create - Kreiranje zadatka pregleda ako je potrebno

---

## Implementacija korak po korak

### Korak 1: Pozovite eksterni API

**Kartica:** CALL_API ili ACTION_CALL_EXTERNAL_API

**Konfiguracija:**
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

**Očekivani odgovor:**
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

**Referenca vodiča:** [Call API Guide](../then/action/call-api-guide.md)

---

### Korak 2: Validirajte API odgovor

**Kartica:** CONDITION_HTTPS_REQUEST_STATUS

**Konfiguracija:**
```
Operator: IS EQUAL TO
Status Code: 200
```

**Logika:**
```
IF API returns 200 (success):
  → Continue to store data
ELSE:
  → Route to "API Error" handling workflow
  → Send email notification
  → Create manual review task
```

**Referenca vodiča:** [Condition Cards Guide - HTTP Status](../and/condition-cards-complete-guide.md#condition-https-request-status)

---

### Korak 3: Sačuvajte API odgovor u poljima dokumenta

**Kartica:** ACTION_SET_FIELD_TO_TEXT (ili ekvivalentni podešivač polja)

**Konfiguracija:**

**Polje 1: Current_API_Price**
```
Field Name: Current_API_Price
Field Value: {{API_RESPONSE:data.unit_price}}
Field Type: Number
```

**Polje 2: API_Price_Valid_Until**
```
Field Name: API_Price_Valid_Until
Field Value: {{API_RESPONSE:data.valid_until}}
Field Type: Date
```

**Polje 3: API_Discount_Available**
```
Field Name: API_Discount_Available
Field Value: {{API_RESPONSE:data.discount_applicable}}
Field Type: Boolean
```

**Rezultat:** Podaci iz API-ja su sada sačuvani u poljima dokumenta za kasniju upotrebu

**Referenca vodiča:** [Field Manipulation Guide - API Data Storage](../then/document-field/field-manipulation-guide.md#storing-api-data)

---

### Korak 4: Uporedite cenu fakture sa API cenom

**Kartica:** CONDITION_COMPARE_TWO_DOCFIELD_VALUES

**Konfiguracija:**
```
Field 1: Invoice_Unit_Price (from OCR extraction)
Field 2: Current_API_Price (from API response)
Operator: Calculate variance percentage
Tolerance: 5%
```

**Izračunavanje:**
```
Variance % = |(Invoice_Price - API_Price)| / API_Price × 100

Example:
  Invoice Price: €52.00
  API Price: €50.00
  Variance = |52 - 50| / 50 × 100 = 4%

  Is 4% ≤ 5% tolerance? YES ✅
  Result: PASS
```

**Referenca vodiča:** [Condition Cards Guide - Field Comparison](../and/condition-cards-complete-guide.md#field-comparison)

---

### Korak 5: Rutirajte na osnovu rezultata validacije

**Scenario A: Cena unutar tolerancije (Prolaz)**

**Kartice:**
- ACTION_SET_FIELD_TO_TEXT
  - Postavite polje "Price_Validation_Status" = "PASS"
  - Postavite polje "Price_Variance_Percent" = "4%"
- ACTION_APPROVE_DOCUMENT
  - Automatski odobrite dokument

**Scenario B: Cena izvan tolerancije (Neuspeh)**

**Kartice:**
- ACTION_SET_FIELD_TO_TEXT
  - Postavite polje "Price_Validation_Status" = "FAIL"
  - Postavite polje "Price_Variance_Percent" = "12%" (primer)
- tasks_create
  - Naslov zadatka: "Review Price Variance - {{DOCUMENT_NUMBER}}"
  - Opis zadatka: "Invoice price (€{{Invoice_Unit_Price}}) exceeds API price (€{{Current_API_Price}}) by {{Price_Variance_Percent}}"
  - Prioritet: Visok
- ACTION_ASSIGN_TO_USER
  - Dodelite: Menadžeru nabavke
- ACTION_SEND_EMAIL_TO_GROUPS
  - Pošaljite obaveštenje timu za nabavku

**Reference vodiča:**
- [Assignment Guide](../then/assignee/assignment-user-guide.md)
- [Task Assignment Guide](../then/task/task-assignment-guide.md)
- [Send Email Guide](../then/action/send-email-groups-guide.md)

---

## Kompletan dijagram toka rada

```
DOCUMENT ARRIVES (Invoice with Product ABC123, Price €52)
│
├─ STEP 1: Call Pricing API
│  Card: CALL_API
│  Request: Get current price for ABC123
│  │
│  ├─ SUCCESS (200) ✅
│  │  Response: {"unit_price": 50.00}
│  │  │
│  │  ├─ STEP 2: Check API Status
│  │  │  Card: CONDITION_HTTPS_REQUEST_STATUS
│  │  │  Result: 200 = Success
│  │  │  │
│  │  │  ├─ STEP 3: Store API Data
│  │  │  │  Card: ACTION_SET_FIELD_TO_TEXT
│  │  │  │  Action: Store €50 in "Current_API_Price" field
│  │  │  │  │
│  │  │  │  ├─ STEP 4: Compare Prices
│  │  │  │  │  Card: CONDITION_COMPARE_TWO_DOCFIELD_VALUES
│  │  │  │  │  Calculate: Variance = |52-50|/50 = 4%
│  │  │  │  │  │
│  │  │  │  │  ├─ IF Variance ≤ 5% (PASS) ✅
│  │  │  │  │  │  │
│  │  │  │  │  │  ├─ Set Status Field: "PASS"
│  │  │  │  │  │  └─ Auto-Approve Document
│  │  │  │  │  │     → END (Document Approved)
│  │  │  │  │  │
│  │  │  │  │  └─ IF Variance > 5% (FAIL) ❌
│  │  │  │  │     │
│  │  │  │  │     ├─ Set Status Field: "FAIL"
│  │  │  │  │     ├─ Create Review Task
│  │  │  │  │     ├─ Assign to Procurement Manager
│  │  │  │  │     └─ Send Email Notification
│  │  │  │  │        → END (Pending Review)
│  │  │  │  │
│  │  │  │  └─ [Field storage complete]
│  │  │  │
│  │  │  └─ [Status check complete]
│  │  │
│  │  └─ [API data retrieved]
│  │
│  └─ ERROR (Non-200) ❌
│     │
│     ├─ Set Error Status
│     ├─ Create "API Error" Task
│     ├─ Assign to IT Support
│     └─ Send Email to Admin
│        → END (API Error - Manual Review)
```

---

## Šabloni za konfiguraciju

### Šablon 1: Jednostavan GET zahtev (Pretraga)

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

**Upotreba:** Jednostavna pretraga podataka po ID-u

---

### Šablon 2: POST zahtev sa telom (Validacija)

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

**Upotreba:** Slanje podataka dokumenta na validaciju

---

### Šablon 3: Složen zahtev sa ugnežđenim podacima

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

**Upotreba:** Složena obrada dokumenta sa podacima tabele

---

## Rukovanje greškama

### Uobičajene greške i rešenja

#### Greška 1: Isticanje vremena veze

**Simptomi:**
- API ne odgovara
- Tok rada zaglavljen u čekanju

**Rešenje:**
```
1. Check API endpoint URL (typo?)
2. Verify network connectivity
3. Check API service status
4. Implement timeout handling:

   IF CONDITION_HTTPS_REQUEST_STATUS = TIMEOUT:
     → Create "API Timeout" task
     → Assign to IT Support
     → Send email notification
     → Use fallback value (if available)
```

#### Greška 2: 401 Unauthorized

**Simptomi:**
- API vraća status 401
- Autentifikacija neuspešna

**Rešenje:**
```
1. Verify API key is correct
2. Check if API key expired
3. Ensure Authorization header formatted correctly
4. Implement auth error handling:

   IF CONDITION_HTTPS_REQUEST_STATUS = 401:
     → Create "API Auth Failed" task
     → Assign to Admin
     → Log error details
     → Stop workflow execution
```

#### Greška 3: Nevažeći format odgovora

**Simptomi:**
- Odgovor primljen ali se ne može parsirati
- Nedostaju očekivana polja

**Rešenje:**
```
1. Verify API documentation
2. Check response structure matches expectations
3. Implement response validation:

   IF API_RESPONSE:data.unit_price IS NULL:
     → Set default value
     → Create "Invalid Response" task
     → Log response for debugging
```

**Referenca vodiča:** [Call API Troubleshooting](../then/action/call-api-guide.md#troubleshooting)

---

## Napredne varijacije

### Varijacija 1: Lančano povezivanje više API-ja

**Scenario:** Treba vam podaci iz više API-ja

```
Step 1: Call Supplier API → Get Supplier Details
Step 2: Call Product API → Get Product Info (using Supplier ID from Step 1)
Step 3: Call Pricing API → Get Price (using Product ID from Step 2)
Step 4: Validate & Store all data
```

---

### Varijacija 2: Uslovni API pozivi

**Scenario:** Pozivajte API samo pod određenim uslovima

```
IF DOCUMENT_TYPE = "Invoice" AND AMOUNT > 10000:
  → Call Pricing Validation API
  → Verify prices
ELSE:
  → Skip API call (not needed for small amounts)
```

---

### Varijacija 3: Keširanje API odgovora

**Scenario:** Smanjite broj API poziva keširanjem odgovora

```
1. Check if "API_Last_Called" date is today
2. IF Yes:
     → Use cached value from "Cached_API_Price" field
3. IF No:
     → Call API
     → Store response in "Cached_API_Price"
     → Set "API_Last_Called" to today
```

---

## Razmatranja performansi

### Najbolje prakse

✅ **Radite:**
- Keširajte API odgovore kada je moguće
- Koristite podešavanja isteka vremena (30-60 sekundi)
- Implementirajte logiku ponovnog pokušaja za privremene greške
- Beležite API pozive za otklanjanje grešaka
- Pratite upotrebu/troškove API-ja
- Prvo testirajte sa uzorcima dokumenata

❌ **Ne radite:**
- Ne pozivajte API-je sinhrono za svaki dokument (razmotrite paketnu obradu)
- Ne ignorišite greške u odgovoru
- Ne kodirajte čvrsto akreditive u tok rada
- Ne pravite nepotrebne API pozive
- Ne zaboravljajte da rukujete istekom vremena

---

## Lista za proveru testiranja

Pre postavljanja ovog obrasca:

- [ ] Testirajte API poziv sa važećim podacima
- [ ] Testirajte API poziv sa nevažećim podacima
- [ ] Testirajte scenario isteka vremena (šta se dešava ako je API spor?)
- [ ] Testirajte neuspeh autentifikacije
- [ ] Testirajte nevažeći format odgovora
- [ ] Testirajte čuvanje polja (da li su podaci ispravno sačuvani?)
- [ ] Testirajte logiku poređenja (ispravno izračunavanje?)
- [ ] Testirajte rutiranje (da li dokumenti idu na pravo mesto?)
- [ ] Testirajte rukovanje greškama (da li se greškama elegantno rukuje?)
- [ ] Testirajte sa velikim obimom (da li su performanse prihvatljive?)

---

## Primeri iz stvarnog sveta

### Primer 1: Pretraga kursa razmene valuta

**API:** https://api.exchangerate-api.com/v4/latest/USD

**Tok rada:**
1. Izvucite valutu fakture: "GBP"
2. Pozovite API za kurs razmene
3. Dobijte kurs razmene GBP→EUR
4. Izračunajte EUR ekvivalent
5. Sačuvajte u polju "Amount_EUR"
6. Nastavite obradu sa EUR iznosom

---

### Primer 2: Provera kreditne sposobnosti dobavljača

**API:** Interni servis za proveru kreditne sposobnosti

**Tok rada:**
1. Izvucite kod dobavljača
2. Pozovite API za proveru kreditne sposobnosti
3. Dobijte kreditni status: "APPROVED" ili "BLOCKED"
4. IF BLOCKED:
   - Zaustavite obradu
   - Kreirajte hitan zadatak
   - Obavestite finansijski tim
5. IF APPROVED:
   - Nastavite normalan tok rada

---

### Primer 3: Obogaćivanje glavnih podataka o proizvodu

**API:** Servis kataloga proizvoda

**Tok rada:**
1. Izvucite kod proizvoda iz fakture
2. Pozovite API za proizvod
3. Dobijte: Naziv proizvoda, kategoriju, GL nalog
4. Sačuvajte u poljima dokumenta
5. Koristite za automatsko knjiženje

---

## Povezani obrasci

### Ovaj obrazac dobro funkcioniše sa:

- **[Data Transformation Pattern](data-transformation-pattern.md)** - Transformišite podatke API odgovora
- **[Decision Logic Pattern](decision-logic-pattern.md)** - Rutirajte na osnovu API podataka
- **[Task Management Pattern](task-management-pattern.md)** - Kreirajte zadatke za API greške
- **[PO Matching Pattern](po-matching-pattern.md)** - Kombinujte API cene sa PO validacijom

---

## Povezani vodiči

### Preduslovi
- [Call API Guide](../then/action/call-api-guide.md) - Dokumentacija API kartice
- [Condition Cards Guide](../and/condition-cards-complete-guide.md) - Uslovna logika
- [Field Manipulation Guide](../then/document-field/field-manipulation-guide.md) - Operacije nad poljima

### Povezane kartice
- **CALL_API** - [Call API Guide](../then/action/call-api-guide.md)
- **ACTION_HTTPS_REQUEST** - [HTTPS Request Guide](../then/action/https-request-guide.md)
- **CONDITION_HTTPS_REQUEST_STATUS** - [Condition Cards Guide](../and/condition-cards-complete-guide.md#condition-https-request-status)
- **ACTION_SET_FIELD_TO_TEXT** - [Field Manipulation Guide](../then/document-field/field-manipulation-guide.md#set-field)
- **CONDITION_COMPARE_TWO_DOCFIELD_VALUES** - [Condition Cards Guide](../and/condition-cards-complete-guide.md#field-comparison)

### Sledeći koraci
- Implementirajte rukovanje greškama: [Error Handling Pattern](error-handling-pattern.md)
- Dodajte kreiranje zadataka: [Task Management Pattern](task-management-pattern.md)
- Transformišite podatke: [Data Transformation Pattern](data-transformation-pattern.md)

---

## Podrška i resursi

**Treba vam pomoć?**
- Pregledajte [Call API Troubleshooting](../then/action/call-api-guide.md#troubleshooting)
- Proverite [API Response Codes](../then/action/call-api-guide.md#response-scenarios)
- Prvo testirajte API sa Postman-om
- Kontaktirajte podršku pružaoca API-ja

**Povratne informacije:**
- Prijavite probleme sa obrascem na: docs@docbits.com
- Predložite poboljšanja
- Podelite svoje slučajeve upotrebe

---

**Verzija obrasca:** 1.0
**Poslednje ažuriranje:** 23. oktobar 2025.
**Težina:** Srednja
**Procenjeno vreme:** 45-60 minuta
**Stopa uspeha:** Visoka (kada je API stabilan)
