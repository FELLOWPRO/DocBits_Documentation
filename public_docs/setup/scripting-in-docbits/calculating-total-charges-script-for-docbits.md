# Calculating Total Charges Script for Docbits

### Introduction

This document provides a detailed guide on the "Calculating Total Charges" script within the Docbits platform. The script is designed to automatically calculate the total amount charged on an invoice by summing up various individual charges. This automation enhances accuracy and efficiency in document processing.

### Objective

The aim of this script is to streamline the calculation process for total charges on invoices. By automatically adding up specified charges, such as base charges, taxes, and additional fees, the script ensures that the total charges reflected on each invoice are accurate and comprehensive.

### Script Details

#### Code Implementation

```python
# Initialize variables to store the values of individual charges
total_charges = get_field_value(fields_dict, 'total_charges', None)
fracht = get_field_value(fields_dict, 'additional_amount_2', None)
verpackung = get_field_value(fields_dict, 'additional_amount', None)

# Calculate the total by converting each charge to a float and summing them up
total = 0
if fracht:
    total += float(fracht)
if verpackung:
    total += float(verpackung)

# Format the total to two decimal places and update the 'total_charges' field
formatted_total = "{0:.2f}".format(total)
if 'total_charges' not in fields_dict:
    new_field = create_new_field('total_charges', formatted_total)
    fields_dict['total_charges'] = new_field
    document_json['fields'].append(new_field)
else:
    set_field_value(fields_dict, 'total_charges', formatted_total)
```

