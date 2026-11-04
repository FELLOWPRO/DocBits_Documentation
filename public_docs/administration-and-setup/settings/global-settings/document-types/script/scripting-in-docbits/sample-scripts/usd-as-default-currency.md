---
description: A script that sets USD as the default currency and checks if its valid or not
---

# USD as Default Currency

### Overview

The script is designed to set USD (United States Dollar) as the default currency for an application or system, ensuring that all monetary values are displayed and processed in USD unless specified otherwise.

### Objective

The primary goal of this script is to automatically fill the currency field with USD and check if it is valid or not.

### Script Implementation

#### Code Snippet

```
// currency = get_field_value(document_data, 'currency', None)

if not currency:
    if 'currency' not in fields_dict:
        new_field = create_new_field('currency','')
        fields_dict['currency'] = new_field
        document_json['fields'].append(new_field)
    set_field_value(document_data, "currency", "USD")
    
elif currency == "USD US Dollar" or currency == "U.S. Dollars":
    set_field_value(document_data, "currency", "USD")
    
if currency != "USD" and currency != "EUR" and currency != "GBP" and currency != "CAD" and currency != "AUD" and currency != "CHF":
    set_field_as_invalid(document_data, "currency", "Currency is not valid")
else:
    set_field_attribute(document_data, "currency", "is_valid", True)
    set_field_attribute(document_data, "currency", "validation_message","")
```
