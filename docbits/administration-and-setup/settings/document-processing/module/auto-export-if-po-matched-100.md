# Auto Export if PO Matched 100%

### Overview

The **Auto Export if PO matched 100%** setting in the Purchase Order (PO) module controls whether a complete PO match can allow the current invoice or document to proceed toward automatic export. The purchase order is the comparison reference; this setting does not export the purchase order itself.

### What Does It Do?

When enabled, this option checks the current document's PO matching result. A 100% match satisfies this matching gate, but does not guarantee immediate export. Document validation, the configured export workflow, required approvals and pending tasks can still prevent or delay export. If the match is incomplete, this gate normally blocks automatic export. The separate `ALLOW_AUTO_EXPORT_FOR_NON_MATCHABLE_PO_LINES` option can permit the `NO_MATCHABLE_PO_LINES` status; it does not generally exempt other incomplete-match statuses.

### Benefits

* **Efficiency:** Can reduce manual intervention for invoices that fully match their PO and satisfy the remaining processing requirements.
* **Control:** Uses the PO matching result as an additional export condition.
* **Processing time:** Can speed up eligible invoice processing; timing depends on the other workflow conditions.

### How to Use

1. **Enable the feature:**
   * Go to **Settings** → **Document Processing** → **Module** → **Purchase Order**.
   * Enable **Auto Export if PO matched 100%** with the corresponding slider.
2. **Monitor processing:**
   * Review the current invoice's matching, validation and export status.
   * If it is not exported despite a 100% match, check export configuration, required approvals and pending tasks.
3. **Review the configuration:**
   * Check that PO matching criteria and export settings reflect the intended workflow.
   * Review exported invoices and exceptions regularly.

### When to Use This Feature

* **High invoice volumes:** When many invoices can be matched reliably against POs.
* **Routine purchases:** When quantities, prices and other matching criteria are consistent.
* **Time-sensitive processing:** When eligible invoices should proceed automatically after all required conditions are met.
