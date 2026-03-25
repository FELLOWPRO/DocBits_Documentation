# Eksik Alanları Belge Geçmişinden Doldurma

{% hint style="info" %}
**Sürüm 11.48.0'dan itibaren kullanılabilir** — `OPENSEARCH_ENABLED` lisansı gerektirir.
{% endhint %}

## Bu script ne yapar?

Bir belgede SB numarası olup tedarikçi adı eksik olduğunda, bu script belge arşivinde aynı SB numarasını içeren diğer faturaları arar ve ilk eşleşmeden tedarikçi adını kopyalar.

## Tetikleyici

`AFTER_FORMATTING` belge türü **INVOICE**

## Tam Script

```python
po = get_field_value(document_data, "purchase_order", "")
supplier = get_field_value(document_data, "supplier_name", "")

if po and not supplier:
    # Arşivde bu SB numarasına sahip belgeleri ara
    history = fulltext_search(
        org_id, po,
        doc_type="INVOICE",
        size=3
    )

    for doc in history:
        if doc.get("vendor_name"):
            set_field_value(document_data, "supplier_name", doc["vendor_name"])
            break
```

## Adım Adım Açıklama

1. **SB numarası ve tedarikçiyi oku** mevcut belgeden
2. **Koşulu kontrol et**: Yalnızca SB varsa ama tedarikçi eksikse devam et
3. **Arşivde ara** SB numarasını içeren belgeleri
4. **Tedarikçi adını kopyala** tedarikçi adı ayarlanmış ilk eşleşmeden

## Varyant: Birden Fazla Alanı Doldurma

```python
po = get_field_value(document_data, "purchase_order", "")
supplier = get_field_value(document_data, "supplier_name", "")

if po and not supplier:
    history = fulltext_search(org_id, po, doc_type="INVOICE", size=3)

    for doc in history:
        if doc.get("vendor_name"):
            set_field_value(document_data, "supplier_name", doc["vendor_name"])
            # Varsa diğer alanları da doldur
            if doc.get("total_amount") and not get_field_value(document_data, "total_amount", ""):
                set_field_value(document_data, "total_amount", doc["total_amount"])
            break
```

## Kullanılan Fonksiyonlar

- [get\_field\_value()](../field-functions.md#get\_field\_value) — Alan değerini oku
- [fulltext\_search()](../fulltext-search-functions.md#fulltext\_search) — Tüm belgelerde OCR metni ara
- [set\_field\_value()](../field-functions.md#set\_field\_value) — Alan değeri yaz
