# Deteccion de Codigo Fiscal

## Que hace este script?

Determina automaticamente el codigo fiscal correcto basado en el contenido de texto completo del documento y los montos de impuesto/neto. Detecta escenarios de inversion de sujeto pasivo (reverse charge), facturas exentas de impuestos y calcula la tasa impositiva para asignar el codigo apropiado (ej., S1 para 19%, S2 para 7%).

## Disparador

`AFTER_FORMATTING` en tipo de documento **INVOICE**

## Script Completo

```python
# Obtener texto completo del documento y montos
content = get_document_content(document_data)
tax_amount = get_field_value(document_data, "tax_amount", "0")
net_amount = get_field_value(document_data, "net_amount", "0")

try:
    tax = float(tax_amount) if tax_amount else 0
    net = float(net_amount) if net_amount else 0
except ValueError:
    tax = 0
    net = 0

# Regla 1: Deteccion de reverse charge via texto completo
if "REVERSE CHARGE" in content.upper() or "UMKEHR DER STEUERSCHULD" in content.upper():
    set_field_value(document_data, "tax_code", "RC")

# Regla 2: Impuesto cero = exento de impuestos
elif tax == 0:
    set_field_value(document_data, "tax_code", "Z0")

# Regla 3: Calcular tasa impositiva a partir de montos
elif net > 0:
    tax_rate = round((tax / net) * 100, 0)
    if tax_rate == 19:
        set_field_value(document_data, "tax_code", "S1")    # Tasa estandar
    elif tax_rate == 7:
        set_field_value(document_data, "tax_code", "S2")    # Tasa reducida
    else:
        set_field_value(document_data, "tax_code", "S3")    # Otra tasa
```

## Explicacion Paso a Paso

1. **Leer texto completo** con `get_document_content()` para deteccion de palabras clave
2. **Leer montos de impuesto y neto** para calculo de tasa impositiva
3. **Verificar reverse charge** buscando palabras clave en el texto del documento (aleman e ingles)
4. **Verificar impuesto cero** — si el monto de impuesto es 0, asignar codigo exento de impuestos
5. **Calcular tasa impositiva** a partir de la relacion impuesto/neto y asignar el codigo correspondiente

## Funciones Utilizadas

- [get\_document\_content()](../business-logic-functions.md#get\_document\_content) — Leer texto completo OCR
- [get\_field\_value()](../field-functions.md#get\_field\_value) — Leer valores de campos
- [set\_field\_value()](../field-functions.md#set\_field\_value) — Establecer codigo fiscal
