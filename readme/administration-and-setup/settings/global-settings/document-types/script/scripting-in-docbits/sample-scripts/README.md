# Sample Scripts

Production-ready script examples for common DocBits automation use cases. Each example includes the full script, a step-by-step explanation, and links to the functions used.

## Examples by Use Case

### Data Validation
- [Supplier Lookup Validation](lookup-supplier-validation.md) — Validate supplier against master data
- [Table Sum Validation](table-sum-validation.md) — Verify line item totals match net amount

### Automation
- [Auto PO Matching](auto-po-matching.md) — Trigger automatic PO matching
- [Auto-Export Based on Conditions](status-auto-export.md) — Skip validation for low-risk invoices
- [Due Date Calculation](due-date-calculation.md) — Calculate payment terms with weekend skip

### Business Rules
- [Tax Code Detection](tax-code-detection.md) — Determine tax code from fulltext and amounts
- [Task for High Amount](task-high-amount.md) — Create approval task for large invoices
- [Dynamic Required Fields](dynamic-required-fields.md) — Adjust required fields based on currency

### Fulltext & Vector Search
- [Duplicate Invoice Detection](duplicate-invoice-detection.md) — Find duplicate invoices using fulltext search
- [Similar Document Detection](similar-document-detection.md) — Flag similar documents using vector search
- [Compliance Text Search](compliance-text-search.md) — Search for compliance keywords (e.g. Reverse Charge)
- [ERP Vendor Validation](erp-vendor-validation.md) — Validate vendor against ERP master data
- [Fill Missing Fields from History](fill-missing-fields-from-history.md) — Auto-fill fields from similar past documents

### Legacy Examples
- [Calculating Total Charges](calculating-total-charges-script-for-docbits-1.md) — Sum freight and packaging amounts
- [Delete Empty Lines](delete-lines-with-empty-quantity-and-amount.md) — Remove rows with zero quantity/amount
- [Export Certificate Numbers](formatting-export-certificate-reference-numbers-script-for-docbits.md) — Pad reference numbers with leading zeros
- [Extended Invoice Numbers](generating-extended-invoice-numbers-script-for-docbits-1.md) — Concatenate invoice ID and PO number
- [USD Default Currency](usd-as-default-currency.md) — Set USD as default currency
