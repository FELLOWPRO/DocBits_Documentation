# Skrypty w DocBits

## Przewodnik po skryptach DocBits

Witaj w przewodniku po skryptach DocBits! Tutaj dowiesz się, jak używać skryptów do automatyzacji i ulepszania przetwarzania dokumentów w DocBits. Skrypty pozwalają na manipulację niestandardowych pól, transformację danych oraz implementację logiki w różnych typach dokumentów.

### Rozpoczęcie

Skrypty w DocBits są pisane w języku Python. Współdziałają one z polami dokumentów i metadanymi, aby wykonywać szeroki zakres operacji, począwszy od prostego formatowania danych, aż po złożoną logikę.

#### Kluczowe Funkcje

* `get_field_value(fields_dict, field_name, default=None)`: Pobiera wartość określonego pola.
* `set_field_value(fields_dict, field_name, value)`: Ustawia wartość określonego pola.
* `create_new_field(field_name, value)`: Tworzy nowe pole o określonej nazwie i wartości.
* `format_decimal_to_locale(value, locale)`: Formatuje wartość dziesiętną zgodnie z określonym ustawieniem regionalnym.

### Przykładowe Skrypty

Poniżej znajdują się kilka przykładów demonstrujących powszechne zadania skryptowe.

#### Przykład 1: Mapowanie Walut dla Faktur

Standaryzuj symbole walut lub tekst na kody walut zgodne z normą ISO.
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

