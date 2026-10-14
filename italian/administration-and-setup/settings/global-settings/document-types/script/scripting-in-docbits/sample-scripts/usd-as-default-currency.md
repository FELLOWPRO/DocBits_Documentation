---
description: Uno script che imposta USD come valuta predefinita e verifica se e valida o meno
---

# USD come Valuta Predefinita

### Panoramica

Lo script e progettato per impostare USD (Dollaro statunitense) come valuta predefinita per un'applicazione o sistema, assicurando che tutti i valori monetari vengano visualizzati ed elaborati in USD a meno che non sia specificato diversamente.

### Obiettivo

L'obiettivo principale di questo script e compilare automaticamente il campo valuta con USD e verificare se e valida o meno.

### Implementazione dello Script

#### Frammento di Codice

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
