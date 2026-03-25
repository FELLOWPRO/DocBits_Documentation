# Tedarikçi Lookup Doğrulaması

## Bu script ne yapar?

Faturadaki tedarikçi numarasını arama tablosundaki ana verilere karşı doğrular. Tedarikçi bulunursa, adı ve ödeme koşulları otomatik olarak doldurulur. Bulunamazsa, kullanıcının düzeltebilmesi için alan geçersiz olarak işaretlenir.

## Tetikleyici

`AFTER_FORMATTING` belge türü **INVOICE** üzerinde

## Tam Script

```python
# Belgeden tedarikçi ID'sini oku
supplier_id = get_field_value(document_data, "supplier_id", "")

if supplier_id:
    # Tedarikçi arama tablosunu sorgula
    records = get_lookup_records(
        org_id,                                    # Mevcut organizasyon
        document_json.get("sub_org_id"),           # Alt org (varsa)
        "supplier",                                # Arama tablosu adı
        [["VENDOR_ID", supplier_id]],              # Filtre: VENDOR_ID üzerinde tam eşleşme
        limit=1                                    # Yalnızca ilk eşleşme gerekli
    )

    if records:
        # Tedarikçi bulundu — ilgili alanları otomatik doldur
        supplier = records[0]
        set_field_value(document_data, "supplier_name", supplier.get("NAME", ""))
        set_field_value(document_data, "payment_terms", supplier.get("PAYMENT_TERMS", ""))
    else:
        # Tedarikçi bulunamadı — geçersiz olarak işaretle
        set_field_as_invalid(document_data, "supplier_id",
                             f"Tedarikçi '{supplier_id}' ana verilerde bulunamadı")
```

## Adım Adım Açıklama

1. **Tedarikçi ID'sini** `get_field_value()` ile belgeden oku
2. **Arama tablosunu sorgula** — tedarikçi numarasını filtre olarak kullanarak `get_lookup_records()` ile
3. **Eşleşme durumunda**: Ana verilerden tedarikçi adı ve ödeme koşullarını otomatik doldur
4. **Eşleşme yoksa**: Tedarikçi ID alanını açıklayıcı bir hata mesajıyla geçersiz olarak işaretle

## Kullanılan Fonksiyonlar

- [get\_field\_value()](../field-functions.md#get\_field\_value) — Alan değerini okuma
- [get\_lookup\_records()](../business-logic-functions.md#get\_lookup\_records) — Ana verileri sorgulama
- [set\_field\_value()](../field-functions.md#set\_field\_value) — Alan değerini yazma
- [set\_field\_as\_invalid()](../field-functions.md#set\_field\_as\_invalid) — Doğrulama hatası gösterme
