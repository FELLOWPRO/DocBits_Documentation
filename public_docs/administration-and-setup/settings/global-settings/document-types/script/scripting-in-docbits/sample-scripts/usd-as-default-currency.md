---
description: Een script dat USD instelt als standaardvaluta en controleert of deze geldig is of niet
---

# USD als Standaardvaluta

### Overzicht

Het script is ontworpen om USD (Amerikaanse dollar) in te stellen als de standaardvaluta voor een applicatie of systeem, zodat alle monetaire waarden worden weergegeven en verwerkt in USD, tenzij anders aangegeven.

### Doelstelling

Het primaire doel van dit script is om het valutaveld automatisch te vullen met USD en te controleren of deze geldig is of niet.

### Script-implementatie

#### Codefragment

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
