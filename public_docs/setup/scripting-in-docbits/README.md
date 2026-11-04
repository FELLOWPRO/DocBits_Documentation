# Scripting in DocBits

## Docbits Scripting Guide

Welcome to the Docbits scripting guide! Here, you'll learn how to use scripts to automate and enhance your document processing within Docbits. Scripts allow for custom field manipulation, data transformation, and logic implementation across various document types.

### Getting Started

Scripts in Docbits are written in Python. They interact with document fields and metadata to perform a wide range of operations, from simple data formatting to complex logic.

#### Key Functions

* `get_field_value(fields_dict, field_name, default=None)`: Retrieves the value of a specified field.
* `set_field_value(fields_dict, field_name, value)`: Sets the value of a specified field.
* `create_new_field(field_name, value)`: Creates a new field with a specified name and value.
* `format_decimal_to_locale(value, locale)`: Formats a decimal value according to a specified locale.

### Example Scripts

Below are several examples demonstrating common scripting tasks.

#### Example 1: Currency Mapping for Invoices

Standardize currency symbols or text to ISO currency codes.

```python
currency_map = {
    "€": "EUR",
    "EURO": "EUR",
    "$": "USD",
    "£": "GBP"
}
currency_value = get_field_value(fields_dict, "currency", None)
if currency_value:
    currency_value = currency_value.upper()
    if currency_value in currency_map:
        currency_value = currency_map[currency_value]
    set_field_value(fields_dict, "currency", currency_value)
```

