# DocBits'te Scripting

## Docbits Scripting Rehberi

Docbits scripting rehberine hoş geldiniz! Burada, Docbits içinde belge işlemenizi otomatikleştirmek ve geliştirmek için scriptleri nasıl kullanacağınızı öğreneceksiniz. Scriptler, çeşitli belge türlerinde özel alan manipülasyonu, veri dönüşümü ve mantık uygulamasına olanak tanır.

### Başlarken

Docbits'teki scriptler Python ile yazılır. Basit veri biçimlendirmeden karmaşık mantığa kadar geniş bir yelpazede işlemler gerçekleştirmek için belge alanları ve meta verileriyle etkileşime girerler.

#### Temel Fonksiyonlar

* `get_field_value(fields_dict, field_name, default=None)`: Belirtilen bir alanın değerini getirir.
* `set_field_value(fields_dict, field_name, value)`: Belirtilen bir alanın değerini ayarlar.
* `create_new_field(field_name, value)`: Belirtilen ad ve değerle yeni bir alan oluşturur.
* `format_decimal_to_locale(value, locale)`: Ondalık bir değeri belirtilen yerel ayara göre biçimlendirir.

### Örnek Scriptler

Aşağıda yaygın scripting görevlerini gösteren çeşitli örnekler bulunmaktadır.

#### Örnek 1: Faturalar için Para Birimi Eşleştirme

Para birimi sembollerini veya metinlerini ISO para birimi kodlarına standartlaştırın.

```python
currency_map = {
    "€": "EUR",
    "EURO": "EUR",
    "$": "USD",
    "£": "GBP"
}
currency_value = get_field_value(fields_dict, "currency", None)
if currency_value:
    currency_value = currency_value.upper()
    if currency_value in currency_map:
        currency_value = currency_map[currency_value]
    set_field_value(fields_dict, "currency", currency_value)
```
