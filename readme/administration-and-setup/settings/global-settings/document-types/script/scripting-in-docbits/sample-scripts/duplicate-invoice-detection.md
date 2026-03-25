# Детекција дупликата фактура

{% hint style="info" %}
**Доступно од верзије 11.48.0** — Захтева `OPENSEARCH_ENABLED` лиценцу.
{% endhint %}

## Шта ради ова скрипта?

Претражује архив докумената за постојеће фактуре са истим бројем фактуре од истог добављача. Ако се пронађе потенцијални дупликат, поље броја фактуре се означава као неважеће са упозорењем које приказује назив документа дупликата и његов статус.

## Окидач

`AFTER_FORMATTING` на типу документа **INVOICE**

## Комплетна скрипта

```python
inv_id = get_field_value(document_data, "invoice_id", "")
vendor = get_field_value(document_data, "supplier_name", "")

if inv_id and vendor:
    # Претрага докумената са истим бројем фактуре од истог добављача
    existing = fulltext_search(
        org_id, inv_id,
        vendor_name=vendor,
        status="ready_for_validation,exported",
        size=5
    )

    # Искључи тренутни документ из резултата
    current_doc_id = document_json["doc_id"]
    duplicates = [d for d in existing if d["doc_id"] != current_doc_id]

    if duplicates:
        dup = duplicates[0]
        set_field_as_invalid(
            document_data, "invoice_id",
            f"Possible duplicate: {dup['name']} ({dup.get('status', 'unknown')})"
        )
```

## Објашњење корак по корак

1. **Прочитај број фактуре и добављача** из тренутног документа
2. **Претражи архив** са `fulltext_search()` филтрирајући по имену добављача и релевантним статусима
3. **Искључи тренутни документ** из резултата да се избегне самоподударање
4. **Означи као неважеће** ако се пронађе дупликат, приказујући назив фајла и статус постојећег документа

## Коришћене функције

- [get\_field\_value()](../field-functions.md#get\_field\_value) — Читање вредности поља
- [fulltext\_search()](../fulltext-search-functions.md#fulltext\_search) — Претрага OCR текста у свим документима
- [set\_field\_as\_invalid()](../field-functions.md#set\_field\_as\_invalid) — Приказ грешке валидације
