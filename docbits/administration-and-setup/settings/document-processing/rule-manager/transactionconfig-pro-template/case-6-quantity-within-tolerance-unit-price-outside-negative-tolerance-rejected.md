# Case 6: Quantity Within Tolerance, Unit Price Below Tolerance (Rejected)

The following scenario is an illustrative configured mapping, not a verified deployed default template. Actual output, amounts, signs and document types depend on the active `conflict_resolution` rules and expressions, export mapping and approval decisions. Any debit or credit note described below is conditional on that configuration; the example does not guarantee automatic issuance or legal compliance.

## Scenario

The quantity is within tolerance, but the invoice unit price is below the permitted range and the price variance has not been approved.

## Illustrative Action

A mapping configured to use the PO price after rejection would retain the quantity and replace the invoice unit price with the PO unit price. Whether the resulting difference produces an adjustment, a debit note, a credit note or no separate document depends on the active mapping and approval decisions. Additional header charges apply only when explicitly configured.

## Example

* **Purchase Order (PO):**
  * Quantity: 100 units
  * Unit price: $10.00 per unit
  * Total: $1,000.00
* **Invoice received:**
  * Quantity: 100 units — actual quantity deviation 0%, within the configured ±2% tolerance.
  * Unit price: $9.00 — actual price deviation -10%, outside the configured ±1% tolerance; rejected.
  * Total: $900.00
* **Configured tolerance levels:**
  * Quantity: ±2%
  * Unit price: ±1%

For this illustrative mapping:

1. Reject the invoice unit price of $9.00 because the price variance is outside tolerance and has not been approved.
2. Use the PO unit price of $10.00.
3. Recalculate the example total: **100 units × $10.00 = $1,000.00**.
4. Calculate the signed variance as invoice total minus recalculated total: **$900.00 - $1,000.00 = -$100.00**.
5. Apply the configured export mapping and approval outcome. The -$100.00 value is a signed variance, not an unconditional instruction to issue a credit note. The mapping determines any adjustment's amount, sign and document type.

Do not interpret this example as a credit note automatically reversing an undercharge. Confirm the intended accounting treatment in the active export mapping before using the rule.
