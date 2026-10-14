# Case 6: Quantity Within Tolerance, Unit Price Outside Negative Tolerance (Rejected)

## Scenario:

The quantity is within tolerance, but the unit price is below the acceptable range (negative tolerance) and is not approved.

## Action:

The system rejects the unit price, adjusts it to match the purchase order, and generates a credit note for the difference. Additional header charges may be applied as necessary.

## Example:

* **Purchase Order (PO):**
  * Quantity: 100 units
  * Unit Price: $10.00 per unit
  * Total Amount: $1,000.00
* **Invoice Received:**
  * Quantity: 100 units (within tolerance of 0%)
  * Unit Price: $9.00 per unit (outside negative tolerance of -10%)
  * Total Amount: $900.00
* **Tolerance Levels:**
  * Quantity Tolerance: ±2%
  * Unit Price Tolerance: ±1%

Since the quantity (100 units) is within the acceptable tolerance range but the unit price ($9.00) is below the acceptable tolerance and is not approved, the system will:

1. **Reject the Unit Price:** The system does not accept the invoiced unit price of $9.00.
2. **Adjust the Unit Price:** The system adjusts the unit price to match the original purchase order unit price.
   * Adjusted Unit Price = $10.00 (from PO)
3. **Calculate the Corrected Total Amount:** Using the adjusted unit price, the system recalculates the total amount.
   * **Corrected Total Amount = Quantity × Adjusted Unit Price**
   * **Corrected Total Amount = 100 units × $10.00 per unit = $1,000.00**
4. **Generate a Credit Note:** The system generates a credit note for the difference between the incorrect total amount on the invoice and the corrected total amount.
   * **Credit Note Amount = Original Invoice Total - Corrected Total Amount**
   * **Credit Note Amount = $900.00 - $1,000.00 = -$100.00**
   * The credit note will effectively reverse the undercharge.
5. **Process the Invoice:** The system processes the invoice with the adjusted total amount of $1,000.00 and applies the credit note for $100.00 to account for the undercharged unit price.

This approach ensures that the pricing aligns with the purchase order terms, even when an incorrect, lower price is invoiced.
