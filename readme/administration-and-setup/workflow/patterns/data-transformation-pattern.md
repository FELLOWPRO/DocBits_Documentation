# Data Transformation Pattern

**Tipo di pattern:** Elaborazione e manipolazione dei dati
**Complessità:** Media
**Configurazione stimata:** 30-45 minuti
**Casi d'uso comuni:** Calcoli sui campi, formattazione dei dati, conversione di valuta, conversione di unità, arricchimento dei dati

---

Costruisci questo pattern nel **Workflow Builder** (Workflow Dashboard → Workflow List → Add Workflow). Clicca **Add Card** e apri la categoria **Document Field** — contiene le card di lettura, scrittura, calcolo e formattazione che questo pattern concatena:

<figure><img src="../../../.gitbook/assets/workflow_add_card_picker.png" alt="Libreria Add Card nel Workflow Builder, raggruppata per categoria"><figcaption><p>La libreria <strong>Add Card</strong> — le card di lettura/scrittura dei campi, di calcolo e di formattazione si trovano nella categoria <strong>Document Field</strong>.</p></figcaption></figure>

---

## Panoramica del pattern

Questo pattern mostra come trasformare, calcolare, formattare e arricchire i dati dei documenti nei workflow di DocBits. La trasformazione dei dati è essenziale per preparare i dati all'esportazione, eseguire calcoli, standardizzare i formati e arricchire i documenti con informazioni aggiuntive.

**Cosa fa questo pattern:**
1. Estrae i dati dai campi del documento
2. Esegue calcoli e trasformazioni
3. Formatta i dati secondo gli standard richiesti
4. Converte tra unità, valute, date
5. Arricchisce i documenti con dati derivati o da lookup
6. Valida e ripulisce i dati

---

## Quando usare questo pattern

Usa questo pattern quando devi:
- ✅ Calcolare totali, subtotali, imposte
- ✅ Convertire valute o unità di misura
- ✅ Formattare date, numeri, testo
- ✅ Derivare valori da campi esistenti
- ✅ Arricchire i dati da fonti esterne
- ✅ Standardizzare i formati dei dati
- ✅ Ripulire e validare i dati
- ✅ Preparare i dati per l'esportazione

**Non usare questo pattern quando:**
- ❌ Non è necessaria alcuna trasformazione
- ❌ I dati sono già nel formato corretto
- ❌ Una semplice copia di campo è sufficiente

---

## Tipi di trasformazione dei dati

### 1. Calcoli

**Operazioni matematiche:**
```
- Addition: Quantity + Bonus_Quantity = Total_Quantity
- Subtraction: Invoice_Total - Tax_Amount = Net_Amount
- Multiplication: Quantity × Unit_Price = Line_Total
- Division: Total_Amount / Quantity = Unit_Price
- Percentage: (Discount / Subtotal) × 100 = Discount_Percent
```

### 2. Operazioni sulle stringhe

**Manipolazione del testo:**
```
- Concatenation: First_Name + " " + Last_Name = Full_Name
- Uppercase: "invoice" → "INVOICE"
- Lowercase: "SUPPLIER" → "supplier"
- Substring: "INV-2025-001" → "2025" (extract year)
- Replace: "01/23/2025" → "2025-01-23"
- Trim: "  ABC Corp  " → "ABC Corp"
```

### 3. Conversione del tipo di dato

**Trasformazioni di tipo:**
```
- String to Number: "123.45" → 123.45
- Number to String: 123.45 → "123.45"
- Date to String: 2025-10-23 → "October 23, 2025"
- String to Date: "23.10.2025" → 2025-10-23
- Boolean to String: true → "Yes"
```

### 4. Conversioni di unità

**Conversioni di misura:**
```
- Weight: kg → lbs, tons → kg
- Length: cm → inches, m → ft
- Volume: liters → gallons
- Temperature: Celsius → Fahrenheit
- Quantity: pieces → dozens, units → pallets
```

### 5. Conversioni di valuta

**Applicazioni dei tassi di cambio:**
```
- USD → EUR: Amount_USD × Rate = Amount_EUR
- Multi-currency: Convert all to base currency
- Historical rates: Use rate from invoice date
```

### 6. Trasformazioni delle date

**Operazioni sulle date:**
```
- Format change: 10/23/2025 → 2025-10-23
- Add days: Invoice_Date + 30 = Due_Date
- Calculate age: Today - Invoice_Date = Age_Days
- Extract parts: "2025-10-23" → Year: 2025, Month: 10, Day: 23
```

---

## Esempio completo di workflow

### Scenario: Calcolo del totale della fattura e arricchimento dei dati

**Requisito aziendale:**
- Estrarre le voci di riga dalla fattura
- Calcolare i totali di riga (Qtà × Prezzo)
- Calcolare il subtotale (somma dei totali di riga)
- Calcolare l'importo dell'imposta (Subtotale × Aliquota fiscale)
- Calcolare il totale generale (Subtotale + Imposta)
- Convertire in EUR se la fattura è in un'altra valuta
- Formattare gli importi a 2 cifre decimali
- Aggiungere il conto contabile aziendale in base alla categoria del prodotto
- Validare i calcoli rispetto al totale della fattura
- Contrassegnare se la varianza > 1%

**Card di workflow utilizzate:**
1. ACTION_CALCULATE_FIELD - Esegue i calcoli
2. ACTION_SET_FIELD_TO_TEXT - Memorizza i risultati
3. ACTION_COPY_FIELD_VALUE - Copia i valori
4. CALL_API - Ottiene i tassi di cambio (se necessario)
5. CONDITION_COMPARE_TWO_DOCFIELD_VALUES - Valida i calcoli
6. ACTION_SET_FIELD_FROM_MASTER_DATA - Arricchisce con i conti contabili

---

## Implementazione passo passo

### Passo 1: Calcoli delle voci di riga

**Calcola i totali di riga:**

**Card:** ACTION_CALCULATE_FIELD

**Per ogni voce di riga:**
```
Field: Line_Total
Formula: {{TABLE_FIELD:Quantity}} * {{TABLE_FIELD:Unit_Price}}
Result Type: Number
Decimal Places: 2
```

**Esempio:**
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

**Riferimento alla guida:** [Field Manipulation Guide - Calculations](../then/document-field/field-manipulation-guide.md#calculate-field)

---

### Passo 2: Calcola il subtotale del documento

**Somma tutti i totali di riga:**

**Card:** ACTION_CALCULATE_FIELD

**Configurazione:**
```
Field: Calculated_Subtotal
Formula: SUM({{TABLE_COLUMN:Line_Total}})
Result Type: Number
Decimal Places: 2
```

**Esempio:**
```
Line 1 Total: €5,000.00
Line 2 Total: €1,000.00
Line 3 Total: €387.50

Subtotal = 5000 + 1000 + 387.50 = €6,387.50
Store in: Calculated_Subtotal
```

---

### Passo 3: Calcola l'importo dell'imposta

**Applica l'aliquota fiscale al subtotale:**

**Card:** ACTION_CALCULATE_FIELD

**Configurazione:**
```
Field: Calculated_Tax_Amount
Formula: {{Calculated_Subtotal}} * ({{Tax_Rate}} / 100)
Result Type: Number
Decimal Places: 2
```

**Esempio:**
```
Calculated_Subtotal: €6,387.50
Tax_Rate: 19% (VAT)

Tax Amount = 6387.50 × (19 / 100)
          = 6387.50 × 0.19
          = €1,213.63

Store in: Calculated_Tax_Amount
```

---

### Passo 4: Calcola il totale generale

**Somma il subtotale e l'imposta:**

**Card:** ACTION_CALCULATE_FIELD

**Configurazione:**
```
Field: Calculated_Grand_Total
Formula: {{Calculated_Subtotal}} + {{Calculated_Tax_Amount}}
Result Type: Number
Decimal Places: 2
```

**Esempio:**
```
Calculated_Subtotal: €6,387.50
Calculated_Tax_Amount: €1,213.63

Grand Total = 6387.50 + 1213.63 = €7,601.13

Store in: Calculated_Grand_Total
```

---

### Passo 5: Conversione di valuta (se necessaria)

**Verifica se è necessaria la conversione:**

**Card:** CONDITION_DOC_FIELD_IS

**Configurazione:**
```
Field: Invoice_Currency
Operator: IS NOT EQUAL TO
Value: EUR
```

**Se è necessaria la conversione:**

**Passo 5a: Ottieni il tasso di cambio**

**Card:** CALL_API

**Configurazione:**
```
Endpoint: https://api.exchangerate-api.com/v4/latest/{{Invoice_Currency}}
Method: GET
Response Path: rates.EUR
Store in: Exchange_Rate_To_EUR
```

**Esempio:**
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

**Passo 5b: Converti gli importi**

**Card:** ACTION_CALCULATE_FIELD

**Configurazione:**
```
Field: Grand_Total_EUR
Formula: {{Calculated_Grand_Total}} * {{Exchange_Rate_To_EUR}}
Result Type: Number
Decimal Places: 2
```

**Esempio:**
```
Grand Total (USD): $7,601.13
Exchange Rate: 0.92

Grand Total (EUR) = 7601.13 × 0.92 = €6,993.04

Store in: Grand_Total_EUR
```

**Riferimento alla guida:** [API Integration Pattern - Currency Conversion](api-integration-pattern.md#currency-conversion-example)

---

### Passo 6: Arricchimento dei dati - Aggiungi i conti contabili

**Cerca il conto contabile per categoria di prodotto:**

**Card:** ACTION_SET_FIELD_FROM_MASTER_DATA

**Configurazione:**
```
Lookup Table: GL_Account_Mapping
Lookup Key: {{TABLE_FIELD:Product_Category}}
Return Field: GL_Account_Number
Store in: GL_Account
```

**Esempio:**
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

**Riferimento alla guida:** [Field Manipulation Guide - Master Data](../then/document-field/field-manipulation-guide.md#master-data-lookup)

---

### Passo 7: Valida i calcoli

**Confronta il totale calcolato con il totale della fattura:**

**Card:** CONDITION_COMPARE_TWO_DOCFIELD_VALUES

**Configurazione:**
```
Field 1: Calculated_Grand_Total
Field 2: Invoice_Total (from OCR)
Operator: Calculate Variance Percentage
Tolerance: 1%
```

**Calcolo:**
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

**Logica:**
```
IF Variance ≤ 1%:
  Set Validation_Status = "PASS"
  Continue processing
ELSE:
  Set Validation_Status = "FAIL"
  Create review task
  Flag for manual verification
```

**Riferimento alla guida:** [Condition Cards Guide - Field Comparison](../and/condition-cards-complete-guide.md#field-comparison)

---

### Passo 8: Formatta i dati per l'esportazione

**Standardizza i formati:**

**Card:** ACTION_SET_FIELD_TO_TEXT

**Formattazione delle date:**
```
Field: Invoice_Date_Formatted
Value: FORMATDATE({{Invoice_Date}}, "YYYY-MM-DD")
Example: 10/23/2025 → 2025-10-23
```

**Formattazione dei numeri:**
```
Field: Amount_Formatted
Value: FORMATNUMBER({{Grand_Total_EUR}}, 2, ",", ".")
Example: 7601.13 → 7.601,13 (German format)
```

**Formattazione del testo:**
```
Field: Supplier_Name_Upper
Value: UPPERCASE({{Supplier_Name}})
Example: "ABC Corporation" → "ABC CORPORATION"
```

---

## Trasformazioni avanzate

### Trasformazione 1: Calcolo dell'imposta multi-livello

**Scenario:** Aliquote fiscali diverse per voce di riga

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

**Implementazione:**
```
For each line:
  1. Get product tax category
  2. Lookup applicable tax rate
  3. Calculate: Line_Net × Tax_Rate = Line_Tax
  4. Sum all Line_Tax values = Total_Tax
```

---

### Trasformazione 2: Calcoli degli sconti

**Scenario:** Applicare lo sconto sul volume e lo sconto per pagamento anticipato

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

**Implementazione:**
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

### Trasformazione 3: Conversione dell'unità di misura

**Scenario:** Convertire l'UOM della fattura nell'UOM standard

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

**Implementazione:**
```
1. Identify invoice UOM
2. Get conversion factor to standard UOM
3. Convert quantity
4. Convert unit price
5. Verify line total remains same
6. Store both original and converted values
```

---

### Trasformazione 4: Calcoli delle date

**Scenario:** Calcolare i termini di pagamento e le date di scadenza

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

**Implementazione:**
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

### Trasformazione 5: Analisi ed estrazione del testo

**Scenario:** Estrarre dati strutturati da testo non strutturato

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

## Diagramma completo del workflow di trasformazione

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

## Modelli di configurazione

### Modello 1: Calcoli standard della fattura

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

### Modello 2: Workflow di conversione di valuta

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

## Gestione degli errori

### Errori comuni di trasformazione

**Errore 1: Divisione per zero**
```
Problem: Unit_Price = Total / Quantity, but Quantity = 0

Solution:
  IF Quantity = 0 OR Quantity IS NULL:
    Set Unit_Price = 0
    Flag for review
  ELSE:
    Calculate normally
```

**Errore 2: Formato numerico non valido**
```
Problem: Field contains "€1,234.56" but need number 1234.56

Solution:
  1. Remove currency symbols
  2. Remove thousand separators
  3. Convert decimal separator if needed
  4. Parse to number
  5. Validate result
```

**Errore 3: Errore di analisi della data**
```
Problem: Date in unexpected format

Solution:
  1. Try multiple date formats
  2. If all fail: Set to null
  3. Flag for manual review
  4. Log original value
```

**Errore 4: Fattore di conversione mancante**
```
Problem: Unknown UOM conversion

Solution:
  1. Check conversion table
  2. If not found: Skip conversion
  3. Flag for admin to add conversion
  4. Use original values
```

---

## Checklist di test

- [ ] Tutti i calcoli producono risultati corretti
- [ ] La precisione decimale è mantenuta
- [ ] Le conversioni di valuta sono accurate
- [ ] I calcoli delle date sono corretti
- [ ] Le trasformazioni del testo funzionano
- [ ] I valori null/vuoti sono gestiti
- [ ] La divisione per zero è prevenuta
- [ ] I formati numerici sono validati
- [ ] Le regole di arrotondamento sono applicate correttamente
- [ ] Tutti i campi trasformati sono popolati
- [ ] La validazione rileva gli errori
- [ ] Il formato di esportazione è corretto

---

## Pattern correlati

### Pattern che funzionano bene insieme:

- **[API Integration Pattern](api-integration-pattern.md)** - Recupera i tassi di cambio, dati di arricchimento
- **[PO Matching Pattern](po-matching-pattern.md)** - Calcoli delle varianze
- **[Decision Logic Pattern](decision-logic-pattern.md)** - Instrada in base ai valori calcolati
- **[Task Management Pattern](task-management-pattern.md)** - Crea task per i fallimenti della validazione

---

## Guide correlate

### Prerequisiti
- [Field Manipulation Guide](../then/document-field/field-manipulation-guide.md) - Tutte le operazioni sui campi
- [Condition Cards Guide](../and/condition-cards-complete-guide.md) - Condizioni di validazione
- [Call API Guide](../then/action/call-api-guide.md) - Recupero di dati esterni

### Card correlate
- **ACTION_CALCULATE_FIELD** - [Field Manipulation Guide](../then/document-field/field-manipulation-guide.md#calculate-field)
- **ACTION_SET_FIELD_TO_TEXT** - [Field Manipulation Guide](../then/document-field/field-manipulation-guide.md#set-field)
- **ACTION_COPY_FIELD_VALUE** - [Field Manipulation Guide](../then/document-field/field-manipulation-guide.md#copy-field)
- **CALL_API** - [Call API Guide](../then/action/call-api-guide.md)
- **CONDITION_COMPARE_TWO_DOCFIELD_VALUES** - [Condition Cards Guide](../and/condition-cards-complete-guide.md)

### Prossimi passi
- Valida i risultati: [Decision Logic Pattern](decision-logic-pattern.md)
- Crea task per gli errori: [Task Management Pattern](task-management-pattern.md)
- Usa nel matching dei PO: [PO Matching Pattern](po-matching-pattern.md)

---

**Versione del pattern:** 1.0
**Ultimo aggiornamento:** 23 ottobre 2025
**Difficoltà:** Media
**Tempo stimato:** 30-45 minuti
**Tasso di successo:** Alto
