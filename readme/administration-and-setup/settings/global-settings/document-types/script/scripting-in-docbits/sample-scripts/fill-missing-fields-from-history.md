# Uzupelnianie Brakujacych Pol z Historii

{% hint style="info" %}
**Dostepne od wersji 11.48.0** — Wymaga licencji `OPENSEARCH_ENABLED`.
{% endhint %}

## Co robi ten skrypt?

Gdy dokument posiada numer ZZ, ale brakuje nazwy dostawcy, ten skrypt przeszukuje archiwum dokumentow pod katem innych faktur zawierajacych ten sam numer ZZ i kopiuje nazwe dostawcy z pierwszego dopasowania.

## Wyzwalacz

`AFTER_FORMATTING` na typie dokumentu **INVOICE**

## Pelny Skrypt

```python
po = get_field_value(document_data, "purchase_order", "")
supplier = get_field_value(document_data, "supplier_name", "")

if po and not supplier:
    # Przeszukaj archiwum pod katem dokumentow z tym numerem ZZ
    history = fulltext_search(
        po,
        doc_type="INVOICE",
        size=3
    )

    for doc in history:
        if doc.get("vendor_name"):
            set_field_value(document_data, "supplier_name", doc["vendor_name"])
            break
```

## Wyjasnienie Krok po Kroku

1. **Odczytaj numer ZZ i dostawce** z biezacego dokumentu
2. **Sprawdz warunek**: Kontynuuj tylko jesli ZZ istnieje, ale brakuje dostawcy
3. **Przeszukaj archiwum** pod katem dokumentow zawierajacych numer ZZ
4. **Skopiuj nazwe dostawcy** z pierwszego dopasowania, ktore ma ustawiona nazwe dostawcy

## Wariant: Uzupelnij Wiele Pol

```python
po = get_field_value(document_data, "purchase_order", "")
supplier = get_field_value(document_data, "supplier_name", "")

if po and not supplier:
    history = fulltext_search(po, doc_type="INVOICE", size=3)

    for doc in history:
        if doc.get("vendor_name"):
            set_field_value(document_data, "supplier_name", doc["vendor_name"])
            # Uzupelnij rowniez inne pola jesli sa dostepne
            if doc.get("total_amount") and not get_field_value(document_data, "total_amount", ""):
                set_field_value(document_data, "total_amount", doc["total_amount"])
            break
```

## Uzyte Funkcje

- [get\_field\_value()](../field-functions.md#get\_field\_value) — Odczytaj wartosc pola
- [fulltext\_search()](../fulltext-search-functions.md#fulltext\_search) — Przeszukaj tekst OCR wszystkich dokumentow
- [set\_field\_value()](../field-functions.md#set\_field\_value) — Zapisz wartosc pola
