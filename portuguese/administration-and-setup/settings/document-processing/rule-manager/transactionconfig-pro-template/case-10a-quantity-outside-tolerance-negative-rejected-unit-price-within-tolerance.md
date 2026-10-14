# Case 10a: Quantity Outside Tolerance (Negative Rejected), Unit Price Within Tolerance

## Scenario:

The quantity is below the acceptable range (negative tolerance) and is not approved, though the unit price is within tolerance.

## Action:

The system adjusts the quantity to match the approved level, keeping the unit price consistent. The transaction is processed accordingly.

## Example:

* **Purchase Order (PO):**
  * Quantity: 150 units
  * Unit Price: $20.00 per unit
  * Total Amount: $3,000.00
* **Invoice Received:**
  * Quantity: 140 units (outside tolerance of -6.67%, rejected)
  * Unit Price: $20.00 per unit (within tolerance)
  * Total Amount: $2,800.00
* **Tolerance Levels:**
  * Quantity Tolerance: ±5%
  * Unit Price Tolerance: ±2%

Since the quantity (140 units) is below the acceptable tolerance limit (negative variance of -6.67%) and is not approved, but the unit price ($20.00) is within tolerance, the system will:

1. **Reject the Lower Quantity:** The system does not accept the lower quantity since it is outside the approved tolerance range.
2. **Adjust the Quantity:** The system adjusts the quantity to match the approved level specified in the purchase order.
   * Approved Quantity = 150 units (from PO)
3. **Maintain the Unit Price:** The unit price of $20.00 per unit is within tolerance and remains unchanged.
4. **Recalculate the Total Amount:** The system calculates the total amount using the approved quantity and the accepted unit price:
   * **Total Amount = Approved Quantity × Unit Price**
   * **Total Amount = 150 units × $20.00 per unit = $3,000.00**
5. **Process the Invoice:** The system processes the invoice with the adjusted total amount of $3,000.00, reflecting the approved quantity and unit price. The supplier is expected to invoice for the full approved quantity.

This approach ensures that the financial transaction aligns with the purchase order's terms, and prevents under-invoicing while maintaining accurate financial records.
