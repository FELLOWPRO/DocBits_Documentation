# Generating Extended Invoice Numbers Script for Docbits

### Overview

This guide focuses on automating the creation of extended invoice numbers in Docbits, a crucial feature for improving invoice management and tracking. The "Generating Extended Invoice Numbers" script concatenates various document identifiers, such as invoice ID and purchase order number, to create a comprehensive and unique identifier for each invoice.

### Objective

The primary goal of this script is to automate the generation of extended invoice numbers, facilitating easier tracking and management of invoices by combining multiple identifiers into a single, unique number.

### Script Implementation

#### Code Snippet

```python
# Retrieve the values of invoice ID and purchase order number from the document
invoice_id = get_field_value(fields_dict, 'invoice_id')
purchase_order = get_field_value(fields_dict, 'purchase_order')

# Concatenate the invoice ID and purchase order number with a hyphen if both exist
extended_number = '-'.join(filter(None, [invoice_id, purchase_order]))

# Check and update the 'invoice_extended_number' field with the concatenated value
if extended_number:
    if 'invoice_extended_number' not in fields_dict:
        new_field = create_new_field('invoice_extended_number', extended_number)
        fields_dict['invoice_extended_number'] = new_field
        document_json['fields'].append(new_field)
    else:
        set_field_value(fields_dict, 'invoice_extended_number', extended_number)
```


