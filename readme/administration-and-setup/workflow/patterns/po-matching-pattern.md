# PO Matching Pattern

**Pattern Type:** Validation & Comparison
**Complexity:** Medium-High
**Estimated Setup:** 60-90 minutes
**Common Use Cases:** Three-way matching, invoice validation, variance checking, tolerance management

---

You build this pattern in the **Workflow Builder** (Workflow Dashboard → Workflow List → Add Workflow). Click **Add Card** and open the **Compare with Purchase Order** category — it holds every matching card this pattern uses (price, quantity, tolerance and line-item comparison cards):

<figure><img src="../../../.gitbook/assets/workflow_add_card_picker.png" alt="Add Card library showing the Compare with Purchase Order cards"><figcaption><p>The <strong>Compare with Purchase Order</strong> category — price, quantity, tolerance and line-item matching cards used throughout this pattern.</p></figcaption></figure>

---

## Pattern Overview

This pattern demonstrates how to implement comprehensive Purchase Order (PO) matching workflows in DocBits. PO matching is a critical control process that compares invoice data against purchase order data to detect discrepancies before payment approval.

**What This Pattern Does:**
1. Retrieves PO data based on PO number from invoice
2. Compares invoice line items with PO line items
3. Calculates variances (price, quantity, totals)
4. Applies tolerance rules
5. Routes for approval or escalation based on match results
6. Tracks matching history and exceptions

---

## When to Use This Pattern

Use this pattern when you need to:
- ✅ Validate invoices against purchase orders
- ✅ Detect pricing errors before payment
- ✅ Identify quantity discrepancies
- ✅ Enforce procurement controls
- ✅ Prevent duplicate payments
- ✅ Automate three-way matching
- ✅ Reduce manual invoice review workload

**Don't use this pattern when:**
- ❌ No PO exists for the invoice (non-PO invoices)
- ❌ PO data not available in DocBits
- ❌ Manual review preferred over automation
- ❌ PO matching not required by business policy

---

## Understanding PO Matching

### The Three-Way Match

**Traditional procurement control:**
```
Purchase Order (PO)  →  Created when ordering
        ↓
Goods Receipt (GR)   →  Created when receiving
        ↓
Invoice              →  Created by supplier

THREE-WAY MATCH = PO + GR + Invoice all match
```

**DocBits Implementation (Two-Way Match):**
```
Purchase Order (PO)  →  Imported to DocBits
        ↓
Invoice              →  Scanned by DocBits
        ↓
COMPARISON           →  Invoice vs PO validation
```

---

## Variance Calculation Formulas

### Unit Price Variance

**Formula:**
```
Variance % = |(Invoice Unit Price - PO Unit Price)| / PO Unit Price × 100
```

**Example:**
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

### Quantity Variance

**Formula:**
```
Variance % = |(Invoice Quantity - PO Quantity)| / PO Quantity × 100
```

**Example:**
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

### Total Amount Variance

**Formula:**
```
Variance % = |(Invoice Total - PO Total)| / PO Total × 100
```

**Example:**
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

## Complete Workflow Example

### Scenario: Invoice Validation with Tolerance-Based Routing

**Business Requirement:**
- All invoices with PO reference must be validated
- Price variance tolerance: 5%
- Quantity variance tolerance: 10%
- Total amount variance tolerance: 3%
- Within tolerance: Auto-approve
- Outside tolerance: Create review task
- Missing PO: Escalate to procurement

**Workflow Cards Used:**
1. CONDITION_DOC_FIELD_EXISTS - Check if PO number present
2. PURCHASE_ORDER_FULL_MATCH - Attempt full match
3. CONDITION_DOC_TO_PO_UNIT_PRICE - Check price variance
4. CONDITION_DOC_TO_PO_QUANTITY - Check quantity variance
5. CONDITION_DOC_TO_PO_TAX_LINES - Check tax alignment
6. ACTION_SET_FIELD_TO_TEXT - Store match results
7. tasks_create - Create review tasks
8. ACTION_SEND_EMAIL_TO_GROUPS - Send notifications

---

## Step-by-Step Implementation

### Step 1: Check for PO Reference

**Card:** CONDITION_DOC_FIELD_EXISTS or CONDITION_DOC_FIELD_CONTAINS

**Configuration:**
```
Field: PO_Number
Operator: IS NOT EMPTY
```

**Logic:**
```
IF PO_Number exists:
  → Continue to PO matching
ELSE:
  → Route to "Non-PO Invoice" workflow
  → Create manual review task
  → Skip PO matching
```

**Guide Reference:** [Condition Cards Guide](../and/condition-cards-complete-guide.md)

---

### Step 2: Retrieve PO Data

**Automatic in DocBits:**
- System looks up PO by PO_Number field
- Retrieves PO line items
- Makes data available for comparison

**Manual Configuration (if needed):**
```
PO Source: DocBits Master Data
PO Lookup Field: PO_Number
Match Type: Exact Match
Include Closed POs: No (or Yes if policy allows)
```

---

### Step 3: Full PO Match Check

**Card:** PURCHASE_ORDER_FULL_MATCH

**Purpose:** Quick check if everything matches perfectly

**Configuration:**
```
Match Level: Full Match
Include: All line items, prices, quantities, totals
Tolerance: None (exact match)
```

**Logic:**
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

**Result:**
- **TRUE**: Perfect match, auto-approve
- **FALSE**: Proceed to detailed checks

---

### Step 4: Check Unit Price Variance

**Card:** CONDITION_DOC_TO_PO_UNIT_PRICE (v5 recommended)

**Configuration:**
```
Comparison Mode: Percentage Variance
Tolerance: 5%
Operator: Variance is Less Than or Equal To
Apply To: All line items
```

**Step-by-Step:**
```
For each line item:
  1. Get Invoice Unit Price
  2. Get PO Unit Price (matched by product code)
  3. Calculate: Variance % = |Invoice - PO| / PO × 100
  4. Check: Variance % ≤ 5%?
  5. Store result
```

**Example Calculation:**
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

**Guide Reference:** [PO Matching Complete Guide - Unit Price](../and/compare-with-purchase-order/po-matching-complete-guide.md#unit-price-comparison)

---

### Step 5: Check Quantity Variance

**Card:** CONDITION_DOC_TO_PO_QUANTITY

**Configuration:**
```
Comparison Mode: Percentage Variance
Tolerance: 10%
Operator: Variance is Less Than or Equal To
Apply To: All line items
Allow Under-Delivery: Yes (within tolerance)
Allow Over-Delivery: No (strict)
```

**Logic:**
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

**Example:**
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

**Guide Reference:** [PO Matching Complete Guide - Quantity](../and/compare-with-purchase-order/po-matching-complete-guide.md#quantity-comparison)

---

### Step 6: Check Tax Lines Alignment

**Card:** CONDITION_DOC_TO_PO_TAX_LINES

**Configuration:**
```
Match Tax Codes: Yes
Match Tax Rates: Yes
Match Tax Amounts: With 1% tolerance
Tax Calculation: Verify recalculation
```

**Validation:**
```
1. Check tax codes match (e.g., "VAT19" on both)
2. Check tax rates match (19% on both)
3. Verify tax amount calculation:
   Tax Amount = Net Amount × Tax Rate
4. Allow small rounding differences
```

**Example:**
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

### Step 7: Store Match Results

**Card:** ACTION_SET_FIELD_TO_TEXT (multiple instances)

**Configuration:**

**Field 1: PO_Match_Status**
```
Field: PO_Match_Status
Value: {{CALCULATED}}
Options: "FULL MATCH" | "WITHIN TOLERANCE" | "OUT OF TOLERANCE" | "NO MATCH"
```

**Field 2: Price_Variance_Percent**
```
Field: Price_Variance_Percent
Value: {{CALCULATED_PRICE_VARIANCE}}
Format: "4.5%" (example)
```

**Field 3: Quantity_Variance_Percent**
```
Field: Quantity_Variance_Percent
Value: {{CALCULATED_QUANTITY_VARIANCE}}
Format: "2.0%" (example)
```

**Field 4: Match_Details**
```
Field: Match_Details
Value: "Price Variance: 4.5% (within 5% tolerance)\nQuantity Variance: 2.0% (within 10% tolerance)\nTotal: PASS"
```

**Guide Reference:** [Field Manipulation Guide](../then/document-field/field-manipulation-guide.md)

---

### Step 8: Route Based on Match Results

**Scenario A: Perfect Match (Full Match)**
```
IF PO_Match_Status = "FULL MATCH":
  1. Set Approval_Status = "AUTO APPROVED"
  2. Set Match_Type = "FULL"
  3. ACTION_APPROVE_DOCUMENT
  4. Export to ERP
  5. Send confirmation email
  → END ✅
```

**Scenario B: Within Tolerance**
```
IF PO_Match_Status = "WITHIN TOLERANCE":
  1. Set Approval_Status = "AUTO APPROVED"
  2. Set Match_Type = "TOLERANCE"
  3. Log variance details
  4. ACTION_APPROVE_DOCUMENT
  5. Export to ERP
  → END ✅
```

**Scenario C: Outside Tolerance (Minor)**
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

**Scenario D: Outside Tolerance (Major)**
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

**Scenario E: Missing PO or No Match**
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

## Complete Workflow Diagram

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

## Configuration Templates

### Template 1: Standard PO Matching (Conservative)

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

**Use:** Strict control environment, low tolerance for variance

---

### Template 2: Flexible PO Matching (Lenient)

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

**Use:** Flexible environment, trusted suppliers, higher tolerance

---

### Template 3: Price-Only Matching

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

**Use:** When only price matters, quantity variations expected

---

## Advanced Scenarios

### Scenario 1: Partial Delivery Handling

**Challenge:** Invoice for partial PO delivery

**Solution:**
```
1. Allow quantity under-delivery within tolerance
2. Track cumulative invoiced quantity vs PO quantity
3. Update PO remaining quantity
4. Create field: "PO_Percentage_Invoiced"
5. When 100% invoiced: Close PO automatically
```

**Implementation:**
```
IF Cumulative_Invoiced_Quantity ≤ PO_Quantity:
  Calculate: Percentage = (Cumulative/PO) × 100
  Store in: PO_Percentage_Invoiced
  IF Percentage ≥ 100:
    Set PO_Status = "FULLY INVOICED"
    Close PO
```

---

### Scenario 2: Multi-Currency PO Matching

**Challenge:** Invoice currency different from PO currency

**Solution:**
```
1. Detect currency mismatch
2. Get exchange rate (from API or master data)
3. Convert invoice amount to PO currency
4. Compare converted amounts
5. Store both original and converted amounts
```

**Implementation:**
```
IF Invoice_Currency ≠ PO_Currency:
  1. Get exchange rate for Invoice_Currency → PO_Currency
  2. Convert: Invoice_Amount_Converted = Invoice_Amount × Rate
  3. Compare: Invoice_Amount_Converted vs PO_Amount
  4. Store: Original_Currency_Amount and Converted_Amount
  5. Flag: "Currency_Conversion_Applied"
```

---

### Scenario 3: Blanket PO / Framework Agreement

**Challenge:** Multiple invoices against single PO

**Solution:**
```
1. Identify PO type = "Blanket"
2. Track cumulative invoiced value
3. Check: Cumulative ≤ Blanket PO Total
4. Update remaining PO value after each invoice
5. Alert when approaching PO limit
```

**Implementation:**
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

## Error Handling & Edge Cases

### Edge Case 1: Missing Line Item on Invoice

**Problem:** Invoice has item not on PO

**Solution:**
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

### Edge Case 2: PO Closed but Invoice Arrives

**Problem:** PO already closed, late invoice received

**Solution:**
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

### Edge Case 3: Multiple POs on Single Invoice

**Problem:** Invoice references multiple POs

**Solution:**
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

## Performance Tips

✅ **Best Practices:**
- Cache PO data to reduce lookups
- Set appropriate tolerances (not too strict, not too lenient)
- Use full match check first (faster)
- Log all variance calculations
- Review tolerance settings quarterly
- Monitor auto-approval rates
- Track common variance reasons

❌ **Avoid:**
- Zero tolerance (too strict, too many manual reviews)
- Extremely high tolerance (defeats purpose)
- Ignoring systematic variances
- Not tracking variance trends
- Processing without PO (when required)

---

## Monitoring & Reporting

### Key Metrics to Track

1. **Match Rate:**
   - Full Match: X%
   - Within Tolerance: Y%
   - Outside Tolerance: Z%

2. **Variance Analysis:**
   - Average price variance
   - Average quantity variance
   - Common variance reasons

3. **Processing Efficiency:**
   - Auto-approval rate
   - Manual review rate
   - Average review time

4. **Supplier Performance:**
   - Variances by supplier
   - Match rate by supplier
   - Problem suppliers

---

## Testing Checklist

- [ ] Perfect match scenario (full match)
- [ ] Within tolerance scenario (minor variance)
- [ ] Outside tolerance scenario (major variance)
- [ ] Missing PO scenario
- [ ] Wrong PO number scenario
- [ ] Partial delivery scenario
- [ ] Over-delivery scenario
- [ ] Currency mismatch scenario
- [ ] Multiple POs scenario
- [ ] Closed PO scenario
- [ ] Tax variance scenario
- [ ] Escalation workflow
- [ ] Task creation
- [ ] Email notifications
- [ ] Field updates
- [ ] Export after approval

---

## Related Patterns

### Patterns That Work Well Together:

- **[Task Management Pattern](task-management-pattern.md)** - Create review tasks for variances
- **[Decision Logic Pattern](decision-logic-pattern.md)** - Complex routing based on variance levels
- **[API Integration Pattern](api-integration-pattern.md)** - Fetch current pricing for comparison
- **[Data Transformation Pattern](data-transformation-pattern.md)** - Currency conversion, unit conversion

---

## Related Guides

### Prerequisites
- [PO Matching Complete Guide](../and/compare-with-purchase-order/po-matching-complete-guide.md) - All PO matching cards
- [Condition Cards Guide](../and/condition-cards-complete-guide.md) - Condition logic
- [Field Manipulation Guide](../then/document-field/field-manipulation-guide.md) - Field operations

### Related Cards
- **PURCHASE_ORDER_FULL_MATCH** - [PO Matching Guide](../and/compare-with-purchase-order/po-matching-complete-guide.md#full-match)
- **CONDITION_DOC_TO_PO_UNIT_PRICE** - [PO Matching Guide](../and/compare-with-purchase-order/po-matching-complete-guide.md#unit-price)
- **CONDITION_DOC_TO_PO_QUANTITY** - [PO Matching Guide](../and/compare-with-purchase-order/po-matching-complete-guide.md#quantity)
- **CONDITION_DOC_TO_PO_TAX_LINES** - [PO Matching Guide](../and/compare-with-purchase-order/po-matching-complete-guide.md#tax-lines)
- **tasks_create** - [Task Assignment Guide](../then/task/task-assignment-guide.md)

### Next Steps
- Create review tasks: [Task Management Pattern](task-management-pattern.md)
- Add email notifications: [Send Email Guide](../then/action/send-email-groups-guide.md)
- Implement complex routing: [Decision Logic Pattern](decision-logic-pattern.md)

---

**Pattern Version:** 1.0
**Last Updated:** October 23, 2025
**Difficulty:** Medium-High
**Estimated Time:** 60-90 minutes
**Success Rate:** High (when properly configured)
