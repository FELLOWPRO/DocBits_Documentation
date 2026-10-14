# Funciones de Logica de Negocio

Funciones para lookups, coincidencia de OC, tareas, gestion de usuarios/grupos y cambios de estado.

**Fuente:** `module/script/helper/document_script_functions.py`

---

## get\_lookup\_records()

Consulta datos maestros de tablas de lookup (proveedores, articulos, cuentas contables, etc.).

```python
get_lookup_records(org_id, sub_org_id, lookup_name, filters, **kwargs)
```

**Parametros:**

| Nombre | Tipo | Descripcion |
| ---- | ---- | ----------- |
| `org_id` | `str` | UUID de la organizacion |
| `sub_org_id` | `str/None` | UUID de la sub-organizacion (o `None`) |
| `lookup_name` | `str` | Nombre del lookup (ej., `"supplier"`, `"item"`, `"gl_account"`) |
| `filters` | `list` | Condiciones de filtro (ver formatos abajo) |
| `skip` | `int` | Desplazamiento para paginacion (por defecto: 0) |
| `limit` | `int` | Resultados maximos (por defecto: 100) |
| `match_all` | `bool` | `True` = AND, `False` = OR (por defecto: `True`) |
| `sort_order` | `list` | Ordenamiento (opcional) |

### Formatos de Filtro

Se soportan tres formatos:

```python
# Formato 1: Dict con field/operator/value
filters = [
    {"field": "VENDOR_ID", "operator": "exact", "value": "V001"},
    {"field": "NAME", "operator": "contains", "value": "ACME"},
]

# Formato 2: Tupla/Lista con 2 elementos (field, value) -> operator = "exact"
filters = [
    ["VENDOR_ID", "V001"],
    ["CITY", "Munich"],
]

# Formato 3: Tupla/Lista con 3 elementos (field, operator, value)
filters = [
    ["VENDOR_ID", "exact", "V001"],
    ["NAME", "contains", "ACME"],
]
```

### Ordenamiento

```python
# Formato 1: Dict
sort_order = [{"field": "NAME", "direction": "asc"}]

# Formato 2: Tupla/Lista
sort_order = [["NAME", "asc"], ["VENDOR_ID", "desc"]]
```

**Ejemplo — Buscar proveedor por ID de vendedor:**

```python
# Buscar proveedor por ID de vendedor
supplier_id = get_field_value(document_data, "supplier_id", "")
records = get_lookup_records(
    org_id, None, "supplier",
    [["VENDOR_ID", supplier_id]],
)
if records:
    supplier = records[0]
    set_field_value(document_data, "supplier_name", supplier.get("NAME", ""))
```

**Ejemplo — Buscar cuentas contables con multiples filtros:**

```python
records = get_lookup_records(
    org_id, document_json.get("sub_org_id"), "gl_account",
    [
        {"field": "ACCOUNT_TYPE", "operator": "exact", "value": "EXPENSE"},
        {"field": "IS_ACTIVE", "operator": "exact", "value": "true"},
    ],
    limit=50,
    sort_order=[["ACCOUNT_NUMBER", "asc"]],
)
```

{% hint style="info" %}
Internamente usa `search_operator="SMART"` que soporta coincidencia difusa.
{% endhint %}

---

## is\_supplier\_valid()

Verifica si un proveedor existe en los datos de lookup.

```python
is_supplier_valid(user, filter_data_json, sub_org_id=None)
```

**Parametros:**

| Nombre | Tipo | Descripcion |
| ---- | ---- | ----------- |
| `user` | `UserAuthentication` | El objeto de contexto `user` |
| `filter_data_json` | `dict` | Filtro en formato `{"match_all": True, "filters": [...]}` |
| `sub_org_id` | `str/None` | Sub-organizacion |

**Retorna:** `True` si hay al menos 1 coincidencia, de lo contrario `False`

**Ejemplo — Validar proveedor:**

```python
supplier_id = get_field_value(document_data, "supplier_id", "")
is_valid = is_supplier_valid(user, {
    "match_all": True,
    "filters": [{"field": "VENDOR_ID", "operator": "exact", "value": supplier_id}]
})
if not is_valid:
    set_field_as_invalid(document_data, "supplier_id", "Supplier not found in master data")
```

---

## auto\_po\_match\_for\_purchase\_orders()

Activa la coincidencia automatica de OC a traves del microservicio po-match-service.

```python
auto_po_match_for_purchase_orders(user, document_data, po_numbers)
```

**Parametros:**

| Nombre | Tipo | Descripcion |
| ---- | ---- | ----------- |
| `user` | `UserAuthentication` | Debe ser un objeto de usuario real |
| `document_data` | `dict` | Contexto del documento |
| `po_numbers` | `str/list` | Numeros de OC (separados por comas o lista) |

**Retorna:** `document_data` actualizado con `po_items`, `po_match_status`, `po_multi_matched`

**Ejemplo — Coincidencia automatica de OC:**

```python
po_nr = get_field_value(document_data, "purchase_order", "")
if po_nr:
    auto_po_match_for_purchase_orders(user, document_data, po_nr)
```

{% hint style="warning" %}
**Proteccion contra duplicados:** Los numeros de OC ya verificados se almacenan en `already_verified_po_numbers` y no se volveran a emparejar.
{% endhint %}

---

## get\_next\_sequence\_number()

Obtiene e incrementa atomicamente un numero de secuencia en la base de datos.

```python
get_next_sequence_number(org_id, sequence_name, default_value=1)
```

**Parametros:**

| Nombre | Tipo | Descripcion |
| ---- | ---- | ----------- |
| `org_id` | `str` | UUID de la organizacion |
| `sequence_name` | `str` | Debe contener `"sequence"` (ej., `"invoice_sequence"`) |
| `default_value` | `int` | Valor inicial cuando la secuencia se crea por primera vez |

**Retorna:** `int` — el siguiente numero, o `None` si el nombre es invalido

**Ejemplo — Generar numero interno de documento:**

```python
seq_nr = get_next_sequence_number(org_id, "invoice_sequence", 1000)
set_field_value(document_data, "internal_number", str(seq_nr))
```

{% hint style="danger" %}
**Regla de nomenclatura:** El `sequence_name` debe comenzar o terminar con "sequence", o contener "SEQUENCE\_". De lo contrario, la funcion retorna `None`.
{% endhint %}

---

## create\_document\_task()

Crea una tarea para el documento actual.

```python
create_document_task(user, document_data, title, description, priority,
                     assigned_to_user_id, assigned_to_group_id, send_email)
```

**Parametros:**

| Nombre | Tipo | Descripcion |
| ---- | ---- | ----------- |
| `user` | `UserAuthentication` | Contexto de usuario |
| `title` | `str` | Titulo de la tarea |
| `description` | `str` | Descripcion |
| `priority` | `str/int` | Prioridad |
| `assigned_to_user_id` | `str/None` | Usuario asignado |
| `assigned_to_group_id` | `str/None` | Grupo asignado |
| `send_email` | `bool` | Enviar notificacion por correo |

**Ejemplo — Crear tarea para facturas de monto alto:**

```python
amount = float(get_field_value(document_data, "total_amount", "0"))
if amount > 50000:
    create_document_task(
        user, document_data,
        title="High invoice amount - review required",
        description=f"Invoice amount: {amount} exceeds 50,000 threshold",
        priority="HIGH",
        assigned_to_user_id=None,
        assigned_to_group_id="uuid-of-finance-group",
        send_email=True
    )
```

---

## set\_document\_sub\_org\_id()

Asigna una sub-organizacion a un documento.

```python
set_document_sub_org_id(document_data, sub_org_id)
```

**Efectos secundarios:**
- Establece `sub_org_id` en `document_json`
- Guarda directamente en la base de datos (si `doc_id` esta presente)

**Ejemplo — Enrutar segun proveedor:**

```python
supplier = get_field_value(document_data, "supplier_name", "", is_clean=True)
sub_org_map = {
    "ACMECORP": "uuid-acme-sub-org",
    "WIDGETSINC": "uuid-widgets-sub-org",
}
for key, sub_org in sub_org_map.items():
    if key in supplier:
        set_document_sub_org_id(document_data, sub_org)
        break
```

---

## update\_document\_status\_with\_doc\_id()

Cambia el estado de un documento.

```python
update_document_status_with_doc_id(doc_id, user, org_id, status, message=None,
                                    doc_classification_class=None)
```

**Parametros:**

| Nombre | Tipo | Descripcion |
| ---- | ---- | ----------- |
| `doc_id` | `str` | UUID del documento |
| `status` | `str` | Nuevo estado (ej., `"error"`, `"ready_for_validation"`) |
| `message` | `str/None` | Mensaje de estado |
| `doc_classification_class` | `str/None` | Para estado `CLASSIFIED`: nuevo tipo de documento |

**Ejemplo — Establecer documento en estado de error:**

```python
doc_id = document_json["doc_id"]
update_document_status_with_doc_id(
    doc_id, user, org_id, "error",
    message="Required field missing: supplier number"
)
```

{% hint style="warning" %}
**Precaucion:** Los cambios de estado activan acciones posteriores (flujos de trabajo DocFlow, hooks de cambio de estado). Use solo cuando sea necesario.
{% endhint %}

---

## get\_document\_content()

Retorna el texto OCR completo del documento.

```python
get_document_content(document_data)
```

**Retorna:** `str` — Texto concatenado de todas las paginas

**Ejemplo — Buscar palabras clave en texto completo:**

```python
content = get_document_content(document_data)
if "REVERSE CHARGE" in content.upper():
    set_field_value(document_data, "tax_code", "RC")

# Busqueda regex en texto completo
match = re_search(r"Order number:\s*(\S+)", content)
if match:
    set_field_value(document_data, "purchase_order", match.group(1))
```

{% hint style="info" %}
El resultado se almacena en cache durante 60 segundos (cache TTL con maximo 128 entradas).
{% endhint %}

---

## get\_user\_by\_id() / get\_user\_by\_email()

Busca un usuario por ID o correo electronico.

```python
get_user_by_id(user_id)
get_user_by_email(email)
```

**Retorna:** Objeto `UsersCache` con atributos como `.email`, `.first_name`, `.last_name`, `.user_id`

**Ejemplo — Asignar tarea a un usuario especifico:**

```python
user_obj = get_user_by_email("manager@company.com")
if user_obj:
    create_document_task(user, document_data,
        title="Review required",
        description="...",
        priority="MEDIUM",
        assigned_to_user_id=str(user_obj.user_id),
        assigned_to_group_id=None,
        send_email=True)
```

---

## get\_group\_by\_id() / get\_group\_by\_name()

Busca un grupo de usuarios por ID o nombre.

```python
get_group_by_id(group_id)
get_group_by_name(org_id, group_name)
```

**Retorna:** Objeto `GroupCache`

**Ejemplo — Encontrar grupo para asignacion de tarea:**

```python
finance_group = get_group_by_name(org_id, "Finance")
if finance_group:
    create_document_task(user, document_data,
        title="Approval needed",
        description="...",
        priority="HIGH",
        assigned_to_user_id=None,
        assigned_to_group_id=str(finance_group.id),
        send_email=True)
```

---

## compare\_values()

Comparacion inteligente de valores con conversion de tipos.

```python
compare_values(value1, value2)
```

**Logica de comparacion:**
1. `None == None` -> `True`
2. `None != non-None` -> `False`
3. Cadenas que son numeros -> comparacion numerica (`"1.0" == "1.00"` -> `True`)
4. Cadenas -> sin distincion de mayusculas/minusculas, insensible a espacios (`"ABC " == " abc"` -> `True`)
5. Bool vs String -> comparacion de cadenas (`True == "true"` -> `True`)
6. Comparacion Decimal como alternativa

**Ejemplo — Verificar que los montos coincidan:**

```python
if compare_values(get_field_value(document_data, "net_amount"),
                  get_field_value(document_data, "calculated_net")):
    set_field_as_valid(document_data, "net_amount", "Amounts match")
```

---

## get\_lov\_values()

Recupera entradas de Lista de Valores (LOV).

```python
get_lov_values(org_id, key, return_type="list_of_objects", sub_org_id=None, language_code="")
```

**Parametros:**

| Nombre | Tipo | Descripcion |
| ---- | ---- | ----------- |
| `org_id` | `str` | UUID de la organizacion |
| `key` | `str` | Clave LOV |
| `return_type` | `str` | `"list_of_objects"` o `"list_of_values"` |
| `sub_org_id` | `str/None` | Filtro opcional de sub-organizacion |
| `language_code` | `str` | Codigo de idioma (ej., `"en"`, `"de"`) |

**Retorna:** Valores LOV como lista de objetos o como lista plana.

**Ejemplo — Obtener codigos fiscales configurados:**

```python
tax_codes = get_lov_values(org_id, "tax_codes", return_type="list_of_values")
```
