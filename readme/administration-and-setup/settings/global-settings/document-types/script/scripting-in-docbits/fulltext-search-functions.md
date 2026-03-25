# Функције претраге Fulltext и векторске претраге

{% hint style="info" %}
**Доступно од верзије 11.48.0**

Ове функције захтевају да лиценца/подешавање **OPENSEARCH\_ENABLED** буде активирано за вашу организацију. Без тога, све функције бацају `RuntimeError("Fulltext search license is missing")`.
{% endhint %}

Функције за претрагу архива докумената, проналажење сличних докумената и упит ERP главних података. Оне претражују **све документе** организације — за разлику од `get_document_content()` који чита само текст тренутног документа.

**Извор:** `module/script/helper/document_script_functions.py`

---

## fulltext\_search()

Претражује комплетан OCR текст **свих докумената** у организацији. Проналази текст у пољима `pages.pageText`, `tfidfCustomPageText` и `ai_text` преко fulltextsearch микросервиса.

```python
fulltext_search(org_id, query, **kwargs)
```

**Параметри:**

| Назив | Тип | Подразумевано | Опис |
| ---- | ---- | ------- | ----------- |
| `org_id` | `str` | обавезно | UUID организације (користите контекстну варијаблу `org_id`) |
| `query` | `str` | обавезно | Термин претраге (претражује се у OCR тексту свих докумената) |
| `search_type` | `str` | `"match_phrase"` | `"match_phrase"` (тачна фраза), `"fuzzy"` (толерантно на грешке, до 2 карактера разлике), `"prefix"` (почиње са) |
| `doc_type` | `str` | `None` | Филтрирај по типу документа (раздвојено зарезом, нпр. `"INVOICE,CREDIT_NOTE"`) |
| `status` | `str` | `None` | Филтрирај по статусу документа (раздвојено зарезом, нпр. `"ready_for_validation,exported"`) |
| `vendor_name` | `str` | `None` | Филтрирај по имену добављача |
| `date_range` | `str` | `None` | `"last_30_days"`, `"last_90_days"`, `"last_180_days"`, `"last_365_days"` |
| `size` | `int` | `10` | Максимално резултата (ограничено на 50) |

**Враћа:** `list[dict]` — Сваки dict садржи:

| Поље | Опис |
| ----- | ----------- |
| `doc_id` | UUID документа |
| `name` | Назив фајла (нпр. `"INV-2026-001.pdf"`) |
| `doc_type` | Тип документа (`"INVOICE"`, `"ORDER_CONFIRMATION"`, итд.) |
| `vendor_name` | Име добављача |
| `status` | Статус документа |
| `total_amount` | Укупан износ |
| `ocr_content` | Одговарајући одломак текста из документа |
| `highlights` | Dict са истакнутим подударањима по пољу |

**Пример — Претрага тачне фразе:**

```python
results = fulltext_search(org_id, "REVERSE CHARGE",
                          doc_type="INVOICE", size=10)
for doc in results:
    print(doc["name"], doc["ocr_content"])
```

**Пример — Fuzzy претрага (толерантна на OCR грешке):**

```python
# Проналази "REVERSE CHARGE" чак и са OCR грешкама попут "REVERS CHARG"
results = fulltext_search(org_id, "REVERSE CHARGE",
                          search_type="fuzzy",
                          vendor_name="ACME Corp")
```

**Пример — Претрага по префиксу:**

```python
# Проналази све документе који садрже речи које почињу са "Rechn"
results = fulltext_search(org_id, "Rechn", search_type="prefix",
                          date_range="last_90_days")
```

{% hint style="warning" %}
**Празан упит:** Прослеђивање празног стринга одмах враћа `[]` без HTTP позива.
{% endhint %}

{% hint style="info" %}
**Руковање грешкама:** Ако је fulltextsearch сервис недоступан, функција враћа `[]` и бележи упозорење. **Не** баца изузетак.
{% endhint %}

---

## vector\_search()

Проналази семантички сличне документе користећи векторска уграђивања (k-NN претрага са 384-димензионалним векторима). Корисно за проналажење докумената са сличним садржајем без обзира на тачно формулисање.

```python
vector_search(org_id, doc_id, **kwargs)
```

**Параметри:**

| Назив | Тип | Подразумевано | Опис |
| ---- | ---- | ------- | ----------- |
| `org_id` | `str` | обавезно | UUID организације |
| `doc_id` | `str` | обавезно | UUID изворног документа (документ за који се траже слични) |
| `k` | `int` | `5` | Број сличних докумената за враћање (ограничено на 50) |

**Враћа:** `list[dict]` — Сваки dict садржи:

| Поље | Опис |
| ----- | ----------- |
| `doc_id` | UUID сличног документа |
| `name` | Назив фајла |
| `doc_type` | Тип документа |
| `similarity_score` | Сирови резултат сличности (0-1) |
| `similarity_percent` | Сличност у процентима (0-100) |

**Пример — Проналажење сличних докумената:**

```python
doc_id = document_json["doc_id"]
similar = vector_search(org_id, doc_id, k=5)
for doc in similar:
    print(f"{doc['name']}: {doc['similarity_percent']}% слично")
```

{% hint style="info" %}
**Како функционише:** Сваки документ се при индексирању конвертује у 384-димензионални вектор. Векторска претрага проналази најближе суседе у овом векторском простору, који одговарају семантички сличним документима.
{% endhint %}

---

## fulltext\_search\_erp()

Претражује ERP главне податке (добављачи, наруџбенице, клијенти, материјали) индексиране у OpenSearch-у.

```python
fulltext_search_erp(org_id, query, **kwargs)
```

**Параметри:**

| Назив | Тип | Подразумевано | Опис |
| ---- | ---- | ------- | ----------- |
| `org_id` | `str` | обавезно | UUID организације |
| `query` | `str` | обавезно | Термин претраге |
| `entity_types` | `str` | `None` | Филтрирај по типу ентитета (раздвојено зарезом: `"vendor"`, `"purchase_order"`, `"customer"`, `"material"`) |
| `vendor_number` | `str` | `None` | Филтрирај по броју добављача |
| `vendor_name` | `str` | `None` | Филтрирај по имену добављача |
| `company_code` | `str` | `None` | Филтрирај по коду компаније |
| `size` | `int` | `10` | Максимално резултата (ограничено на 50) |

**Враћа:** `list[dict]` — Поља специфична за тип ентитета (записи добављача имају `vendor_number`, `vendor_name`, итд.)

**Пример — Валидација добављача у ERP-у:**

```python
vendor = get_field_value(document_data, "supplier_name", "")
if vendor:
    matches = fulltext_search_erp(org_id, vendor,
                                   entity_types="vendor", size=5)
    if not matches:
        set_field_as_invalid(document_data, "supplier_name",
                             "Vendor not found in ERP master data")
```

**Пример — Претрага наруџбеница:**

```python
po_number = get_field_value(document_data, "purchase_order", "")
if po_number:
    results = fulltext_search_erp(org_id, po_number,
                                   entity_types="purchase_order")
    if results:
        # Наруџбеница пронађена у ERP-у
        set_field_as_valid(document_data, "purchase_order", "PO verified in ERP")
```

---

## fulltext\_suggestions()

Враћа предлоге за аутоматско довршавање за термине претраге. Групише резултате по категорији (добављачи, називи фајлова, бројеви фактура).

```python
fulltext_suggestions(org_id, query, **kwargs)
```

**Параметри:**

| Назив | Тип | Подразумевано | Опис |
| ---- | ---- | ------- | ----------- |
| `org_id` | `str` | обавезно | UUID организације |
| `query` | `str` | обавезно | Префикс / термин претраге |
| `limit` | `int` | `10` | Максимално предлога по категорији (ограничено на 20) |

**Враћа:** `dict` са груписаним предлозима:

```python
{
    "vendors": ["ACME Corp", "ACME International"],
    "filenames": ["INV-2026-001.pdf", "INV-2026-002.pdf"],
    "invoice_numbers": ["INV-2026-001", "INV-2026-002"]
}
```

**Пример — Добијање предлога добављача:**

```python
suggestions = fulltext_suggestions(org_id, "ACM", limit=5)
vendor_list = suggestions.get("vendors", [])
```

{% hint style="warning" %}
**Празан упит:** Прослеђивање празног стринга одмах враћа `{}`.
{% endhint %}

---

## Брзи преглед

| Функција | Намена | Враћа |
| -------- | ------- | ------- |
| `fulltext_search()` | Претрага OCR текста у свим документима | `list[dict]` |
| `vector_search()` | Проналажење семантички сличних докумената | `list[dict]` |
| `fulltext_search_erp()` | Претрага ERP главних података | `list[dict]` |
| `fulltext_suggestions()` | Предлози за аутоматско довршавање | `dict` |

---

## Уобичајени обрасци

### Провера лиценце

Све четири функције аутоматски проверавају подешавање `OPENSEARCH_ENABLED`. Ако није активирано:

```python
# Ово ће бацити RuntimeError("Fulltext search license is missing")
results = fulltext_search(org_id, "test")
```

За елегантно руковање овим у скриптама:

```python
try:
    results = fulltext_search(org_id, "test")
except RuntimeError:
    # OpenSearch није активиран за ову организацију — прескочи претрагу
    results = []
```

### Комбиновање са функцијама поља

```python
# Претражи → валидирај → постави поље
results = fulltext_search(org_id, invoice_number,
                          status="exported", size=1)
if results:
    set_field_as_invalid(document_data, "invoice_id",
                         f"Already exists: {results[0]['name']}")
else:
    set_field_as_valid(document_data, "invoice_id", "No duplicate found")
```
