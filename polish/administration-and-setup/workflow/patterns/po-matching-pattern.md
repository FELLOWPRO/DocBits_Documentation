# Wzorzec dopasowania zamówień (PO Matching)

**Typ wzorca:** Walidacja i porównanie
**Złożoność:** Średnia-Wysoka
**Szacowana konfiguracja:** 60–90 minut
**Typowe przypadki użycia:** Dopasowanie trójstronne, walidacja faktur, sprawdzanie odchyleń, zarządzanie tolerancjami

---

Ten wzorzec budujesz w **Workflow Builder** (Workflow Dashboard → Workflow List → Add Workflow). Kliknij **Add Card** i otwórz kategorię **Compare with Purchase Order** — zawiera ona wszystkie karty dopasowania używane przez ten wzorzec (karty porównania cen, ilości, tolerancji i pozycji):

<figure><img src="../../../.gitbook/assets/workflow_add_card_picker.png" alt="Biblioteka Add Card z kartami Compare with Purchase Order"><figcaption><p>Kategoria <strong>Compare with Purchase Order</strong> — karty dopasowania cen, ilości, tolerancji i pozycji, używane w całym tym wzorcu.</p></figcaption></figure>

---

## Przegląd wzorca

Ten wzorzec pokazuje, jak wdrożyć kompleksowe workflow dopasowania zamówień zakupu (PO Matching) w DocBits. Dopasowanie zamówień zakupu to krytyczny proces kontrolny, który porównuje dane faktury z danymi zamówienia, aby wykryć odchylenia przed zatwierdzeniem płatności.

**Co robi ten wzorzec:**
1. Pobiera dane zamówienia na podstawie numeru PO z faktury
2. Porównuje pozycje faktury z pozycjami zamówienia
3. Oblicza odchylenia (cena, ilość, sumy)
4. Stosuje reguły tolerancji
5. Routuje na podstawie wyników dopasowania do zatwierdzenia lub eskalacji
6. Śledzi historię dopasowań i wyjątki

---

## Kiedy stosować ten wzorzec

Stosuj ten wzorzec, gdy potrzebujesz:
- ✅ Walidować faktury względem zamówień zakupu
- ✅ Wykrywać błędy cenowe przed płatnością
- ✅ Identyfikować odchylenia ilościowe
- ✅ Egzekwować kontrole zakupowe
- ✅ Zapobiegać podwójnym płatnościom
- ✅ Automatyzować dopasowanie trójstronne
- ✅ Ograniczać nakład ręcznego przeglądu faktur

**Nie stosuj tego wzorca, gdy:**
- ❌ nie istnieje zamówienie powiązane z fakturą (faktury bez PO)
- ❌ dane zamówienia nie są dostępne w DocBits
- ❌ przegląd ręczny jest preferowany zamiast automatyzacji
- ❌ dopasowanie zamówień nie jest wymagane przez politykę biznesową

---

## Zrozumienie dopasowania zamówień

### Dopasowanie trójstronne

**Klasyczna kontrola zakupowa:**
```
Purchase Order (PO)  →  Created when ordering
        ↓
Goods Receipt (GR)   →  Created when receiving
        ↓
Invoice              →  Created by supplier

THREE-WAY MATCH = PO + GR + Invoice all match
```

**Wdrożenie w DocBits (dopasowanie dwustronne):**
```
Purchase Order (PO)  →  Imported to DocBits
        ↓
Invoice              →  Scanned by DocBits
        ↓
COMPARISON           →  Invoice vs PO validation
```

---

## Formuły obliczania odchyleń

### Odchylenie ceny jednostkowej

**Formuła:**
```
Variance % = |(Invoice Unit Price - PO Unit Price)| / PO Unit Price × 100
```

**Przykład:**
```
PO Unit Price:       €100.00
Invoice Unit Price:  €103.00

Variance = |103 - 100| / 100 × 100
        = 3 / 100 × 100
        = 3%

Tolerance: 5%
Result: 3% ≤ 5% → PASS ✅
```

---

### Odchylenie ilości

**Formuła:**
```
Variance % = |(Invoice Quantity - PO Quantity)| / PO Quantity × 100
```

**Przykład:**
```
PO Quantity:        100 units
Invoice Quantity:   98 units

Variance = |98 - 100| / 100 × 100
        = 2 / 100 × 100
        = 2%

Tolerance: 10%
Result: 2% ≤ 10% → PASS ✅
```

---

### Odchylenie kwoty całkowitej

**Formuła:**
```
Variance % = |(Invoice Total - PO Total)| / PO Total × 100
```

**Przykład:**
```
PO Total:       €10,000.00
Invoice Total:  €10,450.00

Variance = |10450 - 10000| / 10000 × 100
        = 450 / 10000 × 100
        = 4.5%

Tolerance: 5%
Result: 4.5% ≤ 5% → PASS ✅
```

---

## Kompletny przykład workflow

### Scenariusz: Walidacja faktur z routingiem opartym na tolerancji

**Wymaganie biznesowe:**
- Wszystkie faktury z referencją PO muszą zostać zwalidowane
- Tolerancja odchylenia ceny: 5%
- Tolerancja odchylenia ilości: 10%
- Tolerancja odchylenia kwoty całkowitej: 3%
- W granicach tolerancji: Zatwierdzaj automatycznie
- Poza tolerancją: Utwórz zadanie przeglądu
- Brak zamówienia: Eskaluj do zakupów

**Użyte karty workflow:**
1. CONDITION_DOC_FIELD_EXISTS – Sprawdź, czy numer PO jest obecny
2. PURCHASE_ORDER_FULL_MATCH – Spróbuj pełnego dopasowania
3. CONDITION_DOC_TO_PO_UNIT_PRICE – Sprawdź odchylenie ceny
4. CONDITION_DOC_TO_PO_QUANTITY – Sprawdź odchylenie ilości
5. CONDITION_DOC_TO_PO_TAX_LINES – Sprawdź dopasowanie podatku
6. ACTION_SET_FIELD_TO_TEXT – Zapisz wyniki dopasowania
7. tasks_create – Utwórz zadania przeglądu
8. ACTION_SEND_EMAIL_TO_GROUPS – Wyślij powiadomienia

---

## Wdrożenie krok po kroku

### Krok 1: Sprawdź referencję PO

**Karta:** CONDITION_DOC_FIELD_EXISTS lub CONDITION_DOC_FIELD_CONTAINS

**Konfiguracja:**
```
Field: PO_Number
Operator: IS NOT EMPTY
```

**Logika:**
```
IF PO_Number exists:
  → Continue to PO matching
ELSE:
  → Route to "Non-PO Invoice" workflow
  → Create manual review task
  → Skip PO matching
```

**Referencja przewodnika:** [Przewodnik po kartach warunków](../and/condition-cards-complete-guide.md)

---

### Krok 2: Pobierz dane zamówienia

**Automatycznie w DocBits:**
- System wyszukuje zamówienie na podstawie pola PO_Number
- Pobiera pozycje zamówienia
- Udostępnia dane do porównania

**Konfiguracja ręczna (w razie potrzeby):**
```
PO Source: DocBits Master Data
PO Lookup Field: PO_Number
Match Type: Exact Match
Include Closed POs: No (or Yes if policy allows)
```

---

### Krok 3: Sprawdź pełne dopasowanie

**Karta:** PURCHASE_ORDER_FULL_MATCH

**Cel:** Szybkie sprawdzenie, czy wszystko idealnie się zgadza

**Konfiguracja:**
```
Match Level: Full Match
Include: All line items, prices, quantities, totals
Tolerance: None (exact match)
```

**Logika:**
```
IF Full Match = TRUE:
  → Set "PO_Match_Status" = "FULL MATCH"
  → Auto-approve document
  → Skip detailed checks
  → END ✅

IF Full Match = FALSE:
  → Continue to detailed variance checks
  → Identify specific variances
```

**Wynik:**
- **TRUE**: Idealna zgodność, automatyczne zatwierdzenie
- **FALSE**: Kontynuuj ze szczegółowymi sprawdzeniami

---

### Krok 4: Sprawdź odchylenie ceny jednostkowej

**Karta:** CONDITION_DOC_TO_PO_UNIT_PRICE (zalecana v5)

**Konfiguracja:**
```
Comparison Mode: Percentage Variance
Tolerance: 5%
Operator: Variance is Less Than or Equal To
Apply To: All line items
```

**Krok po kroku:**
```
For each line item:
  1. Get Invoice Unit Price
  2. Get PO Unit Price (matched by product code)
  3. Calculate: Variance % = |Invoice - PO| / PO × 100
  4. Check: Variance % ≤ 5%?
  5. Store result
```

**Przykładowe obliczenie:**
```
Line Item 1:
  Product: ABC123
  Invoice Price: €52.00
  PO Price: €50.00
  Variance = |52-50|/50 × 100 = 4%
  Tolerance: 5%
  Result: PASS ✅

Line Item 2:
  Product: XYZ789
  Invoice Price: €120.00
  PO Price: €100.00
  Variance = |120-100|/100 × 100 = 20%
  Tolerance: 5%
  Result: FAIL ❌

Overall Result: FAIL (one or more items failed)
```

**Referencja przewodnika:** [Kompletny przewodnik PO Matching – cena jednostkowa](../and/compare-with-purchase-order/po-matching-complete-guide.md#unit-price-comparison)

---

### Krok 5: Sprawdź odchylenie ilości

**Karta:** CONDITION_DOC_TO_PO_QUANTITY

**Konfiguracja:**
```
Comparison Mode: Percentage Variance
Tolerance: 10%
Operator: Variance is Less Than or Equal To
Apply To: All line items
Allow Under-Delivery: Yes (within tolerance)
Allow Over-Delivery: No (strict)
```

**Logika:**
```
For each line item:
  1. Get Invoice Quantity
  2. Get PO Quantity
  3. Calculate: Variance % = |Invoice - PO| / PO × 100
  4. Check: Variance % ≤ 10%?
  5. Special rules:
     - Under-delivery: Allow within tolerance
     - Over-delivery: Reject (or apply stricter tolerance)
```

**Przykład:**
```
Line Item 1:
  Product: ABC123
  Invoice Qty: 98 units
  PO Qty: 100 units
  Variance = |98-100|/100 × 100 = 2%
  Under-delivery: 2% (within 10% tolerance)
  Result: PASS ✅

Line Item 2:
  Product: XYZ789
  Invoice Qty: 115 units
  PO Qty: 100 units
  Variance = |115-100|/100 × 100 = 15%
  Over-delivery: 15% (exceeds 10% tolerance)
  Result: FAIL ❌ (Escalate)
```

**Referencja przewodnika:** [Kompletny przewodnik PO Matching – ilość](../and/compare-with-purchase-order/po-matching-complete-guide.md#quantity-comparison)

---

### Krok 6: Sprawdź dopasowanie wierszy podatkowych

**Karta:** CONDITION_DOC_TO_PO_TAX_LINES

**Konfiguracja:**
```
Match Tax Codes: Yes
Match Tax Rates: Yes
Match Tax Amounts: With 1% tolerance
Tax Calculation: Verify recalculation
```

**Walidacja:**
```
1. Check tax codes match (e.g., "VAT19" on both)
2. Check tax rates match (19% on both)
3. Verify tax amount calculation:
   Tax Amount = Net Amount × Tax Rate
4. Allow small rounding differences
```

**Przykład:**
```
Invoice:
  Net Amount: €100.00
  Tax Rate: 19%
  Tax Amount: €19.00
  Total: €119.00

PO:
  Net Amount: €100.00
  Tax Rate: 19%
  Tax Amount: €19.00
  Total: €119.00

Result: Tax alignment PASS ✅
```

---

### Krok 7: Zapisz wyniki dopasowania

**Karta:** ACTION_SET_FIELD_TO_TEXT (wielokrotnie)

**Konfiguracja:**

**Pole 1: PO_Match_Status**
```
Field: PO_Match_Status
Value: {{CALCULATED}}
Options: "FULL MATCH" | "WITHIN TOLERANCE" | "OUT OF TOLERANCE" | "NO MATCH"
```

**Pole 2: Price_Variance_Percent**
```
Field: Price_Variance_Percent
Value: {{CALCULATED_PRICE_VARIANCE}}
Format: "4.5%" (example)
```

**Pole 3: Quantity_Variance_Percent**
```
Field: Quantity_Variance_Percent
Value: {{CALCULATED_QUANTITY_VARIANCE}}
Format: "2.0%" (example)
```

**Pole 4: Match_Details**
```
Field: Match_Details
Value: "Price Variance: 4.5% (within 5% tolerance)\nQuantity Variance: 2.0% (within 10% tolerance)\nTotal: PASS"
```

**Referencja przewodnika:** [Przewodnik po manipulacji polami](../then/document-field/field-manipulation-guide.md)

---

### Krok 8: Routuj na podstawie wyników dopasowania

**Scenariusz A: Idealna zgodność (pełne dopasowanie)**
```
IF PO_Match_Status = "FULL MATCH":
  1. Set Approval_Status = "AUTO APPROVED"
  2. Set Match_Type = "FULL"
  3. ACTION_APPROVE_DOCUMENT
  4. Export to ERP
  5. Send confirmation email
  → END ✅
```

**Scenariusz B: W granicach tolerancji**
```
IF PO_Match_Status = "WITHIN TOLERANCE":
  1. Set Approval_Status = "AUTO APPROVED"
  2. Set Match_Type = "TOLERANCE"
  3. Log variance details
  4. ACTION_APPROVE_DOCUMENT
  5. Export to ERP
  → END ✅
```

**Scenariusz C: Poza tolerancją (niewielkie)**
```
IF Variance < 15% (minor exceptions):
  1. Set Match_Status = "REVIEW REQUIRED"
  2. Create Task: "Review PO Variance"
     - Assign to: Accounts Payable Officer
     - Priority: Medium
     - Deadline: 3 days
  3. Send email with variance details
  4. Wait for task completion
  5. IF Approved: Continue processing
     IF Rejected: Return to supplier
```

**Scenariusz D: Poza tolerancją (znaczne)**
```
IF Variance ≥ 15% (major exceptions):
  1. Set Match_Status = "ESCALATION REQUIRED"
  2. Create Task: "URGENT: Major PO Variance"
     - Assign to: Procurement Manager
     - Priority: High
     - Deadline: 1 day
  3. Send urgent email to:
     - Procurement Manager
     - Finance Manager
     - Supplier contact
  4. Block document from processing
  5. Wait for resolution
```

**Scenariusz E: Brak zamówienia lub brak zgodności**
```
IF PO not found OR no items match:
  1. Set Match_Status = "NO MATCH"
  2. Create Task: "PO Not Found"
     - Assign to: Procurement Team
     - Priority: High
  3. Send email to procurement
  4. Block document
  5. Request PO creation or correction
```

---

## Kompletny diagram workflow

```
INVOICE ARRIVES
│
├─ CHECK: Does invoice have PO number?
│  │
│  ├─ NO PO NUMBER ❌
│  │  │
│  │  ├─ Set Match_Status = "NO PO"
│  │  ├─ Route to Non-PO workflow
│  │  └─ Create manual review task
│  │     → END (Non-PO Invoice)
│  │
│  └─ PO NUMBER EXISTS ✅
│     │
│     ├─ RETRIEVE PO DATA
│     │  - Lookup PO by PO_Number
│     │  - Get PO line items
│     │  - Get PO totals
│     │  │
│     │  ├─ PO FOUND ✅
│     │  │  │
│     │  │  ├─ STEP 1: Check Full Match
│     │  │  │  Card: PURCHASE_ORDER_FULL_MATCH
│     │  │  │  │
│     │  │  │  ├─ FULL MATCH ✅✅✅
│     │  │  │  │  │
│     │  │  │  │  ├─ Set Match_Status = "FULL MATCH"
│     │  │  │  │  ├─ Auto-Approve
│     │  │  │  │  └─ Export to ERP
│     │  │  │  │     → END (Perfect Match)
│     │  │  │  │
│     │  │  │  └─ NO FULL MATCH ⚠️
│     │  │  │     │
│     │  │  │     ├─ STEP 2: Check Unit Price Variance
│     │  │  │     │  Card: CONDITION_DOC_TO_PO_UNIT_PRICE
│     │  │  │     │  Tolerance: 5%
│     │  │  │     │  │
│     │  │  │     │  ├─ Calculate for each line:
│     │  │  │     │  │  Variance % = |Invoice-PO|/PO × 100
│     │  │  │     │  │
│     │  │  │     │  ├─ PRICE VARIANCE ≤ 5% ✅
│     │  │  │     │  │  Store variance: 3.2% (example)
│     │  │  │     │  │  Price Check: PASS
│     │  │  │     │  │
│     │  │  │     │  └─ PRICE VARIANCE > 5% ❌
│     │  │  │     │     Store variance: 12.5% (example)
│     │  │  │     │     Price Check: FAIL
│     │  │  │     │     → Flag for review
│     │  │  │     │
│     │  │  │     ├─ STEP 3: Check Quantity Variance
│     │  │  │     │  Card: CONDITION_DOC_TO_PO_QUANTITY
│     │  │  │     │  Tolerance: 10%
│     │  │  │     │  │
│     │  │  │     │  ├─ Calculate for each line:
│     │  │  │     │  │  Variance % = |Inv Qty-PO Qty|/PO Qty × 100
│     │  │  │     │  │
│     │  │  │     │  ├─ QUANTITY VARIANCE ≤ 10% ✅
│     │  │  │     │  │  Store variance: 2.0% (example)
│     │  │  │     │  │  Quantity Check: PASS
│     │  │  │     │  │
│     │  │  │     │  └─ QUANTITY VARIANCE > 10% ❌
│     │  │  │     │     Store variance: 15.0% (example)
│     │  │  │     │     Quantity Check: FAIL
│     │  │  │     │     → Flag for review
│     │  │  │     │
│     │  │  │     ├─ STEP 4: Check Tax Lines
│     │  │  │     │  Card: CONDITION_DOC_TO_PO_TAX_LINES
│     │  │  │     │  │
│     │  │  │     │  ├─ TAX ALIGNED ✅
│     │  │  │     │  │  Tax Check: PASS
│     │  │  │     │  │
│     │  │  │     │  └─ TAX MISMATCH ❌
│     │  │  │     │     Tax Check: FAIL
│     │  │  │     │     → Flag for review
│     │  │  │     │
│     │  │  │     ├─ EVALUATE RESULTS
│     │  │  │     │  │
│     │  │  │     │  ├─ ALL CHECKS PASS ✅
│     │  │  │     │  │  (Within tolerance)
│     │  │  │     │  │  │
│     │  │  │     │  │  ├─ Set Match_Status = "WITHIN TOLERANCE"
│     │  │  │     │  │  ├─ Log variance details
│     │  │  │     │  │  ├─ Auto-Approve
│     │  │  │     │  │  └─ Export to ERP
│     │  │  │     │  │     → END (Approved with Variance)
│     │  │  │     │  │
│     │  │  │     │  ├─ MINOR FAILURES (Variance < 15%) ⚠️
│     │  │  │     │  │  │
│     │  │  │     │  │  ├─ Set Match_Status = "REVIEW REQUIRED"
│     │  │  │     │  │  ├─ Create Review Task
│     │  │  │     │  │  │  - Assign to: AP Officer
│     │  │  │     │  │  │  - Priority: Medium
│     │  │  │     │  │  │  - Deadline: 3 days
│     │  │  │     │  │  ├─ Send email with details
│     │  │  │     │  │  │
│     │  │  │     │  │  └─ WAIT FOR TASK COMPLETION
│     │  │  │     │  │     │
│     │  │  │     │  │     ├─ TASK APPROVED ✅
│     │  │  │     │  │     │  Approve & Export
│     │  │  │     │  │     │  → END (Manual Approval)
│     │  │  │     │  │     │
│     │  │  │     │  │     └─ TASK REJECTED ❌
│     │  │  │     │  │        Reject & Return to Supplier
│     │  │  │     │  │        → END (Rejected)
│     │  │  │     │  │
│     │  │  │     │  └─ MAJOR FAILURES (Variance ≥ 15%) 🚨
│     │  │  │     │     │
│     │  │  │     │     ├─ Set Match_Status = "ESCALATION"
│     │  │  │     │     ├─ Create Urgent Task
│     │  │  │     │     │  - Assign to: Procurement Manager
│     │  │  │     │     │  - Priority: High
│     │  │  │     │     │  - Deadline: 1 day
│     │  │  │     │     ├─ Send urgent emails to:
│     │  │  │     │     │  * Procurement Manager
│     │  │  │     │     │  * Finance Manager
│     │  │  │     │     │  * Supplier
│     │  │  │     │     ├─ Block document processing
│     │  │  │     │     │
│     │  │  │     │     └─ WAIT FOR RESOLUTION
│     │  │  │     │        → END (Pending Escalation)
│     │  │  │     │
│     │  │  │     └─ [Variance checks complete]
│     │  │  │
│     │  │  └─ [Full match check complete]
│     │  │
│     │  └─ PO NOT FOUND ❌
│     │     │
│     │     ├─ Set Match_Status = "PO NOT FOUND"
│     │     ├─ Create Task: "Missing PO"
│     │     │  - Assign to: Procurement Team
│     │     │  - Priority: High
│     │     ├─ Send email to procurement
│     │     └─ Block document
│     │        → END (Missing PO)
│     │
│     └─ [PO retrieval complete]
│
└─ [PO check complete]
```

---

## Szablony konfiguracji

### Szablon 1: Standardowe dopasowanie zamówień (konserwatywne)

```json
{
  "full_match_check": true,
  "price_variance": {
    "enabled": true,
    "tolerance_percent": 3,
    "tolerance_type": "percentage"
  },
  "quantity_variance": {
    "enabled": true,
    "tolerance_percent": 5,
    "tolerance_type": "percentage",
    "allow_under_delivery": true,
    "allow_over_delivery": false
  },
  "tax_validation": {
    "enabled": true,
    "match_tax_codes": true,
    "match_tax_rates": true,
    "tax_amount_tolerance": 0.5
  },
  "auto_approve": {
    "full_match": true,
    "within_tolerance": true
  },
  "escalation": {
    "threshold_percent": 10,
    "assign_to": "procurement_manager"
  }
}
```

**Zastosowanie:** Ściśle kontrolowane środowisko, niska tolerancja na odchylenia

---

### Szablon 2: Elastyczne dopasowanie zamówień (liberalne)

```json
{
  "full_match_check": true,
  "price_variance": {
    "enabled": true,
    "tolerance_percent": 10,
    "tolerance_type": "percentage"
  },
  "quantity_variance": {
    "enabled": true,
    "tolerance_percent": 15,
    "tolerance_type": "percentage",
    "allow_under_delivery": true,
    "allow_over_delivery": true
  },
  "tax_validation": {
    "enabled": true,
    "match_tax_codes": false,
    "match_tax_rates": true,
    "tax_amount_tolerance": 2
  },
  "auto_approve": {
    "full_match": true,
    "within_tolerance": true
  },
  "escalation": {
    "threshold_percent": 20,
    "assign_to": "accounts_payable"
  }
}
```

**Zastosowanie:** Elastyczne środowisko, zaufani dostawcy, wyższa tolerancja

---

### Szablon 3: Wyłącznie dopasowanie cen

```json
{
  "full_match_check": false,
  "price_variance": {
    "enabled": true,
    "tolerance_percent": 5,
    "tolerance_type": "percentage"
  },
  "quantity_variance": {
    "enabled": false
  },
  "tax_validation": {
    "enabled": false
  },
  "auto_approve": {
    "full_match": false,
    "within_tolerance": true
  }
}
```

**Zastosowanie:** Gdy liczy się tylko cena, a odchylenia ilościowe są spodziewane

---

## Zaawansowane scenariusze

### Scenariusz 1: Obsługa dostaw częściowych

**Wyzwanie:** Faktura za częściową dostawę zamówienia

**Rozwiązanie:**
```
1. Allow quantity under-delivery within tolerance
2. Track cumulative invoiced quantity vs PO quantity
3. Update PO remaining quantity
4. Create field: "PO_Percentage_Invoiced"
5. When 100% invoiced: Close PO automatically
```

**Wdrożenie:**
```
IF Cumulative_Invoiced_Quantity ≤ PO_Quantity:
  Calculate: Percentage = (Cumulative/PO) × 100
  Store in: PO_Percentage_Invoiced
  IF Percentage ≥ 100:
    Set PO_Status = "FULLY INVOICED"
    Close PO
```

---

### Scenariusz 2: Dopasowanie zamówień z wieloma walutami

**Wyzwanie:** Waluta faktury różni się od waluty zamówienia

**Rozwiązanie:**
```
1. Detect currency mismatch
2. Get exchange rate (from API or master data)
3. Convert invoice amount to PO currency
4. Compare converted amounts
5. Store both original and converted amounts
```

**Wdrożenie:**
```
IF Invoice_Currency ≠ PO_Currency:
  1. Get exchange rate for Invoice_Currency → PO_Currency
  2. Convert: Invoice_Amount_Converted = Invoice_Amount × Rate
  3. Compare: Invoice_Amount_Converted vs PO_Amount
  4. Store: Original_Currency_Amount and Converted_Amount
  5. Flag: "Currency_Conversion_Applied"
```

---

### Scenariusz 3: Zamówienie ramowe / umowa ramowa

**Wyzwanie:** Wiele faktur względem jednego zamówienia

**Rozwiązanie:**
```
1. Identify PO type = "Blanket"
2. Track cumulative invoiced value
3. Check: Cumulative ≤ Blanket PO Total
4. Update remaining PO value after each invoice
5. Alert when approaching PO limit
```

**Wdrożenie:**
```
IF PO_Type = "Blanket":
  Calculate: Total_Invoiced_To_Date
  Check: Total_Invoiced_To_Date + Current_Invoice ≤ PO_Total_Value
  IF Within limit:
    Approve invoice
    Update: Remaining_PO_Value
  ELSE:
    Escalate: "Blanket PO limit exceeded"
```

---

## Obsługa błędów i przypadki szczególne

### Przypadek szczególny 1: Brakująca pozycja na fakturze

**Problem:** Faktura zawiera pozycję, której nie ma na zamówieniu

**Rozwiązanie:**
```
1. Identify unmatched line items
2. Calculate: Unmatched_Amount
3. IF Unmatched_Amount < €100 (threshold):
     Create review task (minor issue)
   ELSE:
     Escalate immediately (major issue)
4. Store unmatched item details
5. Flag: "Additional_Items_Present"
```

---

### Przypadek szczególny 2: Zamówienie zamknięte, ale faktura przychodzi

**Problem:** Zamówienie już zamknięte, otrzymano spóźnioną fakturę

**Rozwiązanie:**
```
1. Check: PO_Status = "CLOSED"
2. Check: Invoice_Date vs PO_Close_Date
3. IF Invoice within 30 days of close:
     Reopen PO temporarily
     Process invoice
     Close PO again
   ELSE:
     Create task: "Late Invoice for Closed PO"
     Assign to procurement
     Manual decision required
```

---

### Przypadek szczególny 3: Wiele zamówień na jednej fakturze

**Problem:** Faktura odwołuje się do wielu zamówień

**Rozwiązanie:**
```
1. Parse invoice for multiple PO numbers
2. For each PO:
     Retrieve PO data
     Match respective line items
3. Aggregate match results
4. Overall match = ALL individual POs must match
5. Report on each PO separately
```

---

## Wskazówki dotyczące wydajności

✅ **Najlepsze praktyki:**
- Buforuj dane zamówień, aby ograniczyć wyszukiwania
- Ustawiaj odpowiednie tolerancje (nie za ścisłe, nie za luźne)
- Najpierw sprawdzaj pełne dopasowanie (szybsze)
- Rejestruj wszystkie obliczenia odchyleń
- Przeglądaj ustawienia tolerancji co kwartał
- Monitoruj wskaźniki automatycznego zatwierdzania
- Śledź częste przyczyny odchyleń

❌ **Unikaj:**
- Zerowej tolerancji (za ścisłe, zbyt wiele przeglądów ręcznych)
- Wyjątkowo wysokiej tolerancji (podważa cel)
- Ignorowania systematycznych odchyleń
- Nieśledzenia trendów odchyleń
- Przetwarzania bez zamówienia (gdy jest wymagane)

---

## Monitorowanie i raportowanie

### Kluczowe wskaźniki

1. **Wskaźnik dopasowania:**
   - Pełne dopasowanie: X%
   - W granicach tolerancji: Y%
   - Poza tolerancją: Z%

2. **Analiza odchyleń:**
   - Średnie odchylenie ceny
   - Średnie odchylenie ilości
   - Częste przyczyny odchyleń

3. **Efektywność przetwarzania:**
   - Wskaźnik automatycznego zatwierdzania
   - Wskaźnik przeglądu ręcznego
   - Średni czas przeglądu

4. **Wydajność dostawców:**
   - Odchylenia według dostawcy
   - Wskaźnik dopasowania według dostawcy
   - Problematyczni dostawcy

---

## Lista kontrolna testów

- [ ] Scenariusz idealnej zgodności (pełne dopasowanie)
- [ ] Scenariusz w granicach tolerancji (niewielkie odchylenie)
- [ ] Scenariusz poza tolerancją (duże odchylenie)
- [ ] Scenariusz brakującego zamówienia
- [ ] Scenariusz błędnego numeru PO
- [ ] Scenariusz dostawy częściowej
- [ ] Scenariusz nadmiernej dostawy
- [ ] Scenariusz odchylenia walutowego
- [ ] Scenariusz wielu zamówień
- [ ] Scenariusz zamkniętego zamówienia
- [ ] Scenariusz odchylenia podatkowego
- [ ] Workflow eskalacji
- [ ] Tworzenie zadań
- [ ] Powiadomienia e-mail
- [ ] Aktualizacje pól
- [ ] Eksport po zatwierdzeniu

---

## Powiązane wzorce

### Wzorce, które dobrze ze sobą współgrają:

- **[Wzorzec zarządzania zadaniami](task-management-pattern.md)** – Tworzenie zadań przeglądu przy odchyleniach
- **[Wzorzec logiki decyzyjnej](decision-logic-pattern.md)** – Złożony routing na podstawie wielkości odchylenia
- **[Wzorzec integracji API](api-integration-pattern.md)** – Pobieranie aktualnych cen do porównania
- **[Wzorzec transformacji danych](data-transformation-pattern.md)** – Przeliczanie walut i jednostek

---

## Powiązane przewodniki

### Wymagania wstępne
- [Kompletny przewodnik PO Matching](../and/compare-with-purchase-order/po-matching-complete-guide.md) – Wszystkie karty dopasowania PO
- [Przewodnik po kartach warunków](../and/condition-cards-complete-guide.md) – Logika warunków
- [Przewodnik po manipulacji polami](../then/document-field/field-manipulation-guide.md) – Operacje na polach

### Powiązane karty
- **PURCHASE_ORDER_FULL_MATCH** – [Przewodnik PO Matching](../and/compare-with-purchase-order/po-matching-complete-guide.md#full-match)
- **CONDITION_DOC_TO_PO_UNIT_PRICE** – [Przewodnik PO Matching](../and/compare-with-purchase-order/po-matching-complete-guide.md#unit-price)
- **CONDITION_DOC_TO_PO_QUANTITY** – [Przewodnik PO Matching](../and/compare-with-purchase-order/po-matching-complete-guide.md#quantity)
- **CONDITION_DOC_TO_PO_TAX_LINES** – [Przewodnik PO Matching](../and/compare-with-purchase-order/po-matching-complete-guide.md#tax-lines)
- **tasks_create** – [Przewodnik po przypisywaniu zadań](../then/task/task-assignment-guide.md)

### Następne kroki
- Twórz zadania przeglądu: [Wzorzec zarządzania zadaniami](task-management-pattern.md)
- Dodaj powiadomienia e-mail: [Przewodnik po e-mailach](../then/action/send-email-groups-guide.md)
- Wdróż złożony routing: [Wzorzec logiki decyzyjnej](decision-logic-pattern.md)

---

**Wersja wzorca:** 1.0
**Ostatnia aktualizacja:** 23 października 2025
**Trudność:** Średnia-Wysoka
**Szacowany czas:** 60–90 minut
**Wskaźnik sukcesu:** Wysoki (przy poprawnej konfiguracji)
