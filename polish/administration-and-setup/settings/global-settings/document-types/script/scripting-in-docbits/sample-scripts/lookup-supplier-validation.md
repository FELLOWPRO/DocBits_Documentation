# Walidacja Dostawcy przez Lookup

## Co robi ten skrypt?

Waliduje numer dostawcy z faktury względem danych podstawowych w tabeli wyszukiwania. Jeśli dostawca zostanie znaleziony, jego nazwa i warunki płatności są automatycznie uzupełniane. Jeśli nie zostanie znaleziony, pole jest oznaczane jako nieprawidłowe, aby użytkownik mógł je poprawić.

## Wyzwalacz

`AFTER_FORMATTING` na typie dokumentu **INVOICE**

## Pełny skrypt

```python
# Odczytaj ID dostawcy z dokumentu
supplier_id = get_field_value(document_data, "supplier_id", "")

if supplier_id:
    # Odpytaj tabelę wyszukiwania dostawców
    records = get_lookup_records(
        org_id,                                    # Bieżąca organizacja
        document_json.get("sub_org_id"),           # Podorganizacja (jeśli dotyczy)
        "supplier",                                # Nazwa tabeli wyszukiwania
        [["VENDOR_ID", supplier_id]],              # Filtr: dokładne dopasowanie VENDOR_ID
        limit=1                                    # Potrzebujemy tylko pierwszego wyniku
    )

    if records:
        # Dostawca znaleziony — automatyczne uzupełnienie powiązanych pól
        supplier = records[0]
        set_field_value(document_data, "supplier_name", supplier.get("NAME", ""))
        set_field_value(document_data, "payment_terms", supplier.get("PAYMENT_TERMS", ""))
    else:
        # Dostawca nie znaleziony — oznacz jako nieprawidłowy
        set_field_as_invalid(document_data, "supplier_id",
                             f"Dostawca '{supplier_id}' nie znaleziony w danych podstawowych")
```

## Wyjaśnienie krok po kroku

1. **Odczytaj ID dostawcy** z dokumentu za pomocą `get_field_value()`
2. **Odpytaj tabelę wyszukiwania** za pomocą `get_lookup_records()` używając ID dostawcy jako filtra
3. **Przy dopasowaniu**: Automatyczne uzupełnienie nazwy dostawcy i warunków płatności z danych podstawowych
4. **Przy braku dopasowania**: Oznaczenie pola ID dostawcy jako nieprawidłowego z opisowym komunikatem błędu

## Użyte funkcje

- [get\_field\_value()](../field-functions.md#get\_field\_value) — Odczyt wartości pola
- [get\_lookup\_records()](../business-logic-functions.md#get\_lookup\_records) — Odpytywanie danych podstawowych
- [set\_field\_value()](../field-functions.md#set\_field\_value) — Zapis wartości pola
- [set\_field\_as\_invalid()](../field-functions.md#set\_field\_as\_invalid) — Wyświetlanie błędu walidacji
