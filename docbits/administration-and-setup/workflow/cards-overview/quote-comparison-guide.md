# Quote comparison cards

<figure><img src="../../../.gitbook/assets/workflow-card-qa-20261021-category-4a7af1d99c73-en.png" alt="Available cards in the selected category. Configure the placeholders before use."><figcaption><p>Available cards in the selected category. Configure the placeholders before use.</p></figcaption></figure>

These And conditions use the quote or supplier-item data available on the document. Configure and test them after the required quote data has been loaded. A matching item identifier does not by itself prove that its price or unit of measure is correct.

## Select the check

| Card type | Check and configuration |
| --- | --- |
| `CONDITION_QUOTES_ITEM_NUMBER_COMPARISON` | Checks the item identifier against the item-price data. Select the comparison and Any/All fields offered by the card. |
| `CONDITION_SPECIFY_SUPPLIER_TYPE` | Compares the supplier type from the quote data with `supplier_type`. This is a supplier classification check, not a price comparison. |
| `CONDITION_QUOTE_SUPPLIER_ITEM_NUMBER_EXISTS` | Checks whether the supplier item ID is or is not present in the item-price data; choose the operator and Any/All. Missing quote or item data must be investigated in the log. |
| `CONDITION_QUOTE_PRICE_MATCH` | Compares a unit price with the selected supplier price: `ManagedPrice` or `LastPrice`. Choose Any/All and the numeric comparison operator. Lines without a comparable number on either side are skipped and logged; if no line is comparable, the card reports missing document data. |
| `CONDIITON_UNIT_OF_MEASURE_EQUAL` | Checks the unit of measure against the related data. The technical type contains a retained spelling error; do not change it in stored workflow JSON. A price expressed per different units needs separate attention. |
| `CONDITION_ITEM_QUOTES_TO_CONTRACTED_PRICE` | Compares quoted and contracted prices. Version 3 adds Any/All; see below. |

Visible labels can differ by release and UI language. Select by the actual check, not only by the category name. For example, Quoted Item Price may appear under Logic while the other quote checks appear in Compare with Quote Price.

## Quoted Item Price: version 3

Choose the equality or inequality operator and whether any compared line or every compared line must satisfy it:

- `match_any`: one successful comparable line is sufficient.
- `match_all`: every compared line must satisfy the selected operator.

Version 2 retains the All behavior. An unset Any/All setting on v3 falls back to All and is logged. A card with no comparable lines reports missing data; absence of a price is not proof of equality or inequality. Inspect skipped lines and their missing side in the log.

For example, two comparable lines produce results true and false for equality. Any passes; All fails. With inequality the comparison result for each line changes first, and Any/All then combines those results. It does not invert the final All result to implement Any.

## Test cases

Use exact item and supplier IDs, the intended price source and matching units. Test all lines matching, a mixed result, no comparable prices, missing quote data and a wrong supplier ID. Verify both the comparison result and which lines were skipped. Keep approval or export behind the business checks that are actually required; a successful identifier check is not a complete procurement validation.

See [PO Matching](po-matching-complete-guide.md) for purchase-order comparisons and [Workflow Logs](../workflow-logs.md) for troubleshooting.
