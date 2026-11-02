---
description: "P1: Make tolerance and PO reference direction explicit"
---

# P1: Make tolerance and PO reference direction explicit

Percentage tolerance depends on the **reference side**. In the inspected PO card version 5, `document_po` means document value against purchase-order value; the PO is the percentage base. `po_document` reverses both comparison and base. The six allowed directions also include the received value. Set direction, operator and Any/All explicitly.

Example: PO 100, document 102.02, equality with 2 percent. With PO reference the allowed interval is 98–102: outside. With document reference it is 99.9796–104.0604: PO value 100 is inside. Document value 102 lies exactly on the inclusive upper boundary of the first direction. An absolute tolerance of 2 uses the compared value's unit.

The card normalizes prices per pricing unit and uses PO or receipt data according to direction. Check matching, quantities and units first. Any needs one matching comparison; All needs every comparison actually made. **No comparable line** is a data error in v5, not an automatically satisfied All. Track unmatched rows separately.

For existing workflows, reread the saved version, direction and operator: migrations changed comparison settings. Historical labels are insufficient acceptance evidence. Record values and reference, the exact boundary, smallest excess, rounding precision, missing PO and unmatched line. This calculation does not replace acceptance with your own PO master data.

## Cards and example parameters

These values describe individual card parameters, not an importable complete workflow. Replace YOUR_* with your own test selections. The designer manages the hidden caller ID. Catalog: Dev, DocFlow 2.10.38, 21 October 2026; check available versions and entitlements in your own organization.

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
| PO-01 | document_po; PO=100; DOC=102; eq; 2 percent | true |
| PO-02 | document_po; PO=100; DOC=102.02; eq; 2 percent | false |
| PO-03 | po_document; PO=100; DOC=102.02; eq; 2 percent | true |
| PO-04 | compared_rows=0 | data error |
| PO-05 | unmatched_rows>0 | inspect coverage separately |

## Evidence and limits

Parameters and behavior were checked against the Dev catalog and inspected source revision. Business test cases are an acceptance procedure. Personal approvals, real data changes and delivery were not performed for this chapter.

[Continue learning](../workflow-learning-path.md) · [Training kit](../workflow-training-kit.md)
