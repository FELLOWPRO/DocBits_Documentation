# Претрага текста усклађености (Reverse Charge)

{% hint style="info" %}
**Доступно од верзије 11.48.0** — Захтева `OPENSEARCH_ENABLED` лиценцу.
{% endhint %}

## Шта ради ова скрипта?

Претражује текст релевантан за усклађеност попут "REVERSE CHARGE" у архиву докумената. Ако постоје подударајући документи, порески код се аутоматски поставља. Подржава и подударање тачне фразе и fuzzy претрагу (толерантну на OCR грешке).

## Окидач

`AFTER_FORMATTING` на типу документа **INVOICE**

## Комплетна скрипта

```python
# Претрага "REVERSE CHARGE" у архиву докумената организације
rc_docs = fulltext_search(
    org_id, "REVERSE CHARGE",
    search_type="match_phrase",
    doc_type="INVOICE",
    size=5
)

if rc_docs:
    set_field_value(document_data, "tax_code", "RC")
```

## Варијанта: Fuzzy претрага (толерантна на OCR грешке)

```python
# Fuzzy претрага толерише OCR грешке попут "REVERS CHARG" или "REVERSE GHARGE"
rc_fuzzy = fulltext_search(
    org_id, "REVERSE CHARGE",
    search_type="fuzzy",
    vendor_name="ACME Corp"
)

if rc_fuzzy:
    set_field_value(document_data, "tax_code", "RC")
```

## Објашњење корак по корак

1. **Претражи архив** за тачну фразу "REVERSE CHARGE" користећи `fulltext_search()`
2. **Филтрирај по типу документа** да се претражују само фактуре
3. **Ако је пронађено**: Аутоматски постави поље пореског кода на "RC"
4. **Fuzzy варијанта**: Користи `search_type="fuzzy"` за хватање OCR грешака читања (до 2 карактера разлике)

## Коришћене функције

- [fulltext\_search()](../fulltext-search-functions.md#fulltext\_search) — Претрага OCR текста у свим документима
- [set\_field\_value()](../field-functions.md#set\_field\_value) — Уписивање вредности поља
