---
description: Ein Skript, das USD als Standardwährung festlegt und prüft, ob sie gültig ist oder nicht
---

# USD als Standardwährung

### Überblick

Das Skript ist darauf ausgelegt, USD (US-Dollar) als Standardwährung für eine Anwendung oder ein System festzulegen, um sicherzustellen, dass alle Geldbeträge in USD angezeigt und verarbeitet werden, sofern nicht anders angegeben.

### Ziel

Das Hauptziel dieses Skripts ist es, das Währungsfeld automatisch mit USD zu füllen und zu prüfen, ob es gültig ist oder nicht.

### Skript-Implementierung

#### Code-Ausschnitt

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
