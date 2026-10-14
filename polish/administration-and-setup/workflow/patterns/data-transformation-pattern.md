# Wzorzec transformacji danych

**Typ wzorca:** Przetwarzanie i manipulacja danymi
**Złożoność:** Średnia
**Szacowana konfiguracja:** 30–45 minut
**Typowe przypadki użycia:** Obliczenia na polach, formatowanie danych, przeliczanie walut, przeliczanie jednostek, wzbogacanie danych

---

Ten wzorzec budujesz w **Workflow Builder** (Workflow Dashboard → Workflow List → Add Workflow). Kliknij **Add Card** i otwórz kategorię **Document Field** — zawiera ona karty odczytu, zapisu, obliczania i formatowania, które ten wzorzec łączy w łańcuch:

<figure><img src="../../../.gitbook/assets/workflow_add_card_picker.png" alt="Biblioteka Add Card w Workflow Builder, pogrupowana według kategorii"><figcaption><p>Biblioteka <strong>Add Card</strong> — karty do odczytu/zapisu pól, obliczania i formatowania znajdziesz w kategorii <strong>Document Field</strong>.</p></figcaption></figure>

---

## Przegląd wzorca

Ten wzorzec pokazuje, jak transformować, obliczać, formatować i wzbogacać dane dokumentu w workflow DocBits. Transformacja danych jest kluczowa do przygotowania danych do eksportu, wykonywania obliczeń, standaryzacji formatów i wzbogacania dokumentów o dodatkowe informacje.

**Co robi ten wzorzec:**
1. Wyodrębnia dane z pól dokumentu
2. Wykonuje obliczenia i transformacje
3. Formatuje dane zgodnie z wymaganymi standardami
4. Przelicza między jednostkami, walutami i datami
5. Wzbogaca dokumenty o dane wyprowadzone lub wyszukane
6. Waliduje i czyści dane

---

## Kiedy stosować ten wzorzec

Stosuj ten wzorzec, gdy potrzebujesz:
- ✅ Obliczać sumy, sumy częściowe, podatki
- ✅ Przeliczać waluty lub jednostki
- ✅ Formatować daty, liczby i tekst
- ✅ Wyprowadzać wartości z istniejących pól
- ✅ Wzbogacać dane ze źródeł zewnętrznych
- ✅ Standaryzować formaty danych
- ✅ Czyścić i walidować dane
- ✅ Przygotowywać dane do eksportu

**Nie stosuj tego wzorca, gdy:**
- ❌ żadna transformacja nie jest wymagana
- ❌ dane są już w prawidłowym formacie
- ❌ wystarcza proste kopiowanie pól

---

## Typy transformacji danych

### 1. Obliczenia

**Operacje matematyczne:**
```
- Addition: Quantity + Bonus_Quantity = Total_Quantity
- Subtraction: Invoice_Total - Tax_Amount = Net_Amount
- Multiplication: Quantity × Unit_Price = Line_Total
- Division: Total_Amount / Quantity = Unit_Price
- Percentage: (Discount / Subtotal) × 100 = Discount_Percent
```

### 2. Operacje na ciągach znaków

**Manipulacja tekstem:**
```
- Concatenation: First_Name + " " + Last_Name = Full_Name
- Uppercase: "invoice" → "INVOICE"
- Lowercase: "SUPPLIER" → "supplier"
- Substring: "INV-2025-001" → "2025" (extract year)
- Replace: "01/23/2025" → "2025-01-23"
- Trim: "  ABC Corp  " → "ABC Corp"
```

### 3. Konwersja typów danych

**Rzutowanie typów:**
```
- String to Number: "123.45" → 123.45
- Number to String: 123.45 → "123.45"
- Date to String: 2025-10-23 → "October 23, 2025"
- String to Date: "23.10.2025" → 2025-10-23
- Boolean to String: true → "Yes"
```

### 4. Przeliczanie jednostek

**Przeliczanie jednostek miary:**
```
- Weight: kg → lbs, tons → kg
- Length: cm → inches, m → ft
- Volume: liters → gallons
- Temperature: Celsius → Fahrenheit
- Quantity: pieces → dozens, units → pallets
```

### 5. Przeliczanie walut

**Stosowanie kursów wymiany:**
```
- USD → EUR: Amount_USD × Rate = Amount_EUR
- Multi-currency: Convert all to base currency
- Historical rates: Use rate from invoice date
```

### 6. Transformacje dat

**Operacje na datach:**
```
- Format change: 10/23/2025 → 2025-10-23
- Add days: Invoice_Date + 30 = Due_Date
- Calculate age: Today - Invoice_Date = Age_Days
- Extract parts: "2025-10-23" → Year: 2025, Month: 10, Day: 23
```

---

## Kompletny przykład workflow

### Scenariusz: Obliczenie sumy faktury i wzbogacenie danych

**Wymaganie biznesowe:**
- Wyodrębnij pozycje z faktury
- Oblicz sumy pozycji (ilość × cena)
- Oblicz sumę częściową (suma sum pozycji)
- Oblicz kwotę podatku (suma częściowa × stawka podatku)
- Oblicz sumę całkowitą (suma częściowa + podatek)
- Przelicz na EUR, jeśli faktura jest w innej walucie
- Sformatuj kwoty do 2 miejsc dziesiętnych
- Uzupełnij konto księgowe na podstawie kategorii produktu
- Zwaliduj obliczenia względem sumy faktury
- Oznacz, gdy odchylenie > 1%

**Użyte karty workflow:**
1. ACTION_CALCULATE_FIELD – Wykonaj obliczenia
2. ACTION_SET_FIELD_TO_TEXT – Zapisz wyniki
3. ACTION_COPY_FIELD_VALUE – Kopiuj wartości
4. CALL_API – Pobierz kursy wymiany (jeśli potrzebne)
5. CONDITION_COMPARE_TWO_DOCFIELD_VALUES – Zwaliduj obliczenia
6. ACTION_SET_FIELD_FROM_MASTER_DATA – Wzbogać o konta księgowe

---

## Wdrożenie krok po kroku

### Krok 1: Obliczenia pozycji

**Oblicz sumy pozycji:**

**Karta:** ACTION_CALCULATE_FIELD

**Dla każdej pozycji:**
```
Field: Line_Total
Formula: {{TABLE_FIELD:Quantity}} * {{TABLE_FIELD:Unit_Price}}
Result Type: Number
Decimal Places: 2
```

**Przykład:**
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

**Referencja przewodnika:** [Przewodnik po manipulacji polami – obliczenia](../then/document-field/field-manipulation-guide.md#calculate-field)

---

### Krok 2: Oblicz sumę częściową dokumentu

**Zsumuj wszystkie sumy pozycji:**

**Karta:** ACTION_CALCULATE_FIELD

**Konfiguracja:**
```
Field: Calculated_Subtotal
Formula: SUM({{TABLE_COLUMN:Line_Total}})
Result Type: Number
Decimal Places: 2
```

**Przykład:**
```
Line 1 Total: €5,000.00
Line 2 Total: €1,000.00
Line 3 Total: €387.50

Subtotal = 5000 + 1000 + 387.50 = €6,387.50
Store in: Calculated_Subtotal
```

---

### Krok 3: Oblicz kwotę podatku

**Zastosuj stawkę podatku do sumy częściowej:**

**Karta:** ACTION_CALCULATE_FIELD

**Konfiguracja:**
```
Field: Calculated_Tax_Amount
Formula: {{Calculated_Subtotal}} * ({{Tax_Rate}} / 100)
Result Type: Number
Decimal Places: 2
```

**Przykład:**
```
Calculated_Subtotal: €6,387.50
Tax_Rate: 19% (VAT)

Tax Amount = 6387.50 × (19 / 100)
          = 6387.50 × 0.19
          = €1,213.63

Store in: Calculated_Tax_Amount
```

---

### Krok 4: Oblicz sumę całkowitą

**Dodaj sumę częściową i podatek:**

**Karta:** ACTION_CALCULATE_FIELD

**Konfiguracja:**
```
Field: Calculated_Grand_Total
Formula: {{Calculated_Subtotal}} + {{Calculated_Tax_Amount}}
Result Type: Number
Decimal Places: 2
```

**Przykład:**
```
Calculated_Subtotal: €6,387.50
Calculated_Tax_Amount: €1,213.63

Grand Total = 6387.50 + 1213.63 = €7,601.13

Store in: Calculated_Grand_Total
```

---

### Krok 5: Przeliczanie walut (jeśli potrzebne)

**Sprawdź, czy przeliczenie jest potrzebne:**

**Karta:** CONDITION_DOC_FIELD_IS

**Konfiguracja:**
```
Field: Invoice_Currency
Operator: IS NOT EQUAL TO
Value: EUR
```

**Jeśli przeliczenie jest potrzebne:**

**Krok 5a: Pobierz kurs wymiany**

**Karta:** CALL_API

**Konfiguracja:**
```
Endpoint: https://api.exchangerate-api.com/v4/latest/{{Invoice_Currency}}
Method: GET
Response Path: rates.EUR
Store in: Exchange_Rate_To_EUR
```

**Przykład:**
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

**Krok 5b: Przelicz kwoty**

**Karta:** ACTION_CALCULATE_FIELD

**Konfiguracja:**
```
Field: Grand_Total_EUR
Formula: {{Calculated_Grand_Total}} * {{Exchange_Rate_To_EUR}}
Result Type: Number
Decimal Places: 2
```

**Przykład:**
```
Grand Total (USD): $7,601.13
Exchange Rate: 0.92

Grand Total (EUR) = 7601.13 × 0.92 = €6,993.04

Store in: Grand_Total_EUR
```

**Referencja przewodnika:** [Wzorzec integracji API – przeliczanie walut](api-integration-pattern.md#przykład-1-wyszukiwanie-kursu-wymiany)

---

### Krok 6: Wzbogacanie danych – uzupełnij konta księgowe

**Wyszukaj konto księgowe na podstawie kategorii produktu:**

**Karta:** ACTION_SET_FIELD_FROM_MASTER_DATA

**Konfiguracja:**
```
Lookup Table: GL_Account_Mapping
Lookup Key: {{TABLE_FIELD:Product_Category}}
Return Field: GL_Account_Number
Store in: GL_Account
```

**Przykład:**
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

**Referencja przewodnika:** [Przewodnik po manipulacji polami – dane podstawowe](../then/document-field/field-manipulation-guide.md#master-data-lookup)

---

### Krok 7: Zwaliduj obliczenia

**Porównaj obliczoną sumę z sumą faktury:**

**Karta:** CONDITION_COMPARE_TWO_DOCFIELD_VALUES

**Konfiguracja:**
```
Field 1: Calculated_Grand_Total
Field 2: Invoice_Total (from OCR)
Operator: Calculate Variance Percentage
Tolerance: 1%
```

**Obliczenie:**
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

**Referencja przewodnika:** [Przewodnik po kartach warunków – porównanie pól](../and/condition-cards-complete-guide.md#field-comparison)

---

### Krok 8: Sformatuj dane do eksportu

**Standaryzuj formaty:**

**Karta:** ACTION_SET_FIELD_TO_TEXT

**Formatowanie dat:**
```
Field: Invoice_Date_Formatted
Value: FORMATDATE({{Invoice_Date}}, "YYYY-MM-DD")
Example: 10/23/2025 → 2025-10-23
```

**Formatowanie liczb:**
```
Field: Amount_Formatted
Value: FORMATNUMBER({{Grand_Total_EUR}}, 2, ",", ".")
Example: 7601.13 → 7.601,13 (German format)
```

**Formatowanie tekstu:**
```
Field: Supplier_Name_Upper
Value: UPPERCASE({{Supplier_Name}})
Example: "ABC Corporation" → "ABC CORPORATION"
```

---

## Zaawansowane transformacje

### Transformacja 1: Wielopoziomowe obliczenie podatku

**Scenariusz:** Różne stawki podatku dla każdej pozycji

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

**Wdrożenie:**
```
For each line:
  1. Get product tax category
  2. Lookup applicable tax rate
  3. Calculate: Line_Net × Tax_Rate = Line_Tax
  4. Sum all Line_Tax values = Total_Tax
```

---

### Transformacja 2: Obliczenia rabatów

**Scenariusz:** Zastosowanie rabatu ilościowego i skonta

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

**Wdrożenie:**
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

### Transformacja 3: Przeliczanie jednostki miary ilości

**Scenariusz:** Przeliczenie jednostki miary ilości z faktury na jednostkę standardową

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

**Wdrożenie:**
```
1. Identify invoice UOM
2. Get conversion factor to standard UOM
3. Convert quantity
4. Convert unit price
5. Verify line total remains same
6. Store both original and converted values
```

---

### Transformacja 4: Obliczenia dat

**Scenariusz:** Obliczanie warunków płatności i terminów płatności

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

**Wdrożenie:**
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

### Transformacja 5: Analiza i ekstrakcja tekstu

**Scenariusz:** Wyodrębnianie danych strukturalnych z tekstu nieustrukturyzowanego

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

## Kompletny diagram workflow transformacji

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

## Szablony konfiguracji

### Szablon 1: Standardowe obliczenia faktury

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

### Szablon 2: Workflow przeliczania walut

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

## Obsługa błędów

### Typowe błędy transformacji

**Błąd 1: Dzielenie przez zero**
```
Problem: Unit_Price = Total / Quantity, but Quantity = 0

Solution:
  IF Quantity = 0 OR Quantity IS NULL:
    Set Unit_Price = 0
    Flag for review
  ELSE:
    Calculate normally
```

**Błąd 2: Nieprawidłowy format liczby**
```
Problem: Field contains "€1,234.56" but need number 1234.56

Solution:
  1. Remove currency symbols
  2. Remove thousand separators
  3. Convert decimal separator if needed
  4. Parse to number
  5. Validate result
```

**Błąd 3: Parsowanie daty nie powiodło się**
```
Problem: Date in unexpected format

Solution:
  1. Try multiple date formats
  2. If all fail: Set to null
  3. Flag for manual review
  4. Log original value
```

**Błąd 4: Brakujący współczynnik przeliczenia**
```
Problem: Unknown UOM conversion

Solution:
  1. Check conversion table
  2. If not found: Skip conversion
  3. Flag for admin to add conversion
  4. Use original values
```

---

## Lista kontrolna testów

- [ ] Wszystkie obliczenia dają poprawne wyniki
- [ ] Dokładność dziesiętna jest zachowana
- [ ] Przeliczenia walut poprawne
- [ ] Obliczenia dat poprawne
- [ ] Transformacje tekstu działają
- [ ] Wartości null/puste obsłużone
- [ ] Dzielenie przez zero zablokowane
- [ ] Formaty liczb zwalidowane
- [ ] Reguły zaokrąglania zastosowane poprawnie
- [ ] Wszystkie transformowane pola wypełnione
- [ ] Walidacja wykrywa błędy
- [ ] Format eksportu poprawny

---

## Powiązane wzorce

### Wzorce, które dobrze ze sobą współgrają:

- **[Wzorzec integracji API](api-integration-pattern.md)** – Pobieranie kursów wymiany i danych wzbogacających
- **[Wzorzec PO Matching](po-matching-pattern.md)** – Obliczenia odchyleń
- **[Wzorzec logiki decyzyjnej](decision-logic-pattern.md)** – Routing na podstawie obliczonych wartości
- **[Wzorzec zarządzania zadaniami](task-management-pattern.md)** – Tworzenie zadań przy błędach walidacji

---

## Powiązane przewodniki

### Wymagania wstępne
- [Przewodnik po manipulacji polami](../then/document-field/field-manipulation-guide.md) – Wszystkie operacje na polach
- [Przewodnik po kartach warunków](../and/condition-cards-complete-guide.md) – Warunki walidacji
- [Przewodnik Call API](../then/action/call-api-guide.md) – Pobieranie danych zewnętrznych

### Powiązane karty
- **ACTION_CALCULATE_FIELD** – [Przewodnik po manipulacji polami](../then/document-field/field-manipulation-guide.md#calculate-field)
- **ACTION_SET_FIELD_TO_TEXT** – [Przewodnik po manipulacji polami](../then/document-field/field-manipulation-guide.md#set-field)
- **ACTION_COPY_FIELD_VALUE** – [Przewodnik po manipulacji polami](../then/document-field/field-manipulation-guide.md#copy-field)
- **CALL_API** – [Przewodnik Call API](../then/action/call-api-guide.md)
- **CONDITION_COMPARE_TWO_DOCFIELD_VALUES** – [Przewodnik po kartach warunków](../and/condition-cards-complete-guide.md)

### Następne kroki
- Zwaliduj wyniki: [Wzorzec logiki decyzyjnej](decision-logic-pattern.md)
- Twórz zadania dla błędów: [Wzorzec zarządzania zadaniami](task-management-pattern.md)
- Wykorzystaj w PO Matching: [Wzorzec PO Matching](po-matching-pattern.md)

---

**Wersja wzorca:** 1.0
**Ostatnia aktualizacja:** 23 października 2025
**Trudność:** Średnia
**Szacowany czas:** 30–45 minut
**Wskaźnik sukcesu:** Wysoki
