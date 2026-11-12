---
description: 'Make tolerance and PO reference direction explicit'
---

# Make tolerance and PO reference direction explicit

A 2 percent tolerance is not a fixed amount. It is 2 percent of whichever side you compare against, so the same invoice line can fail in one direction and pass in the other. This page shows that on one pair of values, gives you three exercises to reproduce it, and then lists the six comparison directions and the card parameters you can copy into your own test.

Do the exercises in Advanced Test, in your own test organization, against a synthetic document with a matched purchase order.

## The reference side is the base

In the inspected PO card version 5, `document_po` compares the document value against the purchase-order value, so the PO value is the base for a percentage tolerance. `po_document` reverses both the comparison and the base. The six allowed directions also include the received side. Set direction, operator and Any/All explicitly instead of trusting whatever a saved card still holds.

## Exercise 1: same values, two directions

**Goal:** see two different results come out of the same numbers.

1. Set up a matched PO of `100` and a document unit price of `102.02`.
2. Compare with the operator `eq` and a tolerance of `2` percent, first with `document_po`. Expect `false`: 2 percent of 100 is 2, so the inclusive interval is 98 to 102, and 102.02 sits 0.02 above it.
3. Repeat the same case with `po_document`. Expect `true`: 2 percent of 102.02 is 2.0404, so the interval is 99.9796 to 104.0604, and the PO value 100 is inside it.

**Done when:** both results and both intervals are written down, and you can say which value the percentage was calculated from in each direction.

An absolute tolerance of `2` behaves differently: it uses the unit of the compared value and does not move with the reference.

## Exercise 2: find the exact boundary

**Goal:** know whether the edge of the interval counts.

1. Keep `document_po`, `eq` and the 2 percent tolerance, and change the document value to `102`.
2. Run the case, then run it again with `102.01`.

**Done when:** `102` returns `true` and `102.01` returns `false`. The bound is inclusive: 102 lies exactly on the upper boundary of the interval 98 to 102.

## Exercise 3: Any, All and the lines that were compared

**Goal:** know what the card does with several lines, and what happens when there is nothing to compare.

1. Build a document with two lines against the same matched PO: one inside the tolerance and one outside it.
2. Run the card with `match_any`, then with `match_all`.
3. Run a document that has no comparable line at all.

**Done when:** `match_any` passes on the one matching line, `match_all` fails as soon as one comparison fails, and the document without a comparable line returns a data error. In version 5 that is an error, not an All that was satisfied automatically.

## Which side is the base?

| Stored option | Compared side | Reference side (percentage base) |
| --- | --- | --- |
| `po_document` | Purchase order | Document |
| `received_document` | Received data | Document |
| `po_received` | Purchase order | Received data |
| `document_po` | Document | Purchase order |
| `document_received` | Document | Received data |
| `received_po` | Received data | Purchase order |

## Check before you trust an existing workflow

The card normalizes prices per pricing unit and uses PO or receipt data according to direction, so check matching, quantities and units first. Any needs one matching comparison; All needs every comparison actually made. Track unmatched rows separately.

For existing workflows, reread the saved version, direction and operator: migrations changed comparison settings, so historical labels are not sufficient acceptance evidence. Record the values and the reference, the exact boundary, the smallest excess, the rounding precision, the missing PO and the unmatched line. This calculation does not replace acceptance with your own PO master data.

## Cards and example parameters

These values describe individual card parameters, not an importable complete workflow. Replace YOUR\_\* with your own test selections. The designer manages the hidden caller ID. Catalog: Dev, DocFlow 2.10.38, 21 October 2026; check available versions and entitlements in your own organization.

### `condition_docfield_operator_docfield_tolerances` · v2

Identity: `d0472648-d1a2-499d-83e3-b47306ae130a`

| Parameter | Type / choices | Example |
| --- | --- | --- |
| `field_name_left` | `field_name_left:str` | `"total_amount"` |
| `operator` | `eq / neq / gt / ge / lt / le` | `"eq"` |
| `field_name_right` | `field_name_right:str` | `"expected_amount"` |
| `tolerance_amount` | `tolerance_amount` | `"2"` |
| `tolerance_type` | `percent / value` | `"percent"` |

### `condition_doc_to_po_unit_price` · v5

Identity: `ed2cd0fe-ac87-4bae-9a86-0b0576159b28`

| Parameter | Type / choices | Example |
| --- | --- | --- |
| `operator_any_all` | `match_any / match_all` | `"match_all"` |
| `operator` | `eq / neq / gt / ge / lt / le` | `"eq"` |
| `tolerance_amount` | `tolerance_amount` | `"2"` |
| `tolerance_type` | `percent / value` | `"percent"` |
| `comparison_data` | `po_document / received_document / po_received / document_po / document_received / received_po` | `"document_po"` |

## Business test cases

| Case | Input / setup | Expected outcome |
| --- | --- | --- |
| PO-01 | document\_po; PO=100; DOC=102; eq; 2 percent | true |
| PO-02 | document\_po; PO=100; DOC=102.02; eq; 2 percent | false |
| PO-03 | po\_document; PO=100; DOC=102.02; eq; 2 percent | true |
| PO-04 | compared\_rows=0 | data error |
| PO-05 | unmatched\_rows>0 | inspect coverage separately |

## Evidence and limits

Parameters and behavior were checked against the Dev catalog and inspected source revision. Business test cases are an acceptance procedure. Personal approvals, real data changes and delivery were not performed for this chapter.

[Continue learning](./) · [Training kit](workflow-training-kit.md)
