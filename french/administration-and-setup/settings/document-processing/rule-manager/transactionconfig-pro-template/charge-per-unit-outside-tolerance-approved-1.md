# Case 14: Charge Line - Charge Per Unit Outside Tolerance (Approved)

## Scenario:

The charge per unit is outside tolerance but has been approved.

## Action:

The system accepts the charge per unit and applies the approved charges, processing the transaction accordingly.

## Example:

* **Purchase Order (PO):**
  * Charge Per Unit: $4.50
  * Quantity: 1,000 units
  * Total Charge Amount: $4,500.00
* **Invoice Received:**
  * Charge Per Unit: $5.00 (outside tolerance of 11.11%, approved)
  * Quantity: 1,000 units
  * Total Charge Amount: $5,000.00
* **Tolerance Levels:**
  * Charge Per Unit Tolerance: ±5%

Since the charge per unit ($5.00) is outside the acceptable tolerance range of 5% but has been approved, the system will:

1. **Accept the Approved Charge Per Unit:** The system accepts the invoiced charge per unit of $5.00 as it has been approved despite exceeding the tolerance limit.
2. **Process the Transaction:** The system processes the invoice using the approved charge per unit and the quantity:
   * **Total Charge Amount = Quantity × Approved Charge Per Unit**
   * **Total Charge Amount = 1,000 units × $5.00 = $5,000.00**
3. **Finalize the Invoice:** The system processes the transaction with the approved charges, reflecting the total amount of $5,000.00.

This approach ensures that the system can accommodate approved variances in charges, allowing flexibility while maintaining accurate financial records.
