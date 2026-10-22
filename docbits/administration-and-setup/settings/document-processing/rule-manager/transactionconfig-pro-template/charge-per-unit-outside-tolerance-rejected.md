# Case 15: Charge Line - Charge Per Unit Outside Tolerance (Rejected)

The following scenario is an illustrative configured mapping, not a verified deployed default template. Actual output, amounts, signs and document types depend on the active `conflict_resolution` rules and expressions, export mapping and approval decisions. Any debit or credit note described below is conditional on that configuration; the example does not guarantee automatic issuance or legal compliance.

## Scenario

The charge per unit on a charge line is outside tolerance and the variance has not been approved. This case concerns a line charge, not a header charge.

## Illustrative Action

A mapping configured to use the PO charge after rejection would replace the invoice's charge per unit with the PO value. Any separate adjustment or debit/credit note depends on the export mapping and approval decisions.

## Example

* **Purchase Order (PO):**
  * Line charge per unit: $4.00
  * Quantity: 1,500 units
  * Total line charge: $6,000.00
* **Invoice received:**
  * Line charge per unit: $5.00 — 25% above the PO value, outside the configured ±5% tolerance; rejected.
  * Quantity: 1,500 units
  * Total line charge: $7,500.00
* **Configured tolerance:** Charge per unit ±5%.

For this illustrative mapping:

1. Reject the invoiced charge per unit of $5.00 because the 25% variance exceeds the ±5% tolerance and has not been approved.
2. Use the PO charge per unit of $4.00.
3. Recalculate the total line charge: **1,500 units × $4.00 = $6,000.00**.
4. Calculate the excess invoiced charge: **$7,500.00 - $6,000.00 = $1,500.00**.
5. Apply the configured handling of that difference. A credit note for $1,500.00 is one possible mapped outcome, not a guaranteed system action. Its amount, sign, document type and issuance depend on the active rules, export mapping and approvals.

Validate the line charge mapping and resulting accounting documents before using this scenario in production.
