# Tarea por Monto Elevado de Factura

## Que hace este script?

Crea una tarea de aprobacion cuando el total de la factura excede un umbral (ej., 100.000). La tarea se asigna al grupo "Finance Approval" y activa una notificacion por correo electronico para asegurar una revision oportuna.

## Disparador

`AFTER_FORMATTING` en tipo de documento **INVOICE**

## Script Completo

```python
# Leer monto total del documento
total = get_field_value(document_data, "total_amount", "0")

try:
    if float(total) > 100000:
        # Buscar el grupo Finance Approval por nombre
        finance_group = get_group_by_name(org_id, "Finance Approval")

        # Crear una tarea de aprobacion
        create_document_task(
            user,
            document_data,
            title="Amount > 100,000 - Approval required",
            description=f"Total amount: {total}",
            priority="HIGH",
            assigned_to_user_id=None,
            assigned_to_group_id=str(finance_group.id) if finance_group else None,
            send_email=True
        )
except ValueError:
    pass
```

## Explicacion Paso a Paso

1. **Leer monto total** del documento
2. **Verificar umbral** — solo proceder si el monto excede 100.000
3. **Buscar grupo** por nombre usando `get_group_by_name()` para obtener el ID del grupo dinamicamente
4. **Crear tarea** asignada al grupo de finanzas con prioridad alta y notificacion por correo

## Funciones Utilizadas

- [get\_field\_value()](../field-functions.md#get\_field\_value) — Leer valor del campo
- [get\_group\_by\_name()](../business-logic-functions.md#get\_group\_by\_id--get\_group\_by\_name) — Buscar grupo por nombre
- [create\_document\_task()](../business-logic-functions.md#create\_document\_task) — Crear tarea de aprobacion
