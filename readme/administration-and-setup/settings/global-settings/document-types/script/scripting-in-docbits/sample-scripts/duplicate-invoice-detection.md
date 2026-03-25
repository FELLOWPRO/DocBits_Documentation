# Yinelenen Fatura Tespiti

{% hint style="info" %}
**Sürüm 11.48.0'dan itibaren kullanılabilir** — `OPENSEARCH_ENABLED` lisansı gerektirir.
{% endhint %}

## Bu script ne yapar?

Aynı tedarikçiden aynı fatura numarasına sahip mevcut faturalar için belge arşivini arar. Olası bir kopya bulunursa, fatura numarası alanı kopya belgenin adını ve durumunu gösteren bir uyarıyla geçersiz olarak işaretlenir.

## Tetikleyici

`AFTER_FORMATTING` belge türü **INVOICE**

## Tam Script

```python
inv_id = get_field_value(document_data, "invoice_id", "")
vendor = get_field_value(document_data, "supplier_name", "")

if inv_id and vendor:
    # Aynı tedarikçiden aynı fatura numarasına sahip belgeleri ara
    existing = fulltext_search(
        org_id, inv_id,
        vendor_name=vendor,
        status="ready_for_validation,exported",
        size=5
    )

    # Mevcut belgeyi sonuçlardan hariç tut
    current_doc_id = document_json["doc_id"]
    duplicates = [d for d in existing if d["doc_id"] != current_doc_id]

    if duplicates:
        dup = duplicates[0]
        set_field_as_invalid(
            document_data, "invoice_id",
            f"Possible duplicate: {dup['name']} ({dup.get('status', 'unknown')})"
        )
```

## Adım Adım Açıklama

1. **Fatura numarası ve tedarikçiyi oku** mevcut belgeden
2. **Arşivde ara** `fulltext_search()` ile tedarikçi adı ve ilgili durumlara göre filtrele
3. **Mevcut belgeyi hariç tut** sonuçlardan kendi kendine eşleşmeyi önlemek için
4. **Geçersiz olarak işaretle** kopya bulunursa, mevcut belgenin dosya adı ve durumunu göstererek

## Kullanılan Fonksiyonlar

- [get\_field\_value()](../field-functions.md#get\_field\_value) — Alan değerini oku
- [fulltext\_search()](../fulltext-search-functions.md#fulltext\_search) — Tüm belgelerde OCR metni ara
- [set\_field\_as\_invalid()](../field-functions.md#set\_field\_as\_invalid) — Doğrulama hatası göster
