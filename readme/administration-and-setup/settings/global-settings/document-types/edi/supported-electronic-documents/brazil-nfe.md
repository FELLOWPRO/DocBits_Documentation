---
description: DocBits'te BRAZIL NF-E elektronik belge desteği
---

# 🇧🇷 BRAZIL NF-E

| Özellik | Değer |
|---------|-------|
| **Ülke / Bölge** | Brezilya |
| **Belge Türleri** | Fatura (Nota Fiscal Eletrônica) |
| **Format** | XML |
| **Standart** | NF-e 4.0 (Nota Fiscal Eletrônica — mal ve eyaletlerarası ticaret) |
| **Yerel Ayar** | `pt_BR` |

NF-e (Nota Fiscal Eletrônica, `<mod>55</mod>`), SEFAZ tarafından düzenlenen, mal satışları ve eyaletlerarası ticaret için kullanılan Brezilya elektronik faturasıdır. Her NF-e, benzersiz 44 haneli bir erişim anahtarı (`chNFe`), ayrıntılı ürün kalem satırları ve çok katmanlı vergi verileri (ICMS, IPI, PIS, COFINS) içerir. DocBits, NF-e belgelerini `http://www.portalfiscal.inf.br/nfe` ad alanını tespit ederek sınıflandırır.

## Destek Durumu

| Bileşen | Durum |
|---------|-------|
| Önizleme | ✅ Destekleniyor |
| Alan Çıkarımı | ✅ Destekleniyor |
| Dönüşüm | ✅ Destekleniyor |

## Varsayılan Önizleme

<figure><img src="brazil-nfe-preview.png" alt="DocBits'te Brazil NF-e önizlemesi"><figcaption><p>BRAZIL NF-E belgesi için varsayılan DocBits önizlemesi</p></figcaption></figure>

## Alan Eşlemesi

### Başlık Alanları

| DocBits Alanı | Kaynak XPath | Notlar |
|---|---|---|
| `invoice_id` | `//*[local-name()='ide']/*[local-name()='nNF']` | Nota Fiscal numarası |
| `invoice_date` | `//*[local-name()='ide']/*[local-name()='dhEmi']` | BRT ofseti ile ISO 8601 |
| `currency` | Sabit: `BRL` | Her zaman Brezilya Reali |
| `total_amount` | `//*[local-name()='ICMSTot']/*[local-name()='vNF']` | Toplam NF-e değeri |
| `net_amount` | `//*[local-name()='ICMSTot']/*[local-name()='vProd']` | Toplam ürün değeri |
| `tax_amount` | `//*[local-name()='ICMSTot']/*[local-name()='vICMS']` | ICMS vergi toplamı |
| `supplier_name` | `//*[local-name()='emit']/*[local-name()='xNome']` | Düzenleyen şirket adı |
| `supplier_id` | `//*[local-name()='emit']/*[local-name()='CNPJ']` veya `CPF` | CNPJ (14 hane) veya CPF (11 hane) |
| `buyer_name` | `//*[local-name()='dest']/*[local-name()='xNome']` | Alıcı şirket adı |
| `buyer_id` | `//*[local-name()='dest']/*[local-name()='CNPJ']` veya `CPF` | CNPJ veya CPF |

### Kalem Satırı Tablosu (`INVOICE_TABLE`)

Satır yolu: `//*[local-name()='det']`

| Sütun | Göreli XPath | Notlar |
|---|---|---|
| `POSITION` | `@nItem` | Kalem sıra numarası |
| `ITEM_CODE` | `*[local-name()='prod']/*[local-name()='cProd']` | Ürün kodu |
| `DESCRIPTION` | `*[local-name()='prod']/*[local-name()='xProd']` | Ürün açıklaması |
| `NCM_CODE` | `*[local-name()='prod']/*[local-name()='NCM']` | NCM gümrük sınıflandırması |
| `CFOP_CODE` | `*[local-name()='prod']/*[local-name()='CFOP']` | İşlem mali kodu |
| `UNIT` | `*[local-name()='prod']/*[local-name()='uCom']` | Ölçü birimi |
| `QUANTITY` | `*[local-name()='prod']/*[local-name()='qCom']` | Ticari miktar |
| `UNIT_PRICE` | `*[local-name()='prod']/*[local-name()='vUnCom']` | Birim fiyat |
| `TOTAL_AMOUNT` | `*[local-name()='prod']/*[local-name()='vProd']` | Satır toplamı |
| `ICMS_AMOUNT` | `*[local-name()='imposto']/*[local-name()='ICMS']//*[local-name()='vICMS']` | Satır başına ICMS vergisi |
| `PIS_AMOUNT` | `*[local-name()='imposto']/*[local-name()='PIS']//*[local-name()='vPIS']` | Satır başına PIS vergisi |
| `COFINS_AMOUNT` | `*[local-name()='imposto']/*[local-name()='COFINS']//*[local-name()='vCOFINS']` | Satır başına COFINS vergisi |
| `VAT_RATE` | `*[local-name()='imposto']/*[local-name()='ICMS']//*[local-name()='pICMS']` | ICMS oranı (%) |

## Sınıflandırma Kuralı

DocBits, BRAZIL NF-E belgelerini XML ad alanında şu dizeyi arayarak tespit eder:

```
http://www.portalfiscal.inf.br/nfe
```

(`mod=55` NF-e için, `mod=65` NFC-e için ayrıca ayırt edilir).

## İlgili Belgeler

- [BRAZIL NFC-E](brazil-nfce.md)
- [BRAZIL CT-E](brazil-cte.md)
- [BRAZIL NFS-E](brazil-nfse.md)
- [Desteklenen Elektronik Belgeler](./)
