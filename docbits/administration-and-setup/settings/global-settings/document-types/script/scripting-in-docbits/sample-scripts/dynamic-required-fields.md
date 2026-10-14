# Dynamic Required Fields

## What does this script do?

Dynamically sets field requirements based on document content. In this example: when the invoice currency is not EUR, the exchange rate field becomes mandatory and visible. For EUR invoices, the exchange rate field is hidden and optional.

## Trigger

`ON_FIELD_CHANGE` on document type **INVOICE**

## Full Script

```python
# Read current currency
currency = get_field_value(document_data, "currency", "EUR")

# Foreign currency: exchange rate is required and visible
if currency and currency != "EUR":
    set_is_required(document_data, "exchange_rate", True)
    set_is_hidden(document_data, "exchange_rate", False)
else:
    # EUR: exchange rate is optional and hidden
    set_is_required(document_data, "exchange_rate", False)
    set_is_hidden(document_data, "exchange_rate", True)
```

## Variation: Purchase invoice vs. cost invoice

```python
po = get_field_value(document_data, "purchase_order", "")

if po and po.strip():
    # Purchase invoice: PO number is required
    set_field_value(document_data, "invoice_category", "PURCHASE_INVOICE")
    set_is_required(document_data, "purchase_order", True)
else:
    # Cost invoice: PO number not needed, hide table
    set_field_value(document_data, "invoice_category", "COST_INVOICE")
    set_is_required(document_data, "purchase_order", False)
    delete_tables(document_data)
```

## Step-by-Step Explanation

1. **Read the controlling field** (currency in this case)
2. **Apply business rules** — different field requirements based on the value
3. **Set visibility** — hide irrelevant fields to keep the UI clean
4. **Set requirements** — make relevant fields mandatory

{% hint style="info" %}
**Trigger choice:** `ON_FIELD_CHANGE` runs every time a user modifies a field, so the requirements update in real-time. `AFTER_FORMATTING` only runs once after initial extraction.
{% endhint %}

## Functions Used

- [get\_field\_value()](../field-functions.md#get\_field\_value) — Read controlling field
- [set\_is\_required()](../field-functions.md#set\_is\_required) — Set field as mandatory/optional
- [set\_is\_hidden()](../field-functions.md#set\_is\_hidden) — Show/hide fields
- [set\_field\_value()](../field-functions.md#set\_field\_value) — Set category field
- [delete\_tables()](../table-functions.md#delete\_tables) — Remove tables for cost invoices
