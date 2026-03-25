# Validacion de Proveedor por Lookup

## Que hace este script?

Valida el numero de proveedor de la factura contra los datos maestros en la tabla de lookup. Si se encuentra el proveedor, su nombre y terminos de pago se completan automaticamente. Si no se encuentra, el campo se marca como invalido para que el usuario pueda corregirlo.

## Disparador

`AFTER_FORMATTING` en tipo de documento **INVOICE**

## Script Completo

```python
# Leer ID de proveedor del documento
supplier_id = get_field_value(document_data, "supplier_id", "")

if supplier_id:
    # Consultar la tabla de lookup de proveedores
    records = get_lookup_records(
        org_id,                                    # Organizacion actual
        document_json.get("sub_org_id"),           # Sub-org (si aplica)
        "supplier",                                # Nombre de la tabla de lookup
        [["VENDOR_ID", supplier_id]],              # Filtro: coincidencia exacta en VENDOR_ID
        limit=1                                    # Solo necesitamos la primera coincidencia
    )

    if records:
        # Proveedor encontrado — completar campos relacionados automaticamente
        supplier = records[0]
        set_field_value(document_data, "supplier_name", supplier.get("NAME", ""))
        set_field_value(document_data, "payment_terms", supplier.get("PAYMENT_TERMS", ""))
    else:
        # Proveedor no encontrado — marcar como invalido
        set_field_as_invalid(document_data, "supplier_id",
                             f"Supplier '{supplier_id}' not found in master data")
```

## Explicacion Paso a Paso

1. **Leer ID de proveedor** del documento usando `get_field_value()`
2. **Consultar tabla de lookup** con `get_lookup_records()` usando el ID del vendedor como filtro
3. **Si hay coincidencia**: Completar automaticamente nombre del proveedor y terminos de pago desde datos maestros
4. **Si no hay coincidencia**: Marcar el campo de ID de proveedor como invalido con un mensaje de error descriptivo

## Funciones Utilizadas

- [get\_field\_value()](../field-functions.md#get\_field\_value) — Leer valor del campo
- [get\_lookup\_records()](../business-logic-functions.md#get\_lookup\_records) — Consultar datos maestros
- [set\_field\_value()](../field-functions.md#set\_field\_value) — Escribir valor del campo
- [set\_field\_as\_invalid()](../field-functions.md#set\_field\_as\_invalid) — Mostrar error de validacion
