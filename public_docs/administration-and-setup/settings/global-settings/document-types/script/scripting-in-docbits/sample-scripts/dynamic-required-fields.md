# Campos Obligatorios Dinamicos

## Que hace este script?

Establece dinamicamente los requisitos de campos basandose en el contenido del documento. En este ejemplo: cuando la moneda de la factura no es EUR, el campo de tipo de cambio se vuelve obligatorio y visible. Para facturas en EUR, el campo de tipo de cambio se oculta y es opcional.

## Disparador

`ON_FIELD_CHANGE` en tipo de documento **INVOICE**

## Script Completo

```python
# Leer moneda actual
currency = get_field_value(document_data, "currency", "EUR")

# Moneda extranjera: tipo de cambio es requerido y visible
if currency and currency != "EUR":
    set_is_required(document_data, "exchange_rate", True)
    set_is_hidden(document_data, "exchange_rate", False)
else:
    # EUR: tipo de cambio es opcional y oculto
    set_is_required(document_data, "exchange_rate", False)
    set_is_hidden(document_data, "exchange_rate", True)
```

## Variacion: Factura de compra vs. factura de costos

```python
po = get_field_value(document_data, "purchase_order", "")

if po and po.strip():
    # Factura de compra: numero de OC es requerido
    set_field_value(document_data, "invoice_category", "PURCHASE_INVOICE")
    set_is_required(document_data, "purchase_order", True)
else:
    # Factura de costos: numero de OC no necesario, ocultar tabla
    set_field_value(document_data, "invoice_category", "COST_INVOICE")
    set_is_required(document_data, "purchase_order", False)
    delete_tables(document_data)
```

## Explicacion Paso a Paso

1. **Leer el campo de control** (moneda en este caso)
2. **Aplicar reglas de negocio** — diferentes requisitos de campos segun el valor
3. **Establecer visibilidad** — ocultar campos irrelevantes para mantener la UI limpia
4. **Establecer requisitos** — hacer campos relevantes obligatorios

{% hint style="info" %}
**Eleccion de disparador:** `ON_FIELD_CHANGE` se ejecuta cada vez que un usuario modifica un campo, por lo que los requisitos se actualizan en tiempo real. `AFTER_FORMATTING` solo se ejecuta una vez despues de la extraccion inicial.
{% endhint %}

## Funciones Utilizadas

- [get\_field\_value()](../field-functions.md#get\_field\_value) — Leer campo de control
- [set\_is\_required()](../field-functions.md#set\_is\_required) — Establecer campo como obligatorio/opcional
- [set\_is\_hidden()](../field-functions.md#set\_is\_hidden) — Mostrar/ocultar campos
- [set\_field\_value()](../field-functions.md#set\_field\_value) — Establecer campo de categoria
- [delete\_tables()](../table-functions.md#delete\_tables) — Eliminar tablas para facturas de costos
