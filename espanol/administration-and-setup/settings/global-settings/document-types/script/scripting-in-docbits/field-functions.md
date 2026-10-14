# Funciones de Campo

Funciones para leer, escribir y controlar campos del documento.

**Fuente:** `module/script/helper/document_script_functions.py`

---

## get\_field\_value()

Lee el valor de un campo del documento.

```python
get_field_value(document_data, field_name, default_value=None, is_clean=False)
```

**Parametros:**

| Nombre | Tipo | Descripcion |
| ---- | ---- | ----------- |
| `document_data` | `dict` | El objeto de contexto `document_data` |
| `field_name` | `str` | Nombre del campo (ej., `"invoice_id"`) |
| `default_value` | `any` | Valor de retorno si el campo esta vacio/no existe (por defecto: `None`) |
| `is_clean` | `bool` | Si es `True`: el valor se convierte a MAYUSCULAS y se eliminan los espacios |

**Retorna:** El valor del campo como cadena, o `default_value`

**Ejemplo — Leer numero de factura con valor por defecto:**

```python
# Leer campo con valor por defecto
inv_id = get_field_value(document_data, "invoice_id", "UNKNOWN")

# Con is_clean=True: "INV 001" se convierte en "INV001"
inv_id = get_field_value(document_data, "invoice_id", "", is_clean=True)
```

**Que sucede:** Retorna el valor del campo. Cuando `is_clean=True`, el valor se transforma via `value.upper().replace(" ", "").strip()` — util para comparaciones.

---

## set\_field\_value()

Establece el valor de un campo. Crea automaticamente el campo si no existe.

```python
set_field_value(document_data, field_name, value, remove_link=False)
```

**Parametros:**

| Nombre | Tipo | Descripcion |
| ---- | ---- | ----------- |
| `document_data` | `dict` | El objeto de contexto `document_data` |
| `field_name` | `str` | Nombre del campo |
| `value` | `any` | Nuevo valor |
| `remove_link` | `bool` | Si es `True`: elimina coords, confidence, rule, etc. |

**Retorna:** `True` si el valor cambio, `False` si es identico

**Efectos secundarios:**
- Establece `highlight_field = True` (indicador visual en la UI)
- Establece `extraction_method = "SCRIPT"`
- Establece `formatted_value = value`

**Ejemplo — Asignacion condicional de valor:**

```python
# Establecer ID de factura
set_field_value(document_data, "invoice_id", "INV-2026-001")

# Con remove_link: elimina el enlace OCR (coords, confidence, etc.)
set_field_value(document_data, "custom_field", "Calculated", remove_link=True)
```

**Que sucede:** El valor del campo se actualiza y se marca como modificado por script. Si el campo no existe, se crea automaticamente con `extraction_method: "SCRIPT"` y se agrega tanto a `fields` como a `fields_dict`.

---

## set\_date\_value()

Establece un valor de fecha con formato automatico y aritmetica de fechas opcional.

```python
set_date_value(document_data, field_name, value, add_days=0, skip_weekend=False,
               remove_link=False, exclude_final_days=None)
```

**Parametros:**

| Nombre | Tipo | Descripcion |
| ---- | ---- | ----------- |
| `value` | `str` | Fecha ISO: `"2026-03-25"`. Si esta vacio: fecha de hoy |
| `add_days` | `int` | Dias a agregar (ej., `30` para terminos de pago) |
| `skip_weekend` | `bool` | Omitir fines de semana al agregar dias |
| `exclude_final_days` | `str/list` | Dias adicionales a excluir (ej., `"MONDAY,FRIDAY"`) |

**Ejemplo — Calcular fecha de vencimiento de pago (30 dias, sin fines de semana):**

```python
# Fecha de vencimiento: 30 dias despues de la fecha de factura, omitir fines de semana
inv_date = get_field_value(document_data, "invoice_date")
set_date_value(document_data, "due_date", inv_date,
               add_days=30, skip_weekend=True)

# Establecer fecha de entrega como hoy
set_date_value(document_data, "delivery_date", None)  # None = hoy

# 14 dias, excluyendo sabado y lunes
set_date_value(document_data, "delivery_date", "2026-04-01",
               add_days=14, skip_weekend=True, exclude_final_days="MONDAY")
```

**Que sucede:** La fecha se calcula agregando dias (opcionalmente omitiendo fines de semana/dias especificos) y se formatea automaticamente segun el `date_format_pattern` del documento (ej., `%d.%m.%Y` para Alemania).

**Codigos de dia para `exclude_final_days`:**
`MONDAY`, `TUESDAY`, `WEDNESDAY`, `THURSDAY`, `FRIDAY`, `SATURDAY`, `SUNDAY`

---

## set\_amount\_value()

Establece un valor de monto con formato automatico segun la configuracion regional.

```python
set_amount_value(document_data, field_name, value, remove_link=False)
```

**Parametros:**

| Nombre | Tipo | Descripcion |
| ---- | ---- | ----------- |
| `value` | `str/number` | Monto en formato ingles (ej., `"1234.56"`) |

**Ejemplo — Establecer monto neto:**

```python
set_amount_value(document_data, "net_amount", "1234.56")
# formatted_value se convierte en ej., "1.234,56" para la configuracion regional de_DE
```

**Que sucede:** El monto se formatea segun `amount_format_locale` de `document_json` (ej., `de_DE`, `en_US`).

---

## create\_new\_field()

Crea un nuevo diccionario de campo (sin agregarlo al documento).

```python
create_new_field(field_name, value="")
```

**Retorna:** Dict con `name`, `value`, `formatted_value`, `extraction_method: "SCRIPT"`

**Ejemplo:**

```python
new_field = create_new_field("custom_reference", "REF-001")
document_json["fields"].append(new_field)
fields_dict["custom_reference"] = new_field
```

{% hint style="success" %}
**Alternativa mas simple:** Use `set_field_value()` en su lugar — crea automaticamente el campo si no existe. `create_new_field()` solo es necesario cuando desea manipular manualmente el diccionario del campo.
{% endhint %}

---

## delete\_field()

Elimina un campo del documento.

```python
delete_field(document_data, field_name)
```

**Retorna:** Tupla `(doc_json, fields_dict)` despues de la eliminacion

**Ejemplo:**

```python
delete_field(document_data, "unnecessary_field")
```

---

## set\_field\_as\_invalid()

Marca un campo como invalido con un mensaje de error.

```python
set_field_as_invalid(document_data, field_name, message, code=None)
```

**Parametros:**

| Nombre | Tipo | Descripcion |
| ---- | ---- | ----------- |
| `message` | `str` | Mensaje de error (mostrado en la UI) |
| `code` | `str` | Codigo de error (por defecto: `INVALID_VALUE`) |

**Efectos secundarios:**
- `is_valid = False`
- `invalidated_by_script = True`
- `highlight_field = True`
- `validation_message = message`
- `validation_code = code`

**Ejemplo — Validacion de IBAN:**

```python
iban = get_field_value(document_data, "iban", "")
if len(iban) < 15:
    set_field_as_invalid(document_data, "iban",
                         "IBAN must be at least 15 characters",
                         "IBAN_TOO_SHORT")
```

**Que sucede:** El campo se resalta en rojo en la pantalla de validacion con el mensaje de error mostrado al usuario.

---

## set\_field\_as\_valid()

Elimina el estado invalido de un campo.

```python
set_field_as_valid(document_data, field_name, message, code=None)
```

**Ejemplo:**

```python
set_field_as_valid(document_data, "iban", "IBAN valid")
```

**Que sucede:** Elimina `invalidated_by_script`, `validation_message`, `validation_code` y establece `is_valid = True`.

---

## set\_field\_attribute()

Establece un atributo arbitrario en un campo.

```python
set_field_attribute(document_data, field_name, attribute_name, value)
```

**Ejemplo:**

```python
set_field_attribute(document_data, "invoice_id", "highlight_field", True)
set_field_attribute(document_data, "supplier_name", "custom_flag", "reviewed")
```

Consulte la lista completa de [Atributos Soportados](#supported-attributes) a continuacion.

---

## set\_is\_required()

Hace un campo obligatorio o elimina el requisito.

```python
set_is_required(document_data, field_name, value)
```

**Ejemplo — Numero de OC requerido para facturas de compra:**

```python
doc_type_detail = get_field_value(document_data, "document_type_detail", "")
if doc_type_detail == "PURCHASE_INVOICE":
    set_is_required(document_data, "purchase_order", True)
else:
    set_is_required(document_data, "purchase_order", False)
```

---

## set\_is\_readonly()

Hace un campo de solo lectura o editable.

```python
set_is_readonly(document_data, field_name, value)
```

**Parametros:**

| Nombre | Tipo | Descripcion |
| ---- | ---- | ----------- |
| `value` | `bool/None` | `True` = solo lectura, `False` = editable, `None` = eliminar atributo |

**Ejemplo:**

```python
set_is_readonly(document_data, "total_amount", True)
```

---

## set\_is\_hidden()

Oculta o muestra un campo en la UI.

```python
set_is_hidden(document_data, field_name, value)
```

**Ejemplo — Mostrar campos de sub-organizacion solo cuando es relevante:**

```python
if not document_json.get("sub_org_id"):
    set_is_hidden(document_data, "sub_org_reference", True)
```

---

## set\_force\_validation()

Fuerza la validacion manual para un campo.

```python
set_force_validation(document_data, field_name, value, reset_validation=False)
```

**Parametros:**

| Nombre | Tipo | Descripcion |
| ---- | ---- | ----------- |
| `value` | `bool` | `True` = forzar validacion, `False` = eliminar |
| `reset_validation` | `bool` | Si es `True`: restablece `is_validated` a `False` |

**Efectos secundarios cuando `value=True`:**
- `force_validation = True`
- `is_valid = False` (si aun no ha sido validado)
- `validation_code = "FORCED_VALIDATION"`

**Ejemplo — Forzar validacion para montos altos:**

```python
amount = get_field_value(document_data, "total_amount", "0")
try:
    if float(amount) > 10000:
        set_force_validation(document_data, "total_amount", True)
except ValueError:
    pass
```

---

## Atributos Soportados

### Atributos Principales del Campo

| Atributo | Tipo | Descripcion |
| --------- | ---- | ----------- |
| `value` | any | El valor sin procesar del campo |
| `formatted_value` | string | Valor formateado para visualizacion |
| `content` | string | Contenido original extraido |
| `is_required` | bool | Si el campo es obligatorio |
| `is_valid` | bool | Estado de validacion |
| `is_validated` | bool | Si el campo ha sido validado por el usuario |
| `is_readonly` | bool | Si el campo es de solo lectura |
| `is_hidden` | bool | Si el campo esta oculto en la UI |
| `force_validation` | bool | Forzar al usuario a validar este campo |
| `highlight_field` | bool | Resaltar campo en la UI |
| `extraction_method` | string | Como se extrajo el valor (ej., `"SCRIPT"`) |

### Atributos de Validacion

| Atributo | Tipo | Descripcion |
| --------- | ---- | ----------- |
| `validation_message` | string | Mensaje de error mostrado al usuario |
| `validation_code` | string | Codigo de error (ej., `"FORCED_VALIDATION"`, `"INVALID_VALUE"`) |
| `invalidated_by_script` | bool | Marca el campo como invalidado por script |

### Atributos de Extraccion/OCR

| Atributo | Tipo | Descripcion |
| --------- | ---- | ----------- |
| `coords` | object | Coordenadas del cuadro delimitador en el documento |
| `confidence` | float | Puntuacion de confianza de OCR/extraccion |
| `score` | float | Puntuacion de coincidencia/validacion |
| `score_description` | string | Descripcion de la puntuacion |
| `page` | int | Numero de pagina donde se encontro el campo |
| `rule` | string | Regla de extraccion que se aplico |
