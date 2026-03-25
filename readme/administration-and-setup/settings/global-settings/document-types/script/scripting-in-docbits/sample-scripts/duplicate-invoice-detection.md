# Wykrywanie Duplikatow Faktur

{% hint style="info" %}
**Dostepne od wersji 11.48.0** — Wymaga licencji `OPENSEARCH_ENABLED`.
{% endhint %}

## Co robi ten skrypt?

Przeszukuje archiwum dokumentow w poszukiwaniu istniejacych faktur z tym samym numerem faktury od tego samego dostawcy. Jesli zostanie znaleziony potencjalny duplikat, pole numeru faktury jest oznaczane jako nieprawidlowe z ostrzezeniem pokazujacym nazwe i status duplikatu.

## Wyzwalacz

`AFTER_FORMATTING` na typie dokumentu **INVOICE**

## Pelny Skrypt

```python
inv_id = get_field_value(document_data, "invoice_id", "")
vendor = get_field_value(document_data, "supplier_name", "")

if inv_id and vendor:
    # Szukaj dokumentow z tym samym numerem faktury od tego samego dostawcy
    existing = fulltext_search(
        org_id, inv_id,
        vendor_name=vendor,
        status="ready_for_validation,exported",
        size=5
    )

    # Wyklucz biezacy dokument z wynikow
    current_doc_id = document_json["doc_id"]
    duplicates = [d for d in existing if d["doc_id"] != current_doc_id]

    if duplicates:
        dup = duplicates[0]
        set_field_as_invalid(
            document_data, "invoice_id",
            f"Possible duplicate: {dup['name']} ({dup.get('status', 'unknown')})"
        )
```

## Wyjasnienie Krok po Kroku

1. **Odczytaj numer faktury i dostawce** z biezacego dokumentu
2. **Przeszukaj archiwum** za pomoca `fulltext_search()` filtrujac po nazwie dostawcy i odpowiednich statusach
3. **Wyklucz biezacy dokument** z wynikow, aby uniknac samozgodnosci
4. **Oznacz jako nieprawidlowy** jesli znaleziono duplikat, pokazujac nazwe pliku i status istniejacego dokumentu

## Uzyte Funkcje

- [get\_field\_value()](../field-functions.md#get\_field\_value) — Odczytaj wartosc pola
- [fulltext\_search()](../fulltext-search-functions.md#fulltext\_search) — Przeszukaj tekst OCR wszystkich dokumentow
- [set\_field\_as\_invalid()](../field-functions.md#set\_field\_as\_invalid) — Pokaz blad walidacji
