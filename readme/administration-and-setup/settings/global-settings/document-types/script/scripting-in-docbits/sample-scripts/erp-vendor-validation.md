# ERP Tedarikçi Doğrulaması

{% hint style="info" %}
**Sürüm 11.48.0'dan itibaren kullanılabilir** — `OPENSEARCH_ENABLED` lisansı gerektirir.
{% endhint %}

## Bu script ne yapar?

Faturadaki tedarikçinin OpenSearch'te indekslenmiş ERP ana verilerinde var olup olmadığını doğrular. Tedarikçi ERP'de bulunamazsa, alan geçersiz olarak işaretlenir. Bu, lookup tablosu yerine ERP indeksini arayarak mevcut `is_supplier_valid()` fonksiyonunu tamamlar.

## Tetikleyici

`AFTER_FORMATTING` belge türü **INVOICE**

## Tam Script

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

## Varyant: Tedarikçi Numarasıyla Doğrulama

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
        # Tedarikçi adını ERP'den otomatik doldur
        erp_vendor = erp_matches[0]
        set_field_value(document_data, "supplier_name",
                        erp_vendor.get("vendor_name", ""))
    else:
        set_field_as_invalid(
            document_data, "supplier_id",
            f"Vendor '{vendor_nr}' not found in ERP"
        )
```

## Adım Adım Açıklama

1. **Tedarikçi adını oku** mevcut belgeden
2. **ERP ana verilerini ara** `fulltext_search_erp()` ile varlık türü `"vendor"` olarak filtrele
3. **Bulunamazsa**: Tedarikçi adı alanını geçersiz olarak işaretle
4. **Varyant**: Tedarikçi numarasına göre ara ve tedarikçi adını ERP verilerinden otomatik doldur

## Kullanılan Fonksiyonlar

- [get\_field\_value()](../field-functions.md#get\_field\_value) — Alan değerini oku
- [fulltext\_search\_erp()](../fulltext-search-functions.md#fulltext\_search\_erp) — ERP ana verilerini ara
- [set\_field\_as\_invalid()](../field-functions.md#set\_field\_as\_invalid) — Doğrulama hatası göster
- [set\_field\_value()](../field-functions.md#set\_field\_value) — Alan değeri yaz
