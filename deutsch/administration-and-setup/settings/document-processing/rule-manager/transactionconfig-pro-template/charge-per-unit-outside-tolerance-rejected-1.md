# Charge Per Unit Outside Tolerance (Rejected)

## Scenario:

The charge per unit is outside tolerance and has not been approved.

## Action:

The system adjusts the charge per unit to match the purchase order or approved levels, generating any necessary debit or credit notes.

## Example:

* **Purchase Order (PO):**
  * Charge Per Unit: $6.00
  * Quantity: 800 units
  * Total Charge Amount: $4,800.00
* **Invoice Received:**
  * Charge Per Unit: $7.00 (outside tolerance of 16.67%, rejected)
  * Quantity: 800 units
  * Total Charge Amount: $5,600.00
* **Tolerance Levels:**
  * Charge Per Unit Tolerance: ±5%

Since the charge per unit ($7.00) exceeds the acceptable tolerance range of 5% and has not been approved, the system will:

1. **Reject the Invoiced Charge Per Unit:** The system does not accept the invoiced charge per unit of $7.00 due to the variance exceeding the tolerance limit.
2. **Adjust the Charge Per Unit:** The system adjusts the charge per unit to match the purchase order or the approved charge per unit:
   * Adjusted Charge Per Unit = $6.00 (from PO)
3. **Recalculate the Total Charge Amount:** The system recalculates the total charge amount based on the adjusted charge per unit:
   * **Corrected Total Charge Amount = Quantity × Adjusted Charge Per Unit**
   * **Corrected Total Charge Amount = 800 units × $6.00 = $4,800.00**
4. **Generate a Debit Note:** Since the original invoice total was higher than the corrected total, the system generates a debit note for the overcharged amount:
   * **Debit Note Amount = Original Invoice Total - Corrected Total Charge Amount**
   * **Debit Note Amount = $5,600.00 - $4,800.00 = $800.00**
5. **Process the Invoice:** The system processes the invoice with the corrected total charge amount of $4,800.00 and issues a debit note for $800.00 to account for the overcharged amount.

This approach ensures that financial transactions are consistent with the purchase order terms, rejecting unapproved variances and maintaining accurate billing practices.
