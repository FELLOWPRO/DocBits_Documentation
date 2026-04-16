---
description: DocBits'te AUNZ PINT SELF-BILLING elektronik belge desteği
---

# 🇦🇺 AUNZ PINT SELF-BILLING

| Özellik | Değer |
|----------|-------|
| **Ülke / Bölge** | Avustralya / Yeni Zelanda |
| **Belge Türleri** | Self-Billing Faturası |
| **Format** | UBL 2.1 XML |
| **Standard** | PINT A-NZ Self-Billing |
| **Locale** | `en_AU` |

AUNZ PINT Self-Billing, A-NZ Peppol International fatura modelinin self-billing varyantıdır. Self-billing senaryolarında alıcı, faturayı tedarikçi adına oluşturur. Bu belge türü aynı PINT A-NZ yapısını takip eder, ancak taraf rolleri tersine çevrilmiştir — `AccountingCustomerParty` faturalayan taraf olur ve `AccountingSupplierParty` faturalanan taraftır.

## Destek Durumu

| Bileşen | Durum |
|-----------|--------|
| Önizleme | ✅ Destekleniyor |
| Alan Çıkarımı | ✅ Destekleniyor |
| Dönüşüm | ✅ Destekleniyor |

## Varsayılan Önizleme

<figure><img src="aunz-pint-preview.png" alt="DocBits'te AUNZ PINT Self-Billing fatura önizlemesi"><figcaption><p>AUNZ PINT Self-Billing faturası için varsayılan DocBits önizlemesi</p></figcaption></figure>

## Alan Eşlemesi

Alan eşlemesi, aşağıdaki temel farkla [AUNZ PINT](aunz-pint.md) ile aynıdır:

- **Taraf rolleri tersine çevrilmiştir**: Self-billing'de alıcı faturalayan taraf, tedarikçi faturalanan taraftır
- `CustomizationID`, `billing-1@aunz` yerine `urn:peppol.org:pint:selfbilling-1@aunz` içerir

Tam alan eşleme tablosu için bkz. [AUNZ PINT](aunz-pint.md#field-mapping).

## Sınıflandırma Kuralı

DocBits, `CustomizationID` eşleştirerek self-billing belgelerini algılar:

```
urn:peppol.org:pint:selfbilling-1@aunz
```

Self-billing ve normal faturalama, `PINT A-NZ` elektronik belge türü altında sınıflandırılır.

## Ayrıca bakınız

- [AUNZ PINT](aunz-pint.md)
- [Desteklenen elektronik belgeler](./)
