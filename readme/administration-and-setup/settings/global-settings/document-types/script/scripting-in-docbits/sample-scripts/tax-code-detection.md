# Vergi Kodu Tespiti

## Bu script ne yapar?

Belgenin tam metin içeriğine ve vergi/net tutarlara göre doğru vergi kodunu otomatik olarak belirler. Ters yükleme senaryolarını, vergisiz faturaları tespit eder ve uygun kodu atamak için vergi oranını hesaplar (ör. %19 için S1, %7 için S2).

## Tetikleyici

`AFTER_FORMATTING` belge türü **INVOICE** üzerinde

## Tam Script

```python
# Belge tam metnini ve tutarları al
content = get_document_content(document_data)
tax_amount = get_field_value(document_data, "tax_amount", "0")
net_amount = get_field_value(document_data, "net_amount", "0")

try:
    tax = float(tax_amount) if tax_amount else 0
    net = float(net_amount) if net_amount else 0
except ValueError:
    tax = 0
    net = 0

# Kural 1: Tam metin üzerinden ters yükleme tespiti
if "REVERSE CHARGE" in content.upper() or "UMKEHR DER STEUERSCHULD" in content.upper():
    set_field_value(document_data, "tax_code", "RC")

# Kural 2: Sıfır vergi = vergisiz
elif tax == 0:
    set_field_value(document_data, "tax_code", "Z0")

# Kural 3: Tutarlardan vergi oranını hesapla
elif net > 0:
    tax_rate = round((tax / net) * 100, 0)
    if tax_rate == 19:
        set_field_value(document_data, "tax_code", "S1")    # Standart oran
    elif tax_rate == 7:
        set_field_value(document_data, "tax_code", "S2")    # İndirimli oran
    else:
        set_field_value(document_data, "tax_code", "S3")    # Diğer oran
```

## Adım Adım Açıklama

1. **Tam metni oku** — anahtar kelime tespiti için `get_document_content()` ile
2. **Vergi ve net tutarları oku** — vergi oranı hesaplaması için
3. **Ters yükleme kontrolü** — belge metnindeki anahtar kelimeler (Almanca ve İngilizce)
4. **Sıfır vergi kontrolü** — vergi tutarı 0 ise vergisiz kodu ata
5. **Vergi oranını hesapla** — vergi/net oranından hesaplayarak eşleşen kodu ata

## Kullanılan Fonksiyonlar

- [get\_document\_content()](../business-logic-functions.md#get\_document\_content) — OCR tam metnini okuma
- [get\_field\_value()](../field-functions.md#get\_field\_value) — Alan değerlerini okuma
- [set\_field\_value()](../field-functions.md#set\_field\_value) — Vergi kodunu ayarlama
