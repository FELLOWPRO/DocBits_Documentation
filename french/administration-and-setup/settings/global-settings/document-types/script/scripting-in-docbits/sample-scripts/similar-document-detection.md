# Détection de Documents Similaires

{% hint style="info" %}
**Disponible à partir de la version 11.48.0** — Nécessite la licence `OPENSEARCH_ENABLED`.
{% endhint %}

## Que fait ce script ?

Utilise la recherche de similarité vectorielle pour trouver des documents sémantiquement similaires. Si un document avec plus de 95 % de similarité est trouvé, le numéro de facture est signalé comme potentiellement frauduleux ou en double.

## Déclencheur

`AFTER_FORMATTING` sur le type de document **INVOICE**

## Script Complet

```python
doc_id = document_json["doc_id"]
similar = vector_search(doc_id, k=5)

for doc in similar:
    if doc["similarity_percent"] > 95:
        set_field_as_invalid(
            document_data, "invoice_id",
            f"95%+ similaire à : {doc['name']} (Score : {doc['similarity_percent']}%)"
        )
        break
```

## Fonctions Utilisées

* [vector\_search()](../fulltext-search-functions.md#vector_search)
* [set\_field\_as\_invalid()](https://github.com/Fellow-Consulting-AG/docbits/tree/fr/readme/administration-and-setup/settings/global-settings/document-types/script/scripting-in-docbits/field-functions.md#set_field_as_invalid)
