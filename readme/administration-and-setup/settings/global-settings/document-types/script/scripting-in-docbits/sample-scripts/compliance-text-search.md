# Wyszukiwanie Tekstu Zgodnosci (Reverse Charge)

{% hint style="info" %}
**Dostepne od wersji 11.48.0** — Wymaga licencji `OPENSEARCH_ENABLED`.
{% endhint %}

## Co robi ten skrypt?

Wyszukuje tekst zwiazany ze zgodnosciami, taki jak "REVERSE CHARGE", w archiwum dokumentow. Jesli zostanal znalezione pasujace dokumenty, kod podatkowy jest automatycznie ustawiany. Obsluguje zarowno dokladne dopasowanie frazy, jak i wyszukiwanie rozmyte (tolerancja bledow OCR).

## Wyzwalacz

`AFTER_FORMATTING` na typie dokumentu **INVOICE**

## Pelny Skrypt

```python
# Szukaj "REVERSE CHARGE" w archiwum dokumentow organizacji
rc_docs = fulltext_search(
    org_id, "REVERSE CHARGE",
    search_type="match_phrase",
    doc_type="INVOICE",
    size=5
)

if rc_docs:
    set_field_value(document_data, "tax_code", "RC")
```

## Wariant: Wyszukiwanie Rozmyte (Tolerancja Bledow OCR)

```python
# Wyszukiwanie rozmyte toleruje bledy OCR jak "REVERS CHARG" lub "REVERSE GHARGE"
rc_fuzzy = fulltext_search(
    org_id, "REVERSE CHARGE",
    search_type="fuzzy",
    vendor_name="ACME Corp"
)

if rc_fuzzy:
    set_field_value(document_data, "tax_code", "RC")
```

## Wyjasnienie Krok po Kroku

1. **Przeszukaj archiwum** pod katem dokladnej frazy "REVERSE CHARGE" za pomoca `fulltext_search()`
2. **Filtruj po typie dokumentu** aby szukac tylko w fakturach
3. **Jesli znaleziono**: Automatycznie ustaw pole kodu podatkowego na "RC"
4. **Wariant rozmyty**: Uzyj `search_type="fuzzy"` aby wylapac bledy odczytu OCR (do 2 znakow roznicy)

## Uzyte Funkcje

- [fulltext\_search()](../fulltext-search-functions.md#fulltext\_search) — Przeszukaj tekst OCR wszystkich dokumentow
- [set\_field\_value()](../field-functions.md#set\_field\_value) — Zapisz wartosc pola
