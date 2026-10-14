# Table Sum Validation

## What does this script do?

Validates that the sum of all line totals in the invoice table matches the document's net amount. If there is a discrepancy greater than 0.01, the calculated sum replaces the extracted net amount — ensuring consistency between line items and header fields.

## Trigger

`AFTER_FORMATTING` on document type **INVOICE**

## Full Script

```python
table = tables_dict.get("INVOICE_TABLE")
if table:
    # Calculate sum of all line totals
    total = 0
    for row in table["rows"]:
        line_total = get_column_value(row, "LINE_TOTAL", "0")
        try:
            total += float(line_total)
        except ValueError:
            pass

    # Compare with extracted net amount
    net_amount = get_field_value(document_data, "net_amount", "0")
    try:
        if abs(float(net_amount) - total) > 0.01:
            # Line sum differs from header — update net amount
            set_amount_value(document_data, "net_amount", str(round(total, 2)))
    except ValueError:
        pass
```

## Variation: Mark as invalid instead of overwriting

```python
table = tables_dict.get("INVOICE_TABLE")
if table:
    total = 0
    for row in table["rows"]:
        line_total = get_column_value(row, "LINE_TOTAL", "0")
        try:
            total += float(line_total)
        except ValueError:
            pass

    net_amount = get_field_value(document_data, "net_amount", "0")
    try:
        diff = abs(float(net_amount) - total)
        if diff > 0.01:
            set_field_as_invalid(document_data, "net_amount",
                f"Line total sum ({round(total, 2)}) differs from net amount ({net_amount})")
        else:
            set_field_as_valid(document_data, "net_amount", "Amounts match")
    except ValueError:
        pass
```

## Step-by-Step Explanation

1. **Get invoice table** from `tables_dict`
2. **Sum all LINE_TOTAL values** across table rows
3. **Compare** calculated sum with the extracted net amount
4. **Update or flag** — either replace the net amount or mark it as invalid

## Functions Used

- [get\_column\_value()](../table-functions.md#get\_column\_value) — Read column values from rows
- [get\_field\_value()](../field-functions.md#get\_field\_value) — Read net amount
- [set\_amount\_value()](../field-functions.md#set\_amount\_value) — Set corrected amount
- [set\_field\_as\_invalid()](../field-functions.md#set\_field\_as\_invalid) — Mark field as invalid
- [set\_field\_as\_valid()](../field-functions.md#set\_field\_as\_valid) — Mark field as valid
