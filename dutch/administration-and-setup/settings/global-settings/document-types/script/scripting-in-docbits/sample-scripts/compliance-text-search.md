# Compliance Tekstzoeken (Reverse Charge)

{% hint style="info" %}
**Beschikbaar vanaf versie 11.48.0** — Vereist `OPENSEARCH_ENABLED` licentie.
{% endhint %}

## Wat doet dit script?

Zoekt naar compliance-relevante tekst zoals "REVERSE CHARGE" in het documentarchief. Als overeenkomende documenten bestaan, wordt de belastingcode automatisch ingesteld. Ondersteunt zowel exacte frase-matching als fuzzy zoeken (fouttolerant voor OCR-fouten).

## Trigger

`AFTER_FORMATTING` op documenttype **INVOICE**

## Volledig Script

```python
# Zoek naar "REVERSE CHARGE" in het documentarchief van de organisatie
rc_docs = fulltext_search(
    "REVERSE CHARGE",
    search_type="match_phrase",
    doc_type="INVOICE",
    size=5
)

if rc_docs:
    set_field_value(document_data, "tax_code", "RC")
```

## Variatie: Fuzzy Zoeken (OCR-fouttolerant)

```python
# Fuzzy zoeken tolereert OCR-fouten zoals "REVERS CHARG" of "REVERSE GHARGE"
rc_fuzzy = fulltext_search(
    "REVERSE CHARGE",
    search_type="fuzzy",
    vendor_name="ACME Corp"
)

if rc_fuzzy:
    set_field_value(document_data, "tax_code", "RC")
```

## Stapsgewijze Uitleg

1. **Archief doorzoeken** op de exacte frase "REVERSE CHARGE" met `fulltext_search()`
2. **Filteren op documenttype** om alleen in facturen te zoeken
3. **Indien gevonden**: Belastingcodeveld automatisch instellen op "RC"
4. **Fuzzy variatie**: Gebruik `search_type="fuzzy"` om OCR-leesfouten op te vangen (tot 2 tekens verschil)

## Gebruikte Functies

- [fulltext\_search()](../fulltext-search-functions.md#fulltext\_search) — OCR-tekst doorzoeken in alle documenten
- [set\_field\_value()](../field-functions.md#set\_field\_value) — Veldwaarde schrijven
