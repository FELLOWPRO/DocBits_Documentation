# Tablo Toplamı Doğrulaması

## Bu script ne yapar?

Fatura tablosundaki tüm satır toplamlarının toplamının belgenin net tutarıyla eşleşip eşleşmediğini doğrular. 0,01'den büyük bir tutarsızlık varsa, hesaplanan toplam çıkarılan net tutarın yerini alır — satır kalemleri ile başlık alanları arasında tutarlılığı sağlar.

## Tetikleyici

`AFTER_FORMATTING` belge türü **INVOICE** üzerinde

## Tam Script

```python
table = tables_dict.get("INVOICE_TABLE")
if table:
    # Tüm satır toplamlarının toplamını hesapla
    total = 0
    for row in table["rows"]:
        line_total = get_column_value(row, "LINE_TOTAL", "0")
        try:
            total += float(line_total)
        except ValueError:
            pass

    # Çıkarılan net tutarla karşılaştır
    net_amount = get_field_value(document_data, "net_amount", "0")
    try:
        if abs(float(net_amount) - total) > 0.01:
            # Satır toplamı başlıktan farklı — net tutarı güncelle
            set_amount_value(document_data, "net_amount", str(round(total, 2)))
    except ValueError:
        pass
```

## Varyasyon: Üzerine yazmak yerine geçersiz olarak işaretle

```python
table = tables_dict.get("INVOICE_TABLE")
if table:
    total = 0
    for row in table["rows"]:
        line_total = get_column_value(row, "LINE_TOTAL", "0")
        try:
            total += float(line_total)
        except ValueError:
            pass

    net_amount = get_field_value(document_data, "net_amount", "0")
    try:
        diff = abs(float(net_amount) - total)
        if diff > 0.01:
            set_field_as_invalid(document_data, "net_amount",
                f"Satır toplamı ({round(total, 2)}) net tutardan ({net_amount}) farklı")
        else:
            set_field_as_valid(document_data, "net_amount", "Tutarlar eşleşiyor")
    except ValueError:
        pass
```

## Adım Adım Açıklama

1. **Fatura tablosunu** `tables_dict`'ten al
2. **Tüm LINE_TOTAL değerlerini** tablo satırları boyunca topla
3. **Karşılaştır** — hesaplanan toplamı çıkarılan net tutarla
4. **Güncelle veya işaretle** — ya net tutarı değiştir ya da geçersiz olarak işaretle

## Kullanılan Fonksiyonlar

- [get\_column\_value()](../table-functions.md#get\_column\_value) — Satırlardan sütun değerlerini okuma
- [get\_field\_value()](../field-functions.md#get\_field\_value) — Net tutarı okuma
- [set\_amount\_value()](../field-functions.md#set\_amount\_value) — Düzeltilmiş tutarı ayarlama
- [set\_field\_as\_invalid()](../field-functions.md#set\_field\_as\_invalid) — Alanı geçersiz olarak işaretleme
- [set\_field\_as\_valid()](../field-functions.md#set\_field\_as\_valid) — Alanı geçerli olarak işaretleme
