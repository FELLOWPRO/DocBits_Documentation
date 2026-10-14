# Supplier Lookup Validation

## What does this script do?

Validates the supplier number from the invoice against master data in the lookup table. If the supplier is found, their name and payment terms are automatically filled in. If not found, the field is marked as invalid so the user can correct it.

## Trigger

`AFTER_FORMATTING` on document type **INVOICE**

## Full Script

```python
# Read supplier ID from the document
supplier_id = get_field_value(document_data, "supplier_id", "")

if supplier_id:
    # Query the supplier lookup table
    records = get_lookup_records(
        org_id,                                    # Current organization
        document_json.get("sub_org_id"),           # Sub-org (if applicable)
        "supplier",                                # Lookup table name
        [["VENDOR_ID", supplier_id]],              # Filter: exact match on VENDOR_ID
        limit=1                                    # Only need the first match
    )

    if records:
        # Supplier found — auto-fill related fields
        supplier = records[0]
        set_field_value(document_data, "supplier_name", supplier.get("NAME", ""))
        set_field_value(document_data, "payment_terms", supplier.get("PAYMENT_TERMS", ""))
    else:
        # Supplier not found — mark as invalid
        set_field_as_invalid(document_data, "supplier_id",
                             f"Supplier '{supplier_id}' not found in master data")
```

## Step-by-Step Explanation

1. **Read supplier ID** from the document using `get_field_value()`
2. **Query lookup table** with `get_lookup_records()` using the vendor ID as filter
3. **On match**: Auto-fill supplier name and payment terms from master data
4. **On no match**: Mark supplier ID field as invalid with a descriptive error message

## Functions Used

- [get\_field\_value()](../field-functions.md#get\_field\_value) — Read field value
- [get\_lookup\_records()](../business-logic-functions.md#get\_lookup\_records) — Query master data
- [set\_field\_value()](../field-functions.md#set\_field\_value) — Write field value
- [set\_field\_as\_invalid()](../field-functions.md#set\_field\_as\_invalid) — Show validation error
