# Generating Extended Invoice Numbers Script for Docbits

This document details the "Generating Extended Invoice Numbers" script, which automates the creation of extended invoice numbers in Docbits. Extended invoice numbers combine multiple document identifiers, such as the invoice ID and the purchase order number, into a single, comprehensive identifier. This script enhances document traceability and simplifies record-keeping.

### Purpose

The purpose of this script is to streamline the process of generating extended invoice numbers by automatically concatenating the invoice ID and purchase order number, thereby providing a unified and unique identifier for each invoice document.

### Script Overview

The script checks for the presence of invoice ID and purchase order number fields within the document, concatenates their values if both are present (separated by a hyphen), and updates or creates a new field to store the combined value.

#### Code Snippet

```python
invoice_id = get_field_value(fields_dict, 'invoice_id')
purchase_order = get_field_value(fields_dict, 'purchase_order')

# Combining invoice ID and purchase order number with a hyphen separator
extended_number = '-'.join(filter(None, [invoice_id, purchase_order]))

# Check if there is an extended number to set
if extended_number:
    # Updating the 'invoice_extended_number' field with the combined value
    if not 'invoice_extended_number' in fields_dict:
        new_field = create_new_field('invoice_extended_number', extended_number)
        fields_dict['invoice_extended_number'] = new_field
        document_json['fields'].append(new_field)
    else:
        set_field_value(fields_dict, 'invoice_extended_number', extended_number)
```


