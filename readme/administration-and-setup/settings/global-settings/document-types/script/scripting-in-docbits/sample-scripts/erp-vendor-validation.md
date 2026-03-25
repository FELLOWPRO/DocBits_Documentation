# Validación de Proveedor ERP

{% hint style="info" %}
**Disponible desde la versión 11.48.0** — Requiere licencia `OPENSEARCH_ENABLED`.
{% endhint %}

## ¿Qué hace este script?

Valida si el proveedor de la factura existe en los datos maestros de ERP indexados en OpenSearch.

## Disparador

`AFTER_FORMATTING` en tipo de documento **INVOICE**

## Script Completo

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
            "Proveedor no encontrado en datos maestros ERP"
        )
```

## Funciones Utilizadas

- [get\_field\_value()](../field-functions.md#get\_field\_value)
- [fulltext\_search\_erp()](../fulltext-search-functions.md#fulltext\_search\_erp)
- [set\_field\_as\_invalid()](../field-functions.md#set\_field\_as\_invalid)
