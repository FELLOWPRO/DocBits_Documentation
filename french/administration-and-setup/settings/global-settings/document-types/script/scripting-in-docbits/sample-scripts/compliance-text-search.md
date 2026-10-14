# Recherche de Texte de Conformité

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
    "REVERSE CHARGE",
    search_type="match_phrase",
    doc_type="INVOICE",
    size=5
)

if rc_docs:
    set_field_value(document_data, "tax_code", "RC")
```

## Variante : Recherche Floue (Tolérante aux Erreurs OCR)

```python
rc_fuzzy = fulltext_search(
    "REVERSE CHARGE",
    search_type="fuzzy",
    vendor_name="ACME Corp"
)

if rc_fuzzy:
    set_field_value(document_data, "tax_code", "RC")
```

## Fonctions Utilisées

* [fulltext\_search()](../fulltext-search-functions.md#fulltext_search)
* [set\_field\_value()](https://github.com/Fellow-Consulting-AG/docbits/tree/fr/readme/administration-and-setup/settings/global-settings/document-types/script/scripting-in-docbits/field-functions.md#set_field_value)
