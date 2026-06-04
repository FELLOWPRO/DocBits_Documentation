# Data Transformation Pattern

**Tip obrasca:** Obrada i manipulacija podacima
**Složenost:** Srednja
**Procenjeno podešavanje:** 30-45 minuta
**Uobičajeni slučajevi upotrebe:** Izračunavanja polja, formatiranje podataka, konverzija valuta, konverzija jedinica, obogaćivanje podataka

---

Ovaj obrazac gradite u **Workflow Builder**-u (Workflow Dashboard → Workflow List → Add Workflow). Kliknite na **Add Card** i otvorite kategoriju **Document Field** — ona sadrži kartice za čitanje, pisanje, izračunavanje i formatiranje koje ovaj obrazac povezuje u lanac:

<figure><img src="../../../.gitbook/assets/workflow_add_card_picker.png" alt="Biblioteka Add Card u Workflow Builder-u, grupisana po kategoriji"><figcaption><p>Biblioteka <strong>Add Card</strong> — kartice za čitanje/pisanje polja, izračunavanje i formatiranje nalaze se pod kategorijom <strong>Document Field</strong>.</p></figcaption></figure>

---

## Pregled obrasca

Ovaj obrazac pokazuje kako da transformišete, izračunavate, formatirate i obogaćujete podatke dokumenta u DocBits tokovima rada. Transformacija podataka je ključna za pripremu podataka za izvoz, izvođenje izračunavanja, standardizaciju formata i obogaćivanje dokumenata dodatnim informacijama.

**Šta ovaj obrazac radi:**
1. Izvlači podatke iz polja dokumenta
2. Izvodi izračunavanja i transformacije
3. Formatira podatke prema potrebnim standardima
4. Konvertuje između jedinica, valuta, datuma
5. Obogaćuje dokumente izvedenim podacima ili podacima iz pretrage
6. Validira i čisti podatke

---

## Kada koristiti ovaj obrazac

Koristite ovaj obrazac kada treba da:
- ✅ Izračunate ukupne iznose, međuzbirove, poreze
- ✅ Konvertujete valute ili jedinice
- ✅ Formatirate datume, brojeve, tekst
- ✅ Izvedete vrednosti iz postojećih polja
- ✅ Obogatite podatke iz eksternih izvora
- ✅ Standardizujete formate podataka
- ✅ Očistite i validirate podatke
- ✅ Pripremite podatke za izvoz

**Nemojte koristiti ovaj obrazac kada:**
- ❌ Nije potrebna transformacija
- ❌ Podaci su već u ispravnom formatu
- ❌ Jednostavno kopiranje polja je dovoljno

---

## Tipovi transformacije podataka

### 1. Izračunavanja

**Matematičke operacije:**
```
- Addition: Quantity + Bonus_Quantity = Total_Quantity
- Subtraction: Invoice_Total - Tax_Amount = Net_Amount
- Multiplication: Quantity × Unit_Price = Line_Total
- Division: Total_Amount / Quantity = Unit_Price
- Percentage: (Discount / Subtotal) × 100 = Discount_Percent
```

### 2. Operacije sa stringovima

**Manipulacija tekstom:**
```
- Concatenation: First_Name + " " + Last_Name = Full_Name
- Uppercase: "invoice" → "INVOICE"
- Lowercase: "SUPPLIER" → "supplier"
- Substring: "INV-2025-001" → "2025" (extract year)
- Replace: "01/23/2025" → "2025-01-23"
- Trim: "  ABC Corp  " → "ABC Corp"
```

### 3. Konverzija tipa podataka

**Transformacije tipova:**
```
- String to Number: "123.45" → 123.45
- Number to String: 123.45 → "123.45"
- Date to String: 2025-10-23 → "October 23, 2025"
- String to Date: "23.10.2025" → 2025-10-23
- Boolean to String: true → "Yes"
```

### 4. Konverzije jedinica

**Konverzije mernih jedinica:**
```
- Weight: kg → lbs, tons → kg
- Length: cm → inches, m → ft
- Volume: liters → gallons
- Temperature: Celsius → Fahrenheit
- Quantity: pieces → dozens, units → pallets
```

### 5. Konverzije valuta

**Primena kursa razmene:**
```
- USD → EUR: Amount_USD × Rate = Amount_EUR
- Multi-currency: Convert all to base currency
- Historical rates: Use rate from invoice date
```

### 6. Transformacije datuma

**Operacije sa datumima:**
```
- Format change: 10/23/2025 → 2025-10-23
- Add days: Invoice_Date + 30 = Due_Date
- Calculate age: Today - Invoice_Date = Age_Days
- Extract parts: "2025-10-23" → Year: 2025, Month: 10, Day: 23
```

---

## Kompletan primer toka rada

### Scenario: Izračunavanje ukupnog iznosa fakture i obogaćivanje podataka

**Poslovni zahtev:**
- Izvucite stavke iz fakture
- Izračunajte ukupne iznose stavki (Količina × Cena)
- Izračunajte međuzbir (zbir ukupnih iznosa stavki)
- Izračunajte iznos poreza (Međuzbir × Poreska stopa)
- Izračunajte ukupan iznos (Međuzbir + Porez)
- Konvertujte u EUR ako je faktura u drugoj valuti
- Formatirajte iznose na 2 decimalna mesta
- Dodajte GL nalog kompanije na osnovu kategorije proizvoda
- Validirajte izračunavanja u odnosu na ukupan iznos fakture
- Označite ako je odstupanje > 1%

**Korišćene kartice toka rada:**
1. ACTION_CALCULATE_FIELD - Izvođenje izračunavanja
2. ACTION_SET_FIELD_TO_TEXT - Čuvanje rezultata
3. ACTION_COPY_FIELD_VALUE - Kopiranje vrednosti
4. CALL_API - Dobijanje kurseva razmene (ako je potrebno)
5. CONDITION_COMPARE_TWO_DOCFIELD_VALUES - Validacija izračunavanja
6. ACTION_SET_FIELD_FROM_MASTER_DATA - Obogaćivanje GL nalozima

---

## Implementacija korak po korak

### Korak 1: Izračunavanja stavki

**Izračunajte ukupne iznose stavki:**

**Kartica:** ACTION_CALCULATE_FIELD

**Za svaku stavku:**
```
Field: Line_Total
Formula: {{TABLE_FIELD:Quantity}} * {{TABLE_FIELD:Unit_Price}}
Result Type: Number
Decimal Places: 2
```

**Primer:**
```
Line 1:
  Quantity: 100
  Unit Price: €50.00
  Calculation: 100 × 50.00 = €5,000.00
  Store in: Line_Total

Line 2:
  Quantity: 50
  Unit Price: €20.00
  Calculation: 50 × 20.00 = €1,000.00
  Store in: Line_Total

Line 3:
  Quantity: 25
  Unit Price: €15.50
  Calculation: 25 × 15.50 = €387.50
  Store in: Line_Total
```

**Referenca vodiča:** [Field Manipulation Guide - Calculations](../then/document-field/field-manipulation-guide.md#calculate-field)

---

### Korak 2: Izračunajte međuzbir dokumenta

**Saberite sve ukupne iznose stavki:**

**Kartica:** ACTION_CALCULATE_FIELD

**Konfiguracija:**
```
Field: Calculated_Subtotal
Formula: SUM({{TABLE_COLUMN:Line_Total}})
Result Type: Number
Decimal Places: 2
```

**Primer:**
```
Line 1 Total: €5,000.00
Line 2 Total: €1,000.00
Line 3 Total: €387.50

Subtotal = 5000 + 1000 + 387.50 = €6,387.50
Store in: Calculated_Subtotal
```

---

### Korak 3: Izračunajte iznos poreza

**Primenite poresku stopu na međuzbir:**

**Kartica:** ACTION_CALCULATE_FIELD

**Konfiguracija:**
```
Field: Calculated_Tax_Amount
Formula: {{Calculated_Subtotal}} * ({{Tax_Rate}} / 100)
Result Type: Number
Decimal Places: 2
```

**Primer:**
```
Calculated_Subtotal: €6,387.50
Tax_Rate: 19% (VAT)

Tax Amount = 6387.50 × (19 / 100)
          = 6387.50 × 0.19
          = €1,213.63

Store in: Calculated_Tax_Amount
```

---

### Korak 4: Izračunajte ukupan iznos

**Saberite međuzbir i porez:**

**Kartica:** ACTION_CALCULATE_FIELD

**Konfiguracija:**
```
Field: Calculated_Grand_Total
Formula: {{Calculated_Subtotal}} + {{Calculated_Tax_Amount}}
Result Type: Number
Decimal Places: 2
```

**Primer:**
```
Calculated_Subtotal: €6,387.50
Calculated_Tax_Amount: €1,213.63

Grand Total = 6387.50 + 1213.63 = €7,601.13

Store in: Calculated_Grand_Total
```

---

### Korak 5: Konverzija valute (ako je potrebno)

**Proverite da li je potrebna konverzija:**

**Kartica:** CONDITION_DOC_FIELD_IS

**Konfiguracija:**
```
Field: Invoice_Currency
Operator: IS NOT EQUAL TO
Value: EUR
```

**Ako je potrebna konverzija:**

**Korak 5a: Dobijte kurs razmene**

**Kartica:** CALL_API

**Konfiguracija:**
```
Endpoint: https://api.exchangerate-api.com/v4/latest/{{Invoice_Currency}}
Method: GET
Response Path: rates.EUR
Store in: Exchange_Rate_To_EUR
```

**Primer:**
```
Invoice Currency: USD
API Response: {
  "base": "USD",
  "rates": {
    "EUR": 0.92
  }
}

Exchange_Rate_To_EUR = 0.92
```

**Korak 5b: Konvertujte iznose**

**Kartica:** ACTION_CALCULATE_FIELD

**Konfiguracija:**
```
Field: Grand_Total_EUR
Formula: {{Calculated_Grand_Total}} * {{Exchange_Rate_To_EUR}}
Result Type: Number
Decimal Places: 2
```

**Primer:**
```
Grand Total (USD): $7,601.13
Exchange Rate: 0.92

Grand Total (EUR) = 7601.13 × 0.92 = €6,993.04

Store in: Grand_Total_EUR
```

**Referenca vodiča:** [API Integration Pattern - Currency Conversion](api-integration-pattern.md#currency-conversion-example)

---

### Korak 6: Obogaćivanje podataka - Dodajte GL naloge

**Pretražite GL nalog po kategoriji proizvoda:**

**Kartica:** ACTION_SET_FIELD_FROM_MASTER_DATA

**Konfiguracija:**
```
Lookup Table: GL_Account_Mapping
Lookup Key: {{TABLE_FIELD:Product_Category}}
Return Field: GL_Account_Number
Store in: GL_Account
```

**Primer:**
```
Line 1:
  Product Category: "Office Supplies"
  Lookup → GL_Account_Mapping table
  Result: GL Account "4200-100" (Office Expense)

Line 2:
  Product Category: "IT Equipment"
  Lookup → GL_Account_Mapping table
  Result: GL Account "6100-200" (IT Assets)

Line 3:
  Product Category: "Services"
  Lookup → GL_Account_Mapping table
  Result: GL Account "5000-300" (Services Expense)
```

**Referenca vodiča:** [Field Manipulation Guide - Master Data](../then/document-field/field-manipulation-guide.md#master-data-lookup)

---

### Korak 7: Validirajte izračunavanja

**Uporedite izračunati ukupan iznos sa ukupnim iznosom fakture:**

**Kartica:** CONDITION_COMPARE_TWO_DOCFIELD_VALUES

**Konfiguracija:**
```
Field 1: Calculated_Grand_Total
Field 2: Invoice_Total (from OCR)
Operator: Calculate Variance Percentage
Tolerance: 1%
```

**Izračunavanje:**
```
Variance % = |Calculated - Invoice| / Invoice × 100

Example:
  Calculated Total: €7,601.13
  Invoice Total: €7,600.00

  Variance = |7601.13 - 7600.00| / 7600.00 × 100
          = 1.13 / 7600.00 × 100
          = 0.015%

  Is 0.015% ≤ 1% tolerance? YES ✅
  Result: PASS (calculations match invoice)
```

**Logika:**
```
IF Variance ≤ 1%:
  Set Validation_Status = "PASS"
  Continue processing
ELSE:
  Set Validation_Status = "FAIL"
  Create review task
  Flag for manual verification
```

**Referenca vodiča:** [Condition Cards Guide - Field Comparison](../and/condition-cards-complete-guide.md#field-comparison)

---

### Korak 8: Formatirajte podatke za izvoz

**Standardizujte formate:**

**Kartica:** ACTION_SET_FIELD_TO_TEXT

**Formatiranje datuma:**
```
Field: Invoice_Date_Formatted
Value: FORMATDATE({{Invoice_Date}}, "YYYY-MM-DD")
Example: 10/23/2025 → 2025-10-23
```

**Formatiranje brojeva:**
```
Field: Amount_Formatted
Value: FORMATNUMBER({{Grand_Total_EUR}}, 2, ",", ".")
Example: 7601.13 → 7.601,13 (German format)
```

**Formatiranje teksta:**
```
Field: Supplier_Name_Upper
Value: UPPERCASE({{Supplier_Name}})
Example: "ABC Corporation" → "ABC CORPORATION"
```

---

## Napredne transformacije

### Transformacija 1: Višenivovsko izračunavanje poreza

**Scenario:** Različite poreske stope po stavci

```
Line 1: Product A (Tax Rate 19%)
Line 2: Product B (Tax Rate 7% - reduced)
Line 3: Product C (Tax Rate 0% - exempt)

Calculation:
  Line 1 Tax = €5,000.00 × 0.19 = €950.00
  Line 2 Tax = €1,000.00 × 0.07 = €70.00
  Line 3 Tax = €387.50 × 0.00 = €0.00

  Total Tax = €950.00 + €70.00 + €0.00 = €1,020.00
```

**Implementacija:**
```
For each line:
  1. Get product tax category
  2. Lookup applicable tax rate
  3. Calculate: Line_Net × Tax_Rate = Line_Tax
  4. Sum all Line_Tax values = Total_Tax
```

---

### Transformacija 2: Izračunavanja popusta

**Scenario:** Primenite popust na količinu i popust za rano plaćanje

```
Original Subtotal: €10,000.00

Step 1: Volume Discount (10% for orders > €5,000)
  Discount = €10,000.00 × 0.10 = €1,000.00
  After Volume Discount = €10,000.00 - €1,000.00 = €9,000.00

Step 2: Early Payment Discount (2% if paid within 10 days)
  Discount = €9,000.00 × 0.02 = €180.00
  After Payment Discount = €9,000.00 - €180.00 = €8,820.00

Step 3: Calculate Tax (on discounted amount)
  Tax = €8,820.00 × 0.19 = €1,675.80

Final Total = €8,820.00 + €1,675.80 = €10,495.80
```

**Implementacija:**
```
1. Check order value for volume discount eligibility
2. Calculate volume discount
3. Apply volume discount to subtotal
4. Check payment terms for early payment discount
5. Calculate early payment discount
6. Apply early payment discount
7. Calculate tax on final discounted amount
8. Calculate grand total
```

---

### Transformacija 3: Konverzija merne jedinice

**Scenario:** Konvertujte UOM fakture u standardni UOM

```
Invoice shows:
  Product: Steel Rods
  Quantity: 50
  Unit: Meters
  Unit Price: €10.00/meter
  Line Total: €500.00

Company standard UOM: Feet

Conversion:
  1 meter = 3.28084 feet

  Quantity (feet) = 50 meters × 3.28084 = 164.042 feet
  Unit Price (feet) = €10.00/meter ÷ 3.28084 = €3.05/foot

  Verification: 164.042 feet × €3.05/foot ≈ €500.00 ✅
```

**Implementacija:**
```
1. Identify invoice UOM
2. Get conversion factor to standard UOM
3. Convert quantity
4. Convert unit price
5. Verify line total remains same
6. Store both original and converted values
```

---

### Transformacija 4: Izračunavanja datuma

**Scenario:** Izračunajte uslove plaćanja i datume dospeća

```
Invoice Date: 2025-10-23
Payment Terms: NET30

Calculations:
  Due Date = Invoice Date + 30 days = 2025-11-22

  Early Payment Discount Available If:
    Payment Date ≤ Invoice Date + 10 days
    Discount End Date = 2025-11-02

  Days Until Due = Due Date - Today
    If Today = 2025-10-23: Days = 30
    If Today = 2025-11-15: Days = 7
    If Today = 2025-11-23: Days = -1 (overdue)
```

**Implementacija:**
```
1. Extract Invoice_Date
2. Extract Payment_Terms (e.g., "NET30", "NET60", "2/10 NET30")
3. Parse payment terms
4. Calculate Due_Date
5. Calculate Discount_End_Date (if applicable)
6. Calculate Days_Until_Due
7. Set Status: "Current", "Due Soon", "Overdue"
```

---

### Transformacija 5: Parsiranje i izvlačenje teksta

**Scenario:** Izvucite strukturirane podatke iz nestrukturiranog teksta

```
Original Field: "PO-2025-ABC-12345-REV2"

Extract:
  Year: "2025"
  Department: "ABC"
  PO Number: "12345"
  Revision: "2"

Method:
  Split by delimiter "-"
  Array: ["PO", "2025", "ABC", "12345", "REV2"]

  Extract:
    Year = Array[1] = "2025"
    Department = Array[2] = "ABC"
    PO_Number = Array[3] = "12345"
    Revision = Extract digits from Array[4] = "2"
```

---

## Kompletan dijagram toka rada transformacije

```
INVOICE DATA EXTRACTED
│
├─ STEP 1: LINE ITEM CALCULATIONS
│  For each line:
│    Quantity × Unit_Price = Line_Total
│  Result: Line totals calculated
│
├─ STEP 2: SUBTOTAL CALCULATION
│  SUM(All Line_Totals) = Subtotal
│  Result: €6,387.50
│
├─ STEP 3: TAX CALCULATION
│  Subtotal × Tax_Rate = Tax_Amount
│  €6,387.50 × 19% = €1,213.63
│
├─ STEP 4: GRAND TOTAL CALCULATION
│  Subtotal + Tax_Amount = Grand_Total
│  €6,387.50 + €1,213.63 = €7,601.13
│
├─ STEP 5: CURRENCY CHECK
│  │
│  ├─ Currency = EUR? YES
│  │  → Skip conversion
│  │  → Use Grand_Total as is
│  │
│  └─ Currency ≠ EUR? NO (e.g., USD)
│     │
│     ├─ Call Exchange Rate API
│     │  Get: USD → EUR rate (0.92)
│     │
│     ├─ Convert Amount
│     │  $7,601.13 × 0.92 = €6,993.04
│     │
│     └─ Store converted amount
│        Grand_Total_EUR = €6,993.04
│
├─ STEP 6: DATA ENRICHMENT
│  For each line:
│    Lookup Product_Category → GL_Account
│    Store GL_Account in line item
│  Result: All lines have GL accounts
│
├─ STEP 7: VALIDATION
│  │
│  ├─ Compare Calculated vs Invoice Total
│  │  Variance = |Calculated - Invoice| / Invoice × 100
│  │
│  ├─ Variance ≤ 1%? ✅
│  │  Set Validation_Status = "PASS"
│  │  Continue processing
│  │
│  └─ Variance > 1%? ❌
│     Set Validation_Status = "FAIL"
│     Create review task
│     Flag for manual check
│
├─ STEP 8: FORMATTING
│  │
│  ├─ Format Dates
│  │  10/23/2025 → 2025-10-23
│  │
│  ├─ Format Numbers
│  │  7601.13 → 7.601,13 (locale-specific)
│  │
│  ├─ Format Text
│  │  "abc corp" → "ABC CORP"
│  │
│  └─ Format for Export
│     All fields in ERP-compatible format
│
└─ TRANSFORMATION COMPLETE
   Document ready for next workflow step
```

---

## Šabloni za konfiguraciju

### Šablon 1: Standardna izračunavanja fakture

```json
{
  "transformations": [
    {
      "step": 1,
      "name": "Calculate Line Totals",
      "card": "ACTION_CALCULATE_FIELD",
      "formula": "{{Quantity}} * {{Unit_Price}}",
      "result_field": "Line_Total"
    },
    {
      "step": 2,
      "name": "Calculate Subtotal",
      "card": "ACTION_CALCULATE_FIELD",
      "formula": "SUM({{Line_Total}})",
      "result_field": "Calculated_Subtotal"
    },
    {
      "step": 3,
      "name": "Calculate Tax",
      "card": "ACTION_CALCULATE_FIELD",
      "formula": "{{Calculated_Subtotal}} * {{Tax_Rate}} / 100",
      "result_field": "Calculated_Tax"
    },
    {
      "step": 4,
      "name": "Calculate Total",
      "card": "ACTION_CALCULATE_FIELD",
      "formula": "{{Calculated_Subtotal}} + {{Calculated_Tax}}",
      "result_field": "Calculated_Total"
    }
  ]
}
```

---

### Šablon 2: Tok rada konverzije valute

```json
{
  "currency_conversion": {
    "check_needed": {
      "card": "CONDITION_DOC_FIELD_IS",
      "field": "Invoice_Currency",
      "operator": "NOT EQUAL TO",
      "value": "EUR"
    },
    "get_rate": {
      "card": "CALL_API",
      "endpoint": "https://api.exchangerate.com/v1/rates/{{Invoice_Currency}}",
      "method": "GET",
      "response_path": "rates.EUR"
    },
    "convert": {
      "card": "ACTION_CALCULATE_FIELD",
      "formula": "{{Amount}} * {{Exchange_Rate}}",
      "result_field": "Amount_EUR"
    },
    "store_details": {
      "original_currency": "{{Invoice_Currency}}",
      "original_amount": "{{Amount}}",
      "exchange_rate": "{{Exchange_Rate}}",
      "converted_amount": "{{Amount_EUR}}",
      "conversion_date": "{{Today}}"
    }
  }
}
```

---

## Rukovanje greškama

### Uobičajene greške transformacije

**Greška 1: Deljenje nulom**
```
Problem: Unit_Price = Total / Quantity, but Quantity = 0

Solution:
  IF Quantity = 0 OR Quantity IS NULL:
    Set Unit_Price = 0
    Flag for review
  ELSE:
    Calculate normally
```

**Greška 2: Nevažeći format broja**
```
Problem: Field contains "€1,234.56" but need number 1234.56

Solution:
  1. Remove currency symbols
  2. Remove thousand separators
  3. Convert decimal separator if needed
  4. Parse to number
  5. Validate result
```

**Greška 3: Neuspeh parsiranja datuma**
```
Problem: Date in unexpected format

Solution:
  1. Try multiple date formats
  2. If all fail: Set to null
  3. Flag for manual review
  4. Log original value
```

**Greška 4: Nedostaje faktor konverzije**
```
Problem: Unknown UOM conversion

Solution:
  1. Check conversion table
  2. If not found: Skip conversion
  3. Flag for admin to add conversion
  4. Use original values
```

---

## Lista za proveru testiranja

- [ ] Sva izračunavanja daju ispravne rezultate
- [ ] Decimalna preciznost održana
- [ ] Konverzije valuta tačne
- [ ] Izračunavanja datuma ispravna
- [ ] Transformacije teksta funkcionišu
- [ ] Null/prazne vrednosti obrađene
- [ ] Deljenje nulom sprečeno
- [ ] Formati brojeva validirani
- [ ] Pravila zaokruživanja ispravno primenjena
- [ ] Sva transformisana polja popunjena
- [ ] Validacija hvata greške
- [ ] Format za izvoz ispravan

---

## Povezani obrasci

### Obrasci koji dobro funkcionišu zajedno:

- **[API Integration Pattern](api-integration-pattern.md)** - Preuzmite kurseve razmene, podatke za obogaćivanje
- **[PO Matching Pattern](po-matching-pattern.md)** - Izračunavanja odstupanja
- **[Decision Logic Pattern](decision-logic-pattern.md)** - Rutirajte na osnovu izračunatih vrednosti
- **[Task Management Pattern](task-management-pattern.md)** - Kreirajte zadatke za neuspehe validacije

---

## Povezani vodiči

### Preduslovi
- [Field Manipulation Guide](../then/document-field/field-manipulation-guide.md) - Sve operacije nad poljima
- [Condition Cards Guide](../and/condition-cards-complete-guide.md) - Uslovi validacije
- [Call API Guide](../then/action/call-api-guide.md) - Preuzimanje eksternih podataka

### Povezane kartice
- **ACTION_CALCULATE_FIELD** - [Field Manipulation Guide](../then/document-field/field-manipulation-guide.md#calculate-field)
- **ACTION_SET_FIELD_TO_TEXT** - [Field Manipulation Guide](../then/document-field/field-manipulation-guide.md#set-field)
- **ACTION_COPY_FIELD_VALUE** - [Field Manipulation Guide](../then/document-field/field-manipulation-guide.md#copy-field)
- **CALL_API** - [Call API Guide](../then/action/call-api-guide.md)
- **CONDITION_COMPARE_TWO_DOCFIELD_VALUES** - [Condition Cards Guide](../and/condition-cards-complete-guide.md)

### Sledeći koraci
- Validirajte rezultate: [Decision Logic Pattern](decision-logic-pattern.md)
- Kreirajte zadatke za greške: [Task Management Pattern](task-management-pattern.md)
- Koristite u uparivanju PO: [PO Matching Pattern](po-matching-pattern.md)

---

**Verzija obrasca:** 1.0
**Poslednje ažuriranje:** 23. oktobar 2025.
**Težina:** Srednja
**Procenjeno vreme:** 30-45 minuta
**Stopa uspeha:** Visoka
