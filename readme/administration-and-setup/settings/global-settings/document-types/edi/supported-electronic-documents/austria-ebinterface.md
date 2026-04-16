---
description: DocBits'te AUSTRIA EBINTERFACE elektronik belge desteği
---

# 🇦🇹 AUSTRIA EBINTERFACE

| Özellik | Değer |
|----------|-------|
| **Ülke/Bölge** | Avusturya |
| **Belge türleri** | Fatura, Kredi notu |
| **Biçim** | XML |
| **Standart** | ebInterface (sürümler 4.3 – 6.1) |
| **Locale** | `de_AT` |

ebInterface, Avusturya Federal Ekonomi Odası (WKO — Wirtschaftskammer Osterreich) tarafından sürdürülen Avusturya e-faturalandırma standardıdır. Avusturya'da başlıca B2G (işletme-devlet) ve B2B işlemlerinde kullanılan elektronik faturalar için yapılandırılmış bir XML biçimi tanımlar. DocBits, 4.3'ten 6.1'e kadar tüm sürümleri destekler ve her biri kendi XML ad alanı ile tanımlanır.

## Destek durumu

| Bileşen | Durum |
|-----------|--------|
| Önizleme | ✅ Destekleniyor |
| Alan eşlemesi | ✅ Destekleniyor |
| Dönüşüm | ✅ Destekleniyor |

## Varsayılan önizleme

<figure><img src="austria-ebinterface-preview.png" alt="DocBits'te Austria ebInterface fatura önizlemesi"><figcaption><p>AUSTRIA EBINTERFACE faturası için varsayılan DocBits önizlemesi</p></figcaption></figure>

## Alan eşlemesi

### Başlık alanları

| DocBits alanı | Kaynak XML öğesi | Notlar |
|---|---|---|
| `invoice_id` | `eb:InvoiceNumber` | Fatura numarası |
| `invoice_date` | `eb:InvoiceDate` | ISO 8601 tarihi |
| `due_date` | `eb:PaymentConditions/eb:DueDate` | Ödeme vadesi |
| `delivery_date` | `eb:Delivery/eb:Date` | Teslimat tarihi |
| `currency` | `@eb:InvoiceCurrency` | Kök öznitelik, AT için her zaman `EUR` |
| `total_amount` | `eb:TotalGrossAmount` | KDV dahil bruto toplam |
| `net_amount` | `eb:Tax/eb:VAT/eb:VATItem/eb:TaxedAmount` | Net vergi matrahı |
| `tax_amount` | `eb:Tax/eb:VAT/eb:VATItem/eb:Amount` | KDV tutarı |
| `purchase_order` | `eb:OrderReference/eb:OrderID` | Satınalma sipariş referansı |
| `payment_terms` | `eb:PaymentConditions/eb:Comment` | Serbest metin ödeme koşulları |
| `supplier_name` | `eb:Biller/eb:Address/eb:Name` | Fatura kesen şirket adı |
| `supplier_tax_id` | `eb:Biller/eb:VATIdentificationNumber` | Avusturya UID'si (örn. ATU12345678) |
| `supplier_street` | `eb:Biller/eb:Address/eb:Street` | Fatura kesen sokak adresi |
| `supplier_city` | `eb:Biller/eb:Address/eb:Town` | Fatura kesen şehir |
| `supplier_postal_code` | `eb:Biller/eb:Address/eb:ZIP` | Fatura kesen posta kodu |
| `supplier_country` | `eb:Biller/eb:Address/eb:Country/@eb:CountryCode` | ISO ülke kodu |
| `supplier_email` | `eb:Biller/eb:Address/eb:Email` | Fatura kesen e-posta |
| `supplier_iban` | `eb:PaymentMethod/eb:UniversalBankTransaction/eb:BeneficiaryAccount/eb:IBAN` | Fatura kesen IBAN |
| `customer_name` | `eb:InvoiceRecipient/eb:Address/eb:Name` | Alıcı şirket adı |
| `customer_tax_id` | `eb:InvoiceRecipient/eb:VATIdentificationNumber` | Alıcı UID'si |
| `customer_street` | `eb:InvoiceRecipient/eb:Address/eb:Street` | Alıcı sokak adresi |
| `customer_city` | `eb:InvoiceRecipient/eb:Address/eb:Town` | Alıcı şehir |
| `customer_postal_code` | `eb:InvoiceRecipient/eb:Address/eb:ZIP` | Alıcı posta kodu |
| `customer_country` | `eb:InvoiceRecipient/eb:Address/eb:Country/@eb:CountryCode` | ISO ülke kodu |
| `iban` | `eb:PaymentMethod/eb:UniversalBankTransaction/eb:BeneficiaryAccount/eb:IBAN` | Ödeme IBAN'ı |
| `bic` | `eb:PaymentMethod/eb:UniversalBankTransaction/eb:BeneficiaryAccount/eb:BIC` | Ödeme BIC'i |

### Kalem tablosu (`INVOICE_TABLE`)

Satır yolu: `eb:Details/eb:ItemList/eb:ListLineItem`

| Sütun | Kaynak XML öğesi | Notlar |
|---|---|---|
| `POSITION` | Sıralı indeks | 1'den başlayan satır numarası |
| `DESCRIPTION` | `eb:Description` | Ürün/hizmet açıklaması |
| `QUANTITY` | `eb:Quantity` | Sayısal miktar |
| `UNIT` | `eb:Quantity/@eb:Unit` | Birim kodu (örn. `STK` = adet) |
| `UNIT_PRICE` | `eb:UnitPrice` | KDV hariç birim fiyat |
| `VAT_RATE` | `eb:VAT/eb:VATItem/eb:VATRate` | % cinsinden KDV oranı |
| `VAT` | `eb:VAT/eb:VATItem/eb:TaxedAmount` | Satır başına KDV tutarı |
| `NET_AMOUNT` | `eb:LineItemAmount` | KDV hariç satır toplamı |

## Sınıflandırma kuralı

DocBits, XML ad alanını eşleştirerek ebInterface sürümünü algılar:

| Sürüm | Ad alanı |
|---------|-----------|
| ebInterface 4.3 | `http://www.ebinterface.at/schema/4p3/` |
| ebInterface 5.0 | `http://www.ebinterface.at/schema/5p0/` |
| ebInterface 6.0 | `http://www.ebinterface.at/schema/6p0/` |
| ebInterface 6.1 | `http://www.ebinterface.at/schema/6p1/` |

Tüm sürümler, ilgili ad alanı URI'si ile `<eb:Invoice>` kök öğesini paylaşır.

## İlgili

- [Austria ebInterface 6.0](austria-ebinterface-6-0.md)
- [Austria ebInterface 6.1](austria-ebinterface-6-1.md)
- [Desteklenen elektronik belgeler](./)