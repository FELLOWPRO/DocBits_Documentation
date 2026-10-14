---
description: Un script qui définit USD comme devise par défaut et vérifie si elle est valide ou non
---

# USD comme Devise par Défaut

### Aperçu

Le script est conçu pour définir USD (Dollar américain) comme devise par défaut pour une application ou un système, garantissant que toutes les valeurs monétaires sont affichées et traitées en USD sauf indication contraire.

### Objectif

L'objectif principal de ce script est de remplir automatiquement le champ de devise avec USD et de vérifier si elle est valide ou non.

### Implémentation du Script

#### Extrait de Code

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
