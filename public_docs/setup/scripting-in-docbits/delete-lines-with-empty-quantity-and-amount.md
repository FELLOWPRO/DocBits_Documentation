# Delete lines with empty quantity and amount

#### Part 1: Delete Lines with Empty Quantity and Amount

This section of the script processes an invoice table to remove any lines where both the quantity and the total amount are zero or not provided.

* **Check for INVOICE\_TABLE:** It starts by checking if the `INVOICE_TABLE` key exists in the `tables_dict` dictionary.
* **Iterate Over Rows:** For each row in the table, the script initializes flags and variables to determine if the `TOTAL_AMOUNT` and `QUANTITY` columns exist and to capture their values.
* **Check Column Names:** As it iterates through each column in a row, it looks for columns named `TOTAL_AMOUNT` and `QUANTITY`.
  * If `TOTAL_AMOUNT` is found, it captures the value. If this value is non-zero, it converts it to a float.
  * Similarly for `QUANTITY`, capturing and converting the value if it is non-zero.
* **Mark Row for Deletion:** After checking both columns in a row, if both the total amount and quantity are effectively zero (either by being zero or not existing), the row is marked for deletion by setting `row['is_deleted']` to `True`.

#### Part 2: Validate Line Total Against Invoice Total

This section calculates the total amount from all lines in an invoice and compares it to the invoice’s reported total to validate their consistency.

* **Initialize Line Total:** Starts by setting a variable `lines_total` to 0.0 to accumulate the total amount from all lines.
* **Sum Line Amounts:** Iterates over each row in the `INVOICE_TABLE`, extracting the `TOTAL_AMOUNT` from each and adding it to `lines_total`.
* **Retrieve and Convert Invoice Total:** Fetches the total invoice amount using a helper function `get_field_value` and converts it to a float.
* **Compare Totals:** Finally, it checks if the absolute difference between the calculated line total (`lines_total`) and the reported invoice total (`total_amount`) exceeds a threshold of 0.05. If so, it marks the invoice total field as invalid using another helper function `set_field_as_invalid`, citing a mismatch.

```python
##################################################
# Delete lines with empty quantity and amount 
##################################################


if tables_dict.get('INVOICE_TABLE'):
    for row in tables_dict['INVOICE_TABLE']['rows']:
        amount_col_found = False
        quantity_col_found = False
        line_amount = 0.0
        line_quantity = 0.0
        for col in row['columns']:
            if col['name'] == 'TOTAL_AMOUNT':
                amount_col_found = True
                line_amount = col.get('value', 0)
                if line_amount:
                    line_amount = float(line_amount)
            if col['name'] == 'QUANTITY':
                quantity_col_found = True
                line_quantity = col.get('value', 0)
                if line_quantity:
                    line_quantity = float(line_quantity)
            if amount_col_found and quantity_col_found:
                break
        if amount_col_found and quantity_col_found and (not line_amount and not line_quantity or (line_amount + line_quantity) == 0):
            row['is_deleted'] = True
        
##################################################
# End: Delete lines with empty quantity and amount 
##################################################

##################################################
# Validating Line total againg invoice total
##################################################
lines_total = 0.0
# Getting Lines Total
if tables_dict.get('INVOICE_TABLE'):
    for row in tables_dict['INVOICE_TABLE']['rows']:
        line_amount = 0.0
        for col in row['columns']:
            if col['name'] == 'TOTAL_AMOUNT':
                line_amount = col.get('value', 0)
                if line_amount:
                    line_amount = float(line_amount)
                break
        lines_total += line_amount

# Getting Invoice total
total_amount = get_field_value(fields_dict, "net_amount", "0.0")
if total_amount:
    total_amount = float(total_amount)

# Comparing lines total with invoice total    
if abs(total_amount - lines_total) > 0.05:
    set_field_as_invalid(fields_dict, "net_amount", "Invoice total mismatches lines total", "AMOUNTS_MISMATCH")

##################################################
# End: Validating Line total againg invoice total
##################################################






    
```

#### Summary

The script effectively ensures data integrity by:

1. Removing data rows that do not contribute to the invoice’s financial total due to lacking quantities or amounts.
2. Validating the consistency between the sum of individual line amounts and the overall invoice total, highlighting discrepancies for further action.

This automation helps maintain accurate financial records and can be crucial for systems like ERP that require precise data for accounting and financial reporting.

