# Completar Campos Faltantes desde el Historial de Documentos

{% hint style="info" %}
**Disponible desde la versión 11.48.0** — Requiere licencia `OPENSEARCH_ENABLED`.
{% endhint %}

## ¿Qué hace este script?

Cuando un documento tiene número de orden de compra pero falta el nombre del proveedor, este script busca en el archivo de documentos otras facturas que contengan el mismo número de OC y copia el nombre del proveedor de la primera coincidencia.

## Disparador

`AFTER_FORMATTING` en el tipo de documento **INVOICE**

## Script Completo

```python
po = get_field_value(document_data, "purchase_order", "")
supplier = get_field_value(document_data, "supplier_name", "")

if po and not supplier:
    # Search archive for documents with this PO number
    history = fulltext_search(
        po,
        doc_type="INVOICE",
        size=3
    )

    for doc in history:
        if doc.get("vendor_name"):
            set_field_value(document_data, "supplier_name", doc["vendor_name"])
            break
```

## Explicación Paso a Paso

1. **Leer el número de OC y el proveedor** del documento actual
2. **Comprobar la condición**: continuar solo si existe la OC pero falta el proveedor
3. **Buscar en el archivo** documentos que contengan el número de OC
4. **Copiar el nombre del proveedor** de la primera coincidencia que tenga un nombre de proveedor definido

## Variante: Completar Varios Campos

```python
po = get_field_value(document_data, "purchase_order", "")
supplier = get_field_value(document_data, "supplier_name", "")

if po and not supplier:
    history = fulltext_search(po, doc_type="INVOICE", size=3)

    for doc in history:
        if doc.get("vendor_name"):
            set_field_value(document_data, "supplier_name", doc["vendor_name"])
            # Also fill other fields if available
            if doc.get("total_amount") and not get_field_value(document_data, "total_amount", ""):
                set_field_value(document_data, "total_amount", doc["total_amount"])
            break
```

## Funciones Utilizadas

- [get\_field\_value()](../field-functions.md#get\_field\_value) — Leer el valor de un campo
- [fulltext\_search()](../fulltext-search-functions.md#fulltext\_search) — Buscar en el texto OCR de todos los documentos
- [set\_field\_value()](../field-functions.md#set\_field\_value) — Escribir el valor de un campo
