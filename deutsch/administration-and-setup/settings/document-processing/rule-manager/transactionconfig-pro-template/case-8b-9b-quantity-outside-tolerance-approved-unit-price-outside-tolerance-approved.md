# Case 8b, 9b: Quantity Outside Tolerance (Approved), Unit Price Outside Tolerance (Approved)

## Scenario:

Both the quantity and unit price are outside the tolerance range but have been approved.

## Action:

The system processes the transaction using the invoice values for both quantity and unit price, applying any necessary adjustments or line charges.

## Example:

* **Purchase Order (PO):**
  * Quantity: 200 units
  * Unit Price: $25.00 per unit
  * Total Amount: $5,000.00
* **Invoice Received:**
  * Quantity: 220 units (outside tolerance of 10%, approved)
  * Unit Price: $27.00 per unit (outside tolerance of 8%, approved)
  * Total Amount: $5,940.00
* **Tolerance Levels:**
  * Quantity Tolerance: ±5%
  * Unit Price Tolerance: ±2%

Since both the quantity (220 units) and unit price ($27.00) are outside the acceptable tolerance limits but have been approved, the system will:

1. **Accept the Approved Quantity:** The system accepts the invoiced quantity of 220 units as it has been approved despite being outside the tolerance range.
2. **Accept the Approved Unit Price:** The system accepts the invoiced unit price of $27.00 per unit as it has been approved despite being outside the tolerance range.
3. **Calculate the Total Amount:** The system calculates the total amount based on the approved invoice values:
   * **Total Amount = Quantity × Unit Price**
   * **Total Amount = 220 units × $27.00 per unit = $5,940.00**
4. **Apply Necessary Adjustments or Line Charges:** If applicable, the system may apply any additional line charges or adjustments based on the organization's policies for handling approved variances.
5. **Process the Invoice:** The system processes the invoice using the approved values for both quantity and unit price, finalizing the transaction at the total amount of $5,940.00.

This approach ensures that the transaction is processed according to the approved variances, allowing flexibility while maintaining accurate financial records.
