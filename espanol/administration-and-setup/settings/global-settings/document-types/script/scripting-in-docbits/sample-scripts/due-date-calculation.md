# Calculo de Fecha de Vencimiento

## Que hace este script?

Calcula la fecha de vencimiento del pago basada en la fecha de factura agregando un numero configurable de dias (ej., 30). Los fines de semana se omiten automaticamente para que la fecha de vencimiento siempre caiga en un dia habil.

## Disparador

`AFTER_FORMATTING` en tipo de documento **INVOICE**

## Script Completo

```python
# Leer fecha de factura
inv_date = get_field_value(document_data, "invoice_date")

if inv_date:
    # Calcular fecha de vencimiento: 30 dias despues de la fecha de factura, omitir fines de semana
    set_date_value(document_data, "due_date", inv_date,
                   add_days=30, skip_weekend=True)

    # Tambien establecer fecha contable = fecha de factura
    set_date_value(document_data, "accounting_date", inv_date)
```

## Variaciones

### 14 dias, excluyendo lunes

```python
set_date_value(document_data, "due_date", inv_date,
               add_days=14, skip_weekend=True, exclude_final_days="MONDAY")
```

### 60 dias, sin omision de fines de semana

```python
set_date_value(document_data, "due_date", inv_date, add_days=60)
```

### Establecer fecha de entrega como hoy

```python
set_date_value(document_data, "delivery_date", None)  # None = hoy
```

## Explicacion Paso a Paso

1. **Leer fecha de factura** del documento
2. **Calcular fecha de vencimiento** usando `set_date_value()` con `add_days=30` y `skip_weekend=True`
3. **Formato de fecha** es automatico — usa el `date_format_pattern` del documento (ej., `%d.%m.%Y`)
4. **Omision de fines de semana** asegura que la fecha de vencimiento caiga de lunes a viernes

## Codigos de Dia para `exclude_final_days`

`MONDAY`, `TUESDAY`, `WEDNESDAY`, `THURSDAY`, `FRIDAY`, `SATURDAY`, `SUNDAY`

## Funciones Utilizadas

- [get\_field\_value()](../field-functions.md#get\_field\_value) — Leer fecha de factura
- [set\_date\_value()](../field-functions.md#set\_date\_value) — Calcular y establecer fecha de vencimiento
