---
description: Skripta koja postavlja USD kao podrazumevanu valutu i proverava da li je vazeca ili ne
---

# USD kao podrazumevana valuta

### Pregled

Skripta je dizajnirana da postavi USD (americki dolar) kao podrazumevanu valutu za aplikaciju ili sistem, osiguravajuci da se sve monetarne vrednosti prikazuju i obradjuju u USD osim ako nije drugacije navedeno.

### Cilj

Primarni cilj ove skripte je da automatski popuni polje valute sa USD i proveri da li je vazeca ili ne.

### Implementacija skripte

#### Isecak koda

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
