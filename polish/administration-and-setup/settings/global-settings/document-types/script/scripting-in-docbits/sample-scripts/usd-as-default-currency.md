---
description: Skrypt ustawiający USD jako domyślną walutę i sprawdzający jej poprawność
---

# USD jako Domyślna Waluta

### Przegląd

Skrypt został zaprojektowany w celu ustawienia USD (Dolar Amerykański) jako domyślnej waluty dla aplikacji lub systemu, zapewniając, że wszystkie wartości pieniężne są wyświetlane i przetwarzane w USD, chyba że określono inaczej.

### Cel

Głównym celem tego skryptu jest automatyczne wypełnienie pola waluty wartością USD oraz sprawdzenie, czy jest ona poprawna.

### Implementacja Skryptu

#### Fragment Kodu

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
