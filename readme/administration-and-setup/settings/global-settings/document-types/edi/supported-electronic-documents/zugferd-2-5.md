---
description: ZUGFERD 2.5 elektronik belge desteği - DocBits
---

# 🇩🇪 ZUGFERD 2.5

| Özellik | Değer |
|-----------|-------|
| **Ülke/Bölge** | Almanya |
| **Belge türleri** | Fatura, Kredi notu |
| **Biçim** | CII (PDF/A-3 gömülü) veya UBL XML |
| **Standart** | ZUGFeRD 2.5 |
| **Temel aldığı standart** | EN 16931 |

ZUGFeRD 2.5 (Haziran 2026 FeRD/FNFE-MPE ortak yayını), Factur-X 1.09 ile eşdeğerdir. CII XML'i, D16B ile geriye dönük uyumlu olan UN/CEFACT D22B tabanını kullanır; bu nedenle ZUGFeRD 2.4'ün tüm çıkarma ve dönüştürme sözleşmesi geçerliliğini korur. EXTENDED profili; ödeme araçları ve BIC için yeni alanlar, üçüncü taraf lehtar (faktör) ve indirim/artırım için vergi muafiyeti nedeni alanlarını ekler.

Beş profilin tamamı desteklenir: MINIMUM, BASIC WL, BASIC, EN 16931 (COMFORT) ve EXTENDED. DocBits, CII ve UBL varyantlarını ayrı ayrı sınıflandırır.

## Destek Durumu

| Bileşen | Durum |
|-----------|--------|
| Önizleme | ✅ Destekleniyor |
| Alan çıkarımı | ✅ Destekleniyor |
| Dönüştürme | ✅ Destekleniyor |

## İlgili

- [Factur-X 1.09 / ZUGFeRD 2.5](facturx-1-09-zugferd-2-5.md)
- [ZUGFeRD Yapılandırması](../zugferd/configuration.md)
- [ZUGFeRD Alan Eşlemesi](../zugferd/README.md)
- [Desteklenen Elektronik Belgeler](./)
