# Case 1, 2, 3: Quantity and Unit Price Within Tolerance

## Scenario:

Both the quantity and unit price on the invoice are within an acceptable tolerance range compared to the purchase order.

## Action:

The system accepts the invoice values and calculates the total amount based on the provided quantity and unit price.

## Example:

**Purchase Order (PO):**

Quantity: 100 units

Unit Price: $10.00 per unit

Total Amount: $1,000.00

**Invoice Received:**

Quantity: 101 units (within tolerance of 1%)

Unit Price: $10.05 per unit (within tolerance of 0.5%)

Total Amount: $1,015.05

**Tolerance Levels:**

Quantity Tolerance: ±2%

Unit Price Tolerance: ±1%\


Since the quantity (101 units) and unit price ($10.05) are both within the acceptable tolerance levels compared to the purchase order, the system will:\


1\. **Accept the Invoice Values:** The quantity and unit price on the invoice are accepted as valid because they fall within the defined tolerance limits.

2\. **Calculate the Total Amount:** The total amount is calculated using the accepted values:

• Total Amount = Quantity × Unit Price

• Total Amount = 101 units × $10.05 per unit = $1,015.05

3\. **Process the Invoice:** The invoice is processed with the total amount of $1,015.05, and the financial records are updated accordingly.

This approach ensures that minor discrepancies that fall within acceptable tolerance levels do not lead to invoice rejections or delays in payment, thus streamlining the financial process.
