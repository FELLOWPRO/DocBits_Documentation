# Scripting in DocBits

## Video guide: the most important script functions

{% embed url="https://docbits-videos.fra1.cdn.digitaloceanspaces.com/settings-assistant/doc-config-script-functions/v3/en.mp4" %}
The most important script functions in DocBits
{% endembed %}

The video shows in the script editor how to read a field (`get_field_value`), set a value (`set_field_value`), calculate a due date (`set_date_value`), mark a field as invalid (`set_field_as_invalid`) and make a field required (`set_is_required`).

## Docbits Scripting Guide

Welcome to the Docbits scripting guide! Here, you'll learn how to use scripts to automate and enhance your document processing within Docbits. Scripts allow for custom field manipulation, data transformation, and logic implementation across various document types.

### Getting Started

Scripts in Docbits are written in Python. They interact with document fields and metadata to perform a wide range of operations, from simple data formatting to complex logic.

#### Key Functions

Every script receives the document as `document_data`. Pass it as the first argument to the field functions. The full reference is on the [Field Functions](field-functions.md) page.

* `get_field_value(document_data, field_name, default_value=None, is_clean=False)`: Reads the value of a field.
* `set_field_value(document_data, field_name, value)`: Writes a value into a field and creates the field if it does not exist.
* `set_date_value(document_data, field_name, value, add_days=0, skip_weekend=False)`: Writes a date, optionally adding days and skipping weekends.
* `set_amount_value(document_data, field_name, value)`: Writes an amount formatted for the document's locale.
* `set_field_as_invalid(document_data, field_name, message, code=None)`: Marks a field as invalid and shows the message to the user.
* `set_is_required(document_data, field_name, value)`: Makes a field required or optional.

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
currency_value = get_field_value(document_data, "currency", None)
if currency_value:
    currency_value = currency_value.upper()
    if currency_value in currency_map:
        currency_value = currency_map[currency_value]
    set_field_value(document_data, "currency", currency_value)
```


