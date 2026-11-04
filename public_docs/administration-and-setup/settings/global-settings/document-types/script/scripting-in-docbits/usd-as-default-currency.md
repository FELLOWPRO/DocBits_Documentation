---
description: Um script que define USD como a moeda padrão e verifica se ela é válida ou não
---

# USD como Moeda Padrão

### Visão Geral

O script foi projetado para definir o USD (Dólar dos Estados Unidos) como a moeda padrão para um aplicativo ou sistema, garantindo que todos os valores monetários sejam exibidos e processados em USD, a menos que especificado de outra forma.

### Objetivo

O objetivo principal deste script é preencher automaticamente o campo de moeda com USD e verificar se ele é válido ou não.

### Implementação do Script

#### Snippet de Código

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
    set_field_as_invalid(document_data, "currency", "A moeda não é válida")
else:
    set_field_attribute(document_data, "currency", "is_valid", True)
    set_field_attribute(document_data, "currency", "validation_message","")
```
