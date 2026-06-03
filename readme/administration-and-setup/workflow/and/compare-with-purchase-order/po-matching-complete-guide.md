# Purchase Order (PO) Matching Cards - Complete Guide

Os cartões de correspondência de pedidos desta página ficam no grupo **And** do Construtor de fluxos de trabalho — comparam os dados da fatura com o pedido correspondente antes de as ações Then serem executadas:

<figure><img src="../../../../.gitbook/assets/workflow_designer_cards.png" alt="Workflow Builder"><figcaption><p>Os cartões de correspondência de pedidos são adicionados ao grupo <strong>And</strong> através de <strong>Add Card</strong>.</p></figcaption></figure>

**Status:** Covers 15 PO comparison cards with detailed calculations

---

## 📌 Version Information

**Most Evolved Card:** CONDITION_DOC_TO_PO_UNIT_PRICE (5 versions, v5 latest)
**Other Complex Cards:** CONDITION_OC_TO_PO_ITEMS (v4), CONDITION_LESS_THAN_TOLERANCE_AS_VALUE_OF_ORDERED_QUANTITY (v4)

**Key Patterns:**
- **v2 → v3+:** Addition of tolerance parameters for flexible matching
- **v3 → v4:** Addition of comparison mode parameters
- **v4 → v5:** Enhanced tolerance with multiple units (%, EUR, $, etc.)

📖 [Complete Version History](../../../changelog/release.md#-po-comparison--validation-cards) | [Card Version Database](../../../../DocFlow/docs/card_version.md)

---

## Understanding PO Matching

{% embed url="https://youtu.be/qR-lrSaj4Ug" %}
DocBits PO Matching Tutorial: Auto/Manual Line Matching, Tolerances & Mismatch Indicators
{% endembed %}

In this video, you’ll learn how PO Matching works end-to-end, including the key settings that control matching behavior and how to resolve mismatches quickly.

**What you’ll learn:**
*   What PO Matching is and why it matters for invoice accuracy
*   How to configure tolerances (allowed differences) for quantities, unit prices, freight, charges, and tax
*   The 3 quantity-based matching modes:
    *   Ordered Quantity (compare to ordered amount)
    *   Received Quantity (compare to received amount)
    *   Received Delivery Open Quantity (received minus previously matched quantities)
*   How automatic matching works (item numbers, quantities, unit prices, etc.)
*   How to manually match lines using drag & drop
*   How to interpret match status with color indicators:
    *   Green = full match
    *   Orange = mismatch (hover to see tooltip details like quantity/unit price/item number mismatch)

When you receive an invoice, it should match the Purchase Order (PO) placed earlier. PO matching cards automatically check if invoice data matches PO data.

**The Big Picture:**
```
PO Placed     Invoice Arrives     PO Matching     Decision
(€100)    →   (€103)          →   (Check if       → Approve/Reject
Qty: 100      Qty: 100            within tolerance)
```

---

# 1. Purchase Order Full Match

## Purpose
Checks if the entire invoice matches the PO perfectly or within tolerance

## When to Use
- Before approving an invoice
- As a preliminary quality check
- To identify problems early

## How It Works
System compares:
- Invoice quantities vs PO quantities
- Invoice prices vs PO prices
- Invoice items vs PO items
- Invoice total vs PO total

## Result
- **TRUE** (Full Match): Everything matches, proceed
- **FALSE** (Mismatch): Something doesn't match, needs review

## Example
```
PO:
- Item ABC: Qty 100, Unit Price €50 = €5000
- Item XYZ: Qty 50, Unit Price €20 = €1000
- Total: €6000

Invoice:
- Item ABC: Qty 100, Unit Price €50 = €5000
- Item XYZ: Qty 50, Unit Price €20 = €1000
- Total: €6000

Result: ✅ FULL MATCH
```

---

# 2. Unit Price Comparison (Document vs PO)

## Purpose
Compares the unit price on the invoice with the unit price on the PO

## Parameters
- **Unit Price Tolerance**: Allow variance up to this amount
- **Tolerance Type**: Percentage (%) or Absolute (€/$)
- **Operator**: Is Equal to, Is Greater than, Is Less than, etc.

## How It Works (Percentage Tolerance)

**Formula:**
```
Variance % = |(Invoice Price - PO Price)| / PO Price × 100

Check: Is Variance % ≤ Tolerance %?
```

**Step-by-Step Example:**
```
Step 1: Get prices
  PO Unit Price: €100.00
  Invoice Unit Price: €103.00

Step 2: Calculate difference
  Difference = |€103.00 - €100.00| = €3.00

Step 3: Calculate percentage
  Percentage = (€3.00 / €100.00) × 100 = 3%

Step 4: Check tolerance (5% allowed)
  Is 3% ≤ 5%? YES ✅

Result: PASS - Within tolerance
```

## Real-World Examples

### Example 1: Small Increase (Accepted)
```
PO Price: €50.00
Invoice Price: €51.50
Tolerance: ±3%

Calculation:
  Variance = |(€51.50 - €50.00)| / €50.00 × 100
  Variance = €1.50 / €50.00 × 100 = 3%

Is 3% ≤ 3%? YES ✅ ACCEPT
```

### Example 2: Large Increase (Rejected)
```
PO Price: €50.00
Invoice Price: €55.00
Tolerance: ±3%

Calculation:
  Variance = |(€55.00 - €50.00)| / €50.00 × 100
  Variance = €5.00 / €50.00 × 100 = 10%

Is 10% ≤ 3%? NO ❌ REJECT - NEEDS REVIEW
```

### Example 3: Discount (Also Checked)
```
PO Price: €100.00
Invoice Price: €97.00
Tolerance: ±5%

Calculation:
  Variance = |(€97.00 - €100.00)| / €100.00 × 100
  Variance = €3.00 / €100.00 × 100 = 3%

Is 3% ≤ 5%? YES ✅ ACCEPT (Discount is within tolerance)
```

### Example 4: Absolute Value Tolerance
```
PO Price: €10.00
Invoice Price: €10.50
Tolerance: ±€1.00 (absolute, not %)

Calculation:
  Variance = |€10.50 - €10.00| = €0.50

Is €0.50 ≤ €1.00? YES ✅ ACCEPT
```

## What to Do With Results

**If PASS ✅:**
- Continue to next check
- Or approve invoice
- Or proceed with export

**If FAIL ❌:**
- Flag for manual review
- Ask supplier for explanation
- Contact procurement team
- Approve with note if acceptable

---

# 3. Quantity Comparison

## Purpose
Checks if the quantity ordered matches the quantity invoiced

## Parameters
- **Tolerance**: Amount or % allowed to differ
- **Operator**: Equals, Greater than, Less than
- **Quantity Type**: Ordered, Received, Open

## Calculation Example

**Percentage Tolerance:**
```
Formula:
  Quantity Variance % = |(Invoice Qty - PO Qty)| / PO Qty × 100

Example:
  PO Quantity: 100 units
  Invoice Quantity: 103 units
  Tolerance: ±5%

  Variance = |(103 - 100)| / 100 × 100
  Variance = 3 / 100 × 100 = 3%

  Is 3% ≤ 5%? YES ✅ ACCEPT
```

**Absolute Tolerance:**
```
Formula:
  Quantity Variance = |Invoice Qty - PO Qty|

Example:
  PO Quantity: 100 units
  Invoice Quantity: 102 units
  Tolerance: ±5 units

  Variance = |102 - 100| = 2 units

  Is 2 units ≤ 5 units? YES ✅ ACCEPT
```

## Real-World Scenarios

### Over-Delivery (More than Ordered)
```
Ordered: 100 units
Invoiced: 110 units
Tolerance: ±5%

Variance = |(110-100)|/100 × 100 = 10%

Is 10% ≤ 5%? NO ❌

Decision: Contact supplier - more delivered than ordered
Possible reason: Error by supplier, partial shipment already received
```

### Under-Delivery (Less than Ordered)
```
Ordered: 100 units
Invoiced: 95 units
Tolerance: ±5%

Variance = |(95-100)|/100 × 100 = 5%

Is 5% ≤ 5%? YES ✅

Decision: Accept - within tolerance
Possible reason: Partial shipment, rest to follow
```

---

# 4. Combined Price of Quantity Difference

## Purpose
When quantity differs, calculates if the total price difference is acceptable

## Why This Matters
```
Scenario: You ordered 100 units but received 110
- Quantity is 10% over (bad)
- BUT: You're only charged for 10% extra
- Combined effect might be acceptable
```

## Calculation

**Formula:**
```
Combined Variance = Quantity Variance × Price Variance

If both are within tolerance, combined is usually acceptable
```

**Example:**
```
PO:
- Unit Price: €100
- Quantity: 100
- Total: €10,000

Invoice:
- Unit Price: €102 (2% higher)
- Quantity: 105 (5% higher)
- Total: €10,710

Analysis:
- Price variance: 2% ✅
- Quantity variance: 5% ✅
- Combined effect: 1.02 × 1.05 = 1.071 = 7.1% total increase

Is combined variance acceptable? Usually YES ✅
```

---

# 5. Item ID / Supplier Item Number Comparison

## Purpose
Checks if the items in the invoice match the items in the PO

## How It Works

**Exact Match (Simplest):**
```
PO Item ID: ABC-123
Invoice Item ID: ABC-123
Result: ✅ MATCH
```

**Supplier Item Number (More Common):**
```
PO Item: ABC-123 (Our internal code)
Supplier Item: SUPP-456 (Their code for same item)
System matches these as same item
Result: ✅ MATCH
```

## Scenario: What If It Doesn't Match?

```
PO Item: ABC-123 (Copper Wire, 2mm)
Invoice Item: ABC-124 (Steel Wire, 2mm)

Result: ❌ NO MATCH

Actions:
1. Is this a substitution? Check with procurement
2. Is this an error? Contact supplier
3. Is the description similar? Verify manually
```

---

# 6. Order Type Verification

## Purpose
Verifies the purchase order type is correct

## Order Types
- **Standard Order**: Regular purchase
- **Rush Order**: Urgent, may have premium
- **Frame Agreement**: Long-term contract
- **Blanket Order**: Open-ended contract
- **Consignment**: You don't pay until used

## Check Example
```
PO Order Type: Standard Order
Invoice Order Type: Standard Order
Result: ✅ MATCH

If mismatch: Could affect terms, payment, pricing
```

---

# 7. Delivery Date Verification

## Purpose
Checks if delivery date matches the promised date on the PO

## Calculation

**Late Delivery:**
```
Formula:
  Days Late = Invoice Delivery Date - PO Promised Date

Example:
  PO Promised: 2025-10-15
  Actual Delivery: 2025-10-22
  Days Late = 7 days

If tolerance is ±3 days:
  Is 7 ≤ 3? NO ❌ LATE
```

**Early Delivery:**
```
Formula:
  Days Early = PO Promised Date - Invoice Delivery Date

Example:
  PO Promised: 2025-10-15
  Actual Delivery: 2025-10-10
  Days Early = 5 days

Early delivery is usually OK ✅
Unless you need it at specific time
```

## Tolerance Settings
```
±3 days: Allow 3 days late or early
±5 days: Allow up to 5 days variance
0 days: Must match exactly
```

---

# 8. Charge Verification (Taxes, Shipping, Etc.)

## Purpose
Checks if additional charges (taxes, shipping, handling) match PO

## Common Charges
```
- Shipping: €50
- Handling: €10
- Packaging: €5
- Insurance: €15
- Taxes: €300
```

## Calculation

**Example: Shipping Charge Check**
```
PO Shipping: €50.00
Invoice Shipping: €51.00
Tolerance: ±3%

Variance = |€51.00 - €50.00| / €50.00 × 100 = 2%

Is 2% ≤ 3%? YES ✅ ACCEPT
```

**Example: Multiple Charges**
```
PO Total Charges:
  - Shipping: €50
  - Taxes: €300
  - Handling: €10
  Total: €360

Invoice Total Charges:
  - Shipping: €50
  - Taxes: €312 (11% tax)
  - Handling: €10
  Total: €372

Difference: €12
Check if within tolerance ✅ or ❌
```

---

# 9. Tax Verification

## Purpose
Verifies tax amounts are calculated correctly

## Calculation

**Formula:**
```
Tax Amount = Subtotal × Tax Rate

Example:
  Subtotal: €1000
  Tax Rate: 19%
  Expected Tax: €1000 × 0.19 = €190

Invoice Tax: €190
Match? YES ✅
```

**Common Issues:**
```
1. Tax rate changed (region-based)
2. Tax applied to wrong amount (before/after discounts)
3. Multiple tax rates (some items 7%, others 19%)
4. Tax exempt items (0% tax)
```

**Example: Multi-Rate Taxation**
```
Item A: €100 @ 19% tax = €119
Item B: €100 @ 7% tax = €107
Item C: €100 @ 0% tax = €100
Total: €326

Invoice shows €325 (€1 error)

Check: Within tolerance or needs attention?
```

---

# 10. Facility/Cost Center Matching

## Purpose
Ensures the invoice is for the correct facility/cost center

## Example
```
PO is for:
- Facility: Berlin Plant
- Cost Center: CC-2025

Invoice should have:
- Facility: Berlin Plant ✅
- Cost Center: CC-2025 ✅

If different facility: May need different approval
```

---

# 11. Supplier Status Validation

## Purpose
Checks if the supplier is still approved/active

## Status Types
```
✅ ACTIVE: Approved, can do business
⚠️ ON HOLD: Temporarily blocked
❌ INACTIVE: No longer doing business
⚠️ CONDITIONAL: Only for specific items
```

## Check Example
```
Supplier: ABC Corp
Status in Database: ACTIVE
Status when creating PO: ACTIVE
Status when invoice arrives: INACTIVE

Alert: Supplier status changed! Investigate why.
```

---

# Which Tolerance Should I Use?

## Strict Tolerances (Lower Risk, More Manual Work)
```
Use for:
- High-value items
- Items where exactness matters
- Regulated industries

Settings:
- Unit Price: ±1%
- Quantity: ±1%
- Delivery Date: ±1 day
- Charges: ±1%
```

## Moderate Tolerances (Balanced)
```
Use for:
- Most business transactions
- Standard items
- Normal purchasing

Settings:
- Unit Price: ±3-5%
- Quantity: ±3-5%
- Delivery Date: ±3 days
- Charges: ±5%
```

## Loose Tolerances (Higher Risk, Less Manual Work)
```
Use for:
- Low-value items
- Bulk purchases
- Supplier agreements with flexibility

Settings:
- Unit Price: ±10%
- Quantity: ±10%
- Delivery Date: ±7 days
- Charges: ±10%
```

---

# PO Matching Workflow Example

```
Invoice Arrives
    ↓
Condition: "Is amount > €5000?" → YES
    ↓
Check: Full Match? → NO (10% price difference)
    ↓
Check: Unit Price within 5%? → NO (12% difference)
    ↓
Check: Quantity within 5%? → YES (2% difference)
    ↓
Decision: FAIL - Price variance too high
    ↓
Flag for: Manual review / Buyer approval
    ↓
Wait for: Buyer comment
    ↓
If Approved: Continue to Export
If Rejected: Return to Supplier
```

---

# Troubleshooting PO Matching

## "PO Not Found"
```
Cause: Invoice PO number doesn't exist in system
Fix:
1. Verify PO number spelling
2. Check if PO was created
3. Verify PO is in correct organization
4. Ask supplier for PO reference
```

## "Items Don't Match"
```
Cause: Invoice items are different from PO items
Possible Reasons:
1. Substitution approved by procurement
2. Different item numbers for same item
3. Error by supplier
Fix: Contact procurement or supplier
```

## "Price Higher Than PO"
```
Cause: Invoice price > PO price
Possible Reasons:
1. Price increase approved
2. Supplier error
3. Currency difference
4. Additional services included
Fix: Verify with procurement
```

## "Delivery Date Wrong"
```
Cause: Invoice dated after promised delivery
Possible Reasons:
1. Shipment was delayed
2. Receiving date different from invoice date
3. Partial shipment
Fix: Check shipping documents or contact supplier
```

---

# Summary Table

| Card | What It Checks | Main Calculation | Common Tolerance |
|------|----------------|------------------|-----------------|
| Full Match | Everything | All checks | Varies |
| Unit Price | Price per unit | % or € difference | ±3-5% |
| Quantity | Amount ordered | % or unit difference | ±3-5% |
| Combined Price | Total with qty change | Qty × Price | ±5-10% |
| Item ID | Right items | String match | Exact |
| Order Type | Type of purchase | String match | Exact |
| Delivery Date | When arrived | Day difference | ±3 days |
| Charges | Extra fees | % or € difference | ±5% |
| Tax | Tax amount | Tax % calculation | ±1% |
| Facility | Cost center | String match | Exact |
| Supplier | Approved? | Status check | Active only |

---

# Related Documentation

- See "Invoice Validation" guide for complete workflow
- See "Tolerance Settings" for recommended values by industry
- See "Exception Handling" for what to do with failures
- Contact your procurement team for specific tolerance policies

