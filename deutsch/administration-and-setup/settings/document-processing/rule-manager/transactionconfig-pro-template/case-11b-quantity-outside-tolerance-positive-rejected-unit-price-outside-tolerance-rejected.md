# Case 11b: Quantity Outside Tolerance (Positive Rejected), Unit Price Outside Tolerance (Rejected)

## Scenario:

The quantity exceeds the acceptable range (positive) and is rejected, and the unit price is also outside tolerance and rejected.

## Action:

The system adjusts the quantity and unit price to match the approved levels from the purchase order, rejecting any excesses, and processes the transaction.

## Example:

* **Purchase Order (PO):**
  * Quantity: 200 units
  * Unit Price: $50.00 per unit
  * Total Amount: $10,000.00
* **Invoice Received:**
  * Quantity: 220 units (outside tolerance of 10%, rejected)
  * Unit Price: $55.00 per unit (outside tolerance of 10%, rejected)
  * Total Amount: $12,100.00
* **Tolerance Levels:**
  * Quantity Tolerance: ±5%
  * Unit Price Tolerance: ±2%

Since both the quantity (220 units) and unit price ($55.00) exceed the acceptable tolerance limits and neither has been approved, the system will:

1. **Reject the Excess Quantity:** The system does not accept the invoiced quantity of 220 units and adjusts it to match the original purchase order.
   * Adjusted Quantity = 200 units (from PO)
2. **Reject the Invoice Unit Price:** The system does not accept the invoiced unit price of $55.00 and adjusts it to match the original purchase order.
   * Adjusted Unit Price = $50.00 per unit (from PO)
3. **Recalculate the Total Amount:** The system calculates the total amount using the adjusted quantity and unit price:
   * **Corrected Total Amount = Adjusted Quantity × Adjusted Unit Price**
   * **Corrected Total Amount = 200 units × $50.00 per unit = $10,000.00**
4. **Process the Invoice:** The system processes the invoice with the corrected total amount of $10,000.00, rejecting the excess quantity and higher unit price.

This approach ensures that the transaction aligns with the original terms of the purchase order, maintaining consistent pricing and quantity controls while rejecting unapproved variances.
