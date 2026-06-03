# Datentransformations-Pattern

**Pattern-Typ:** Datenverarbeitung & -manipulation
**Komplexität:** Mittel
**Geschätzte Einrichtung:** 30–45 Minuten
**Typische Anwendungsfälle:** Feldberechnungen, Datenformatierung, Währungsumrechnung, Einheitenumrechnung, Datenanreicherung

---

Dieses Pattern bauen Sie im **Workflow-Builder** (Workflow Dashboard → Workflow List → Add Workflow). Klicken Sie auf **Add Card** und öffnen Sie die Kategorie **Document Field** — sie enthält die Lese-, Schreib-, Berechnungs- und Formatierungskarten, die dieses Pattern aneinanderreiht:

<figure><img src="../../../.gitbook/assets/workflow_add_card_picker.png" alt="Add Card-Bibliothek im Workflow-Builder, nach Kategorie gruppiert"><figcaption><p>Die <strong>Add Card</strong>-Bibliothek — Karten zum Lesen/Schreiben von Feldern, zum Berechnen und Formatieren finden Sie unter der Kategorie <strong>Document Field</strong>.</p></figcaption></figure>

---

## Pattern-Überblick

Dieses Pattern zeigt, wie Sie Dokumentdaten in DocBits-Workflows transformieren, berechnen, formatieren und anreichern. Die Datentransformation ist entscheidend, um Daten für den Export vorzubereiten, Berechnungen durchzuführen, Formate zu standardisieren und Dokumente mit zusätzlichen Informationen anzureichern.

**Was dieses Pattern macht:**
1. Extrahiert Daten aus Dokumentfeldern
2. Führt Berechnungen und Transformationen durch
3. Formatiert Daten auf die erforderlichen Standards
4. Rechnet zwischen Einheiten, Währungen und Datumsangaben um
5. Reichert Dokumente mit abgeleiteten oder nachgeschlagenen Daten an
6. Validiert und bereinigt Daten

---

## Wann dieses Pattern verwenden

Verwenden Sie dieses Pattern, wenn Sie Folgendes benötigen:
- ✅ Summen, Zwischensummen, Steuern berechnen
- ✅ Währungen oder Einheiten umrechnen
- ✅ Datums-, Zahlen- und Textformate anpassen
- ✅ Werte aus bestehenden Feldern ableiten
- ✅ Daten aus externen Quellen anreichern
- ✅ Datenformate standardisieren
- ✅ Daten bereinigen und validieren
- ✅ Daten für den Export vorbereiten

**Verwenden Sie dieses Pattern nicht, wenn:**
- ❌ keine Transformation erforderlich ist
- ❌ die Daten bereits im richtigen Format vorliegen
- ❌ ein einfaches Kopieren von Feldern genügt

---

## Typen der Datentransformation

### 1. Berechnungen

**Mathematische Operationen:**
```
- Addition: Quantity + Bonus_Quantity = Total_Quantity
- Subtraction: Invoice_Total - Tax_Amount = Net_Amount
- Multiplication: Quantity × Unit_Price = Line_Total
- Division: Total_Amount / Quantity = Unit_Price
- Percentage: (Discount / Subtotal) × 100 = Discount_Percent
```

### 2. Zeichenketten-Operationen

**Textmanipulation:**
```
- Concatenation: First_Name + " " + Last_Name = Full_Name
- Uppercase: "invoice" → "INVOICE"
- Lowercase: "SUPPLIER" → "supplier"
- Substring: "INV-2025-001" → "2025" (extract year)
- Replace: "01/23/2025" → "2025-01-23"
- Trim: "  ABC Corp  " → "ABC Corp"
```

### 3. Datentyp-Konvertierung

**Typumwandlungen:**
```
- String to Number: "123.45" → 123.45
- Number to String: 123.45 → "123.45"
- Date to String: 2025-10-23 → "October 23, 2025"
- String to Date: "23.10.2025" → 2025-10-23
- Boolean to String: true → "Yes"
```

### 4. Einheitenumrechnungen

**Maßeinheiten-Umrechnungen:**
```
- Weight: kg → lbs, tons → kg
- Length: cm → inches, m → ft
- Volume: liters → gallons
- Temperature: Celsius → Fahrenheit
- Quantity: pieces → dozens, units → pallets
```

### 5. Währungsumrechnungen

**Anwendung von Wechselkursen:**
```
- USD → EUR: Amount_USD × Rate = Amount_EUR
- Multi-currency: Convert all to base currency
- Historical rates: Use rate from invoice date
```

### 6. Datumstransformationen

**Datumsoperationen:**
```
- Format change: 10/23/2025 → 2025-10-23
- Add days: Invoice_Date + 30 = Due_Date
- Calculate age: Today - Invoice_Date = Age_Days
- Extract parts: "2025-10-23" → Year: 2025, Month: 10, Day: 23
```

---

## Vollständiges Workflow-Beispiel

### Szenario: Rechnungssummenberechnung & Datenanreicherung

**Geschäftliche Anforderung:**
- Positionen aus der Rechnung extrahieren
- Positionssummen berechnen (Menge × Preis)
- Zwischensumme berechnen (Summe der Positionssummen)
- Steuerbetrag berechnen (Zwischensumme × Steuersatz)
- Gesamtsumme berechnen (Zwischensumme + Steuer)
- In EUR umrechnen, falls die Rechnung in einer anderen Währung vorliegt
- Beträge auf 2 Dezimalstellen formatieren
- Sachkonto anhand der Produktkategorie ergänzen
- Berechnungen gegen die Rechnungssumme validieren
- Bei Abweichung > 1 % markieren

**Verwendete Workflow-Karten:**
1. ACTION_CALCULATE_FIELD – Berechnungen durchführen
2. ACTION_SET_FIELD_TO_TEXT – Ergebnisse speichern
3. ACTION_COPY_FIELD_VALUE – Werte kopieren
4. CALL_API – Wechselkurse abrufen (falls nötig)
5. CONDITION_COMPARE_TWO_DOCFIELD_VALUES – Berechnungen validieren
6. ACTION_SET_FIELD_FROM_MASTER_DATA – Mit Sachkonten anreichern

---

## Schritt-für-Schritt-Umsetzung

### Schritt 1: Positionsberechnungen

**Positionssummen berechnen:**

**Karte:** ACTION_CALCULATE_FIELD

**Für jede Position:**
```
Field: Line_Total
Formula: {{TABLE_FIELD:Quantity}} * {{TABLE_FIELD:Unit_Price}}
Result Type: Number
Decimal Places: 2
```

**Beispiel:**
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

**Leitfaden-Referenz:** [Leitfaden Feldmanipulation – Berechnungen](../then/document-field/field-manipulation-guide.md#calculate-field)

---

### Schritt 2: Zwischensumme des Dokuments berechnen

**Alle Positionssummen aufsummieren:**

**Karte:** ACTION_CALCULATE_FIELD

**Konfiguration:**
```
Field: Calculated_Subtotal
Formula: SUM({{TABLE_COLUMN:Line_Total}})
Result Type: Number
Decimal Places: 2
```

**Beispiel:**
```
Line 1 Total: €5,000.00
Line 2 Total: €1,000.00
Line 3 Total: €387.50

Subtotal = 5000 + 1000 + 387.50 = €6,387.50
Store in: Calculated_Subtotal
```

---

### Schritt 3: Steuerbetrag berechnen

**Steuersatz auf die Zwischensumme anwenden:**

**Karte:** ACTION_CALCULATE_FIELD

**Konfiguration:**
```
Field: Calculated_Tax_Amount
Formula: {{Calculated_Subtotal}} * ({{Tax_Rate}} / 100)
Result Type: Number
Decimal Places: 2
```

**Beispiel:**
```
Calculated_Subtotal: €6,387.50
Tax_Rate: 19% (VAT)

Tax Amount = 6387.50 × (19 / 100)
          = 6387.50 × 0.19
          = €1,213.63

Store in: Calculated_Tax_Amount
```

---

### Schritt 4: Gesamtsumme berechnen

**Zwischensumme und Steuer addieren:**

**Karte:** ACTION_CALCULATE_FIELD

**Konfiguration:**
```
Field: Calculated_Grand_Total
Formula: {{Calculated_Subtotal}} + {{Calculated_Tax_Amount}}
Result Type: Number
Decimal Places: 2
```

**Beispiel:**
```
Calculated_Subtotal: €6,387.50
Calculated_Tax_Amount: €1,213.63

Grand Total = 6387.50 + 1213.63 = €7,601.13

Store in: Calculated_Grand_Total
```

---

### Schritt 5: Währungsumrechnung (falls nötig)

**Prüfen, ob eine Umrechnung nötig ist:**

**Karte:** CONDITION_DOC_FIELD_IS

**Konfiguration:**
```
Field: Invoice_Currency
Operator: IS NOT EQUAL TO
Value: EUR
```

**Falls eine Umrechnung nötig ist:**

**Schritt 5a: Wechselkurs abrufen**

**Karte:** CALL_API

**Konfiguration:**
```
Endpoint: https://api.exchangerate-api.com/v4/latest/{{Invoice_Currency}}
Method: GET
Response Path: rates.EUR
Store in: Exchange_Rate_To_EUR
```

**Beispiel:**
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

**Schritt 5b: Beträge umrechnen**

**Karte:** ACTION_CALCULATE_FIELD

**Konfiguration:**
```
Field: Grand_Total_EUR
Formula: {{Calculated_Grand_Total}} * {{Exchange_Rate_To_EUR}}
Result Type: Number
Decimal Places: 2
```

**Beispiel:**
```
Grand Total (USD): $7,601.13
Exchange Rate: 0.92

Grand Total (EUR) = 7601.13 × 0.92 = €6,993.04

Store in: Grand_Total_EUR
```

**Leitfaden-Referenz:** [API-Integrations-Pattern – Währungsumrechnung](api-integration-pattern.md#beispiel-1-wechselkurs-lookup)

---

### Schritt 6: Datenanreicherung – Sachkonten ergänzen

**Sachkonto anhand der Produktkategorie nachschlagen:**

**Karte:** ACTION_SET_FIELD_FROM_MASTER_DATA

**Konfiguration:**
```
Lookup Table: GL_Account_Mapping
Lookup Key: {{TABLE_FIELD:Product_Category}}
Return Field: GL_Account_Number
Store in: GL_Account
```

**Beispiel:**
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

**Leitfaden-Referenz:** [Leitfaden Feldmanipulation – Stammdaten](../then/document-field/field-manipulation-guide.md#master-data-lookup)

---

### Schritt 7: Berechnungen validieren

**Berechnete Summe mit der Rechnungssumme vergleichen:**

**Karte:** CONDITION_COMPARE_TWO_DOCFIELD_VALUES

**Konfiguration:**
```
Field 1: Calculated_Grand_Total
Field 2: Invoice_Total (from OCR)
Operator: Calculate Variance Percentage
Tolerance: 1%
```

**Berechnung:**
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

**Logik:**
```
IF Variance ≤ 1%:
  Set Validation_Status = "PASS"
  Continue processing
ELSE:
  Set Validation_Status = "FAIL"
  Create review task
  Flag for manual verification
```

**Leitfaden-Referenz:** [Leitfaden Bedingungskarten – Feldvergleich](../and/condition-cards-complete-guide.md#field-comparison)

---

### Schritt 8: Daten für den Export formatieren

**Formate standardisieren:**

**Karte:** ACTION_SET_FIELD_TO_TEXT

**Datumsformatierung:**
```
Field: Invoice_Date_Formatted
Value: FORMATDATE({{Invoice_Date}}, "YYYY-MM-DD")
Example: 10/23/2025 → 2025-10-23
```

**Zahlenformatierung:**
```
Field: Amount_Formatted
Value: FORMATNUMBER({{Grand_Total_EUR}}, 2, ",", ".")
Example: 7601.13 → 7.601,13 (German format)
```

**Textformatierung:**
```
Field: Supplier_Name_Upper
Value: UPPERCASE({{Supplier_Name}})
Example: "ABC Corporation" → "ABC CORPORATION"
```

---

## Erweiterte Transformationen

### Transformation 1: Mehrstufige Steuerberechnung

**Szenario:** Unterschiedliche Steuersätze pro Position

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

**Umsetzung:**
```
For each line:
  1. Get product tax category
  2. Lookup applicable tax rate
  3. Calculate: Line_Net × Tax_Rate = Line_Tax
  4. Sum all Line_Tax values = Total_Tax
```

---

### Transformation 2: Rabattberechnungen

**Szenario:** Mengenrabatt und Skonto anwenden

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

**Umsetzung:**
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

### Transformation 3: Umrechnung der Mengeneinheit

**Szenario:** Rechnungs-Mengeneinheit in die Standard-Einheit umrechnen

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

**Umsetzung:**
```
1. Identify invoice UOM
2. Get conversion factor to standard UOM
3. Convert quantity
4. Convert unit price
5. Verify line total remains same
6. Store both original and converted values
```

---

### Transformation 4: Datumsberechnungen

**Szenario:** Zahlungsbedingungen und Fälligkeitsdaten berechnen

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

**Umsetzung:**
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

### Transformation 5: Textanalyse & -extraktion

**Szenario:** Strukturierte Daten aus unstrukturiertem Text extrahieren

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

## Vollständiges Transformations-Workflow-Diagramm

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

## Konfigurationsvorlagen

### Vorlage 1: Standard-Rechnungsberechnungen

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

### Vorlage 2: Workflow zur Währungsumrechnung

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

## Fehlerbehandlung

### Häufige Transformationsfehler

**Fehler 1: Division durch Null**
```
Problem: Unit_Price = Total / Quantity, but Quantity = 0

Solution:
  IF Quantity = 0 OR Quantity IS NULL:
    Set Unit_Price = 0
    Flag for review
  ELSE:
    Calculate normally
```

**Fehler 2: Ungültiges Zahlenformat**
```
Problem: Field contains "€1,234.56" but need number 1234.56

Solution:
  1. Remove currency symbols
  2. Remove thousand separators
  3. Convert decimal separator if needed
  4. Parse to number
  5. Validate result
```

**Fehler 3: Datums-Parsing fehlgeschlagen**
```
Problem: Date in unexpected format

Solution:
  1. Try multiple date formats
  2. If all fail: Set to null
  3. Flag for manual review
  4. Log original value
```

**Fehler 4: Fehlender Umrechnungsfaktor**
```
Problem: Unknown UOM conversion

Solution:
  1. Check conversion table
  2. If not found: Skip conversion
  3. Flag for admin to add conversion
  4. Use original values
```

---

## Test-Checkliste

- [ ] Alle Berechnungen liefern korrekte Ergebnisse
- [ ] Dezimalgenauigkeit bleibt erhalten
- [ ] Währungsumrechnungen korrekt
- [ ] Datumsberechnungen korrekt
- [ ] Texttransformationen funktionieren
- [ ] Null-/Leerwerte behandelt
- [ ] Division durch Null verhindert
- [ ] Zahlenformate validiert
- [ ] Rundungsregeln korrekt angewendet
- [ ] Alle transformierten Felder befüllt
- [ ] Validierung erkennt Fehler
- [ ] Exportformat korrekt

---

## Verwandte Patterns

### Patterns, die gut zusammenpassen:

- **[API-Integrations-Pattern](api-integration-pattern.md)** – Wechselkurse und Anreicherungsdaten abrufen
- **[PO-Matching-Pattern](po-matching-pattern.md)** – Abweichungsberechnungen
- **[Entscheidungslogik-Pattern](decision-logic-pattern.md)** – Anhand berechneter Werte routen
- **[Aufgabenverwaltungs-Pattern](task-management-pattern.md)** – Aufgaben bei Validierungsfehlern erstellen

---

## Verwandte Leitfäden

### Voraussetzungen
- [Leitfaden Feldmanipulation](../then/document-field/field-manipulation-guide.md) – Alle Feldoperationen
- [Leitfaden Bedingungskarten](../and/condition-cards-complete-guide.md) – Validierungsbedingungen
- [Call API-Leitfaden](../then/action/call-api-guide.md) – Externe Datenabfrage

### Verwandte Karten
- **ACTION_CALCULATE_FIELD** – [Leitfaden Feldmanipulation](../then/document-field/field-manipulation-guide.md#calculate-field)
- **ACTION_SET_FIELD_TO_TEXT** – [Leitfaden Feldmanipulation](../then/document-field/field-manipulation-guide.md#set-field)
- **ACTION_COPY_FIELD_VALUE** – [Leitfaden Feldmanipulation](../then/document-field/field-manipulation-guide.md#copy-field)
- **CALL_API** – [Call API-Leitfaden](../then/action/call-api-guide.md)
- **CONDITION_COMPARE_TWO_DOCFIELD_VALUES** – [Leitfaden Bedingungskarten](../and/condition-cards-complete-guide.md)

### Nächste Schritte
- Ergebnisse validieren: [Entscheidungslogik-Pattern](decision-logic-pattern.md)
- Aufgaben für Fehler erstellen: [Aufgabenverwaltungs-Pattern](task-management-pattern.md)
- In PO-Matching verwenden: [PO-Matching-Pattern](po-matching-pattern.md)

---

**Pattern-Version:** 1.0
**Zuletzt aktualisiert:** 23. Oktober 2025
**Schwierigkeit:** Mittel
**Geschätzte Zeit:** 30–45 Minuten
**Erfolgsquote:** Hoch
