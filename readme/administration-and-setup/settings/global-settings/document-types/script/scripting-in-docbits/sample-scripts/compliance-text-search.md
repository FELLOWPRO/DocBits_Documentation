# Recherche de Texte de Conformité (Reverse Charge)

{% hint style="info" %}
**Disponible à partir de la version 11.48.0** — Nécessite la licence `OPENSEARCH_ENABLED`.
{% endhint %}

## Que fait ce script ?

Recherche du texte pertinent pour la conformité comme "REVERSE CHARGE" dans l'archive de documents et définit automatiquement le code fiscal.

## Déclencheur

`AFTER_FORMATTING` sur le type de document **INVOICE**

## Script Complet

```python
rc_docs = fulltext_search(
    org_id, "REVERSE CHARGE",
    search_type="match_phrase",
    doc_type="INVOICE",
    size=5
)

if rc_docs:
    set_field_value(document_data, "tax_code", "RC")
```

## Variante : Recherche Fuzzy (Tolérante aux Erreurs OCR)

```python
rc_fuzzy = fulltext_search(
    org_id, "REVERSE CHARGE",
    search_type="fuzzy",
    vendor_name="ACME Corp"
)

if rc_fuzzy:
    set_field_value(document_data, "tax_code", "RC")
```

## Fonctions Utilisées

- [fulltext\_search()](../fulltext-search-functions.md#fulltext\_search)
- [set\_field\_value()](../field-functions.md#set\_field\_value)
