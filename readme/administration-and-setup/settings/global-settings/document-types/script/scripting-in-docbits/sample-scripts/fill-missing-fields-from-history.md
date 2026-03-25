# Попуњавање недостајућих поља из историје докумената

{% hint style="info" %}
**Доступно од верзије 11.48.0** — Захтева `OPENSEARCH_ENABLED` лиценцу.
{% endhint %}

## Шта ради ова скрипта?

Када документ има број наруџбенице али недостаје име добављача, ова скрипта претражује архив докумената за друге фактуре које садрже исти број наруџбенице и копира име добављача из првог подударања.

## Окидач

`AFTER_FORMATTING` на типу документа **INVOICE**

## Комплетна скрипта

```python
po = get_field_value(document_data, "purchase_order", "")
supplier = get_field_value(document_data, "supplier_name", "")

if po and not supplier:
    # Претрага архива за документе са овим бројем наруџбенице
    history = fulltext_search(
        po,
        doc_type="INVOICE",
        size=3
    )

    for doc in history:
        if doc.get("vendor_name"):
            set_field_value(document_data, "supplier_name", doc["vendor_name"])
            break
```

## Објашњење корак по корак

1. **Прочитај број наруџбенице и добављача** из тренутног документа
2. **Провери услов**: Настави само ако наруџбеница постоји али добављач недостаје
3. **Претражи архив** за документе који садрже број наруџбенице
4. **Копирај име добављача** из првог подударања које има постављено име добављача

## Варијанта: Попуњавање више поља

```python
po = get_field_value(document_data, "purchase_order", "")
supplier = get_field_value(document_data, "supplier_name", "")

if po and not supplier:
    history = fulltext_search(po, doc_type="INVOICE", size=3)

    for doc in history:
        if doc.get("vendor_name"):
            set_field_value(document_data, "supplier_name", doc["vendor_name"])
            # Попуни и друга поља ако су доступна
            if doc.get("total_amount") and not get_field_value(document_data, "total_amount", ""):
                set_field_value(document_data, "total_amount", doc["total_amount"])
            break
```

## Коришћене функције

- [get\_field\_value()](../field-functions.md#get\_field\_value) — Читање вредности поља
- [fulltext\_search()](../fulltext-search-functions.md#fulltext\_search) — Претрага OCR текста у свим документима
- [set\_field\_value()](../field-functions.md#set\_field\_value) — Уписивање вредности поља
