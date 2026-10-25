# Skrypty w DocBits

## Przewodnik po skryptach Docbits

Witamy w przewodniku po skryptach Docbits! Tutaj dowiesz się, jak używać skryptów do automatyzacji i ulepszania przetwarzania dokumentów w Docbits. Skrypty umożliwiają niestandardową manipulację polami, transformację danych i implementację logiki w różnych typach dokumentów.

### Pierwsze kroki

Skrypty w Docbits są pisane w języku Python. Wchodzą w interakcję z polami dokumentów i metadanymi, aby wykonywać szeroki zakres operacji, od prostego formatowania danych po złożoną logikę.

#### Kluczowe funkcje

Każdy skrypt otrzymuje dokument pod nazwą `document_data`. Przekazuj go jako pierwszy argument do funkcji pól. Pełną dokumentację znajdziesz na stronie [Funkcje Pol](field-functions.md).

* `get_field_value(document_data, field_name, default_value=None, is_clean=False)`: Odczytuje wartość pola.
* `set_field_value(document_data, field_name, value)`: Zapisuje wartość w polu i tworzy pole, jeśli nie istnieje.
* `set_date_value(document_data, field_name, value, add_days=0, skip_weekend=False)`: Zapisuje datę, opcjonalnie z dodaniem dni i pominięciem weekendów.
* `set_amount_value(document_data, field_name, value)`: Zapisuje kwotę sformatowaną zgodnie z lokalizacją dokumentu.
* `set_field_as_invalid(document_data, field_name, message, code=None)`: Oznacza pole jako nieprawidłowe i wyświetla użytkownikowi komunikat.
* `set_is_required(document_data, field_name, value)`: Ustawia pole jako wymagane lub opcjonalne.

### Przykładowe skrypty

Poniżej znajduje się kilka przykładów demonstrujących typowe zadania skryptowe.

#### Przykład 1: Mapowanie walut dla faktur

Standaryzacja symboli walut lub tekstu do kodów walut ISO.

```python
currency_map = {
    "€": "EUR",
    "EURO": "EUR",
    "$": "USD",
    "£": "GBP"
}
currency_value = get_field_value(document_data, "currency", None)
if currency_value:
    currency_value = currency_value.upper()
    if currency_value in currency_map:
        currency_value = currency_map[currency_value]
    set_field_value(document_data, "currency", currency_value)
```


