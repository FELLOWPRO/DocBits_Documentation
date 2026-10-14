# Auto-Export Based on Conditions

## What does this script do?

Automatically sets the document status to "ready for export" when specific conditions are met: the supplier is a known/trusted vendor AND the invoice amount is below a threshold. This skips manual validation for low-risk invoices.

## Trigger

`AFTER_FORMATTING` on document type **INVOICE**

## Full Script

```python
# Read relevant fields
net = get_field_value(document_data, "net_amount", "0")
supplier = get_field_value(document_data, "supplier_name", "", is_clean=True)

try:
    net_float = float(net)
except ValueError:
    net_float = 0

# Define trusted suppliers for auto-export
auto_export_suppliers = ["OFFICEDEPOT", "STAPLES", "AMAZON"]

# Auto-export for known suppliers with small amounts
if any(s in supplier for s in auto_export_suppliers) and net_float < 500:
    doc_id = document_json["doc_id"]
    update_document_status_with_doc_id(
        doc_id, user, org_id, "ready_for_export",
        message="Auto-exported (small amount, known supplier)"
    )
```

## Step-by-Step Explanation

1. **Read net amount and supplier name** from the document (supplier with `is_clean=True` for comparison)
2. **Define trusted suppliers** — list of known vendor names (cleaned/uppercase)
3. **Check conditions** — supplier must be in the trusted list AND amount must be below 500
4. **Change status** to `"ready_for_export"` with a descriptive message

{% hint style="warning" %}
**Caution:** Status changes trigger downstream workflows (DocFlow, export hooks). Make sure the conditions are strict enough to avoid unintended exports.
{% endhint %}

## Functions Used

- [get\_field\_value()](../field-functions.md#get\_field\_value) — Read field values
- [update\_document\_status\_with\_doc\_id()](../business-logic-functions.md#update\_document\_status\_with\_doc\_id) — Change document status
