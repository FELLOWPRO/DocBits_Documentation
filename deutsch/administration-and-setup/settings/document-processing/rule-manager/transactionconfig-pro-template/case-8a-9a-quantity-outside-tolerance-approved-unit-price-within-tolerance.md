# Case 8a, 9a: Quantity Outside Tolerance (Approved), Unit Price Within Tolerance

## Scenario:

The quantity on the invoice is outside the acceptable tolerance but has been approved, while the unit price remains within tolerance.

## Action:

The system accepts the approved quantity and the unit price as per the invoice and processes the transaction accordingly.

## Example:

* **Purchase Order (PO):**
  * Quantity: 150 units
  * Unit Price: $12.00 per unit
  * Total Amount: $1,800.00
* **Invoice Received:**
  * Quantity: 160 units (outside tolerance of 6.67% but approved)
  * Unit Price: $12.00 per unit (within tolerance)
  * Total Amount: $1,920.00
* **Tolerance Levels:**
  * Quantity Tolerance: ±5%
  * Unit Price Tolerance: ±2%

Since the quantity (160 units) exceeds the acceptable tolerance limit but has been approved, and the unit price ($12.00) is within the acceptable range, the system will:

1. **Accept the Approved Quantity:** The system acknowledges that the quantity has been approved despite being outside the normal tolerance range.
2. **Accept the Unit Price:** The unit price of $12.00 per unit is within the acceptable tolerance, so it is accepted as invoiced.
3. **Process the Transaction:** The system calculates the total amount using the approved quantity and unit price:
   * **Total Amount = Quantity × Unit Price**
   * **Total Amount = 160 units × $12.00 per unit = $1,920.00**
4. **Finalize the Invoice:** The system processes the invoice with the total amount of $1,920.00, reflecting the approved quantity and accepted unit price.

This approach allows the system to accommodate approved variances in quantity while ensuring the unit price remains within the expected range, facilitating smooth transaction processing.
