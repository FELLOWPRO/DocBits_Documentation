# Dynamiczne Pola Wymagane

## Co robi ten skrypt?

Dynamicznie ustawia wymagania pól na podstawie zawartości dokumentu. W tym przykładzie: gdy waluta faktury nie jest EUR, pole kursu wymiany staje się obowiązkowe i widoczne. Dla faktur w EUR pole kursu wymiany jest ukryte i opcjonalne.

## Wyzwalacz

`ON_FIELD_CHANGE` na typie dokumentu **INVOICE**

## Pełny skrypt

```python
# Odczytaj bieżącą walutę
currency = get_field_value(document_data, "currency", "EUR")

# Waluta obca: kurs wymiany jest wymagany i widoczny
if currency and currency != "EUR":
    set_is_required(document_data, "exchange_rate", True)
    set_is_hidden(document_data, "exchange_rate", False)
else:
    # EUR: kurs wymiany jest opcjonalny i ukryty
    set_is_required(document_data, "exchange_rate", False)
    set_is_hidden(document_data, "exchange_rate", True)
```

## Wariant: Faktura zakupowa vs. faktura kosztowa

```python
po = get_field_value(document_data, "purchase_order", "")

if po and po.strip():
    # Faktura zakupowa: numer ZZ jest wymagany
    set_field_value(document_data, "invoice_category", "PURCHASE_INVOICE")
    set_is_required(document_data, "purchase_order", True)
else:
    # Faktura kosztowa: numer ZZ nie jest potrzebny, ukryj tabelę
    set_field_value(document_data, "invoice_category", "COST_INVOICE")
    set_is_required(document_data, "purchase_order", False)
    delete_tables(document_data)
```

## Wyjaśnienie krok po kroku

1. **Odczytaj pole sterujące** (w tym przypadku walutę)
2. **Zastosuj reguły biznesowe** — różne wymagania pól na podstawie wartości
3. **Ustaw widoczność** — ukryj nieistotne pola, aby interfejs był przejrzysty
4. **Ustaw wymagania** — ustaw odpowiednie pola jako obowiązkowe

{% hint style="info" %}
**Wybór wyzwalacza:** `ON_FIELD_CHANGE` uruchamia się za każdym razem gdy użytkownik modyfikuje pole, więc wymagania aktualizują się w czasie rzeczywistym. `AFTER_FORMATTING` uruchamia się tylko raz po początkowej ekstrakcji.
{% endhint %}

## Użyte funkcje

- [get\_field\_value()](../field-functions.md#get\_field\_value) — Odczyt pola sterującego
- [set\_is\_required()](../field-functions.md#set\_is\_required) — Ustawienie pola jako obowiązkowego/opcjonalnego
- [set\_is\_hidden()](../field-functions.md#set\_is\_hidden) — Pokazywanie/ukrywanie pól
- [set\_field\_value()](../field-functions.md#set\_field\_value) — Ustawienie pola kategorii
- [delete\_tables()](../table-functions.md#delete\_tables) — Usuwanie tabel dla faktur kosztowych
