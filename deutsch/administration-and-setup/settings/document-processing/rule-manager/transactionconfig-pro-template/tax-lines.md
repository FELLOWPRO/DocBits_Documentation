# Tax Lines

## Scenario:

Handles discrepancies in tax amounts between the invoice and purchase order.

## Action:

The system adjusts the tax lines according to the approved tax rates and amounts, ensuring compliance with applicable tax regulations.

## Example:

* **Purchase Order (PO):**
  * Subtotal Amount: $10,000.00
  * Tax Rate: 8%
  * Expected Tax Amount: $800.00
  * Total Amount with Tax: $10,800.00
* **Invoice Received:**
  * Subtotal Amount: $10,000.00
  * Tax Rate: 10% (discrepancy)
  * Invoiced Tax Amount: $1,000.00
  * Total Amount with Tax: $11,000.00

Since the tax rate on the invoice (10%) differs from the expected tax rate (8%) and is not approved, the system will:

1. **Reject the Invoiced Tax Rate:** The system does not accept the 10% tax rate because it does not match the approved rate in the purchase order.
2. **Adjust the Tax Rate:** The system adjusts the tax rate to match the approved rate from the purchase order.
   * Adjusted Tax Rate = 8% (from PO)
3. **Recalculate the Tax Amount:** The system recalculates the tax amount based on the adjusted tax rate:
   * **Corrected Tax Amount = Subtotal Amount × Adjusted Tax Rate**
   * **Corrected Tax Amount = $10,000.00 × 8% = $800.00**
4. **Recalculate the Total Amount:** The system recalculates the total amount including tax:
   * **Corrected Total Amount with Tax = Subtotal Amount + Corrected Tax Amount**
   * **Corrected Total Amount with Tax = $10,000.00 + $800.00 = $10,800.00**
5. **Generate a Credit Note:** The system generates a credit note to correct the overcharged tax:
   * **Credit Note Amount = Original Invoice Tax Amount - Corrected Tax Amount**
   * **Credit Note Amount = $1,000.00 - $800.00 = $200.00**
6. **Process the Invoice:** The system processes the invoice with the corrected tax amount of $800.00 and the total amount of $10,800.00, issuing a credit note for the $200.00 tax discrepancy.

This approach ensures that the invoice tax is consistent with the purchase order and complies with applicable tax regulations, preventing overpayment and ensuring accuracy in financial records.
