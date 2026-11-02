# Búsqueda de Texto de Cumplimiento (Reverse Charge)

{% hint style="info" %}
**Disponible desde la versión 11.48.0** — Requiere licencia `OPENSEARCH_ENABLED`.
{% endhint %}

## ¿Qué hace este script?

Busca texto relevante para el cumplimiento como "REVERSE CHARGE" en el archivo de documentos y establece automáticamente el código fiscal.

## Disparador

`AFTER_FORMATTING` en tipo de documento **INVOICE**

## Script Completo

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

## Variante: Búsqueda Fuzzy (Tolerante a Errores OCR)

```python
rc_fuzzy = fulltext_search(
    "REVERSE CHARGE",
    search_type="fuzzy",
    vendor_name="ACME Corp"
)

if rc_fuzzy:
    set_field_value(document_data, "tax_code", "RC")
```

## Funciones Utilizadas

- [fulltext\_search()](../fulltext-search-functions.md#fulltext\_search)
- [set\_field\_value()](../field-functions.md#set\_field\_value)
