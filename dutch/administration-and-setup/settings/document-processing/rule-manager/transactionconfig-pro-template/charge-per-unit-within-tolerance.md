# Charge Per Unit Within Tolerance

## Scenario:

The charge per unit on the invoice is within the acceptable tolerance range compared to the purchase order.

## Action:

The system accepts the charge per unit as invoiced and processes the transaction without adjustments.

## Example:

* **Purchase Order (PO):**
  * Charge Per Unit: $5.00
  * Quantity: 500 units
  * Total Charge Amount: $2,500.00
* **Invoice Received:**
  * Charge Per Unit: $5.10 (within tolerance of 2%)
  * Quantity: 500 units
  * Total Charge Amount: $2,550.00
* **Tolerance Levels:**
  * Charge Per Unit Tolerance: ±3%

Since the charge per unit ($5.10) is within the acceptable tolerance range of 3% compared to the purchase order, the system will:

1. **Accept the Charge Per Unit:** The system accepts the invoiced charge per unit of $5.10 as it falls within the defined tolerance limit.
2. **Process the Transaction:** The system processes the invoice with the total charge amount based on the invoiced charge per unit and quantity:
   * **Total Charge Amount = Quantity × Charge Per Unit**
   * **Total Charge Amount = 500 units × $5.10 = $2,550.00**
3. **Finalize the Invoice:** The system processes the transaction without any adjustments, accepting the invoice as it is.

This approach allows the system to accommodate minor acceptable variances in charges, ensuring smooth and efficient processing of transactions without unnecessary rejections or delays.
