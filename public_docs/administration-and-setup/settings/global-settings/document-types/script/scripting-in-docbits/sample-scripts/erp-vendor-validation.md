# Validation de Fournisseur ERP

{% hint style="info" %}
**Disponible à partir de la version 11.48.0** — Nécessite la licence `OPENSEARCH_ENABLED`.
{% endhint %}

## Que fait ce script ?

Vérifie si le fournisseur de la facture existe dans les données de référence ERP indexées dans OpenSearch. Si le fournisseur n'est pas trouvé dans l'ERP, le champ est marqué comme invalide.

## Déclencheur

`AFTER_FORMATTING` sur le type de document **INVOICE**

## Script Complet

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
            "Fournisseur introuvable dans les données de référence ERP"
        )
```

## Variante : Validation avec Numéro de Fournisseur

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
        erp_vendor = erp_matches[0]
        set_field_value(document_data, "supplier_name",
                        erp_vendor.get("vendor_name", ""))
    else:
        set_field_as_invalid(
            document_data, "supplier_id",
            f"Fournisseur '{vendor_nr}' introuvable dans l'ERP"
        )
```

## Fonctions Utilisées

- [get\_field\_value()](../field-functions.md#get\_field\_value)
- [fulltext\_search\_erp()](../fulltext-search-functions.md#fulltext\_search\_erp)
- [set\_field\_as\_invalid()](../field-functions.md#set\_field\_as\_invalid)
- [set\_field\_value()](../field-functions.md#set\_field\_value)
