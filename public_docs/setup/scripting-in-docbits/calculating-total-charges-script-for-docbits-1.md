# Calculating Total Charges Script for Docbits

##

The "Calculating Total Charges" script automates the process of summing up various charges and additional amounts within invoice documents. This guide walks you through the script setup, logic, and application to ensure accurate total charge calculations across your documents.

### Purpose

This script aims to provide a dynamic way to calculate the total charges on an invoice by adding up different charge types, such as base charges, freight (Fracht), and packaging (Verpackung). It then updates the invoice's total charges field with the calculated sum, ensuring accurate billing information.

### Script Overview

The script retrieves values from specified fields, converts them to floats, sums them up, and then updates the `total_charges` field with the result. If the `total_charges` field doesn't exist, the script creates this field and sets its value accordingly.

#### Code Snippet

```python
total_charges = get_field_value(fields_dict, 'total_charges', None)
fracht = get_field_value(fields_dict, 'additional_amount_2', None)
verpackung = get_field_value(fields_dict, 'additional_amount', None)

# Initialize total to 0
total = 0

# Add fracht to total if it exists
if fracht:
    fracht = float(fracht)
    total += fracht

# Add verpackung to total if it exists
if verpackung:
    verpackung = float(verpackung)
    total += verpackung

# Formatting the total to two decimal places
formatted_total = "{0:.2f}".format(total)

# Checking if the total_charges field exists and updating or creating accordingly
if 'total_charges' not in fields_dict:
    new_field = create_new_field('total_charges', formatted_total)
    fields_dict['total_charges'] = new_field
    document_json['fields'].append(new_field)
else:
    set_field_value(fields_dict, 'total_charges', formatted_total)
```

