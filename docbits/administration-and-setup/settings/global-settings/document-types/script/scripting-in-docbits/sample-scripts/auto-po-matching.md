# Auto PO Matching

## What does this script do?

Automatically triggers PO (Purchase Order) matching when a PO number is present on the invoice. The po-match-service microservice compares invoice line items against the PO and populates match results.

## Trigger

`AFTER_FORMATTING` on document type **INVOICE**

## Full Script

```python
# Read PO number from the document
po_nr = get_field_value(document_data, "purchase_order", "")

if po_nr:
    # Clean up PO number: remove prefix and whitespace
    po_nr = po_nr.strip()
    if po_nr.upper().startswith("PO"):
        po_nr = po_nr[2:].strip()
    if po_nr.startswith("-") or po_nr.startswith(" "):
        po_nr = po_nr[1:].strip()

    # Update cleaned PO number
    set_field_value(document_data, "purchase_order", po_nr)

    # Trigger automatic PO matching
    auto_po_match_for_purchase_orders(user, document_data, po_nr)
```

## Step-by-Step Explanation

1. **Read PO number** from the invoice
2. **Clean up** the PO number by removing common prefixes like "PO-" or "PO "
3. **Update** the cleaned PO number back to the document
4. **Trigger PO matching** which calls the po-match-service to compare invoice lines against PO lines

## What happens after matching?

The `document_data` is updated with:
- `po_items` — Matched PO line items
- `po_match_status` — Match result (`"matched"`, `"partially_matched"`, etc.)
- `po_multi_matched` — Whether multiple POs were matched

## Functions Used

- [get\_field\_value()](../field-functions.md#get\_field\_value) — Read field value
- [set\_field\_value()](../field-functions.md#set\_field\_value) — Write cleaned PO number
- [auto\_po\_match\_for\_purchase\_orders()](../business-logic-functions.md#auto\_po\_match\_for\_purchase\_orders) — Trigger PO matching
