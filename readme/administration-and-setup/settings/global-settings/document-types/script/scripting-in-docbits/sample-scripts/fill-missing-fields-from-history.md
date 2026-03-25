# Remplir les Champs Manquants depuis l'Historique

{% hint style="info" %}
**Disponible à partir de la version 11.48.0** — Nécessite la licence `OPENSEARCH_ENABLED`.
{% endhint %}

## Que fait ce script ?

Lorsqu'un document a un numéro de bon de commande mais que le nom du fournisseur est manquant, ce script recherche dans l'archive de documents d'autres factures avec le même numéro de BC et copie le nom du fournisseur.

## Déclencheur

`AFTER_FORMATTING` sur le type de document **INVOICE**

## Script Complet

```python
po = get_field_value(document_data, "purchase_order", "")
supplier = get_field_value(document_data, "supplier_name", "")

if po and not supplier:
    history = fulltext_search(
        org_id, po,
        doc_type="INVOICE",
        size=3
    )

    for doc in history:
        if doc.get("vendor_name"):
            set_field_value(document_data, "supplier_name", doc["vendor_name"])
            break
```

## Fonctions Utilisées

- [get\_field\_value()](../field-functions.md#get\_field\_value)
- [fulltext\_search()](../fulltext-search-functions.md#fulltext\_search)
- [set\_field\_value()](../field-functions.md#set\_field\_value)
