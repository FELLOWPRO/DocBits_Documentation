# Funciones de Búsqueda Fulltext y Vectorial

{% hint style="info" %}
**Disponible desde la versión 11.48.0**

Estas funciones requieren que la licencia/preferencia **OPENSEARCH\_ENABLED** esté activada para su organización. Sin ella, todas las funciones lanzan un `RuntimeError("Fulltext search license is missing")`.
{% endhint %}

Funciones para buscar en archivos de documentos, encontrar documentos similares y consultar datos maestros de ERP. Estas buscan en **todos los documentos** de la organización — a diferencia de `get_document_content()` que solo lee el texto del documento actual.

{% hint style="success" %}
**Security:** The `org_id` is automatically injected by the script sandbox. You never need to pass it — your scripts always operate within your own organization's data.
{% endhint %}

**Fuente:** `module/script/helper/document_script_functions.py`

---

## fulltext\_search()

Busca en el texto OCR completo de **todos los documentos** de la organización. Encuentra texto en los campos `pages.pageText`, `tfidfCustomPageText` y `ai_text` a través del microservicio fulltextsearch.

```python
fulltext_search(query, **kwargs)
```

**Parámetros:**

| Nombre | Tipo | Por defecto | Descripción |
| ------ | ---- | ----------- | ----------- |
| `query` | `str` | obligatorio | Término de búsqueda (buscado en el texto OCR de todos los documentos) |
| `search_type` | `str` | `"match_phrase"` | `"match_phrase"` (frase exacta), `"fuzzy"` (tolerante a errores, hasta 2 caracteres de diferencia), `"prefix"` (comienza con) |
| `doc_type` | `str` | `None` | Filtrar por tipo de documento (separado por comas, ej. `"INVOICE,CREDIT_NOTE"`) |
| `status` | `str` | `None` | Filtrar por estado del documento (separado por comas, ej. `"ready_for_validation,exported"`) |
| `vendor_name` | `str` | `None` | Filtrar por nombre del proveedor |
| `date_range` | `str` | `None` | `"last_30_days"`, `"last_90_days"`, `"last_180_days"`, `"last_365_days"` |
| `size` | `int` | `10` | Máx. resultados (limitado a 50) |

**Retorna:** `list[dict]` — Cada dict contiene:

| Campo | Descripción |
| ----- | ----------- |
| `doc_id` | UUID del documento |
| `name` | Nombre del archivo (ej. `"INV-2026-001.pdf"`) |
| `doc_type` | Tipo de documento (`"INVOICE"`, `"ORDER_CONFIRMATION"`, etc.) |
| `vendor_name` | Nombre del proveedor |
| `status` | Estado del documento |
| `total_amount` | Importe total |
| `ocr_content` | Extracto de texto coincidente del documento |
| `highlights` | Dict con coincidencias resaltadas por campo |

**Ejemplo — Búsqueda de frase exacta:**

```python
results = fulltext_search("REVERSE CHARGE",
                          doc_type="INVOICE", size=10)
for doc in results:
    print(doc["name"], doc["ocr_content"])
```

**Ejemplo — Búsqueda fuzzy (tolerante a errores OCR):**

```python
results = fulltext_search("REVERSE CHARGE",
                          search_type="fuzzy",
                          vendor_name="ACME Corp")
```

**Ejemplo — Búsqueda por prefijo:**

```python
results = fulltext_search("Rechn", search_type="prefix",
                          date_range="last_90_days")
```

{% hint style="warning" %}
**Consulta vacía:** Pasar una cadena vacía retorna `[]` inmediatamente sin realizar una llamada HTTP.
{% endhint %}

{% hint style="info" %}
**Manejo de errores:** Si el servicio fulltextsearch no está disponible, la función retorna `[]` y registra una advertencia. **No** lanza una excepción.
{% endhint %}

---

## vector\_search()

Encuentra documentos semánticamente similares mediante embeddings vectoriales (búsqueda k-NN con vectores de 384 dimensiones).

```python
vector_search(doc_id, **kwargs)
```

**Parámetros:**

| Nombre | Tipo | Por defecto | Descripción |
| ------ | ---- | ----------- | ----------- |
| `doc_id` | `str` | obligatorio | UUID del documento fuente |
| `k` | `int` | `5` | Número de documentos similares a retornar (limitado a 50) |

**Retorna:** `list[dict]` — Cada dict contiene: `doc_id`, `name`, `doc_type`, `similarity_score` (0-1), `similarity_percent` (0-100).

**Ejemplo:**

```python
doc_id = document_json["doc_id"]
similar = vector_search(doc_id, k=5)
for doc in similar:
    print(f"{doc['name']}: {doc['similarity_percent']}% similar")
```

{% hint style="info" %}
**Cómo funciona:** Cada documento se convierte en un vector de 384 dimensiones al indexarse. La búsqueda vectorial encuentra los vecinos más cercanos en este espacio vectorial, que corresponden a documentos semánticamente similares.
{% endhint %}

---

## fulltext\_search\_erp()

Busca en datos maestros de ERP (proveedores, órdenes de compra, clientes, materiales) indexados en OpenSearch.

```python
fulltext_search_erp(query, **kwargs)
```

**Parámetros:**

| Nombre | Tipo | Por defecto | Descripción |
| ------ | ---- | ----------- | ----------- |
| `query` | `str` | obligatorio | Término de búsqueda |
| `entity_types` | `str` | `None` | Filtrar por tipo de entidad (separado por comas: `"vendor"`, `"purchase_order"`, `"customer"`, `"material"`) |
| `vendor_number` | `str` | `None` | Filtrar por número de proveedor |
| `vendor_name` | `str` | `None` | Filtrar por nombre del proveedor |
| `company_code` | `str` | `None` | Filtrar por código de empresa |
| `size` | `int` | `10` | Máx. resultados (limitado a 50) |

**Ejemplo — Validar proveedor en ERP:**

```python
vendor = get_field_value(document_data, "supplier_name", "")
if vendor:
    matches = fulltext_search_erp(vendor,
                                   entity_types="vendor", size=5)
    if not matches:
        set_field_as_invalid(document_data, "supplier_name",
                             "Proveedor no encontrado en datos maestros ERP")
```

---

## fulltext\_suggestions()

Retorna sugerencias de autocompletado para términos de búsqueda.

```python
fulltext_suggestions(query, **kwargs)
```

**Parámetros:**

| Nombre | Tipo | Por defecto | Descripción |
| ------ | ---- | ----------- | ----------- |
| `query` | `str` | obligatorio | Prefijo / término de búsqueda |
| `limit` | `int` | `10` | Máx. sugerencias por categoría (limitado a 20) |

**Ejemplo:**

```python
suggestions = fulltext_suggestions("ACM", limit=5)
vendor_list = suggestions.get("vendors", [])
```

---

## Referencia Rápida

| Función | Propósito | Retorna |
| ------- | --------- | ------- |
| `fulltext_search(query, ...)` | Buscar texto OCR en todos los documentos | `list[dict]` |
| `vector_search(doc_id, ...)` | Encontrar documentos semánticamente similares | `list[dict]` |
| `fulltext_search_erp(query, ...)` | Buscar en datos maestros ERP | `list[dict]` |
| `fulltext_suggestions(query, ...)` | Sugerencias de autocompletado | `dict` |

---

## Patrones Comunes

### Verificación de Licencia

```python
try:
    results = fulltext_search("test")
except RuntimeError:
    results = []
```

### Combinación con Funciones de Campo

```python
invoice_number = get_field_value(document_data, "invoice_id", "")
results = fulltext_search(invoice_number,
                          status="exported", size=1)
if results:
    set_field_as_invalid(document_data, "invoice_id",
                         f"Ya existe: {results[0]['name']}")
else:
    set_field_as_valid(document_data, "invoice_id", "No se encontró duplicado")
```
