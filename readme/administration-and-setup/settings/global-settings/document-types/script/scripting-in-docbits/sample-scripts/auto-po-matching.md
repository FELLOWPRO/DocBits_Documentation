# Coincidencia Automatica de OC

## Que hace este script?

Activa automaticamente la coincidencia de OC (Orden de Compra) cuando hay un numero de OC presente en la factura. El microservicio po-match-service compara las partidas de la factura contra la OC y completa los resultados de coincidencia.

## Disparador

`AFTER_FORMATTING` en tipo de documento **INVOICE**

## Script Completo

```python
# Leer numero de OC del documento
po_nr = get_field_value(document_data, "purchase_order", "")

if po_nr:
    # Limpiar numero de OC: eliminar prefijo y espacios
    po_nr = po_nr.strip()
    if po_nr.upper().startswith("PO"):
        po_nr = po_nr[2:].strip()
    if po_nr.startswith("-") or po_nr.startswith(" "):
        po_nr = po_nr[1:].strip()

    # Actualizar numero de OC limpio
    set_field_value(document_data, "purchase_order", po_nr)

    # Activar coincidencia automatica de OC
    auto_po_match_for_purchase_orders(user, document_data, po_nr)
```

## Explicacion Paso a Paso

1. **Leer numero de OC** de la factura
2. **Limpiar** el numero de OC eliminando prefijos comunes como "PO-" o "PO "
3. **Actualizar** el numero de OC limpio de vuelta al documento
4. **Activar coincidencia de OC** que llama al po-match-service para comparar lineas de factura contra lineas de OC

## Que sucede despues de la coincidencia?

El `document_data` se actualiza con:
- `po_items` — Partidas de OC coincidentes
- `po_match_status` — Resultado de coincidencia (`"matched"`, `"partially_matched"`, etc.)
- `po_multi_matched` — Si se coincidieron multiples OCs

## Funciones Utilizadas

- [get\_field\_value()](../field-functions.md#get\_field\_value) — Leer valor del campo
- [set\_field\_value()](../field-functions.md#set\_field\_value) — Escribir numero de OC limpio
- [auto\_po\_match\_for\_purchase\_orders()](../business-logic-functions.md#auto\_po\_match\_for\_purchase\_orders) — Activar coincidencia de OC
