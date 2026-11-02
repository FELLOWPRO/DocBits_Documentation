# Tax Code Detection

## What does this script do?

Automatically determines the correct tax code based on the document's fulltext content and tax/net amounts. Detects reverse charge scenarios, tax-free invoices, and calculates the tax rate to assign the appropriate code (e.g., S1 for 19%, S2 for 7%).

## Trigger

`AFTER_FORMATTING` on document type **INVOICE**

## Full Script

```python
# Get document fulltext and amounts
content = get_document_content(document_data)
tax_amount = get_field_value(document_data, "tax_amount", "0")
net_amount = get_field_value(document_data, "net_amount", "0")

try:
    tax = float(tax_amount) if tax_amount else 0
    net = float(net_amount) if net_amount else 0
except ValueError:
    tax = 0
    net = 0

# Rule 1: Reverse charge detection via fulltext
if "REVERSE CHARGE" in content.upper() or "UMKEHR DER STEUERSCHULD" in content.upper():
    set_field_value(document_data, "tax_code", "RC")

# Rule 2: Zero tax = tax-free
elif tax == 0:
    set_field_value(document_data, "tax_code", "Z0")

# Rule 3: Calculate tax rate from amounts
elif net > 0:
    tax_rate = round((tax / net) * 100, 0)
    if tax_rate == 19:
        set_field_value(document_data, "tax_code", "S1")    # Standard rate
    elif tax_rate == 7:
        set_field_value(document_data, "tax_code", "S2")    # Reduced rate
    else:
        set_field_value(document_data, "tax_code", "S3")    # Other rate
```

## Step-by-Step Explanation

1. **Read fulltext** with `get_document_content()` for keyword detection
2. **Read tax and net amounts** for tax rate calculation
3. **Check for reverse charge** keywords in the document text (German and English)
4. **Check for zero tax** — if tax amount is 0, assign tax-free code
5. **Calculate tax rate** from tax/net ratio and assign the matching code

## Functions Used

- [get\_document\_content()](../business-logic-functions.md#get\_document\_content) — Read OCR fulltext
- [get\_field\_value()](../field-functions.md#get\_field\_value) — Read field values
- [set\_field\_value()](../field-functions.md#set\_field\_value) — Set tax code
