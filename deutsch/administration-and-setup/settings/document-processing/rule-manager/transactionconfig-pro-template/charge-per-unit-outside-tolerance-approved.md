# Case 14: Header Charge - Charge Per Unit Outside Tolerance (Approved)

## Scenario:

The header charge per unit is outside tolerance but has been approved.

## Action:

The system processes the approved charge per unit, applying it to the transaction.

## Example:

* **Purchase Order (PO):**
  * Header Charge Per Unit: $2.50
  * Quantity: 2,000 units
  * Total Header Charge Amount: $5,000.00
* **Invoice Received:**
  * Header Charge Per Unit: $3.00 (outside tolerance of 20%, approved)
  * Quantity: 2,000 units
  * Total Header Charge Amount: $6,000.00
* **Tolerance Levels:**
  * Header Charge Per Unit Tolerance: ±5%

Since the header charge per unit ($3.00) exceeds the acceptable tolerance range of 5% but has been approved, the system will:

1. **Accept the Approved Header Charge Per Unit:** The system accepts the invoiced header charge per unit of $3.00 as it has been approved despite exceeding the tolerance limit.
2. **Process the Header Charge:** The system processes the invoice using the approved charge per unit and the quantity:
   * **Total Header Charge Amount = Quantity × Approved Header Charge Per Unit**
   * **Total Header Charge Amount = 2,000 units × $3.00 = $6,000.00**
3. **Finalize the Invoice:** The system processes the transaction with the approved charges, reflecting the total amount of $6,000.00.

This approach allows the system to accommodate approved variances in header charges, ensuring that the transaction is processed according to the approval while maintaining accurate financial records.
