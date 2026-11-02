# ERP Vendor Validation

{% hint style="info" %}
**Available from version 11.48.0** — Requires `OPENSEARCH_ENABLED` license.
{% endhint %}

## What does this script do?

Validates whether the vendor on the invoice exists in the ERP master data indexed in OpenSearch. If the vendor is not found in ERP, the field is marked as invalid. This complements the existing `is_supplier_valid()` function by searching the ERP index rather than the lookup table.

## Trigger

`AFTER_FORMATTING` on document type **INVOICE**

## Full Script

```python
vendor = get_field_value(document_data, "supplier_name", "")

if vendor:
    erp_matches = fulltext_search_erp(
        vendor,
        entity_types="vendor",
        size=5
    )

    if not erp_matches:
        set_field_as_invalid(
            document_data, "supplier_name",
            "Vendor not found in ERP master data"
        )
```

## Variant: Validate with Vendor Number

```python
vendor_nr = get_field_value(document_data, "supplier_id", "")

if vendor_nr:
    erp_matches = fulltext_search_erp(
        vendor_nr,
        entity_types="vendor",
        vendor_number=vendor_nr,
        size=1
    )

    if erp_matches:
        # Auto-fill vendor name from ERP
        erp_vendor = erp_matches[0]
        set_field_value(document_data, "supplier_name",
                        erp_vendor.get("vendor_name", ""))
    else:
        set_field_as_invalid(
            document_data, "supplier_id",
            f"Vendor '{vendor_nr}' not found in ERP"
        )
```

## Step-by-Step Explanation

1. **Read vendor name** from the current document
2. **Search ERP master data** with `fulltext_search_erp()` filtering by entity type `"vendor"`
3. **If not found**: Mark the supplier name field as invalid
4. **Variant**: Search by vendor number and auto-fill the vendor name from ERP data

## Functions Used

- [get\_field\_value()](../field-functions.md#get\_field\_value) — Read field value
- [fulltext\_search\_erp()](../fulltext-search-functions.md#fulltext\_search\_erp) — Search ERP master data
- [set\_field\_as\_invalid()](../field-functions.md#set\_field\_as\_invalid) — Show validation error
- [set\_field\_value()](../field-functions.md#set\_field\_value) — Write field value
