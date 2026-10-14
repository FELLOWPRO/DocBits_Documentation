# Due Date Calculation

## What does this script do?

Calculates the payment due date based on the invoice date by adding a configurable number of days (e.g., 30). Weekends are automatically skipped so the due date always falls on a business day.

## Trigger

`AFTER_FORMATTING` on document type **INVOICE**

## Full Script

```python
# Read invoice date
inv_date = get_field_value(document_data, "invoice_date")

if inv_date:
    # Calculate due date: 30 days after invoice date, skip weekends
    set_date_value(document_data, "due_date", inv_date,
                   add_days=30, skip_weekend=True)

    # Also set accounting date = invoice date
    set_date_value(document_data, "accounting_date", inv_date)
```

## Variations

### 14 days, excluding Mondays

```python
set_date_value(document_data, "due_date", inv_date,
               add_days=14, skip_weekend=True, exclude_final_days="MONDAY")
```

### 60 days, no weekend skip

```python
set_date_value(document_data, "due_date", inv_date, add_days=60)
```

### Set delivery date to today

```python
set_date_value(document_data, "delivery_date", None)  # None = today
```

## Step-by-Step Explanation

1. **Read invoice date** from the document
2. **Calculate due date** using `set_date_value()` with `add_days=30` and `skip_weekend=True`
3. **Date formatting** is automatic — uses the document's `date_format_pattern` (e.g., `%d.%m.%Y`)
4. **Weekend skip** ensures the due date falls on Mon-Fri

## Day Codes for `exclude_final_days`

`MONDAY`, `TUESDAY`, `WEDNESDAY`, `THURSDAY`, `FRIDAY`, `SATURDAY`, `SUNDAY`

## Functions Used

- [get\_field\_value()](../field-functions.md#get\_field\_value) — Read invoice date
- [set\_date\_value()](../field-functions.md#set\_date\_value) — Calculate and set due date
