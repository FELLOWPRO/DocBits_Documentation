# Validation Fournisseur ERP

{% hint style="info" %}
**Disponible à partir de la version 11.48.0** — Nécessite la licence `OPENSEARCH_ENABLED`.
{% endhint %}

## Que fait ce script ?

Vérifie si le fournisseur de la facture existe dans les données maîtres ERP indexées dans OpenSearch.

## Déclencheur

`AFTER_FORMATTING` sur le type de document **INVOICE**

## Script Complet

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
            "Fournisseur non trouvé dans les données maîtres ERP"
        )
```

## Fonctions Utilisées

- [get\_field\_value()](../field-functions.md#get\_field\_value)
- [fulltext\_search\_erp()](../fulltext-search-functions.md#fulltext\_search\_erp)
- [set\_field\_as\_invalid()](../field-functions.md#set\_field\_as\_invalid)
