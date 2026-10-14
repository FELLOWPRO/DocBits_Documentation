# Case 15: Charge Line - Charge Per Unit Outside Tolerance (Rejected)

## Scenario:

The header charge per unit is outside tolerance and has not been approved.

## Action:

The system adjusts the header charge to match the purchase order, processing the transaction accordingly, and generating any necessary notes.

## Example:

* **Purchase Order (PO):**
  * Header Charge Per Unit: $4.00
  * Quantity: 1,500 units
  * Total Header Charge Amount: $6,000.00
* **Invoice Received:**
  * Header Charge Per Unit: $5.00 (outside tolerance of 25%, rejected)
  * Quantity: 1,500 units
  * Total Header Charge Amount: $7,500.00
* **Tolerance Levels:**
  * Header Charge Per Unit Tolerance: ±5%

Since the header charge per unit ($5.00) exceeds the acceptable tolerance range of 5% and has not been approved, the system will:

1. **Reject the Invoiced Header Charge Per Unit:** The system does not accept the invoiced header charge per unit of $5.00 due to the variance exceeding the tolerance limit.
2. **Adjust the Header Charge Per Unit:** The system adjusts the charge per unit to match the original purchase order or the approved charge per unit:
   * Adjusted Header Charge Per Unit = $4.00 (from PO)
3. **Recalculate the Total Header Charge Amount:** The system recalculates the total charge amount based on the adjusted charge per unit:
   * **Corrected Total Header Charge Amount = Quantity × Adjusted Header Charge Per Unit**
   * **Corrected Total Header Charge Amount = 1,500 units × $4.00 = $6,000.00**
4. **Generate a Credit Note:** Since the original invoice total was higher than the corrected total, the system generates a credit note for the overcharged amount:
   * **Credit Note Amount = Original Invoice Total - Corrected Total Header Charge Amount**
   * **Credit Note Amount = $7,500.00 - $6,000.00 = $1,500.00**
5. **Process the Invoice:** The system processes the invoice with the corrected total charge amount of $6,000.00 and issues a credit note for $1,500.00 to account for the overcharged amount.

This approach ensures that the transaction is aligned with the original terms of the purchase order, maintaining accurate financial processing while correcting any overcharges.
