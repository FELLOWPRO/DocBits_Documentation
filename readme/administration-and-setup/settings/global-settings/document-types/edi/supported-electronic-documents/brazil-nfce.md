---
description: DocBits'te BRAZIL NFC-E elektronik belge desteği
---

# 🇧🇷 BRAZIL NFC-E

| Özellik | Değer |
|---------|-------|
| **Ülke / Bölge** | Brezilya |
| **Belge Türleri** | Tüketici Faturası (Nota Fiscal de Consumidor Eletrônica) |
| **Format** | XML |
| **Standart** | NFC-e 4.0 (perakende / satış noktası tüketici faturası) |
| **Yerel Ayar** | `pt_BR` |

NFC-e (Nota Fiscal de Consumidor Eletrônica, `<mod>65</mod>`), son tüketicilere yapılan perakende satışlar için kullanılan Brezilya elektronik faturasıdır. NF-e XML şemasını (`nfeProc` ad alanı) paylaşır, ancak model kodu 65 kullanır. NFC-e belgelerinde alıcı için genellikle CNPJ yerine CPF (bireysel vergi kimliği) bulunur ve basit perakende işlemlerde satır başına PIS/COFINS yer almaz.

## Destek Durumu

| Bileşen | Durum |
|---------|-------|
| Önizleme | ✅ Destekleniyor |
| Alan Çıkarımı | ✅ Destekleniyor |
| Dönüşüm | ✅ Destekleniyor |

## Varsayılan Önizleme

<figure><img src="brazil-nfce-preview.png" alt="DocBits'te Brazil NFC-e önizlemesi"><figcaption><p>BRAZIL NFC-E belgesi için varsayılan DocBits önizlemesi</p></figcaption></figure>

## Alan Eşlemesi

### Başlık Alanları

| DocBits Alanı | Kaynak XPath | Notlar |
|---|---|---|
| `invoice_id` | `//*[local-name()='ide']/*[local-name()='nNF']` | Nota Fiscal numarası |
| `invoice_date` | `//*[local-name()='ide']/*[local-name()='dhEmi']` | BRT ofseti ile ISO 8601 |
| `currency` | Sabit: `BRL` | Her zaman Brezilya Reali |
| `total_amount` | `//*[local-name()='ICMSTot']/*[local-name()='vNF']` | Toplam NFC-e değeri |
| `net_amount` | `//*[local-name()='ICMSTot']/*[local-name()='vProd']` | Ürün alt toplamı |
| `tax_amount` | `//*[local-name()='ICMSTot']/*[local-name()='vICMS']` | ICMS vergi toplamı |
| `supplier_name` | `//*[local-name()='emit']/*[local-name()='xNome']` | Perakendeci adı |
| `supplier_id` | `//*[local-name()='emit']/*[local-name()='CNPJ']` veya `CPF` | CNPJ veya CPF |
| `buyer_name` | `//*[local-name()='dest']/*[local-name()='xNome']` | Tüketici adı |
| `buyer_id` | `//*[local-name()='dest']/*[local-name()='CPF']` veya `CNPJ` | CPF (bireysel) veya CNPJ |

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
| `VAT_RATE` | `*[local-name()='imposto']/*[local-name()='ICMS']//*[local-name()='pICMS']` | ICMS oranı (%) |

> NFC-e, basit perakende işlemler için satır başına PIS/COFINS içermez.

## Sınıflandırma Kuralı

DocBits, BRAZIL NFC-E belgelerini `http://www.portalfiscal.inf.br/nfe` ad alanı içindeki `<mod>65</mod>` deseni aracılığıyla tespit eder.

## İlgili Belgeler

- [BRAZIL NF-E](brazil-nfe.md)
- [BRAZIL CT-E](brazil-cte.md)
- [BRAZIL NFS-E](brazil-nfse.md)
- [Desteklenen Elektronik Belgeler](./)
