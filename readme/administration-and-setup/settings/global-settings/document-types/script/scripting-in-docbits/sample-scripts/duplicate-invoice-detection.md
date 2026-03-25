# Dubbele Factuur Detectie

{% hint style="info" %}
**Beschikbaar vanaf versie 11.48.0** — Vereist `OPENSEARCH_ENABLED` licentie.
{% endhint %}

## Wat doet dit script?

Doorzoekt het documentarchief op bestaande facturen met hetzelfde factuurnummer van dezelfde leverancier. Als een mogelijk duplicaat wordt gevonden, wordt het factuurnummerveld als ongeldig gemarkeerd met een waarschuwing die de documentnaam en status van het duplicaat toont.

## Trigger

`AFTER_FORMATTING` op documenttype **INVOICE**

## Volledig Script

```python
inv_id = get_field_value(document_data, "invoice_id", "")
vendor = get_field_value(document_data, "supplier_name", "")

if inv_id and vendor:
    # Zoek naar documenten met hetzelfde factuurnummer van dezelfde leverancier
    existing = fulltext_search(
        org_id, inv_id,
        vendor_name=vendor,
        status="ready_for_validation,exported",
        size=5
    )

    # Huidig document uitsluiten van resultaten
    current_doc_id = document_json["doc_id"]
    duplicates = [d for d in existing if d["doc_id"] != current_doc_id]

    if duplicates:
        dup = duplicates[0]
        set_field_as_invalid(
            document_data, "invoice_id",
            f"Possible duplicate: {dup['name']} ({dup.get('status', 'unknown')})"
        )
```

## Stapsgewijze Uitleg

1. **Factuurnummer en leverancier lezen** uit het huidige document
2. **Archief doorzoeken** met `fulltext_search()` gefilterd op leveranciersnaam en relevante statussen
3. **Huidig document uitsluiten** van resultaten om zelfovereenkomsten te voorkomen
4. **Als ongeldig markeren** als een duplicaat wordt gevonden, met weergave van bestandsnaam en status van het bestaande document

## Gebruikte Functies

- [get\_field\_value()](../field-functions.md#get\_field\_value) — Veldwaarde lezen
- [fulltext\_search()](../fulltext-search-functions.md#fulltext\_search) — OCR-tekst doorzoeken in alle documenten
- [set\_field\_as\_invalid()](../field-functions.md#set\_field\_as\_invalid) — Validatiefout weergeven
