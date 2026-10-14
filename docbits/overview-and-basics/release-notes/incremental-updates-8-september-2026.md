# Hotfixes 8 September 2026

> Purchase order matching: what changed with the hotfixes deployed on 8 September 2026. The behaviour below is live on the development environment and reaches stage, sandbox and production with the next upgrades.

## Purchase order matching

- **The match survives saving.** A purchase order match that a transformation rule used to drop silently on every save (rules that rebuild the line items) is now kept as long as the rule produces the same lines. When a rule really does replace matched lines, the document records the rule and the screen names it.
- **Matching runs again on save.** When the purchase order number on the document changes — or when master data filled it in after processing and no matching run has looked it up yet — the save matches the document straight away. An existing match is never overwritten by a save.
- **The screen says why there is no match.** The Purchase Order Matching screen shows one sentence above the purchase order area: no purchase order number, purchase order not found in the ERP, not looked up yet, loaded but not connected, no line matches, no table, table columns not mapped, no open lines left. Candidates that were set aside are listed with the reason (for example an invoice number that had been read into the purchase order column).
- **A dropped match is never reported as saved.** If the server does not keep a match, the screen restores it, marks the document as unsaved and reports the rejection with its reason instead of "saved".
- **Matching history shows the transformation rules.** The matching history of a document now has a _Transformation rules_ step before the first matching stage, listing the rules that ran and whether one of them dropped the match. Administrators get a link to the rule.
- **PO unit price from the net amount.** With _Calculate PO unit price_ switched on, the price is now derived from the purchase order line's **net** amount first and from the total only when there is no net amount. Purchase orders from Infor carry tax in the line total; invoices priced net used to show as "unit price under-matched" by exactly the tax rate. The calculated price is refreshed on every match, so existing documents benefit without reloading the purchase order.
- **Invoice numbers are no longer mistaken for purchase order numbers.** A candidate from a line-item column or an earlier lookup that equals the document's own invoice number is set aside.

## Documentation

- New page [Transformation Rules](../../administration-and-setup/settings/global-settings/document-types/transformation-rules.md).
- [Purchase Order Matching Rules](../../administration-and-setup/settings/global-settings/document-types/more-settings/purchase-order/purchase-order-matching-rules.md) now covers rule types, activation conditions, fallback rules, the default rule set, tolerance types and the effective columns.
- [Calculate PO unit price](../../administration-and-setup/settings/global-settings/document-types/more-settings/purchase-order/calculate-po-unit-price.md) describes the net-amount calculation.
- [Purchase Order Matching Screen](../../end-user-and-partner-section/end-user-section/purchase-order-matching/README.md) explains the "why is there no match" messages and the matching history.
