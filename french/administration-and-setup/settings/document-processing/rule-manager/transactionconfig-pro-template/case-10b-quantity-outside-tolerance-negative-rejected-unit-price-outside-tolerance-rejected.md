# Case 10b: Quantity Outside Tolerance (Negative Rejected), Unit Price Outside Tolerance (Rejected)

## Scenario:

Both the quantity and unit price are outside tolerance, and neither has been approved.

## Action:

The system rejects the invoice data, adjusts the values to match the purchase order, and generates necessary debit or credit notes.

## Example:

* **Purchase Order (PO):**
  * Quantity: 150 units
  * Unit Price: $30.00 per unit
  * Total Amount: $4,500.00
* **Invoice Received:**
  * Quantity: 140 units (outside tolerance of -6.67%, rejected)
  * Unit Price: $33.00 per unit (outside tolerance of 10%, rejected)
  * Total Amount: $4,620.00
* **Tolerance Levels:**
  * Quantity Tolerance: ±5%
  * Unit Price Tolerance: ±2%

Since both the quantity (140 units) and unit price ($33.00) are outside the acceptable tolerance limits and neither has been approved, the system will:

1. **Reject the Invoice Data:** The system does not accept the invoiced quantity or unit price due to their deviation from the tolerance limits.
2. **Adjust the Quantity:** The system adjusts the quantity to match the original purchase order quantity.
   * Adjusted Quantity = 150 units (from PO)
3. **Adjust the Unit Price:** The system adjusts the unit price to match the original purchase order unit price.
   * Adjusted Unit Price = $30.00 per unit (from PO)
4. **Recalculate the Total Amount:** The system recalculates the total amount using the adjusted quantity and unit price:
   * **Corrected Total Amount = Adjusted Quantity × Adjusted Unit Price**
   * **Corrected Total Amount = 150 units × $30.00 per unit = $4,500.00**
5. **Generate a Debit Note:** Since the original invoice total was higher than the corrected total, the system generates a debit note for the overcharged amount.
   * **Debit Note Amount = Original Invoice Total - Corrected Total Amount**
   * **Debit Note Amount = $4,620.00 - $4,500.00 = $120.00**
6. **Process the Invoice:** The system processes the invoice with the corrected total amount of $4,500.00 and issues a debit note for $120.00 to offset the overcharged amount.

This approach ensures that the financial transaction is corrected to match the purchase order terms, maintaining accurate and fair billing practices.
