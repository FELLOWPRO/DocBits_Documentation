---
description: Un script que establece USD como moneda predeterminada y verifica si es valida o no
---

# USD como Moneda Predeterminada

### Descripcion General

El script esta disenado para establecer USD (Dolar estadounidense) como la moneda predeterminada para una aplicacion o sistema, asegurando que todos los valores monetarios se muestren y procesen en USD a menos que se especifique lo contrario.

### Objetivo

El objetivo principal de este script es llenar automaticamente el campo de moneda con USD y verificar si es valido o no.

### Implementacion del Script

#### Fragmento de Codigo

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
