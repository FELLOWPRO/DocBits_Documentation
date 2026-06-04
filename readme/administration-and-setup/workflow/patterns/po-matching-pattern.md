# PO Matching Pattern

**Tip obrasca:** Validacija i poređenje
**Složenost:** Srednja-visoka
**Procenjeno podešavanje:** 60-90 minuta
**Uobičajeni slučajevi upotrebe:** Trostruko uparivanje, validacija faktura, provera odstupanja, upravljanje tolerancijom

---

Ovaj obrazac gradite u **Workflow Builder**-u (Workflow Dashboard → Workflow List → Add Workflow). Kliknite na **Add Card** i otvorite kategoriju **Compare with Purchase Order** — ona sadrži svaku karticu za uparivanje koju ovaj obrazac koristi (kartice za poređenje cene, količine, tolerancije i stavki):

<figure><img src="../../../.gitbook/assets/workflow_add_card_picker.png" alt="Biblioteka Add Card koja prikazuje kartice Compare with Purchase Order"><figcaption><p>Kategorija <strong>Compare with Purchase Order</strong> — kartice za uparivanje cene, količine, tolerancije i stavki koje se koriste kroz ceo ovaj obrazac.</p></figcaption></figure>

---

## Pregled obrasca

Ovaj obrazac pokazuje kako da implementirate sveobuhvatne tokove rada za uparivanje narudžbenica (PO) u DocBits-u. Uparivanje PO je kritičan kontrolni proces koji poredi podatke fakture sa podacima narudžbenice radi otkrivanja neslaganja pre odobravanja plaćanja.

**Šta ovaj obrazac radi:**
1. Preuzima PO podatke na osnovu broja PO sa fakture
2. Poredi stavke fakture sa stavkama PO
3. Izračunava odstupanja (cena, količina, ukupni iznosi)
4. Primenjuje pravila tolerancije
5. Rutira za odobravanje ili eskalaciju na osnovu rezultata uparivanja
6. Prati istoriju uparivanja i izuzetke

---

## Kada koristiti ovaj obrazac

Koristite ovaj obrazac kada treba da:
- ✅ Validirate fakture u odnosu na narudžbenice
- ✅ Otkrijete greške u cenama pre plaćanja
- ✅ Identifikujete neslaganja u količini
- ✅ Sprovedete kontrole nabavke
- ✅ Sprečite dupla plaćanja
- ✅ Automatizujete trostruko uparivanje
- ✅ Smanjite obim ručnog pregleda faktura

**Nemojte koristiti ovaj obrazac kada:**
- ❌ Ne postoji PO za fakturu (fakture bez PO)
- ❌ PO podaci nisu dostupni u DocBits-u
- ❌ Ručni pregled se preferira u odnosu na automatizaciju
- ❌ Uparivanje PO nije zahtevano poslovnom politikom

---

## Razumevanje uparivanja PO

### Trostruko uparivanje

**Tradicionalna kontrola nabavke:**
```
Purchase Order (PO)  →  Created when ordering
        ↓
Goods Receipt (GR)   →  Created when receiving
        ↓
Invoice              →  Created by supplier

THREE-WAY MATCH = PO + GR + Invoice all match
```

**DocBits implementacija (Dvostruko uparivanje):**
```
Purchase Order (PO)  →  Imported to DocBits
        ↓
Invoice              →  Scanned by DocBits
        ↓
COMPARISON           →  Invoice vs PO validation
```

---

## Formule za izračunavanje odstupanja

### Odstupanje jedinične cene

**Formula:**
```
Variance % = |(Invoice Unit Price - PO Unit Price)| / PO Unit Price × 100
```

**Primer:**
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

### Odstupanje količine

**Formula:**
```
Variance % = |(Invoice Quantity - PO Quantity)| / PO Quantity × 100
```

**Primer:**
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

### Odstupanje ukupnog iznosa

**Formula:**
```
Variance % = |(Invoice Total - PO Total)| / PO Total × 100
```

**Primer:**
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

## Kompletan primer toka rada

### Scenario: Validacija fakture sa rutiranjem zasnovanim na toleranciji

**Poslovni zahtev:**
- Sve fakture sa PO referencom moraju biti validirane
- Tolerancija odstupanja cene: 5%
- Tolerancija odstupanja količine: 10%
- Tolerancija odstupanja ukupnog iznosa: 3%
- Unutar tolerancije: Automatsko odobravanje
- Izvan tolerancije: Kreiranje zadatka pregleda
- Nedostaje PO: Eskalacija ka nabavci

**Korišćene kartice toka rada:**
1. CONDITION_DOC_FIELD_EXISTS - Provera da li je broj PO prisutan
2. PURCHASE_ORDER_FULL_MATCH - Pokušaj potpunog uparivanja
3. CONDITION_DOC_TO_PO_UNIT_PRICE - Provera odstupanja cene
4. CONDITION_DOC_TO_PO_QUANTITY - Provera odstupanja količine
5. CONDITION_DOC_TO_PO_TAX_LINES - Provera usklađenosti poreza
6. ACTION_SET_FIELD_TO_TEXT - Čuvanje rezultata uparivanja
7. tasks_create - Kreiranje zadataka pregleda
8. ACTION_SEND_EMAIL_TO_GROUPS - Slanje obaveštenja

---

## Implementacija korak po korak

### Korak 1: Proverite PO referencu

**Kartica:** CONDITION_DOC_FIELD_EXISTS ili CONDITION_DOC_FIELD_CONTAINS

**Konfiguracija:**
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

**Referenca vodiča:** [Condition Cards Guide](../and/condition-cards-complete-guide.md)

---

### Korak 2: Preuzmite PO podatke

**Automatski u DocBits-u:**
- Sistem pretražuje PO po polju PO_Number
- Preuzima stavke PO
- Čini podatke dostupnim za poređenje

**Ručna konfiguracija (ako je potrebno):**
```
PO Source: DocBits Master Data
PO Lookup Field: PO_Number
Match Type: Exact Match
Include Closed POs: No (or Yes if policy allows)
```

---

### Korak 3: Provera potpunog uparivanja PO

**Kartica:** PURCHASE_ORDER_FULL_MATCH

**Svrha:** Brza provera da li se sve savršeno poklapa

**Konfiguracija:**
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

**Rezultat:**
- **TRUE**: Savršeno poklapanje, automatsko odobravanje
- **FALSE**: Pređite na detaljne provere

---

### Korak 4: Proverite odstupanje jedinične cene

**Kartica:** CONDITION_DOC_TO_PO_UNIT_PRICE (v5 preporučeno)

**Konfiguracija:**
```
Comparison Mode: Percentage Variance
Tolerance: 5%
Operator: Variance is Less Than or Equal To
Apply To: All line items
```

**Korak po korak:**
```
For each line item:
  1. Get Invoice Unit Price
  2. Get PO Unit Price (matched by product code)
  3. Calculate: Variance % = |Invoice - PO| / PO × 100
  4. Check: Variance % ≤ 5%?
  5. Store result
```

**Primer izračunavanja:**
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

**Referenca vodiča:** [PO Matching Complete Guide - Unit Price](../and/compare-with-purchase-order/po-matching-complete-guide.md#unit-price-comparison)

---

### Korak 5: Proverite odstupanje količine

**Kartica:** CONDITION_DOC_TO_PO_QUANTITY

**Konfiguracija:**
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

**Primer:**
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

**Referenca vodiča:** [PO Matching Complete Guide - Quantity](../and/compare-with-purchase-order/po-matching-complete-guide.md#quantity-comparison)

---

### Korak 6: Proverite usklađenost poreskih stavki

**Kartica:** CONDITION_DOC_TO_PO_TAX_LINES

**Konfiguracija:**
```
Match Tax Codes: Yes
Match Tax Rates: Yes
Match Tax Amounts: With 1% tolerance
Tax Calculation: Verify recalculation
```

**Validacija:**
```
1. Check tax codes match (e.g., "VAT19" on both)
2. Check tax rates match (19% on both)
3. Verify tax amount calculation:
   Tax Amount = Net Amount × Tax Rate
4. Allow small rounding differences
```

**Primer:**
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

### Korak 7: Sačuvajte rezultate uparivanja

**Kartica:** ACTION_SET_FIELD_TO_TEXT (više instanci)

**Konfiguracija:**

**Polje 1: PO_Match_Status**
```
Field: PO_Match_Status
Value: {{CALCULATED}}
Options: "FULL MATCH" | "WITHIN TOLERANCE" | "OUT OF TOLERANCE" | "NO MATCH"
```

**Polje 2: Price_Variance_Percent**
```
Field: Price_Variance_Percent
Value: {{CALCULATED_PRICE_VARIANCE}}
Format: "4.5%" (example)
```

**Polje 3: Quantity_Variance_Percent**
```
Field: Quantity_Variance_Percent
Value: {{CALCULATED_QUANTITY_VARIANCE}}
Format: "2.0%" (example)
```

**Polje 4: Match_Details**
```
Field: Match_Details
Value: "Price Variance: 4.5% (within 5% tolerance)\nQuantity Variance: 2.0% (within 10% tolerance)\nTotal: PASS"
```

**Referenca vodiča:** [Field Manipulation Guide](../then/document-field/field-manipulation-guide.md)

---

### Korak 8: Rutirajte na osnovu rezultata uparivanja

**Scenario A: Savršeno poklapanje (Potpuno uparivanje)**
```
IF PO_Match_Status = "FULL MATCH":
  1. Set Approval_Status = "AUTO APPROVED"
  2. Set Match_Type = "FULL"
  3. ACTION_APPROVE_DOCUMENT
  4. Export to ERP
  5. Send confirmation email
  → END ✅
```

**Scenario B: Unutar tolerancije**
```
IF PO_Match_Status = "WITHIN TOLERANCE":
  1. Set Approval_Status = "AUTO APPROVED"
  2. Set Match_Type = "TOLERANCE"
  3. Log variance details
  4. ACTION_APPROVE_DOCUMENT
  5. Export to ERP
  → END ✅
```

**Scenario C: Izvan tolerancije (Manje)**
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

**Scenario D: Izvan tolerancije (Veliko)**
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

**Scenario E: Nedostaje PO ili nema poklapanja**
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

## Kompletan dijagram toka rada

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

## Šabloni za konfiguraciju

### Šablon 1: Standardno uparivanje PO (Konzervativno)

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

**Upotreba:** Okruženje stroge kontrole, niska tolerancija za odstupanje

---

### Šablon 2: Fleksibilno uparivanje PO (Tolerantno)

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

**Upotreba:** Fleksibilno okruženje, pouzdani dobavljači, viša tolerancija

---

### Šablon 3: Uparivanje samo cene

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

**Upotreba:** Kada je važna samo cena, a očekivane su varijacije u količini

---

## Napredni scenariji

### Scenario 1: Rukovanje delimičnom isporukom

**Izazov:** Faktura za delimičnu isporuku PO

**Rešenje:**
```
1. Allow quantity under-delivery within tolerance
2. Track cumulative invoiced quantity vs PO quantity
3. Update PO remaining quantity
4. Create field: "PO_Percentage_Invoiced"
5. When 100% invoiced: Close PO automatically
```

**Implementacija:**
```
IF Cumulative_Invoiced_Quantity ≤ PO_Quantity:
  Calculate: Percentage = (Cumulative/PO) × 100
  Store in: PO_Percentage_Invoiced
  IF Percentage ≥ 100:
    Set PO_Status = "FULLY INVOICED"
    Close PO
```

---

### Scenario 2: Uparivanje PO sa više valuta

**Izazov:** Valuta fakture se razlikuje od valute PO

**Rešenje:**
```
1. Detect currency mismatch
2. Get exchange rate (from API or master data)
3. Convert invoice amount to PO currency
4. Compare converted amounts
5. Store both original and converted amounts
```

**Implementacija:**
```
IF Invoice_Currency ≠ PO_Currency:
  1. Get exchange rate for Invoice_Currency → PO_Currency
  2. Convert: Invoice_Amount_Converted = Invoice_Amount × Rate
  3. Compare: Invoice_Amount_Converted vs PO_Amount
  4. Store: Original_Currency_Amount and Converted_Amount
  5. Flag: "Currency_Conversion_Applied"
```

---

### Scenario 3: Okvirni PO / Okvirni sporazum

**Izazov:** Više faktura u odnosu na jedan PO

**Rešenje:**
```
1. Identify PO type = "Blanket"
2. Track cumulative invoiced value
3. Check: Cumulative ≤ Blanket PO Total
4. Update remaining PO value after each invoice
5. Alert when approaching PO limit
```

**Implementacija:**
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

## Rukovanje greškama i granični slučajevi

### Granični slučaj 1: Nedostaje stavka na fakturi

**Problem:** Faktura ima stavku koja nije na PO

**Rešenje:**
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

### Granični slučaj 2: PO zatvoren ali faktura stiže

**Problem:** PO je već zatvoren, primljena je zakasnela faktura

**Rešenje:**
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

### Granični slučaj 3: Više PO na jednoj fakturi

**Problem:** Faktura referencira više PO

**Rešenje:**
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

## Saveti za performanse

✅ **Najbolje prakse:**
- Keširajte PO podatke da smanjite pretrage
- Postavite odgovarajuće tolerancije (ne previše stroge, ne previše tolerantne)
- Prvo koristite proveru potpunog uparivanja (brže)
- Beležite sva izračunavanja odstupanja
- Pregledajte podešavanja tolerancije kvartalno
- Pratite stope automatskog odobravanja
- Pratite uobičajene razloge odstupanja

❌ **Izbegavajte:**
- Nultu toleranciju (previše strogo, previše ručnih pregleda)
- Ekstremno visoku toleranciju (poništava svrhu)
- Ignorisanje sistematskih odstupanja
- Nepraćenje trendova odstupanja
- Obradu bez PO (kada je zahtevano)

---

## Praćenje i izveštavanje

### Ključne metrike za praćenje

1. **Stopa uparivanja:**
   - Potpuno uparivanje: X%
   - Unutar tolerancije: Y%
   - Izvan tolerancije: Z%

2. **Analiza odstupanja:**
   - Prosečno odstupanje cene
   - Prosečno odstupanje količine
   - Uobičajeni razlozi odstupanja

3. **Efikasnost obrade:**
   - Stopa automatskog odobravanja
   - Stopa ručnog pregleda
   - Prosečno vreme pregleda

4. **Performanse dobavljača:**
   - Odstupanja po dobavljaču
   - Stopa uparivanja po dobavljaču
   - Problematični dobavljači

---

## Lista za proveru testiranja

- [ ] Scenario savršenog poklapanja (potpuno uparivanje)
- [ ] Scenario unutar tolerancije (manje odstupanje)
- [ ] Scenario izvan tolerancije (veliko odstupanje)
- [ ] Scenario nedostajućeg PO
- [ ] Scenario pogrešnog broja PO
- [ ] Scenario delimične isporuke
- [ ] Scenario prekomerne isporuke
- [ ] Scenario neslaganja valute
- [ ] Scenario sa više PO
- [ ] Scenario zatvorenog PO
- [ ] Scenario odstupanja poreza
- [ ] Tok rada eskalacije
- [ ] Kreiranje zadatka
- [ ] Obaveštenja e-poštom
- [ ] Ažuriranja polja
- [ ] Izvoz nakon odobravanja

---

## Povezani obrasci

### Obrasci koji dobro funkcionišu zajedno:

- **[Task Management Pattern](task-management-pattern.md)** - Kreirajte zadatke pregleda za odstupanja
- **[Decision Logic Pattern](decision-logic-pattern.md)** - Složeno rutiranje na osnovu nivoa odstupanja
- **[API Integration Pattern](api-integration-pattern.md)** - Preuzmite trenutne cene za poređenje
- **[Data Transformation Pattern](data-transformation-pattern.md)** - Konverzija valuta, konverzija jedinica

---

## Povezani vodiči

### Preduslovi
- [PO Matching Complete Guide](../and/compare-with-purchase-order/po-matching-complete-guide.md) - Sve kartice za uparivanje PO
- [Condition Cards Guide](../and/condition-cards-complete-guide.md) - Uslovna logika
- [Field Manipulation Guide](../then/document-field/field-manipulation-guide.md) - Operacije nad poljima

### Povezane kartice
- **PURCHASE_ORDER_FULL_MATCH** - [PO Matching Guide](../and/compare-with-purchase-order/po-matching-complete-guide.md#full-match)
- **CONDITION_DOC_TO_PO_UNIT_PRICE** - [PO Matching Guide](../and/compare-with-purchase-order/po-matching-complete-guide.md#unit-price)
- **CONDITION_DOC_TO_PO_QUANTITY** - [PO Matching Guide](../and/compare-with-purchase-order/po-matching-complete-guide.md#quantity)
- **CONDITION_DOC_TO_PO_TAX_LINES** - [PO Matching Guide](../and/compare-with-purchase-order/po-matching-complete-guide.md#tax-lines)
- **tasks_create** - [Task Assignment Guide](../then/task/task-assignment-guide.md)

### Sledeći koraci
- Kreirajte zadatke pregleda: [Task Management Pattern](task-management-pattern.md)
- Dodajte obaveštenja e-poštom: [Send Email Guide](../then/action/send-email-groups-guide.md)
- Implementirajte složeno rutiranje: [Decision Logic Pattern](decision-logic-pattern.md)

---

**Verzija obrasca:** 1.0
**Poslednje ažuriranje:** 23. oktobar 2025.
**Težina:** Srednja-visoka
**Procenjeno vreme:** 60-90 minuta
**Stopa uspeha:** Visoka (kada je ispravno konfigurisano)
