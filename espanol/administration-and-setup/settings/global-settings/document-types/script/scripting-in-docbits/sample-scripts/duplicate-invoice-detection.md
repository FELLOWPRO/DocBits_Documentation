# Detección de Facturas Duplicadas

{% hint style="info" %}
**Disponible desde la versión 11.48.0** — Requiere licencia `OPENSEARCH_ENABLED`.
{% endhint %}

## ¿Qué hace este script?

Busca en el archivo de documentos facturas existentes con el mismo número de factura del mismo proveedor. Si se encuentra un posible duplicado, el campo del número de factura se marca como inválido.

## Disparador

`AFTER_FORMATTING` en tipo de documento **INVOICE**

## Script Completo

```python
inv_id = get_field_value(document_data, "invoice_id", "")
vendor = get_field_value(document_data, "supplier_name", "")

if inv_id and vendor:
    existing = fulltext_search(
        inv_id,
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
            f"Posible duplicado: {dup['name']} ({dup.get('status', 'unknown')})"
        )
```

## Funciones Utilizadas

- [get\_field\_value()](../field-functions.md#get\_field\_value)
- [fulltext\_search()](../fulltext-search-functions.md#fulltext\_search)
- [set\_field\_as\_invalid()](../field-functions.md#set\_field\_as\_invalid)
