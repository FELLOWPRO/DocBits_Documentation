# PO-Matching-Pattern

**Pattern-Typ:** Validierung & Vergleich
**Komplexität:** Mittel-Hoch
**Geschätzte Einrichtung:** 60–90 Minuten
**Typische Anwendungsfälle:** Drei-Wege-Abgleich, Rechnungsvalidierung, Abweichungsprüfung, Toleranzverwaltung

---

Dieses Pattern bauen Sie im **Workflow-Builder** (Workflow Dashboard → Workflow List → Add Workflow). Klicken Sie auf **Add Card** und öffnen Sie die Kategorie **Compare with Purchase Order** — sie enthält alle von diesem Pattern verwendeten Abgleichskarten (Preis-, Mengen-, Toleranz- und Positionsvergleichskarten):

<figure><img src="../../../.gitbook/assets/workflow_add_card_picker.png" alt="Add Card-Bibliothek mit den Compare with Purchase Order-Karten"><figcaption><p>Die Kategorie <strong>Compare with Purchase Order</strong> — Preis-, Mengen-, Toleranz- und Positionsabgleichskarten, die in diesem Pattern durchgängig verwendet werden.</p></figcaption></figure>

---

## Pattern-Überblick

Dieses Pattern zeigt, wie Sie umfassende Bestellabgleich-Workflows (PO Matching) in DocBits umsetzen. Der Bestellabgleich ist ein kritischer Kontrollprozess, der Rechnungsdaten mit Bestelldaten vergleicht, um Abweichungen vor der Zahlungsfreigabe zu erkennen.

**Was dieses Pattern macht:**
1. Ruft Bestelldaten anhand der PO-Nummer aus der Rechnung ab
2. Vergleicht Rechnungspositionen mit Bestellpositionen
3. Berechnet Abweichungen (Preis, Menge, Summen)
4. Wendet Toleranzregeln an
5. Leitet anhand der Abgleichsergebnisse zur Freigabe oder Eskalation weiter
6. Verfolgt Abgleichsverlauf und Ausnahmen

---

## Wann dieses Pattern verwenden

Verwenden Sie dieses Pattern, wenn Sie Folgendes benötigen:
- ✅ Rechnungen gegen Bestellungen validieren
- ✅ Preisfehler vor der Zahlung erkennen
- ✅ Mengenabweichungen identifizieren
- ✅ Beschaffungskontrollen durchsetzen
- ✅ Doppelzahlungen verhindern
- ✅ Drei-Wege-Abgleich automatisieren
- ✅ Den manuellen Prüfaufwand für Rechnungen reduzieren

**Verwenden Sie dieses Pattern nicht, wenn:**
- ❌ keine Bestellung zur Rechnung existiert (Nicht-PO-Rechnungen)
- ❌ Bestelldaten in DocBits nicht verfügbar sind
- ❌ eine manuelle Prüfung der Automatisierung vorgezogen wird
- ❌ der Bestellabgleich laut Geschäftsrichtlinie nicht erforderlich ist

---

## Den Bestellabgleich verstehen

### Der Drei-Wege-Abgleich

**Klassische Beschaffungskontrolle:**
```
Purchase Order (PO)  →  Created when ordering
        ↓
Goods Receipt (GR)   →  Created when receiving
        ↓
Invoice              →  Created by supplier

THREE-WAY MATCH = PO + GR + Invoice all match
```

**DocBits-Umsetzung (Zwei-Wege-Abgleich):**
```
Purchase Order (PO)  →  Imported to DocBits
        ↓
Invoice              →  Scanned by DocBits
        ↓
COMPARISON           →  Invoice vs PO validation
```

---

## Formeln zur Abweichungsberechnung

### Stückpreis-Abweichung

**Formel:**
```
Variance % = |(Invoice Unit Price - PO Unit Price)| / PO Unit Price × 100
```

**Beispiel:**
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

### Mengen-Abweichung

**Formel:**
```
Variance % = |(Invoice Quantity - PO Quantity)| / PO Quantity × 100
```

**Beispiel:**
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

### Gesamtbetrags-Abweichung

**Formel:**
```
Variance % = |(Invoice Total - PO Total)| / PO Total × 100
```

**Beispiel:**
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

## Vollständiges Workflow-Beispiel

### Szenario: Rechnungsvalidierung mit toleranzbasiertem Routing

**Geschäftliche Anforderung:**
- Alle Rechnungen mit PO-Referenz müssen validiert werden
- Toleranz für Preisabweichung: 5 %
- Toleranz für Mengenabweichung: 10 %
- Toleranz für Gesamtbetragsabweichung: 3 %
- Innerhalb der Toleranz: Automatisch freigeben
- Außerhalb der Toleranz: Prüfaufgabe erstellen
- Fehlende Bestellung: An den Einkauf eskalieren

**Verwendete Workflow-Karten:**
1. CONDITION_DOC_FIELD_EXISTS – Prüfen, ob die PO-Nummer vorhanden ist
2. PURCHASE_ORDER_FULL_MATCH – Vollabgleich versuchen
3. CONDITION_DOC_TO_PO_UNIT_PRICE – Preisabweichung prüfen
4. CONDITION_DOC_TO_PO_QUANTITY – Mengenabweichung prüfen
5. CONDITION_DOC_TO_PO_TAX_LINES – Steuerabgleich prüfen
6. ACTION_SET_FIELD_TO_TEXT – Abgleichsergebnisse speichern
7. tasks_create – Prüfaufgaben erstellen
8. ACTION_SEND_EMAIL_TO_GROUPS – Benachrichtigungen senden

---

## Schritt-für-Schritt-Umsetzung

### Schritt 1: Auf PO-Referenz prüfen

**Karte:** CONDITION_DOC_FIELD_EXISTS oder CONDITION_DOC_FIELD_CONTAINS

**Konfiguration:**
```
Field: PO_Number
Operator: IS NOT EMPTY
```

**Logik:**
```
IF PO_Number exists:
  → Continue to PO matching
ELSE:
  → Route to "Non-PO Invoice" workflow
  → Create manual review task
  → Skip PO matching
```

**Leitfaden-Referenz:** [Leitfaden Bedingungskarten](../and/condition-cards-complete-guide.md)

---

### Schritt 2: Bestelldaten abrufen

**Automatisch in DocBits:**
- System schlägt die Bestellung anhand des Felds PO_Number nach
- Ruft die Bestellpositionen ab
- Stellt die Daten zum Vergleich bereit

**Manuelle Konfiguration (bei Bedarf):**
```
PO Source: DocBits Master Data
PO Lookup Field: PO_Number
Match Type: Exact Match
Include Closed POs: No (or Yes if policy allows)
```

---

### Schritt 3: Vollabgleich prüfen

**Karte:** PURCHASE_ORDER_FULL_MATCH

**Zweck:** Schnelle Prüfung, ob alles perfekt übereinstimmt

**Konfiguration:**
```
Match Level: Full Match
Include: All line items, prices, quantities, totals
Tolerance: None (exact match)
```

**Logik:**
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

**Ergebnis:**
- **TRUE**: Perfekte Übereinstimmung, automatische Freigabe
- **FALSE**: Mit detaillierten Prüfungen fortfahren

---

### Schritt 4: Stückpreis-Abweichung prüfen

**Karte:** CONDITION_DOC_TO_PO_UNIT_PRICE (v5 empfohlen)

**Konfiguration:**
```
Comparison Mode: Percentage Variance
Tolerance: 5%
Operator: Variance is Less Than or Equal To
Apply To: All line items
```

**Schritt für Schritt:**
```
For each line item:
  1. Get Invoice Unit Price
  2. Get PO Unit Price (matched by product code)
  3. Calculate: Variance % = |Invoice - PO| / PO × 100
  4. Check: Variance % ≤ 5%?
  5. Store result
```

**Beispielberechnung:**
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

**Leitfaden-Referenz:** [PO-Matching-Komplettleitfaden – Stückpreis](../and/compare-with-purchase-order/po-matching-complete-guide.md#unit-price-comparison)

---

### Schritt 5: Mengen-Abweichung prüfen

**Karte:** CONDITION_DOC_TO_PO_QUANTITY

**Konfiguration:**
```
Comparison Mode: Percentage Variance
Tolerance: 10%
Operator: Variance is Less Than or Equal To
Apply To: All line items
Allow Under-Delivery: Yes (within tolerance)
Allow Over-Delivery: No (strict)
```

**Logik:**
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

**Beispiel:**
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

**Leitfaden-Referenz:** [PO-Matching-Komplettleitfaden – Menge](../and/compare-with-purchase-order/po-matching-complete-guide.md#quantity-comparison)

---

### Schritt 6: Steuerzeilen-Abgleich prüfen

**Karte:** CONDITION_DOC_TO_PO_TAX_LINES

**Konfiguration:**
```
Match Tax Codes: Yes
Match Tax Rates: Yes
Match Tax Amounts: With 1% tolerance
Tax Calculation: Verify recalculation
```

**Validierung:**
```
1. Check tax codes match (e.g., "VAT19" on both)
2. Check tax rates match (19% on both)
3. Verify tax amount calculation:
   Tax Amount = Net Amount × Tax Rate
4. Allow small rounding differences
```

**Beispiel:**
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

### Schritt 7: Abgleichsergebnisse speichern

**Karte:** ACTION_SET_FIELD_TO_TEXT (mehrfach)

**Konfiguration:**

**Feld 1: PO_Match_Status**
```
Field: PO_Match_Status
Value: {{CALCULATED}}
Options: "FULL MATCH" | "WITHIN TOLERANCE" | "OUT OF TOLERANCE" | "NO MATCH"
```

**Feld 2: Price_Variance_Percent**
```
Field: Price_Variance_Percent
Value: {{CALCULATED_PRICE_VARIANCE}}
Format: "4.5%" (example)
```

**Feld 3: Quantity_Variance_Percent**
```
Field: Quantity_Variance_Percent
Value: {{CALCULATED_QUANTITY_VARIANCE}}
Format: "2.0%" (example)
```

**Feld 4: Match_Details**
```
Field: Match_Details
Value: "Price Variance: 4.5% (within 5% tolerance)\nQuantity Variance: 2.0% (within 10% tolerance)\nTotal: PASS"
```

**Leitfaden-Referenz:** [Leitfaden Feldmanipulation](../then/document-field/field-manipulation-guide.md)

---

### Schritt 8: Anhand der Abgleichsergebnisse weiterleiten

**Szenario A: Perfekte Übereinstimmung (Vollabgleich)**
```
IF PO_Match_Status = "FULL MATCH":
  1. Set Approval_Status = "AUTO APPROVED"
  2. Set Match_Type = "FULL"
  3. ACTION_APPROVE_DOCUMENT
  4. Export to ERP
  5. Send confirmation email
  → END ✅
```

**Szenario B: Innerhalb der Toleranz**
```
IF PO_Match_Status = "WITHIN TOLERANCE":
  1. Set Approval_Status = "AUTO APPROVED"
  2. Set Match_Type = "TOLERANCE"
  3. Log variance details
  4. ACTION_APPROVE_DOCUMENT
  5. Export to ERP
  → END ✅
```

**Szenario C: Außerhalb der Toleranz (geringfügig)**
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

**Szenario D: Außerhalb der Toleranz (erheblich)**
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

**Szenario E: Fehlende Bestellung oder keine Übereinstimmung**
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

## Vollständiges Workflow-Diagramm

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

## Konfigurationsvorlagen

### Vorlage 1: Standard-Bestellabgleich (konservativ)

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

**Verwendung:** Streng kontrolliertes Umfeld, geringe Toleranz für Abweichungen

---

### Vorlage 2: Flexibler Bestellabgleich (großzügig)

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

**Verwendung:** Flexibles Umfeld, vertrauenswürdige Lieferanten, höhere Toleranz

---

### Vorlage 3: Reiner Preisabgleich

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

**Verwendung:** Wenn nur der Preis zählt und Mengenabweichungen erwartet werden

---

## Erweiterte Szenarien

### Szenario 1: Teillieferungen behandeln

**Herausforderung:** Rechnung für eine Teillieferung einer Bestellung

**Lösung:**
```
1. Allow quantity under-delivery within tolerance
2. Track cumulative invoiced quantity vs PO quantity
3. Update PO remaining quantity
4. Create field: "PO_Percentage_Invoiced"
5. When 100% invoiced: Close PO automatically
```

**Umsetzung:**
```
IF Cumulative_Invoiced_Quantity ≤ PO_Quantity:
  Calculate: Percentage = (Cumulative/PO) × 100
  Store in: PO_Percentage_Invoiced
  IF Percentage ≥ 100:
    Set PO_Status = "FULLY INVOICED"
    Close PO
```

---

### Szenario 2: Bestellabgleich mit mehreren Währungen

**Herausforderung:** Rechnungswährung weicht von der Bestellwährung ab

**Lösung:**
```
1. Detect currency mismatch
2. Get exchange rate (from API or master data)
3. Convert invoice amount to PO currency
4. Compare converted amounts
5. Store both original and converted amounts
```

**Umsetzung:**
```
IF Invoice_Currency ≠ PO_Currency:
  1. Get exchange rate for Invoice_Currency → PO_Currency
  2. Convert: Invoice_Amount_Converted = Invoice_Amount × Rate
  3. Compare: Invoice_Amount_Converted vs PO_Amount
  4. Store: Original_Currency_Amount and Converted_Amount
  5. Flag: "Currency_Conversion_Applied"
```

---

### Szenario 3: Rahmenbestellung / Rahmenvereinbarung

**Herausforderung:** Mehrere Rechnungen gegen eine einzige Bestellung

**Lösung:**
```
1. Identify PO type = "Blanket"
2. Track cumulative invoiced value
3. Check: Cumulative ≤ Blanket PO Total
4. Update remaining PO value after each invoice
5. Alert when approaching PO limit
```

**Umsetzung:**
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

## Fehlerbehandlung & Sonderfälle

### Sonderfall 1: Fehlende Position auf der Rechnung

**Problem:** Rechnung enthält eine Position, die nicht auf der Bestellung steht

**Lösung:**
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

### Sonderfall 2: Bestellung geschlossen, aber Rechnung trifft ein

**Problem:** Bestellung bereits geschlossen, verspätete Rechnung erhalten

**Lösung:**
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

### Sonderfall 3: Mehrere Bestellungen auf einer Rechnung

**Problem:** Rechnung verweist auf mehrere Bestellungen

**Lösung:**
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

## Leistungstipps

✅ **Best Practices:**
- Bestelldaten cachen, um Lookups zu reduzieren
- Angemessene Toleranzen setzen (nicht zu streng, nicht zu großzügig)
- Zuerst den Vollabgleich prüfen (schneller)
- Alle Abweichungsberechnungen protokollieren
- Toleranzeinstellungen vierteljährlich überprüfen
- Automatische Freigabequoten überwachen
- Häufige Abweichungsgründe verfolgen

❌ **Vermeiden:**
- Nulltoleranz (zu streng, zu viele manuelle Prüfungen)
- Extrem hohe Toleranz (untergräbt den Zweck)
- Systematische Abweichungen ignorieren
- Abweichungstrends nicht verfolgen
- Ohne Bestellung verarbeiten (wenn erforderlich)

---

## Überwachung & Berichterstattung

### Wichtige Kennzahlen

1. **Abgleichsquote:**
   - Vollabgleich: X %
   - Innerhalb der Toleranz: Y %
   - Außerhalb der Toleranz: Z %

2. **Abweichungsanalyse:**
   - Durchschnittliche Preisabweichung
   - Durchschnittliche Mengenabweichung
   - Häufige Abweichungsgründe

3. **Verarbeitungseffizienz:**
   - Automatische Freigabequote
   - Manuelle Prüfquote
   - Durchschnittliche Prüfzeit

4. **Lieferantenleistung:**
   - Abweichungen nach Lieferant
   - Abgleichsquote nach Lieferant
   - Problematische Lieferanten

---

## Test-Checkliste

- [ ] Szenario perfekte Übereinstimmung (Vollabgleich)
- [ ] Szenario innerhalb der Toleranz (geringe Abweichung)
- [ ] Szenario außerhalb der Toleranz (große Abweichung)
- [ ] Szenario fehlende Bestellung
- [ ] Szenario falsche PO-Nummer
- [ ] Szenario Teillieferung
- [ ] Szenario Überlieferung
- [ ] Szenario Währungsabweichung
- [ ] Szenario mehrere Bestellungen
- [ ] Szenario geschlossene Bestellung
- [ ] Szenario Steuerabweichung
- [ ] Eskalations-Workflow
- [ ] Aufgabenerstellung
- [ ] E-Mail-Benachrichtigungen
- [ ] Feldaktualisierungen
- [ ] Export nach Freigabe

---

## Verwandte Patterns

### Patterns, die gut zusammenpassen:

- **[Aufgabenverwaltungs-Pattern](task-management-pattern.md)** – Prüfaufgaben bei Abweichungen erstellen
- **[Entscheidungslogik-Pattern](decision-logic-pattern.md)** – Komplexes Routing anhand der Abweichungshöhe
- **[API-Integrations-Pattern](api-integration-pattern.md)** – Aktuelle Preise zum Vergleich abrufen
- **[Datentransformations-Pattern](data-transformation-pattern.md)** – Währungs- und Einheitenumrechnung

---

## Verwandte Leitfäden

### Voraussetzungen
- [PO-Matching-Komplettleitfaden](../and/compare-with-purchase-order/po-matching-complete-guide.md) – Alle PO-Abgleichskarten
- [Leitfaden Bedingungskarten](../and/condition-cards-complete-guide.md) – Bedingungslogik
- [Leitfaden Feldmanipulation](../then/document-field/field-manipulation-guide.md) – Feldoperationen

### Verwandte Karten
- **PURCHASE_ORDER_FULL_MATCH** – [PO-Matching-Leitfaden](../and/compare-with-purchase-order/po-matching-complete-guide.md#full-match)
- **CONDITION_DOC_TO_PO_UNIT_PRICE** – [PO-Matching-Leitfaden](../and/compare-with-purchase-order/po-matching-complete-guide.md#unit-price)
- **CONDITION_DOC_TO_PO_QUANTITY** – [PO-Matching-Leitfaden](../and/compare-with-purchase-order/po-matching-complete-guide.md#quantity)
- **CONDITION_DOC_TO_PO_TAX_LINES** – [PO-Matching-Leitfaden](../and/compare-with-purchase-order/po-matching-complete-guide.md#tax-lines)
- **tasks_create** – [Leitfaden Aufgabenzuweisung](../then/task/task-assignment-guide.md)

### Nächste Schritte
- Prüfaufgaben erstellen: [Aufgabenverwaltungs-Pattern](task-management-pattern.md)
- E-Mail-Benachrichtigungen hinzufügen: [E-Mail-Leitfaden](../then/action/send-email-groups-guide.md)
- Komplexes Routing umsetzen: [Entscheidungslogik-Pattern](decision-logic-pattern.md)

---

**Pattern-Version:** 1.0
**Zuletzt aktualisiert:** 23. Oktober 2025
**Schwierigkeit:** Mittel-Hoch
**Geschätzte Zeit:** 60–90 Minuten
**Erfolgsquote:** Hoch (bei korrekter Konfiguration)
