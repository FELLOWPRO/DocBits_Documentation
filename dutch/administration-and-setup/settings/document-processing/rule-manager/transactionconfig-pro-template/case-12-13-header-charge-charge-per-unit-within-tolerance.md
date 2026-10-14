# Charge Per Unit Within Tolerance

## Scenario:

The header charge per unit is within the acceptable tolerance range compared to the purchase order.

## Action:

The system processes the header charge as invoiced, applying it without adjustments.

## Example:

* **Purchase Order (PO):**
  * Header Charge Per Unit: $3.50
  * Quantity: 1,200 units
  * Total Header Charge Amount: $4,200.00
* **Invoice Received:**
  * Header Charge Per Unit: $3.55 (within tolerance of 1.43%)
  * Quantity: 1,200 units
  * Total Header Charge Amount: $4,260.00
* **Tolerance Levels:**
  * Header Charge Per Unit Tolerance: ±2%

Since the header charge per unit ($3.55) is within the acceptable tolerance range of 2% compared to the purchase order, the system will:

1. **Accept the Header Charge Per Unit:** The system accepts the invoiced header charge per unit of $3.55 as it falls within the defined tolerance limit.
2. **Process the Header Charge:** The system processes the invoice with the total header charge amount based on the invoiced charge per unit and quantity:
   * **Total Header Charge Amount = Quantity × Header Charge Per Unit**
   * **Total Header Charge Amount = 1,200 units × $3.55 = $4,260.00**
3. **Finalize the Invoice:** The system processes the transaction without any adjustments, accepting the invoice as it is.

This approach ensures smooth and efficient processing of transactions when the header charges fall within the acceptable tolerance range, avoiding unnecessary rejections or delays.
