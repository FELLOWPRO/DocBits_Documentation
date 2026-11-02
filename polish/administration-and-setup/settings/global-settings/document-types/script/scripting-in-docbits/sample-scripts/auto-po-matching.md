# Automatyczne Dopasowanie ZZ

## Co robi ten skrypt?

Automatycznie uruchamia dopasowanie ZZ (Zamówienia Zakupu) gdy na fakturze obecny jest numer ZZ. Mikroserwis po-match-service porównuje pozycje faktury z pozycjami ZZ i uzupełnia wyniki dopasowania.

## Wyzwalacz

`AFTER_FORMATTING` na typie dokumentu **INVOICE**

## Pełny skrypt

```python
# Odczytaj numer ZZ z dokumentu
po_nr = get_field_value(document_data, "purchase_order", "")

if po_nr:
    # Wyczyść numer ZZ: usuń prefiks i białe znaki
    po_nr = po_nr.strip()
    if po_nr.upper().startswith("PO"):
        po_nr = po_nr[2:].strip()
    if po_nr.startswith("-") or po_nr.startswith(" "):
        po_nr = po_nr[1:].strip()

    # Zaktualizuj oczyszczony numer ZZ
    set_field_value(document_data, "purchase_order", po_nr)

    # Uruchom automatyczne dopasowanie ZZ
    auto_po_match_for_purchase_orders(user, document_data, po_nr)
```

## Wyjaśnienie krok po kroku

1. **Odczytaj numer ZZ** z faktury
2. **Wyczyść** numer ZZ usuwając typowe prefiksy jak "PO-" lub "PO "
3. **Zaktualizuj** oczyszczony numer ZZ w dokumencie
4. **Uruchom dopasowanie ZZ** które wywołuje po-match-service w celu porównania pozycji faktury z pozycjami ZZ

## Co się dzieje po dopasowaniu?

`document_data` jest aktualizowane o:
- `po_items` — Dopasowane pozycje ZZ
- `po_match_status` — Wynik dopasowania (`"matched"`, `"partially_matched"` itp.)
- `po_multi_matched` — Czy dopasowano wiele zamówień zakupu

## Użyte funkcje

- [get\_field\_value()](../field-functions.md#get\_field\_value) — Odczyt wartości pola
- [set\_field\_value()](../field-functions.md#set\_field\_value) — Zapis oczyszczonego numeru ZZ
- [auto\_po\_match\_for\_purchase\_orders()](../business-logic-functions.md#auto\_po\_match\_for\_purchase\_orders) — Uruchomienie dopasowania ZZ
