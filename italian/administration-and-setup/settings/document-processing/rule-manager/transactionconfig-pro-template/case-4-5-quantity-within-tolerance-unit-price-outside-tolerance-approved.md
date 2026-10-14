# Case 4, 5: Quantity Within Tolerance, Unit Price Outside Tolerance (Approved)

## Scenario:

The quantity on the invoice is within tolerance, but the unit price is outside the acceptable tolerance range. However, this variance in the unit price has been reviewed and approved by the appropriate authorities.

## Action:

The system adjusts the unit price to match the purchase order and applies any necessary line charges to account for the difference.

## Example:

**Purchase Order (PO):**

Quantity: <mark style="color:green;">100</mark> units

Unit Price: $10.00 per unit

Total Amount: <mark style="color:purple;">$1,000.00</mark>

**Invoice Received:**

Quantity: <mark style="color:green;">100</mark> units (within tolerance)

Unit Price: <mark style="color:red;">$11.00</mark> per unit (outside tolerance of ±5%)

Total Amount: <mark style="color:red;">$1,100.00</mark>

**Tolerance Levels:**

Quantity Tolerance: ±2%

Unit Price Tolerance: ±5% (expected range: $9.50 to $10.50)

**Approval:**

• The $11.00 unit price is outside the tolerance range but has been manually approved by the appropriate department.

Since the quantity is within tolerance but the unit price is outside tolerance (yet approved), the system will:

1\. **Adjust the Unit Price**: The system adjusts the unit price back to the PO’s unit price because the variance was approved:

• **Adjusted Unit Price = $10.00 per unit**

• **Adjusted Total Amount = 100 units × $10.00 per unit = $1,000.00**

2\. **Apply a Line Charge for the Difference**: Since the approved unit price of $11.00 is higher than the PO unit price of $10.00, the system applies a line charge to account for this difference:

• **Line Charge Amount = (Approved Invoice Unit Price - PO Unit Price) × Quantity**

• **Line Charge Amount = ($11.00 - $10.00) × 100 units = $100.00**

3\. **Process the Invoice**: The system processes the invoice with:

• **Base Amount:** $1,000.00

• **Line Charge:** $100.00

• **Total Processed Amount:** $1,100.00

This ensures that while the base PO values are maintained for consistency, the approved variance in the unit price is accounted for through an additional line charge, resulting in accurate financial processing and record-keeping.
