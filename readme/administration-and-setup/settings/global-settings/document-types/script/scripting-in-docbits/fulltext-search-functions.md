# Funciones de búsqueda Fulltext y vectorial

{% hint style="info" %}
**Disponible desde la versión 11.48.0**

Estas funciones requieren que la licencia/preferencia **OPENSEARCH\_ENABLED** esté activada para su organización. Sin ella, todas las funciones lanzan un `RuntimeError("Fulltext search license is missing")`.
{% endhint %}

Funciones para buscar en archivos de documentos, encontrar documentos similares y consultar datos maestros de ERP. Estas buscan en **todos los documentos** de la organización, a diferencia de `get_document_content()`, que solo lee el texto del documento actual.

{% hint style="success" %}
**Seguridad:** El `org_id` lo inyecta automáticamente el sandbox de scripts. Nunca necesita pasarlo: sus scripts siempre operan dentro de los datos de su propia organización.
{% endhint %}

**Fuente:** `module/script/helper/document_script_functions.py`

---

## fulltext\_search()

Busca en el texto OCR completo de **todos los documentos** de la organización. Encuentra texto en los campos `pages.pageText`, `tfidfCustomPageText` y `ai_text` a través del microservicio fulltextsearch.

```python
fulltext_search(query, **kwargs)
```

**Parámetros:**

| Nombre | Tipo | Valor predeterminado | Descripción |
| ---- | ---- | ------- | ----------- |
| `query` | `str` | obligatorio | Término de búsqueda (se busca en el texto OCR de todos los documentos) |
| `search_type` | `str` | `"match_phrase"` | `"match_phrase"` (frase exacta), `"fuzzy"` (tolerante a errores tipográficos, hasta 2 caracteres de diferencia), `"prefix"` (empieza por) |
| `doc_type` | `str` | `None` | Filtrar por tipo de documento (separado por comas, p. ej. `"INVOICE,CREDIT_NOTE"`) |
| `status` | `str` | `None` | Filtrar por estado del documento (separado por comas, p. ej. `"ready_for_validation,exported"`) |
| `vendor_name` | `str` | `None` | Filtrar por nombre del proveedor |
| `date_range` | `str` | `None` | `"last_30_days"`, `"last_90_days"`, `"last_180_days"`, `"last_365_days"` |
| `size` | `int` | `10` | Máximo de resultados (limitado a 50) |

**Devuelve:** `list[dict]`. Cada dict contiene:

| Campo | Descripción |
| ----- | ----------- |
| `doc_id` | UUID del documento |
| `name` | Nombre del archivo (p. ej. `"INV-2026-001.pdf"`) |
| `doc_type` | Tipo de documento (`"INVOICE"`, `"ORDER_CONFIRMATION"`, etc.) |
| `vendor_name` | Nombre del proveedor |
| `status` | Estado del documento |
| `total_amount` | Importe total |
| `ocr_content` | Extracto de texto coincidente del documento |
| `highlights` | Dict con las coincidencias resaltadas por campo |

**Ejemplo: búsqueda de una frase exacta:**

```python
results = fulltext_search("REVERSE CHARGE",
                          doc_type="INVOICE", size=10)
for doc in results:
    print(doc["name"], doc["ocr_content"])
```

**Ejemplo: búsqueda aproximada (tolerante a errores de OCR):**

```python
# Finds "REVERSE CHARGE" even with OCR errors like "REVERS CHARG"
results = fulltext_search("REVERSE CHARGE",
                          search_type="fuzzy",
                          vendor_name="ACME Corp")
```

**Ejemplo: búsqueda por prefijo:**

```python
# Finds all documents containing words starting with "Rechn"
results = fulltext_search("Rechn", search_type="prefix",
                          date_range="last_90_days")
```

{% hint style="warning" %}
**Consulta vacía:** Pasar una cadena vacía devuelve `[]` de inmediato, sin realizar ninguna llamada HTTP.
{% endhint %}

{% hint style="info" %}
**Gestión de errores:** Si el servicio fulltextsearch no está accesible, la función devuelve `[]` y registra una advertencia. **No** lanza ninguna excepción.
{% endhint %}

---

## vector\_search()

Encuentra documentos semánticamente similares mediante embeddings vectoriales (búsqueda k-NN con vectores de 384 dimensiones). Es útil para encontrar documentos con contenido similar, independientemente de la redacción exacta.

```python
vector_search(doc_id, **kwargs)
```

**Parámetros:**

| Nombre | Tipo | Valor predeterminado | Descripción |
| ---- | ---- | ------- | ----------- |
| `doc_id` | `str` | obligatorio | UUID del documento de origen (el documento para el que se buscan coincidencias similares) |
| `k` | `int` | `5` | Número de documentos similares que se devuelven (limitado a 50) |

**Devuelve:** `list[dict]`. Cada dict contiene:

| Campo | Descripción |
| ----- | ----------- |
| `doc_id` | UUID del documento similar |
| `name` | Nombre del archivo |
| `doc_type` | Tipo de documento |
| `similarity_score` | Puntuación de similitud sin procesar (0-1) |
| `similarity_percent` | Similitud como porcentaje (0-100) |

**Ejemplo: encontrar documentos similares:**

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

Busca en los datos maestros de ERP (proveedores, órdenes de compra, clientes, materiales) indexados en OpenSearch.

```python
fulltext_search_erp(query, **kwargs)
```

**Parámetros:**

| Nombre | Tipo | Valor predeterminado | Descripción |
| ---- | ---- | ------- | ----------- |
| `query` | `str` | obligatorio | Término de búsqueda |
| `entity_types` | `str` | `None` | Filtrar por tipo de entidad (separado por comas: `"vendor"`, `"purchase_order"`, `"customer"`, `"material"`) |
| `vendor_number` | `str` | `None` | Filtrar por número de proveedor |
| `vendor_name` | `str` | `None` | Filtrar por nombre del proveedor |
| `company_code` | `str` | `None` | Filtrar por código de sociedad |
| `size` | `int` | `10` | Máximo de resultados (limitado a 50) |

**Devuelve:** `list[dict]`. Campos específicos de cada tipo de entidad (los registros de proveedor tienen `vendor_number`, `vendor_name`, etc.)

**Ejemplo: validar un proveedor en el ERP:**

```python
vendor = get_field_value(document_data, "supplier_name", "")
if vendor:
    matches = fulltext_search_erp(vendor,
                                   entity_types="vendor", size=5)
    if not matches:
        set_field_as_invalid(document_data, "supplier_name",
                             "Vendor not found in ERP master data")
```

**Ejemplo: buscar órdenes de compra:**

```python
po_number = get_field_value(document_data, "purchase_order", "")
if po_number:
    results = fulltext_search_erp(po_number,
                                   entity_types="purchase_order")
    if results:
        # PO found in ERP
        set_field_as_valid(document_data, "purchase_order", "PO verified in ERP")
```

---

## fulltext\_suggestions()

Devuelve sugerencias de autocompletado para los términos de búsqueda. Agrupa los resultados por categoría (proveedores, nombres de archivo, números de factura).

```python
fulltext_suggestions(query, **kwargs)
```

**Parámetros:**

| Nombre | Tipo | Valor predeterminado | Descripción |
| ---- | ---- | ------- | ----------- |
| `query` | `str` | obligatorio | Prefijo / término de búsqueda |
| `limit` | `int` | `10` | Máximo de sugerencias por categoría (limitado a 20) |

**Devuelve:** `dict` con las sugerencias agrupadas:

```python
{
    "vendors": ["ACME Corp", "ACME International"],
    "filenames": ["INV-2026-001.pdf", "INV-2026-002.pdf"],
    "invoice_numbers": ["INV-2026-001", "INV-2026-002"]
}
```

**Ejemplo: obtener sugerencias de proveedores:**

```python
suggestions = fulltext_suggestions("ACM", limit=5)
vendor_list = suggestions.get("vendors", [])
```

{% hint style="warning" %}
**Consulta vacía:** Pasar una cadena vacía devuelve `{}` de inmediato.
{% endhint %}

---

## Referencia rápida

| Función | Finalidad | Devuelve |
| -------- | ------- | ------- |
| `fulltext_search(query, ...)` | Buscar en el texto OCR de todos los documentos | `list[dict]` |
| `vector_search(doc_id, ...)` | Encontrar documentos semánticamente similares | `list[dict]` |
| `fulltext_search_erp(query, ...)` | Buscar en los datos maestros de ERP | `list[dict]` |
| `fulltext_suggestions(query, ...)` | Sugerencias de autocompletado | `dict` |

---

## Patrones habituales

### Comprobación de licencia

Las cuatro funciones comprueban automáticamente la preferencia `OPENSEARCH_ENABLED`. Si no está activada:

```python
# This will raise RuntimeError("Fulltext search license is missing")
results = fulltext_search("test")
```

Para gestionarlo de forma elegante en los scripts:

```python
try:
    results = fulltext_search("test")
except RuntimeError:
    # OpenSearch not enabled for this org — skip search
    results = []
```

### Combinación con funciones de campo

```python
# Search → validate → set field
invoice_number = get_field_value(document_data, "invoice_id", "")
results = fulltext_search(invoice_number,
                          status="exported", size=1)
if results:
    set_field_as_invalid(document_data, "invoice_id",
                         f"Already exists: {results[0]['name']}")
else:
    set_field_as_valid(document_data, "invoice_id", "No duplicate found")
```
