# ERP валидација добављача

{% hint style="info" %}
**Доступно од верзије 11.48.0** — Захтева `OPENSEARCH_ENABLED` лиценцу.
{% endhint %}

## Шта ради ова скрипта?

Валидира да ли добављач на фактури постоји у ERP главним подацима индексираним у OpenSearch-у. Ако добављач није пронађен у ERP-у, поље се означава као неважеће. Ово допуњава постојећу функцију `is_supplier_valid()` претражујући ERP индекс уместо lookup табеле.

## Окидач

`AFTER_FORMATTING` на типу документа **INVOICE**

## Комплетна скрипта

```python
vendor = get_field_value(document_data, "supplier_name", "")

if vendor:
    erp_matches = fulltext_search_erp(
        org_id, vendor,
        entity_types="vendor",
        size=5
    )

    if not erp_matches:
        set_field_as_invalid(
            document_data, "supplier_name",
            "Vendor not found in ERP master data"
        )
```

## Варијанта: Валидација са бројем добављача

```python
vendor_nr = get_field_value(document_data, "supplier_id", "")

if vendor_nr:
    erp_matches = fulltext_search_erp(
        org_id, vendor_nr,
        entity_types="vendor",
        vendor_number=vendor_nr,
        size=1
    )

    if erp_matches:
        # Аутоматски попуни име добављача из ERP-а
        erp_vendor = erp_matches[0]
        set_field_value(document_data, "supplier_name",
                        erp_vendor.get("vendor_name", ""))
    else:
        set_field_as_invalid(
            document_data, "supplier_id",
            f"Vendor '{vendor_nr}' not found in ERP"
        )
```

## Објашњење корак по корак

1. **Прочитај име добављача** из тренутног документа
2. **Претражи ERP главне податке** са `fulltext_search_erp()` филтрирајући по типу ентитета `"vendor"`
3. **Ако није пронађен**: Означи поље имена добављача као неважеће
4. **Варијанта**: Претражи по броју добављача и аутоматски попуни име добављача из ERP података

## Коришћене функције

- [get\_field\_value()](../field-functions.md#get\_field\_value) — Читање вредности поља
- [fulltext\_search\_erp()](../fulltext-search-functions.md#fulltext\_search\_erp) — Претрага ERP главних података
- [set\_field\_as\_invalid()](../field-functions.md#set\_field\_as\_invalid) — Приказ грешке валидације
- [set\_field\_value()](../field-functions.md#set\_field\_value) — Уписивање вредности поља
