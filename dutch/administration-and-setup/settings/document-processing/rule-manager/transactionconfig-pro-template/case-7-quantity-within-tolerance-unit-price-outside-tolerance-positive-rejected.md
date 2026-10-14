# Case 7: Quantity Within Tolerance, Unit Price Outside Tolerance (Positive Rejected)

## Scenario:

The quantity is within tolerance, but the unit price exceeds the acceptable range (positive tolerance) and is not approved.

## Action:

The system rejects the invoice unit price, adjusts it to match the purchase order, and may generate a debit note to account for the overcharged amount.

## Example:

* **Purchase Order (PO):**
  * Quantity: 200 units
  * Unit Price: $15.00 per unit
  * Total Amount: $3,000.00
* **Invoice Received:**
  * Quantity: 198 units (within tolerance of 1%)
  * Unit Price: $17.00 per unit (outside positive tolerance of 13.33%)
  * Total Amount: $3,366.00
* **Tolerance Levels:**
  * Quantity Tolerance: ±2%
  * Unit Price Tolerance: ±1%

Since the quantity (198 units) is within the acceptable tolerance range but the unit price ($17.00) exceeds the acceptable tolerance and is not approved, the system will:

1. **Reject the Invoice Unit Price:** The system does not accept the invoiced unit price of $17.00.
2. **Adjust the Unit Price:** The system adjusts the unit price to match the original purchase order unit price.
   * Adjusted Unit Price = $15.00 (from PO)
3. **Calculate the Corrected Total Amount:** Using the adjusted unit price, the system recalculates the total amount.
   * **Corrected Total Amount = Quantity × Adjusted Unit Price**
   * **Corrected Total Amount = 198 units × $15.00 per unit = $2,970.00**
4. **Generate a Debit Note:** The system generates a debit note to account for the difference due to the overcharge.
   * **Debit Note Amount = Original Invoice Total - Corrected Total Amount**
   * **Debit Note Amount = $3,366.00 - $2,970.00 = $396.00**
   * This debit note represents the amount overcharged by the supplier.
5. **Process the Invoice:** The system processes the invoice with the corrected total amount of $2,970.00 and issues a debit note for $396.00 to offset the overcharge.

This approach ensures that any overcharging is corrected, aligning the transaction with the purchase order terms and protecting the financial interests of the business.
