# TransactionConfig Pro Template

## Configuring Financial Document Processing

_TransactionConfig Pro Template_ documents mapping examples for financial documents such as invoices, debit notes and credit notes. Rule Manager can use configured `conflict_resolution` rules and expressions to determine processing actions. This documentation does not establish that a predefined template is deployed in your environment.

Field mappings, transaction types and workflow decisions must be configured for the relevant Infor M3/LN integration. These examples can help explain that configuration; they do not guarantee accurate results, seamless integration or compliance with global financial standards.

### Configuration Areas

* **Mapping:** Define source and target fields for each transaction type and verify the resulting data.
* **Customization:** Configure the rules for the business workflow and approval process.
* **Automation:** Automate only the decisions explicitly covered by the active rules and expressions.
* **Integration:** Check the export mapping and requirements of the target Infor M3/LN system.
* **Compliance:** Review accounting and tax requirements separately; configuration alone is no guarantee of legal compliance.

## Illustrative Conflict Resolution Cases

The following scenario is an illustrative configured mapping, not a verified deployed default template. Actual output, amounts, signs and document types depend on the active `conflict_resolution` rules and expressions, export mapping and approval decisions. Any debit or credit note described below is conditional on that configuration; the example does not guarantee automatic issuance or legal compliance.

### [Cases 1, 2, 3: Quantity and Unit Price Within Tolerance](case-1-2-3-quantity-and-unit-price-within-tolerance.md)

**Scenario:** Both invoice quantity and unit price are within the configured PO tolerances.

**Illustrative action:** The illustrative mapping accepts the invoice values and calculates quantity × unit price.

### [Cases 4, 5: Quantity Within Tolerance, Price Outside Tolerance (Approved)](case-4-5-quantity-within-tolerance-unit-price-outside-tolerance-approved.md)

**Scenario:** Quantity is within tolerance; the price variance is outside tolerance and approved.

**Illustrative action:** The illustrative mapping uses the PO unit price and maps the approved difference as a line charge where configured.

### [Case 6: Quantity Within Tolerance, Price Below Tolerance (Rejected)](case-6-quantity-within-tolerance-unit-price-outside-negative-tolerance-rejected.md)

**Scenario:** Quantity is within tolerance; the price is below the permitted range and rejected.

**Illustrative action:** The illustrative mapping uses the PO price. The signed difference is not automatically a credit note; adjustment type and sign depend on the mapping.

### [Case 7: Quantity Within Tolerance, Price Above Tolerance (Rejected)](case-7-quantity-within-tolerance-unit-price-outside-tolerance-positive-rejected.md)

**Scenario:** Quantity is within tolerance; the positive price variance is rejected.

**Illustrative action:** The illustrative mapping uses the PO price. Any note or adjustment for the difference depends on the export mapping.

### [Cases 8a, 9a: Quantity Outside Tolerance (Approved), Price Within Tolerance](case-8a-9a-quantity-outside-tolerance-approved-unit-price-within-tolerance.md)

**Scenario:** The quantity variance is approved and the price remains within tolerance.

**Illustrative action:** The illustrative mapping uses the approved invoice quantity and the invoice unit price.

### [Case 11a: Quantity Above Tolerance (Rejected), Price Within Tolerance](case-11a-quantity-outside-tolerance-positive-rejected-unit-price-within-tolerance.md)

**Scenario:** Quantity exceeds tolerance and is rejected; price is within tolerance.

**Illustrative action:** The illustrative mapping uses the approved quantity and retains the unit price. Handling of excess quantity depends on the configured rules.

### [Case 10a: Quantity Below Tolerance (Rejected), Price Within Tolerance](case-10a-quantity-outside-tolerance-negative-rejected-unit-price-within-tolerance.md)

**Scenario:** Quantity is below tolerance and rejected; price is within tolerance.

**Illustrative action:** The illustrative mapping uses the approved quantity while retaining the unit price.

### [Cases 8b, 9b: Quantity and Price Outside Tolerance (Approved)](case-8b-9b-quantity-outside-tolerance-approved-unit-price-outside-tolerance-approved.md)

**Scenario:** Both quantity and price variances are approved.

**Illustrative action:** The illustrative mapping uses approved invoice values and any explicitly configured line charges or adjustments.

### [Case 10b: Quantity Below Tolerance and Price Outside Tolerance (Rejected)](case-10b-quantity-outside-tolerance-negative-rejected-unit-price-outside-tolerance-rejected.md)

**Scenario:** Neither the negative quantity variance nor the price variance is approved.

**Illustrative action:** The illustrative mapping uses PO or approved values. Any debit or credit note requires the corresponding mapping and approval outcome.

### [Case 11b: Quantity Above Tolerance and Price Outside Tolerance (Rejected)](case-11b-quantity-outside-tolerance-positive-rejected-unit-price-outside-tolerance-rejected.md)

**Scenario:** The positive quantity variance and the price variance are rejected.

**Illustrative action:** The illustrative mapping uses approved PO values; handling of excesses depends on the active configuration.

### [Cases 12, 13: Charge Line - Charge Per Unit Within Tolerance](charge-per-unit-within-tolerance.md)

**Scenario:** The line charge per unit is within the configured PO tolerance.

**Illustrative action:** The illustrative mapping accepts the invoiced line charge without adjustment.

### [Case 14: Charge Line - Charge Per Unit Outside Tolerance (Approved)](charge-per-unit-outside-tolerance-approved-1.md)

**Scenario:** The line charge per unit is outside tolerance and approved.

**Illustrative action:** The illustrative mapping applies the approved line charge.

### [Case 15: Charge Line - Charge Per Unit Outside Tolerance (Rejected)](charge-per-unit-outside-tolerance-rejected.md)

**Scenario:** The line charge per unit is outside tolerance and rejected.

**Illustrative action:** The illustrative mapping uses the PO or approved line charge. Any note for the difference depends on the export mapping.

### [Cases 12, 13: Header Charge - Charge Per Unit Within Tolerance](case-12-13-header-charge-charge-per-unit-within-tolerance.md)

**Scenario:** The header charge per unit is within the configured PO tolerance.

**Illustrative action:** The illustrative mapping applies the invoiced header charge without adjustment.

### [Case 14: Header Charge - Charge Per Unit Outside Tolerance (Approved)](charge-per-unit-outside-tolerance-approved.md)

**Scenario:** The header charge per unit is outside tolerance and approved.

**Illustrative action:** The illustrative mapping applies the approved header charge.

### [Case 15: Header Charge - Charge Per Unit Outside Tolerance (Rejected)](case-15-header-charge-charge-per-unit-outside-tolerance-rejected.md)

**Scenario:** The header charge per unit is outside tolerance and rejected.

**Illustrative action:** The illustrative mapping uses the PO or approved header charge. Any separate note depends on the configured handling.

### [Tax Lines](tax-lines.md "mention")

**Scenario:** Tax amounts on the invoice and PO differ.

**Illustrative action:** The illustrative mapping uses approved tax rates and amounts. The configuration must be checked against applicable tax requirements; the example guarantees no legal compliance.
