# Smart Search Ranking

Smart Search Ranking puts the documents you mean at the top of a dashboard search. A keyword search finds every document that contains your word; Smart Search Ranking adds one step: an AI reads the best matches and moves the documents that are really about your search to the top. Exact matches — invoice numbers, order numbers, supplier names — always stay first.

## What changes

| | Keyword order | With Smart Search Ranking |
| --- | --- | --- |
| Which documents are found | The same | The same |
| Order of the results | By keyword match | Documents that are about your search first |
| Exact matches (invoice number, order number, supplier) | First | First |
| Column sort, `ocr:` and field searches | Unchanged | Unchanged — these keep their own order |

## Example

Eleven test invoices all contain the word *screw*: screws, a screwdriver set, a screw compressor service, screw-cap bottles, a screw pine plant, a screw-post binder, a "screwdriver" cocktail, a toy tool case.

* Search for **screw**. In keyword order the screwdriver set is the first result and the invoice for stainless-steel screws is fifth. With Smart Search Ranking the screws come first, then the screw assortment; the screwdriver set moves down.
* Search for **screwdriver**. The screwdriver set is first in keyword order and stays first with Smart Search Ranking — this time it is what you meant. The professional screwdrivers move up; the cocktail and the toy move down.

## Where it applies

* The dashboard [Quick Search](quick-search.md) with plain text (not the field-specific `field:` chips).
* The top of the result list is re-ordered; further down, long result lists keep their keyword order.
* If the ranking service does not answer within its time budget, the search shows the normal keyword order. Nothing is hidden and no result is removed.

## How to switch it on

Smart Search Ranking is enabled per organization by DocBits. Ask your DocBits contact to switch it on. It takes effect for all users of the organization within a minute, with no change to how you search.
