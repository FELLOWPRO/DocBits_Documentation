# Détection de Factures en Double

{% hint style="info" %}
**Disponible à partir de la version 11.48.0** — Nécessite la licence `OPENSEARCH_ENABLED`.
{% endhint %}

## Que fait ce script ?

Recherche dans l'archive de documents les factures existantes avec le même numéro de facture du même fournisseur. Si un doublon potentiel est trouvé, le champ du numéro de facture est marqué comme invalide.

## Déclencheur

`AFTER_FORMATTING` sur le type de document **INVOICE**

## Script Complet

```python
inv_id = get_field_value(document_data, "invoice_id", "")
vendor = get_field_value(document_data, "supplier_name", "")

if inv_id and vendor:
    existing = fulltext_search(
        org_id, inv_id,
        vendor_name=vendor,
        status="ready_for_validation,exported",
        size=5
    )
    current_doc_id = document_json["doc_id"]
    duplicates = [d for d in existing if d["doc_id"] != current_doc_id]

    if duplicates:
        dup = duplicates[0]
        set_field_as_invalid(
            document_data, "invoice_id",
            f"Doublon possible : {dup['name']} ({dup.get('status', 'unknown')})"
        )
```

## Fonctions Utilisées

- [get\_field\_value()](../field-functions.md#get\_field\_value)
- [fulltext\_search()](../fulltext-search-functions.md#fulltext\_search)
- [set\_field\_as\_invalid()](../field-functions.md#set\_field\_as\_invalid)
