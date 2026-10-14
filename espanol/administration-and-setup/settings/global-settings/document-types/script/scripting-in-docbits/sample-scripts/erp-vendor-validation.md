# Validación de Proveedor ERP

{% hint style="info" %}
**Disponible desde la versión 11.48.0** — Requiere licencia `OPENSEARCH_ENABLED`.
{% endhint %}

## ¿Qué hace este script?

Valida si el proveedor de la factura existe en los datos maestros de ERP indexados en OpenSearch. Si el proveedor no se encuentra en el ERP, el campo se marca como no válido. Esto complementa la función existente `is_supplier_valid()`, ya que busca en el índice del ERP en lugar de en la tabla de búsqueda.

## Disparador

`AFTER_FORMATTING` en el tipo de documento **INVOICE**

## Script Completo

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
            "Vendor not found in ERP master data"
        )
```

## Variante: Validar con el Número de Proveedor

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
        # Auto-fill vendor name from ERP
        erp_vendor = erp_matches[0]
        set_field_value(document_data, "supplier_name",
                        erp_vendor.get("vendor_name", ""))
    else:
        set_field_as_invalid(
            document_data, "supplier_id",
            f"Vendor '{vendor_nr}' not found in ERP"
        )
```

## Explicación Paso a Paso

1. **Leer el nombre del proveedor** del documento actual
2. **Buscar en los datos maestros del ERP** con `fulltext_search_erp()`, filtrando por el tipo de entidad `"vendor"`
3. **Si no se encuentra**: marcar el campo del nombre del proveedor como no válido
4. **Variante**: buscar por número de proveedor y rellenar automáticamente el nombre del proveedor con los datos del ERP

## Funciones Utilizadas

- [get\_field\_value()](../field-functions.md#get\_field\_value) — Leer el valor de un campo
- [fulltext\_search\_erp()](../fulltext-search-functions.md#fulltext\_search\_erp) — Buscar en los datos maestros del ERP
- [set\_field\_as\_invalid()](../field-functions.md#set\_field\_as\_invalid) — Mostrar un error de validación
- [set\_field\_value()](../field-functions.md#set\_field\_value) — Escribir el valor de un campo
