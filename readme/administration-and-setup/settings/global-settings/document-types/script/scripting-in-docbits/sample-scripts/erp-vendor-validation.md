# ERP Leverancier Validatie

{% hint style="info" %}
**Beschikbaar vanaf versie 11.48.0** — Vereist `OPENSEARCH_ENABLED` licentie.
{% endhint %}

## Wat doet dit script?

Valideert of de leverancier op de factuur bestaat in de ERP-stamgegevens die in OpenSearch zijn geindexeerd. Als de leverancier niet in het ERP wordt gevonden, wordt het veld als ongeldig gemarkeerd. Dit vult de bestaande `is_supplier_valid()` functie aan door in de ERP-index te zoeken in plaats van in de opzoektabel.

## Trigger

`AFTER_FORMATTING` op documenttype **INVOICE**

## Volledig Script

```python
vendor = get_field_value(document_data, "supplier_name", "")

if vendor:
    erp_matches = fulltext_search_erp(
        org_id, vendor,
        entity_types="vendor",
        size=5
    )

    if not erp_matches:
        set_field_as_invalid(
            document_data, "supplier_name",
            "Vendor not found in ERP master data"
        )
```

## Variatie: Validatie met Leveranciersnummer

```python
vendor_nr = get_field_value(document_data, "supplier_id", "")

if vendor_nr:
    erp_matches = fulltext_search_erp(
        org_id, vendor_nr,
        entity_types="vendor",
        vendor_number=vendor_nr,
        size=1
    )

    if erp_matches:
        # Leveranciersnaam automatisch invullen vanuit ERP
        erp_vendor = erp_matches[0]
        set_field_value(document_data, "supplier_name",
                        erp_vendor.get("vendor_name", ""))
    else:
        set_field_as_invalid(
            document_data, "supplier_id",
            f"Vendor '{vendor_nr}' not found in ERP"
        )
```

## Stapsgewijze Uitleg

1. **Leveranciersnaam lezen** uit het huidige document
2. **ERP-stamgegevens doorzoeken** met `fulltext_search_erp()` gefilterd op entiteittype `"vendor"`
3. **Indien niet gevonden**: Leveranciersnaamveld als ongeldig markeren
4. **Variatie**: Zoeken op leveranciersnummer en leveranciersnaam automatisch invullen vanuit ERP-gegevens

## Gebruikte Functies

- [get\_field\_value()](../field-functions.md#get\_field\_value) — Veldwaarde lezen
- [fulltext\_search\_erp()](../fulltext-search-functions.md#fulltext\_search\_erp) — ERP-stamgegevens doorzoeken
- [set\_field\_as\_invalid()](../field-functions.md#set\_field\_as\_invalid) — Validatiefout weergeven
- [set\_field\_value()](../field-functions.md#set\_field\_value) — Veldwaarde schrijven
