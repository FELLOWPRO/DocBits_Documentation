# Completar Campos Faltantes desde el Historial

{% hint style="info" %}
**Disponible desde la versión 11.48.0** — Requiere licencia `OPENSEARCH_ENABLED`.
{% endhint %}

## ¿Qué hace este script?

Cuando un documento tiene número de orden de compra pero falta el nombre del proveedor, este script busca en el archivo de documentos otras facturas con el mismo número de OC y copia el nombre del proveedor.

## Disparador

`AFTER_FORMATTING` en tipo de documento **INVOICE**

## Script Completo

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

## Funciones Utilizadas

- [get\_field\_value()](../field-functions.md#get\_field\_value)
- [fulltext\_search()](../fulltext-search-functions.md#fulltext\_search)
- [set\_field\_value()](../field-functions.md#set\_field\_value)
