# Auto-Exportacion por Condiciones

## Que hace este script?

Establece automaticamente el estado del documento a "listo para exportar" cuando se cumplen condiciones especificas: el proveedor es un vendedor conocido/confiable Y el monto de la factura esta por debajo de un umbral. Esto omite la validacion manual para facturas de bajo riesgo.

## Disparador

`AFTER_FORMATTING` en tipo de documento **INVOICE**

## Script Completo

```python
# Leer campos relevantes
net = get_field_value(document_data, "net_amount", "0")
supplier = get_field_value(document_data, "supplier_name", "", is_clean=True)

try:
    net_float = float(net)
except ValueError:
    net_float = 0

# Definir proveedores confiables para auto-exportacion
auto_export_suppliers = ["OFFICEDEPOT", "STAPLES", "AMAZON"]

# Auto-exportar para proveedores conocidos con montos pequenos
if any(s in supplier for s in auto_export_suppliers) and net_float < 500:
    doc_id = document_json["doc_id"]
    update_document_status_with_doc_id(
        doc_id, user, org_id, "ready_for_export",
        message="Auto-exported (small amount, known supplier)"
    )
```

## Explicacion Paso a Paso

1. **Leer monto neto y nombre del proveedor** del documento (proveedor con `is_clean=True` para comparacion)
2. **Definir proveedores confiables** — lista de nombres de vendedores conocidos (limpios/mayusculas)
3. **Verificar condiciones** — el proveedor debe estar en la lista de confianza Y el monto debe ser menor a 500
4. **Cambiar estado** a `"ready_for_export"` con un mensaje descriptivo

{% hint style="warning" %}
**Precaucion:** Los cambios de estado activan flujos de trabajo posteriores (DocFlow, hooks de exportacion). Asegurese de que las condiciones sean lo suficientemente estrictas para evitar exportaciones no deseadas.
{% endhint %}

## Funciones Utilizadas

- [get\_field\_value()](../field-functions.md#get\_field\_value) — Leer valores de campos
- [update\_document\_status\_with\_doc\_id()](../business-logic-functions.md#update\_document\_status\_with\_doc\_id) — Cambiar estado del documento
