# Field & Table Manipulation Cards - Complete Guide

Deze kaarten horen in de **Then**-groep van de Workflow Builder — de acties die worden uitgevoerd zodra aan de When/And-voorwaarden is voldaan:

<figure><img src="../../../../.gitbook/assets/workflow_designer_cards.png" alt="Workflow Builder"><figcaption><p>Kaarten worden via <strong>Add Card</strong> aan de <strong>Then</strong>-groep toegevoegd.</p></figcaption></figure>

**Covers:** 9 cards for modifying document fields and tables

---

# Document Field Manipulation

## Card: ACTION_SET_FIELD_TO_TEXT / Set Field to Text Value

### Purpose
Automatically fills a document field with specific text

### When to Use
- Populate field from decision
- Set default values
- Fill in standardized information
- Update field based on conditions

### How It Works
```
IF Condition is true
    THEN Set Field "Category" to Value "Premium"
```

### Example Scenarios

**Scenario 1: Set Approval Category**
```
Condition: Invoice amount > €10,000
    ↓
Action: Set "Approval_Category" field to "High Value"
    ↓
Result: Document now shows "Approval_Category: High Value"
```

**Scenario 2: Set Supplier Category**
```
Condition: Supplier name contains "ABC"
    ↓
Action: Set "Supplier_Type" field to "Preferred Supplier"
    ↓
Result: Document marked as "Preferred Supplier"
```

**Scenario 3: Set Processing Notes**
```
Condition: Document has been rejected
    ↓
Action: Set "Processing_Notes" to "Requires supplier revision"
    ↓
Result: Note appears for next processor
```

### Parameters

**Field Name**
Which field to update
```
Examples: Category, Type, Status, Comment, Notes
```

**Text Value**
What to put in the field
```
Examples: "Approved", "Pending Review", "High Priority"
```

### Configuration Steps
1. Choose the field to fill
2. Enter the text value
3. Set conditions (when to fill)
4. Save

---

## Card: ACTION_SET_BOOLEAN_FIELD / Set Checkbox Field

### Purpose
Automatically checks or unchecks a checkbox field

### When to Use
- Mark as processed
- Set approval flags
- Enable/disable options
- Mark for export

### How It Works
```
IF Condition is true
    THEN Check/Uncheck the "Approved" box
```

### True = Checked, False = Unchecked

**Examples:**

**Example 1: Mark as Verified**
```
Condition: PO matches perfectly
    ↓
Action: Check "Verified" checkbox
    ↓
Result: ✅ Verified (checked)
```

**Example 2: Flag for Manual Review**
```
Condition: Price variance > 10%
    ↓
Action: Check "Requires_Manual_Review" checkbox
    ↓
Result: ✅ Requires_Manual_Review (marked)
```

**Example 3: Uncheck Pre-filled Box**
```
Condition: Supplier is blacklisted
    ↓
Action: Uncheck "Approved_for_Payment" checkbox
    ↓
Result: ☐ Approved_for_Payment (unchecked - blocked)
```

### Parameters
```
Checkbox Field: [Choose field]
Set To: ☑ Checked (✅ True)
   or: ☐ Unchecked (❌ False)
```

---

## Card: ACTION_INVERT_BOOLEAN_FIELD / Toggle Checkbox

### Purpose
Flips checkbox state (checked → unchecked, vice versa)

### When to Use
- Toggle approval status
- Switch processing mode
- Reverse previous state
- Update boolean flags

### How It Works
```
Current state: ✅ (Checked)
    ↓
ACTION_INVERT: Toggle the box
    ↓
New state: ☐ (Unchecked)

OR

Current state: ☐ (Unchecked)
    ↓
ACTION_INVERT: Toggle the box
    ↓
New state: ✅ (Checked)
```

### Example
```
Invoice received with "Priority" checked
    ↓
After processing, invert "Priority" checkbox
    ↓
Checkbox now unchecked (no longer priority)
```

---

## Card: ACTION_COPY_DOCFIELD_TO_DOCFIELD / Copy Field Value

### Purpose
Copies value from one field to another field

### When to Use
- Copy supplier info to billing info
- Duplicate data across fields
- Standardize data format
- Create backup of value

### How It Works
```
Source Field: "Invoice_Supplier"  Value: "ABC Corp"
    ↓
COPY TO
    ↓
Target Field: "Billing_Partner"  Value: "ABC Corp"

Both fields now have same value
```

### Real Examples

**Example 1: Copy Delivery Address**
```
Source: "Delivery_Address" = "123 Main St, Berlin"
    ↓
Copy to: "Billing_Address"
    ↓
Result: Both fields show "123 Main St, Berlin"
```

**Example 2: Copy Supplier Code**
```
Source: "Supplier_Code_External" = "SUPP-789"
    ↓
Copy to: "Supplier_Code_Internal"
    ↓
Result: Both codes match, system recognizes supplier
```

**Example 3: Copy Amount for Validation**
```
Source: "Invoice_Total" = "€5000"
    ↓
Copy to: "Amount_to_Validate"
    ↓
Result: Validation field has correct amount
```

### Parameters
```
Source Field: [Choose field to copy FROM]
Target Field: [Choose field to copy TO]
```

### Notes
- Original field unchanged
- Target field overwritten with source value
- Good for standardizing data

---

# Table Manipulation

## Card: EDIT_COLUMN / Edit Table Column

### Purpose
Changes values in a table column based on conditions

### When to Use
- Fix pricing errors in line items
- Update quantities
- Correct item descriptions
- Standardize values

### How It Works
```
Table Column: "Unit_Price"
Original Values: [100, 105, 103]
    ↓
FIND: Values matching condition
REPLACE: With new value
    ↓
Updated Column: [100, 110, 110] (example)
```

### Example: Fix Pricing

**Scenario: Prices in wrong currency**
```
Table "Line_Items" with column "Price"

Current prices: [100, 100, 100] (in wrong currency)
    ↓
Condition: "If Price column equals 100"
    ↓
Action: Replace with 95 (corrected price)
    ↓
Result: [95, 95, 95] (prices corrected)
```

### Parameters
```
Table: [Choose table]
Column: [Choose column to edit]
Find: [Value to find]
Replace with: [New value]
Condition: [When to apply]
```

### Common Uses
- Fix unit prices
- Standardize descriptions
- Correct quantities
- Update SKU numbers

---

## Card: CALC_COLUMNS / Calculate Column Values

### Purpose
Performs calculation on table columns and stores result

### When to Use
- Calculate line totals (Qty × Unit Price)
- Sum columns
- Calculate discounts
- Compute percentages

### How It Works
```
Column A (Quantity): 100
Column B (Unit Price): €50
    ↓
CALCULATE: A × B
    ↓
Column C (Line Total): €5000
```

### Calculation Types

**Type 1: Simple Multiplication**
```
Formula: Qty × Unit Price = Line Total

Example:
100 units × €50/unit = €5000

Config:
  Column 1: Quantity
  Operator: ×
  Column 2: Unit Price
  Result Column: Line Total
```

**Type 2: Addition**
```
Formula: Base Price + Shipping + Tax = Total

Example:
€5000 + €100 + €950 = €6050

Config:
  Column 1: Base Price
  Operator: +
  Column 2: Shipping
  Operator: +
  Column 3: Tax
  Result Column: Total
```

**Type 3: Percentage Calculation**
```
Formula: Amount × (1 + Tax%) = Total with Tax

Example:
€5000 × 1.19 = €5950

Config:
  Column: Amount
  Operator: × (1 + Tax%)
  Result Column: Amount_with_Tax
```

**Type 4: Subtraction**
```
Formula: Original Price - Discount = Final Price

Example:
€100 - €10 = €90

Config:
  Column 1: Original Price
  Operator: -
  Column 2: Discount
  Result Column: Final Price
```

### Real-World Example

**Invoice Line Items Calculation:**
```
Table: Invoice_Lines

Row 1:
  Quantity: 100
  Unit Price: €25.00
  Calculate: 100 × €25.00 = €2500.00 (Line Total)

Row 2:
  Quantity: 50
  Unit Price: €40.00
  Calculate: 50 × €40.00 = €2000.00 (Line Total)

Row 3:
  Quantity: 200
  Unit Price: €10.00
  Calculate: 200 × €10.00 = €2000.00 (Line Total)

Subtotal: €6500.00 (sum of line totals)
Tax (19%): €1235.00
Shipping: €100.00
TOTAL: €7835.00
```

### Parameters
```
Table: [Select table]
Column 1: [First column]
Operator: [×, +, -, ÷, %]
Column 2: [Second column] (if needed)
Result Column: [Where to put answer]
```

---

## Card: CALC_COLUMNS_REGEX / Calculate with Regex Pattern

### Purpose
Calculates column values based on pattern matching

### When to Use
- Extract values from text using patterns
- Format data based on rules
- Convert values based on patterns
- Parse structured text

### How It Works

**Regex Pattern Matching:**
```
Original Value: "ABC-12345-XYZ"
Pattern: Extract numbers only
Calculation: Convert to "12345"
Result: "12345"
```

### Example: Extract Supplier Code

**Scenario: Article numbers contain supplier info**
```
Table Column: "Article_Code"
Values: ["SUPP001-2025-A", "SUPP002-2025-B"]

Pattern: Extract supplier code (first 7 characters)
    ↓
Calculate: SUPP001, SUPP002
    ↓
Store in: "Supplier_Code" column

Result:
Article_Code: SUPP001-2025-A  →  Supplier_Code: SUPP001
Article_Code: SUPP002-2025-B  →  Supplier_Code: SUPP002
```

### Example: Format Phone Numbers

**Scenario: Unformatted phone numbers**
```
Original: "491234567890"
Pattern: Format as: +49 123 4567 890
Result: "+49 123 4567 890"
```

### Example: Extract Prices from Text

**Scenario: Prices in text format**
```
Original: "Price is 99.99 EUR"
Pattern: Extract number only
Result: "99.99"
```

### Parameters
```
Table: [Select table]
Column: [Column to analyze]
Regex Pattern: [Pattern to find]
Replacement: [What to replace with]
Result Column: [Where to store result]
```

### Common Regex Patterns
```
Numbers only: [0-9]+
Letters only: [a-zA-Z]+
First word: ^\w+
Extract €: €(\d+\.\d{2})
Date format: \d{4}-\d{2}-\d{2}
```

---

# Calculation Examples

## Example 1: Invoice Total Calculation
```
Step 1: Calculate line totals
  Each row: Qty × Unit Price

Step 2: Sum all line totals
  Sum: €2500 + €2000 + €2000 = €6500

Step 3: Calculate tax
  Tax: €6500 × 0.19 = €1235

Step 4: Add shipping
  Final: €6500 + €1235 + €100 = €7835
```

## Example 2: Variance Calculation
```
PO Price: €100
Invoice Price: €103

Variance = |(Invoice - PO)| / PO × 100
Variance = |3| / 100 × 100 = 3%

Store in "Price_Variance%" column
```

## Example 3: Discount Application
```
Original Price: €100
Discount %: 10%
Discount Amount: €100 × 0.10 = €10
Final Price: €100 - €10 = €90
```

---

# Field Manipulation Workflow Example

```
Document arrives
    ↓
Check condition: "Amount > €5000?"
    ↓
YES → Set field "Category" = "High Value"
    ↓
Check condition: "Supplier is preferred?"
    ↓
YES → Check "FastTrack" checkbox
    ↓
Copy "Delivery_Address" to "Invoice_Address"
    ↓
In table: Calculate line totals (Qty × Price)
    ↓
In table: Calculate total with tax
    ↓
Document now has all calculated and populated fields
```

---

# Best Practices

✅ **Do:**
- Keep formulas simple
- Test calculations with sample data
- Verify results make sense
- Document why you're changing fields
- Use copy field when data is same

❌ **Don't:**
- Create circular references (A=B, B=A)
- Overwrite important data without reason
- Create overly complex regex patterns
- Forget to verify calculation results
- Calculate on wrong table/columns

---

# Troubleshooting

## "Field not updating"
**Cause:** Condition not met or card not triggered

**Solution:**
- Check condition is true
- Verify card is in workflow
- Test with sample data
- Check for typos in field name

## "Calculation result wrong"
**Cause:** Wrong columns selected or formula incorrect

**Solution:**
- Verify source columns
- Check formula is correct
- Test manually
- Review decimal places/rounding

## "Table shows error"
**Cause:** Referenced column doesn't exist

**Solution:**
- Verify column name spelling
- Check column has data
- Ensure column data type matches calculation
- Add missing columns if needed

---

# Related Cards

- **ACTION_COPY_DOCFIELD_TO_DOCFIELD** - Copy values
- **EDIT_COLUMN** - Change table values
- **CALC_COLUMNS** - Calculate formulas
- **ACTION_SET_FIELD_TO_TEXT** - Set text values
- **ACTION_SET_BOOLEAN_FIELD** - Check boxes

