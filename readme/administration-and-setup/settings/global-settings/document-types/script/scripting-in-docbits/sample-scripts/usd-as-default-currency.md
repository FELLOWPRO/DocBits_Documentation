---
description: USD'yi varsayılan para birimi olarak ayarlayan ve geçerli olup olmadığını kontrol eden bir script
---

# Varsayılan Para Birimi Olarak USD

### Genel Bakış

Script, bir uygulama veya sistem için varsayılan para birimi olarak USD (Amerikan Doları) ayarlamak üzere tasarlanmıştır ve aksi belirtilmedikçe tüm parasal değerlerin USD olarak görüntülenmesini ve işlenmesini sağlar.

### Amaç

Bu scriptin temel amacı, para birimi alanını otomatik olarak USD ile doldurmak ve geçerli olup olmadığını kontrol etmektir.

### Script Uygulaması

#### Kod Parçası

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
