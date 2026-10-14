# Walidacja Dostawcy ERP

{% hint style="info" %}
**Dostepne od wersji 11.48.0** — Wymaga licencji `OPENSEARCH_ENABLED`.
{% endhint %}

## Co robi ten skrypt?

Sprawdza, czy dostawca na fakturze istnieje w danych bazowych ERP zaindeksowanych w OpenSearch. Jesli dostawca nie zostanie znaleziony w ERP, pole jest oznaczane jako nieprawidlowe. Uzupelnia istniejaca funkcje `is_supplier_valid()` przeszukujac indeks ERP zamiast tabeli wyszukiwania.

## Wyzwalacz

`AFTER_FORMATTING` na typie dokumentu **INVOICE**

## Pelny Skrypt

```python
vendor = get_field_value(document_data, "supplier_name", "")

if vendor:
    erp_matches = fulltext_search_erp(
        vendor,
        entity_types="vendor",
        size=5
    )

    if not erp_matches:
        set_field_as_invalid(
            document_data, "supplier_name",
            "Vendor not found in ERP master data"
        )
```

## Wariant: Walidacja z Numerem Dostawcy

```python
vendor_nr = get_field_value(document_data, "supplier_id", "")

if vendor_nr:
    erp_matches = fulltext_search_erp(
        vendor_nr,
        entity_types="vendor",
        vendor_number=vendor_nr,
        size=1
    )

    if erp_matches:
        # Automatycznie uzupelnij nazwe dostawcy z ERP
        erp_vendor = erp_matches[0]
        set_field_value(document_data, "supplier_name",
                        erp_vendor.get("vendor_name", ""))
    else:
        set_field_as_invalid(
            document_data, "supplier_id",
            f"Vendor '{vendor_nr}' not found in ERP"
        )
```

## Wyjasnienie Krok po Kroku

1. **Odczytaj nazwe dostawcy** z biezacego dokumentu
2. **Przeszukaj dane bazowe ERP** za pomoca `fulltext_search_erp()` filtrujac po typie encji `"vendor"`
3. **Jesli nie znaleziono**: Oznacz pole nazwy dostawcy jako nieprawidlowe
4. **Wariant**: Szukaj po numerze dostawcy i automatycznie uzupelnij nazwe dostawcy z danych ERP

## Uzyte Funkcje

- [get\_field\_value()](../field-functions.md#get\_field\_value) — Odczytaj wartosc pola
- [fulltext\_search\_erp()](../fulltext-search-functions.md#fulltext\_search\_erp) — Przeszukaj dane bazowe ERP
- [set\_field\_as\_invalid()](../field-functions.md#set\_field\_as\_invalid) — Pokaz blad walidacji
- [set\_field\_value()](../field-functions.md#set\_field\_value) — Zapisz wartosc pola
