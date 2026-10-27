# Review quote details and line prices

Use **Quote Details** for a document configured for quote processing. Its document type, layout, permissions and workflow determine available fields and actions. This view is separate from purchase-order matching.

## Review and correct lines

1. Open the intended quote. Compare supplier, reference, date and currency with the original.
2. Compare line-item numbers, descriptions, quantities, units, prices and amounts with the original. An item-number match does not establish a price or unit match.
3. Select a line to display its details below the table.
4. Use the configured master-data lookup where available. Check the selected item and any populated values; investigate lookup warnings.
5. Correct the line and choose **Save**, or **Save & Next** to continue. **Cancel** leaves the line editor without submitting that line's changes.
6. Use **Save & Next — Copy Defaults** only when the defaults fit the next line. Review copied values.
7. Reopen the document and line to verify stored values. For a rejected line, inspect its note where available and resolve the business reason.

## Special cases

**Add line row** creates a manually entered position when editing is allowed. Compare it with the original and complete required fields. Removing a manually created row is a separate action; do not remove a real position to make totals agree.

For read-only documents, check permissions, lock and processing stage. For missing line items, inspect the source, extraction and layout.

Automatic managed/last/contracted-price checks use [Quote comparison cards](../../administration-and-setup/workflow/cards-overview/quote-comparison-guide.md). Saving a line does not establish that these checks ran, approval was granted or ERP export completed.
