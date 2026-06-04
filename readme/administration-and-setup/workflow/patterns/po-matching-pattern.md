# PO Matching Pattern

**Tipo di pattern:** Validazione e confronto
**Complessità:** Media-Alta
**Configurazione stimata:** 60-90 minuti
**Casi d'uso comuni:** Matching a tre vie, validazione delle fatture, controllo delle varianze, gestione delle tolleranze

---

Costruisci questo pattern nel **Workflow Builder** (Workflow Dashboard → Workflow List → Add Workflow). Clicca **Add Card** e apri la categoria **Compare with Purchase Order** — contiene tutte le card di matching usate da questo pattern (card di confronto di prezzo, quantità, tolleranza e voci di riga):

<figure><img src="../../../.gitbook/assets/workflow_add_card_picker.png" alt="Libreria Add Card che mostra le card Compare with Purchase Order"><figcaption><p>La categoria <strong>Compare with Purchase Order</strong> — card di matching di prezzo, quantità, tolleranza e voci di riga usate in tutto questo pattern.</p></figcaption></figure>

---

## Panoramica del pattern

Questo pattern mostra come implementare workflow completi di matching degli ordini di acquisto (PO) in DocBits. Il matching dei PO è un processo di controllo critico che confronta i dati della fattura con i dati dell'ordine di acquisto per rilevare le discrepanze prima dell'approvazione del pagamento.

**Cosa fa questo pattern:**
1. Recupera i dati del PO in base al numero di PO della fattura
2. Confronta le voci di riga della fattura con le voci di riga del PO
3. Calcola le varianze (prezzo, quantità, totali)
4. Applica le regole di tolleranza
5. Instrada per l'approvazione o l'escalation in base ai risultati del matching
6. Monitora la cronologia del matching e le eccezioni

---

## Quando usare questo pattern

Usa questo pattern quando devi:
- ✅ Validare le fatture rispetto agli ordini di acquisto
- ✅ Rilevare errori di prezzo prima del pagamento
- ✅ Identificare discrepanze nelle quantità
- ✅ Applicare controlli sugli approvvigionamenti
- ✅ Prevenire pagamenti duplicati
- ✅ Automatizzare il matching a tre vie
- ✅ Ridurre il carico di lavoro di revisione manuale delle fatture

**Non usare questo pattern quando:**
- ❌ Non esiste un PO per la fattura (fatture non-PO)
- ❌ I dati del PO non sono disponibili in DocBits
- ❌ Si preferisce la revisione manuale all'automazione
- ❌ Il matching dei PO non è richiesto dalla policy aziendale

---

## Comprendere il matching dei PO

### Il matching a tre vie

**Controllo tradizionale degli approvvigionamenti:**
```
Purchase Order (PO)  →  Created when ordering
        ↓
Goods Receipt (GR)   →  Created when receiving
        ↓
Invoice              →  Created by supplier

THREE-WAY MATCH = PO + GR + Invoice all match
```

**Implementazione DocBits (matching a due vie):**
```
Purchase Order (PO)  →  Imported to DocBits
        ↓
Invoice              →  Scanned by DocBits
        ↓
COMPARISON           →  Invoice vs PO validation
```

---

## Formule di calcolo della varianza

### Varianza del prezzo unitario

**Formula:**
```
Variance % = |(Invoice Unit Price - PO Unit Price)| / PO Unit Price × 100
```

**Esempio:**
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

### Varianza della quantità

**Formula:**
```
Variance % = |(Invoice Quantity - PO Quantity)| / PO Quantity × 100
```

**Esempio:**
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

### Varianza dell'importo totale

**Formula:**
```
Variance % = |(Invoice Total - PO Total)| / PO Total × 100
```

**Esempio:**
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

## Esempio completo di workflow

### Scenario: Validazione delle fatture con instradamento basato sulla tolleranza

**Requisito aziendale:**
- Tutte le fatture con riferimento al PO devono essere validate
- Tolleranza della varianza di prezzo: 5%
- Tolleranza della varianza di quantità: 10%
- Tolleranza della varianza dell'importo totale: 3%
- Entro la tolleranza: Approvazione automatica
- Oltre la tolleranza: Crea un task di revisione
- PO mancante: Escalation agli approvvigionamenti

**Card di workflow utilizzate:**
1. CONDITION_DOC_FIELD_EXISTS - Verifica se il numero di PO è presente
2. PURCHASE_ORDER_FULL_MATCH - Tenta il matching completo
3. CONDITION_DOC_TO_PO_UNIT_PRICE - Verifica la varianza di prezzo
4. CONDITION_DOC_TO_PO_QUANTITY - Verifica la varianza di quantità
5. CONDITION_DOC_TO_PO_TAX_LINES - Verifica l'allineamento fiscale
6. ACTION_SET_FIELD_TO_TEXT - Memorizza i risultati del matching
7. tasks_create - Crea i task di revisione
8. ACTION_SEND_EMAIL_TO_GROUPS - Invia le notifiche

---

## Implementazione passo passo

### Passo 1: Verifica il riferimento al PO

**Card:** CONDITION_DOC_FIELD_EXISTS o CONDITION_DOC_FIELD_CONTAINS

**Configurazione:**
```
Field: PO_Number
Operator: IS NOT EMPTY
```

**Logica:**
```
IF PO_Number exists:
  → Continue to PO matching
ELSE:
  → Route to "Non-PO Invoice" workflow
  → Create manual review task
  → Skip PO matching
```

**Riferimento alla guida:** [Condition Cards Guide](../and/condition-cards-complete-guide.md)

---

### Passo 2: Recupera i dati del PO

**Automatico in DocBits:**
- Il sistema cerca il PO tramite il campo PO_Number
- Recupera le voci di riga del PO
- Rende i dati disponibili per il confronto

**Configurazione manuale (se necessaria):**
```
PO Source: DocBits Master Data
PO Lookup Field: PO_Number
Match Type: Exact Match
Include Closed POs: No (or Yes if policy allows)
```

---

### Passo 3: Verifica del matching completo del PO

**Card:** PURCHASE_ORDER_FULL_MATCH

**Scopo:** Verifica rapida se tutto corrisponde perfettamente

**Configurazione:**
```
Match Level: Full Match
Include: All line items, prices, quantities, totals
Tolerance: None (exact match)
```

**Logica:**
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

**Risultato:**
- **TRUE**: Corrispondenza perfetta, approvazione automatica
- **FALSE**: Procedi con i controlli dettagliati

---

### Passo 4: Verifica la varianza del prezzo unitario

**Card:** CONDITION_DOC_TO_PO_UNIT_PRICE (v5 consigliata)

**Configurazione:**
```
Comparison Mode: Percentage Variance
Tolerance: 5%
Operator: Variance is Less Than or Equal To
Apply To: All line items
```

**Passo passo:**
```
For each line item:
  1. Get Invoice Unit Price
  2. Get PO Unit Price (matched by product code)
  3. Calculate: Variance % = |Invoice - PO| / PO × 100
  4. Check: Variance % ≤ 5%?
  5. Store result
```

**Esempio di calcolo:**
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

**Riferimento alla guida:** [PO Matching Complete Guide - Unit Price](../and/compare-with-purchase-order/po-matching-complete-guide.md#unit-price-comparison)

---

### Passo 5: Verifica la varianza della quantità

**Card:** CONDITION_DOC_TO_PO_QUANTITY

**Configurazione:**
```
Comparison Mode: Percentage Variance
Tolerance: 10%
Operator: Variance is Less Than or Equal To
Apply To: All line items
Allow Under-Delivery: Yes (within tolerance)
Allow Over-Delivery: No (strict)
```

**Logica:**
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

**Esempio:**
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

**Riferimento alla guida:** [PO Matching Complete Guide - Quantity](../and/compare-with-purchase-order/po-matching-complete-guide.md#quantity-comparison)

---

### Passo 6: Verifica l'allineamento delle righe fiscali

**Card:** CONDITION_DOC_TO_PO_TAX_LINES

**Configurazione:**
```
Match Tax Codes: Yes
Match Tax Rates: Yes
Match Tax Amounts: With 1% tolerance
Tax Calculation: Verify recalculation
```

**Validazione:**
```
1. Check tax codes match (e.g., "VAT19" on both)
2. Check tax rates match (19% on both)
3. Verify tax amount calculation:
   Tax Amount = Net Amount × Tax Rate
4. Allow small rounding differences
```

**Esempio:**
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

### Passo 7: Memorizza i risultati del matching

**Card:** ACTION_SET_FIELD_TO_TEXT (istanze multiple)

**Configurazione:**

**Campo 1: PO_Match_Status**
```
Field: PO_Match_Status
Value: {{CALCULATED}}
Options: "FULL MATCH" | "WITHIN TOLERANCE" | "OUT OF TOLERANCE" | "NO MATCH"
```

**Campo 2: Price_Variance_Percent**
```
Field: Price_Variance_Percent
Value: {{CALCULATED_PRICE_VARIANCE}}
Format: "4.5%" (example)
```

**Campo 3: Quantity_Variance_Percent**
```
Field: Quantity_Variance_Percent
Value: {{CALCULATED_QUANTITY_VARIANCE}}
Format: "2.0%" (example)
```

**Campo 4: Match_Details**
```
Field: Match_Details
Value: "Price Variance: 4.5% (within 5% tolerance)\nQuantity Variance: 2.0% (within 10% tolerance)\nTotal: PASS"
```

**Riferimento alla guida:** [Field Manipulation Guide](../then/document-field/field-manipulation-guide.md)

---

### Passo 8: Instrada in base ai risultati del matching

**Scenario A: Corrispondenza perfetta (Full Match)**
```
IF PO_Match_Status = "FULL MATCH":
  1. Set Approval_Status = "AUTO APPROVED"
  2. Set Match_Type = "FULL"
  3. ACTION_APPROVE_DOCUMENT
  4. Export to ERP
  5. Send confirmation email
  → END ✅
```

**Scenario B: Entro la tolleranza**
```
IF PO_Match_Status = "WITHIN TOLERANCE":
  1. Set Approval_Status = "AUTO APPROVED"
  2. Set Match_Type = "TOLERANCE"
  3. Log variance details
  4. ACTION_APPROVE_DOCUMENT
  5. Export to ERP
  → END ✅
```

**Scenario C: Oltre la tolleranza (Minore)**
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

**Scenario D: Oltre la tolleranza (Maggiore)**
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

**Scenario E: PO mancante o nessuna corrispondenza**
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

## Diagramma completo del workflow

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

## Modelli di configurazione

### Modello 1: Matching standard del PO (Conservativo)

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

**Uso:** Ambiente a controllo rigoroso, bassa tolleranza alla varianza

---

### Modello 2: Matching flessibile del PO (Tollerante)

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

**Uso:** Ambiente flessibile, fornitori fidati, tolleranza più elevata

---

### Modello 3: Matching solo sul prezzo

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

**Uso:** Quando conta solo il prezzo, varianze di quantità previste

---

## Scenari avanzati

### Scenario 1: Gestione delle consegne parziali

**Sfida:** Fattura per una consegna parziale del PO

**Soluzione:**
```
1. Allow quantity under-delivery within tolerance
2. Track cumulative invoiced quantity vs PO quantity
3. Update PO remaining quantity
4. Create field: "PO_Percentage_Invoiced"
5. When 100% invoiced: Close PO automatically
```

**Implementazione:**
```
IF Cumulative_Invoiced_Quantity ≤ PO_Quantity:
  Calculate: Percentage = (Cumulative/PO) × 100
  Store in: PO_Percentage_Invoiced
  IF Percentage ≥ 100:
    Set PO_Status = "FULLY INVOICED"
    Close PO
```

---

### Scenario 2: Matching del PO multi-valuta

**Sfida:** Valuta della fattura diversa dalla valuta del PO

**Soluzione:**
```
1. Detect currency mismatch
2. Get exchange rate (from API or master data)
3. Convert invoice amount to PO currency
4. Compare converted amounts
5. Store both original and converted amounts
```

**Implementazione:**
```
IF Invoice_Currency ≠ PO_Currency:
  1. Get exchange rate for Invoice_Currency → PO_Currency
  2. Convert: Invoice_Amount_Converted = Invoice_Amount × Rate
  3. Compare: Invoice_Amount_Converted vs PO_Amount
  4. Store: Original_Currency_Amount and Converted_Amount
  5. Flag: "Currency_Conversion_Applied"
```

---

### Scenario 3: PO aperto / Accordo quadro

**Sfida:** Più fatture su un singolo PO

**Soluzione:**
```
1. Identify PO type = "Blanket"
2. Track cumulative invoiced value
3. Check: Cumulative ≤ Blanket PO Total
4. Update remaining PO value after each invoice
5. Alert when approaching PO limit
```

**Implementazione:**
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

## Gestione degli errori e casi limite

### Caso limite 1: Voce di riga mancante sulla fattura

**Problema:** La fattura ha una voce non presente sul PO

**Soluzione:**
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

### Caso limite 2: PO chiuso ma arriva una fattura

**Problema:** PO già chiuso, ricevuta una fattura in ritardo

**Soluzione:**
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

### Caso limite 3: Più PO su una singola fattura

**Problema:** La fattura fa riferimento a più PO

**Soluzione:**
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

## Suggerimenti sulle prestazioni

✅ **Best practice:**
- Memorizza in cache i dati del PO per ridurre i lookup
- Imposta tolleranze appropriate (non troppo rigide, non troppo permissive)
- Usa prima il controllo del matching completo (più veloce)
- Registra tutti i calcoli delle varianze
- Esamina le impostazioni di tolleranza trimestralmente
- Monitora i tassi di approvazione automatica
- Tieni traccia delle cause comuni delle varianze

❌ **Da evitare:**
- Tolleranza zero (troppo rigida, troppe revisioni manuali)
- Tolleranza estremamente elevata (vanifica lo scopo)
- Ignorare le varianze sistematiche
- Non monitorare le tendenze delle varianze
- Elaborare senza PO (quando richiesto)

---

## Monitoraggio e reporting

### Metriche chiave da monitorare

1. **Tasso di matching:**
   - Full Match: X%
   - Within Tolerance: Y%
   - Outside Tolerance: Z%

2. **Analisi della varianza:**
   - Varianza media di prezzo
   - Varianza media di quantità
   - Cause comuni delle varianze

3. **Efficienza di elaborazione:**
   - Tasso di approvazione automatica
   - Tasso di revisione manuale
   - Tempo medio di revisione

4. **Prestazioni dei fornitori:**
   - Varianze per fornitore
   - Tasso di matching per fornitore
   - Fornitori problematici

---

## Checklist di test

- [ ] Scenario di corrispondenza perfetta (full match)
- [ ] Scenario entro la tolleranza (varianza minore)
- [ ] Scenario oltre la tolleranza (varianza maggiore)
- [ ] Scenario di PO mancante
- [ ] Scenario di numero di PO errato
- [ ] Scenario di consegna parziale
- [ ] Scenario di consegna in eccesso
- [ ] Scenario di mancata corrispondenza della valuta
- [ ] Scenario con più PO
- [ ] Scenario di PO chiuso
- [ ] Scenario di varianza fiscale
- [ ] Workflow di escalation
- [ ] Creazione dei task
- [ ] Notifiche via email
- [ ] Aggiornamenti dei campi
- [ ] Esportazione dopo l'approvazione

---

## Pattern correlati

### Pattern che funzionano bene insieme:

- **[Task Management Pattern](task-management-pattern.md)** - Crea task di revisione per le varianze
- **[Decision Logic Pattern](decision-logic-pattern.md)** - Instradamento complesso basato sui livelli di varianza
- **[API Integration Pattern](api-integration-pattern.md)** - Recupera il pricing corrente per il confronto
- **[Data Transformation Pattern](data-transformation-pattern.md)** - Conversione di valuta, conversione di unità

---

## Guide correlate

### Prerequisiti
- [PO Matching Complete Guide](../and/compare-with-purchase-order/po-matching-complete-guide.md) - Tutte le card di matching del PO
- [Condition Cards Guide](../and/condition-cards-complete-guide.md) - Logica delle condizioni
- [Field Manipulation Guide](../then/document-field/field-manipulation-guide.md) - Operazioni sui campi

### Card correlate
- **PURCHASE_ORDER_FULL_MATCH** - [PO Matching Guide](../and/compare-with-purchase-order/po-matching-complete-guide.md#full-match)
- **CONDITION_DOC_TO_PO_UNIT_PRICE** - [PO Matching Guide](../and/compare-with-purchase-order/po-matching-complete-guide.md#unit-price)
- **CONDITION_DOC_TO_PO_QUANTITY** - [PO Matching Guide](../and/compare-with-purchase-order/po-matching-complete-guide.md#quantity)
- **CONDITION_DOC_TO_PO_TAX_LINES** - [PO Matching Guide](../and/compare-with-purchase-order/po-matching-complete-guide.md#tax-lines)
- **tasks_create** - [Task Assignment Guide](../then/task/task-assignment-guide.md)

### Prossimi passi
- Crea task di revisione: [Task Management Pattern](task-management-pattern.md)
- Aggiungi le notifiche via email: [Send Email Guide](../then/action/send-email-groups-guide.md)
- Implementa l'instradamento complesso: [Decision Logic Pattern](decision-logic-pattern.md)

---

**Versione del pattern:** 1.0
**Ultimo aggiornamento:** 23 ottobre 2025
**Difficoltà:** Media-Alta
**Tempo stimato:** 60-90 minuti
**Tasso di successo:** Alto (se configurato correttamente)
