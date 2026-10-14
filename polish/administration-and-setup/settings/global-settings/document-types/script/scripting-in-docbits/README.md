# Skrypty w DocBits

## Przewodnik po skryptach Docbits

Witamy w przewodniku po skryptach Docbits! Tutaj dowiesz się, jak używać skryptów do automatyzacji i ulepszania przetwarzania dokumentów w Docbits. Skrypty umożliwiają niestandardową manipulację polami, transformację danych i implementację logiki w różnych typach dokumentów.

### Pierwsze kroki

Skrypty w Docbits są pisane w języku Python. Wchodzą w interakcję z polami dokumentów i metadanymi, aby wykonywać szeroki zakres operacji, od prostego formatowania danych po złożoną logikę.

**Kluczowe funkcje**

* `get_field_value(fields_dict, field_name, default=None)`: Pobiera wartość określonego pola.
* `set_field_value(fields_dict, field_name, value)`: Ustawia wartość określonego pola.
* `create_new_field(field_name, value)`: Tworzy nowe pole o określonej nazwie i wartości.
* `format_decimal_to_locale(value, locale)`: Formatuje wartość dziesiętną zgodnie z określoną lokalizacją.

### Przykładowe skrypty

Poniżej znajduje się kilka przykładów demonstrujących typowe zadania skryptowe.

**Przykład 1: Mapowanie walut dla faktur**

Standaryzacja symboli walut lub tekstu do kodów walut ISO.

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
