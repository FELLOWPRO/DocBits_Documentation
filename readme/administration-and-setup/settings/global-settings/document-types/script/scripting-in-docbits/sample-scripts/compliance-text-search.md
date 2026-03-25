# Uyumluluk Metin Araması (Reverse Charge)

{% hint style="info" %}
**Sürüm 11.48.0'dan itibaren kullanılabilir** — `OPENSEARCH_ENABLED` lisansı gerektirir.
{% endhint %}

## Bu script ne yapar?

Belge arşivinde "REVERSE CHARGE" gibi uyumlulukla ilgili metinleri arar. Eşleşen belgeler varsa, vergi kodu otomatik olarak ayarlanır. Hem tam ifade eşleştirmesini hem de bulanık aramayı (OCR hataları için toleranslı) destekler.

## Tetikleyici

`AFTER_FORMATTING` belge türü **INVOICE**

## Tam Script

```python
# Kuruluşun belge arşivinde "REVERSE CHARGE" ara
rc_docs = fulltext_search(
    org_id, "REVERSE CHARGE",
    search_type="match_phrase",
    doc_type="INVOICE",
    size=5
)

if rc_docs:
    set_field_value(document_data, "tax_code", "RC")
```

## Varyant: Bulanık Arama (OCR Hatalarına Toleranslı)

```python
# Bulanık arama "REVERS CHARG" veya "REVERSE GHARGE" gibi OCR hatalarını tolere eder
rc_fuzzy = fulltext_search(
    org_id, "REVERSE CHARGE",
    search_type="fuzzy",
    vendor_name="ACME Corp"
)

if rc_fuzzy:
    set_field_value(document_data, "tax_code", "RC")
```

## Adım Adım Açıklama

1. **Arşivde ara** `fulltext_search()` kullanarak "REVERSE CHARGE" tam ifadesini
2. **Belge türüne göre filtrele** yalnızca faturaları aramak için
3. **Bulunursa**: Vergi kodu alanını otomatik olarak "RC" olarak ayarla
4. **Bulanık varyant**: OCR okuma hatalarını yakalamak için `search_type="fuzzy"` kullan (2 karakter farkına kadar)

## Kullanılan Fonksiyonlar

- [fulltext\_search()](../fulltext-search-functions.md#fulltext\_search) — Tüm belgelerde OCR metni ara
- [set\_field\_value()](../field-functions.md#set\_field\_value) — Alan değeri yaz
