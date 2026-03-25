# Yüksek Fatura Tutarı için Görev

## Bu script ne yapar?

Fatura toplamı bir eşiği (ör. 100.000) aştığında bir onay görevi oluşturur. Görev, "Finance Approval" grubuna atanır ve zamanında inceleme sağlamak için e-posta bildirimi tetikler.

## Tetikleyici

`AFTER_FORMATTING` belge türü **INVOICE** üzerinde

## Tam Script

```python
# Belgeden toplam tutarı oku
total = get_field_value(document_data, "total_amount", "0")

try:
    if float(total) > 100000:
        # Finance Approval grubunu ada göre bul
        finance_group = get_group_by_name(org_id, "Finance Approval")

        # Onay görevi oluştur
        create_document_task(
            user,
            document_data,
            title="Tutar > 100.000 - Onay gerekli",
            description=f"Toplam tutar: {total}",
            priority="HIGH",
            assigned_to_user_id=None,
            assigned_to_group_id=str(finance_group.id) if finance_group else None,
            send_email=True
        )
except ValueError:
    pass
```

## Adım Adım Açıklama

1. **Toplam tutarı** belgeden oku
2. **Eşiği kontrol et** — yalnızca tutar 100.000'i aştığında devam et
3. **Grubu bul** — grup ID'sini dinamik olarak almak için `get_group_by_name()` kullan
4. **Görev oluştur** — yüksek öncelik ve e-posta bildirimi ile finans grubuna atanmış

## Kullanılan Fonksiyonlar

- [get\_field\_value()](../field-functions.md#get\_field\_value) — Alan değerini okuma
- [get\_group\_by\_name()](../business-logic-functions.md#get\_group\_by\_id--get\_group\_by\_name) — Ada göre grup bulma
- [create\_document\_task()](../business-logic-functions.md#create\_document\_task) — Onay görevi oluşturma
