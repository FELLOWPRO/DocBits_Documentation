# Case 11a: Quantity Outside Tolerance (Positive Rejected), Unit Price Within Tolerance

## Scenario:

The quantity on the invoice exceeds the acceptable range (positive) and is rejected, but the unit price is within tolerance.

## Action:

The system adjusts the quantity to the approved level, maintaining the unit price, and processes the transaction. Any excess quantity is rejected and not invoiced.

## Example:

* **Purchase Order (PO):**
  * Quantity: 100 units
  * Unit Price: $8.00 per unit
  * Total Amount: $800.00
* **Invoice Received:**
  * Quantity: 110 units (outside tolerance of 10%, rejected)
  * Unit Price: $8.00 per unit (within tolerance)
  * Total Amount: $880.00
* **Tolerance Levels:**
  * Quantity Tolerance: ±5%
  * Unit Price Tolerance: ±2%

Since the quantity (110 units) exceeds the acceptable tolerance limit (positive variance of 10%) and is not approved, but the unit price ($8.00) is within tolerance, the system will:

1. **Reject the Excess Quantity:** The system rejects the quantity that exceeds the approved tolerance level.
2. **Adjust the Quantity:** The system adjusts the quantity to match the approved level specified in the purchase order.
   * Approved Quantity = 100 units (from PO)
3. **Maintain the Unit Price:** The unit price of $8.00 per unit is within tolerance and remains unchanged.
4. **Recalculate the Total Amount:** The system calculates the total amount using the approved quantity and the accepted unit price:
   * **Total Amount = Approved Quantity × Unit Price**
   * **Total Amount = 100 units × $8.00 per unit = $800.00**
5. **Process the Invoice:** The system processes the invoice with the adjusted total amount of $800.00, reflecting only the approved quantity and unit price. The excess quantity of 10 units is rejected and not invoiced.

This approach ensures that the invoiced amount aligns with the agreed terms in the purchase order, even when the supplier attempts to invoice for an excess quantity.
