# Otomatik SB Eşleştirme

## Bu script ne yapar?

Faturada bir SB (Satınalma Belgesi) numarası bulunduğunda otomatik olarak SB eşleştirmesini tetikler. po-match-service mikroservisi, fatura satır kalemlerini SB ile karşılaştırır ve eşleşme sonuçlarını doldurur.

## Tetikleyici

`AFTER_FORMATTING` belge türü **INVOICE** üzerinde

## Tam Script

```python
# Belgeden SB numarasını oku
po_nr = get_field_value(document_data, "purchase_order", "")

if po_nr:
    # SB numarasını temizle: ön eki ve boşlukları kaldır
    po_nr = po_nr.strip()
    if po_nr.upper().startswith("PO"):
        po_nr = po_nr[2:].strip()
    if po_nr.startswith("-") or po_nr.startswith(" "):
        po_nr = po_nr[1:].strip()

    # Temizlenmiş SB numarasını güncelle
    set_field_value(document_data, "purchase_order", po_nr)

    # Otomatik SB eşleştirmesini tetikle
    auto_po_match_for_purchase_orders(user, document_data, po_nr)
```

## Adım Adım Açıklama

1. **SB numarasını** faturadan oku
2. **Temizle** — "PO-" veya "PO " gibi yaygın ön ekleri kaldırarak SB numarasını düzenle
3. **Güncelle** — temizlenmiş SB numarasını belgeye geri yaz
4. **SB eşleştirmesini tetikle** — fatura satırlarını SB satırlarıyla karşılaştırmak için po-match-service'i çağırır

## Eşleştirme sonrası ne olur?

`document_data` şu bilgilerle güncellenir:
- `po_items` — Eşleşen SB satır kalemleri
- `po_match_status` — Eşleşme sonucu (`"matched"`, `"partially_matched"` vb.)
- `po_multi_matched` — Birden fazla SB'nin eşleşip eşleşmediği

## Kullanılan Fonksiyonlar

- [get\_field\_value()](../field-functions.md#get\_field\_value) — Alan değerini okuma
- [set\_field\_value()](../field-functions.md#set\_field\_value) — Temizlenmiş SB numarasını yazma
- [auto\_po\_match\_for\_purchase\_orders()](../business-logic-functions.md#auto\_po\_match\_for\_purchase\_orders) — SB eşleştirmesini tetikleme
