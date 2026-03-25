# Vade Tarihi Hesaplama

## Bu script ne yapar?

Fatura tarihine yapılandırılabilir sayıda gün (ör. 30) ekleyerek ödeme vadesini hesaplar. Hafta sonları otomatik olarak atlanır, böylece vade tarihi her zaman bir iş gününe denk gelir.

## Tetikleyici

`AFTER_FORMATTING` belge türü **INVOICE** üzerinde

## Tam Script

```python
# Fatura tarihini oku
inv_date = get_field_value(document_data, "invoice_date")

if inv_date:
    # Vade tarihini hesapla: fatura tarihinden 30 gün sonra, hafta sonlarını atla
    set_date_value(document_data, "due_date", inv_date,
                   add_days=30, skip_weekend=True)

    # Muhasebe tarihini de fatura tarihi olarak ayarla
    set_date_value(document_data, "accounting_date", inv_date)
```

## Varyasyonlar

### 14 gün, Pazartesiler hariç

```python
set_date_value(document_data, "due_date", inv_date,
               add_days=14, skip_weekend=True, exclude_final_days="MONDAY")
```

### 60 gün, hafta sonu atlamasız

```python
set_date_value(document_data, "due_date", inv_date, add_days=60)
```

### Teslimat tarihini bugün olarak ayarla

```python
set_date_value(document_data, "delivery_date", None)  # None = bugün
```

## Adım Adım Açıklama

1. **Fatura tarihini** belgeden oku
2. **Vade tarihini hesapla** — `set_date_value()` ile `add_days=30` ve `skip_weekend=True` kullanarak
3. **Tarih biçimlendirmesi** otomatiktir — belgenin `date_format_pattern`'ini kullanır (ör. `%d.%m.%Y`)
4. **Hafta sonu atlama** vade tarihinin Pazartesi-Cuma arasına denk gelmesini sağlar

## `exclude_final_days` için Gün Kodları

`MONDAY`, `TUESDAY`, `WEDNESDAY`, `THURSDAY`, `FRIDAY`, `SATURDAY`, `SUNDAY`

## Kullanılan Fonksiyonlar

- [get\_field\_value()](../field-functions.md#get\_field\_value) — Fatura tarihini okuma
- [set\_date\_value()](../field-functions.md#set\_date\_value) — Vade tarihini hesaplama ve ayarlama
