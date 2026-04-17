---
description: DocBits'te Danimarka OIOUBL 2.1 elektronik belge desteği
---

# 🇩🇰 Danimarka OIOUBL 2.1

| Özellik | Değer |
|----------|-------|
| **Ülke / Bölge** | Danimarka |
| **Belge Türleri** | Fatura (Faktura), Alacak Dekontu |
| **Format** | XML (UBL 2.1) |
| **Standart** | OIOUBL 2.1 (Offentlig Information Online UBL) |
| **Yerel Ayar** | `da_DK` |

OIOUBL (Offentlig Information Online UBL), UBL 2.1 tabanlı Danimarka e-fatura standardıdır. Danimarka kamu sektörü kuruluşlarına yönelik faturalar için zorunludur ve B2B işlemlerinde yaygın olarak kullanılmaktadır. DocBits, `<cbc:CustomizationID>OIOUBL-2.1</cbc:CustomizationID>` öğesinin varlığını kontrol ederek OIOUBL 2.1 belgelerini tespit eder. `urn:www.nesubl.eu:profiles:profile5:ver2.0` profil tanımlayıcısı, NES (Northern European Subset) fatura profilini belirtir.

## Destek Durumu

| Bileşen | Durum |
|-----------|--------|
| Önizleme | ✅ Desteklenir |
| Alan Çıkarma | ✅ Desteklenir |
| Dönüştürme | ✅ Desteklenir |

## Varsayılan Önizleme

<figure><img src="denmark-oioubl-preview.png" alt="DocBits'te Danimarka OIOUBL 2.1 fatura önizlemesi"><figcaption><p>Danimarka OIOUBL 2.1 faturası (Faktura) için varsayılan DocBits önizlemesi</p></figcaption></figure>

## Alan Eşleştirmesi

### Başlık Alanları

| DocBits Alanı | Kaynak XML Öğesi | Notlar |
|---|---|---|
| `invoice_id` | `cbc:ID` | Fatura numarası |
| `invoice_date` | `cbc:IssueDate` | ISO 8601 düzenleme tarihi |
| `due_date` | `cbc:DueDate` | Ödeme son tarihi |
| `invoice_type` | `cbc:InvoiceTypeCode` | UNCL 1001 kodu (380=Fatura, 381=Alacak Dekontu) |
| `currency` | `cbc:DocumentCurrencyCode` | Her zaman `DKK` (Danimarka Kronu) |
| `purchase_order` | `cac:OrderReference/cbc:ID` | Alıcının sipariş referans numarası |
| `buyer_reference` | `cbc:BuyerReference` | Alıcının dahili referansı / EAN konum numarası |
| `note` | `cbc:Note` | Serbest metin ödeme talimatları veya notları |
| `net_amount` | `cac:LegalMonetaryTotal/cbc:TaxExclusiveAmount` | KDV hariç net tutar |
| `tax_amount` | `cac:TaxTotal/cbc:TaxAmount` | Toplam KDV tutarı (%25 standart oran) |
| `total_amount` | `cac:LegalMonetaryTotal/cbc:PayableAmount` | KDV dahil toplam tutar |
| `tax_rate` | `cac:TaxTotal/cac:TaxSubtotal/cac:TaxCategory/cbc:Percent` | % olarak KDV oranı |
| `supplier_name` | `cac:AccountingSupplierParty/cac:Party/cac:PartyName/cbc:Name` | Tedarikçi şirket adı |
| `supplier_id` | `cac:AccountingSupplierParty/cac:Party/cac:PartyIdentification/cbc:ID` | CVR numarası (ör. `DK12345678`) |
| `supplier_vat` | `cac:AccountingSupplierParty/cac:Party/cac:PartyTaxScheme/cbc:CompanyID` | KDV/CVR numarası |
| `supplier_address` | `cac:AccountingSupplierParty/.../cbc:StreetName` | Tedarikçi sokak adresi |
| `supplier_city` | `cac:AccountingSupplierParty/.../cbc:CityName` | Tedarikçi şehri |
| `supplier_postal_code` | `cac:AccountingSupplierParty/.../cbc:PostalZone` | Tedarikçi posta kodu |
| `supplier_country` | `cac:AccountingSupplierParty/.../cbc:IdentificationCode` | ISO ülke kodu (`DK`) |
| `customer_name` | `cac:AccountingCustomerParty/cac:Party/cac:PartyName/cbc:Name` | Müşteri şirket adı |
| `customer_id` | `cac:AccountingCustomerParty/cac:Party/cac:PartyIdentification/cbc:ID` | CVR numarası |
| `customer_vat` | `cac:AccountingCustomerParty/cac:Party/cac:PartyTaxScheme/cbc:CompanyID` | KDV/CVR numarası |
| `customer_address` | `cac:AccountingCustomerParty/.../cbc:StreetName` | Müşteri sokak adresi |
| `customer_city` | `cac:AccountingCustomerParty/.../cbc:CityName` | Müşteri şehri |
| `customer_postal_code` | `cac:AccountingCustomerParty/.../cbc:PostalZone` | Müşteri posta kodu |
| `customer_country` | `cac:AccountingCustomerParty/.../cbc:IdentificationCode` | ISO ülke kodu (`DK`) |
| `iban` | `cac:PaymentMeans/cac:PayeeFinancialAccount/cbc:ID` | Banka hesabı / IBAN |
| `bic` | `cac:PaymentMeans/cac:PayeeFinancialAccount/cac:FinancialInstitutionBranch/cbc:ID` | BIC/SWIFT kodu |

### Satır Kalemi Tablosu (`INVOICE_TABLE`)

Satır yolu: `cac:InvoiceLine`

| Sütun | Kaynak XML Öğesi | Notlar |
|---|---|---|
| `POSITION` | `cbc:ID` | Satır sıra numarası |
| `DESCRIPTION` | `cac:Item/cbc:Name` | Kalem adı / açıklaması |
| `QUANTITY` | `cbc:InvoicedQuantity` | Faturalandırılan miktar |
| `UNIT_PRICE` | `cac:Price/cbc:PriceAmount` | KDV hariç birim fiyat |
| `NET_AMOUNT` | `cbc:LineExtensionAmount` | KDV hariç satır toplamı |

## Sınıflandırma Kuralı

DocBits, `CustomizationID` öğesiyle eşleşerek OIOUBL 2.1 belgelerini tespit eder:

| Elektronik Belge Türü | Desen |
|--------------------------|---------|
| OIOUBL 2.1 | `<cbc:CustomizationID>OIOUBL-2\.1\s*</cbc:CustomizationID>` |

Kök öğe, `urn:oasis:names:specification:ubl:schema:xsd:Invoice-2` UBL 2.1 ad alanında `<Invoice>` (veya `<CreditNote>`) şeklindedir.

## İlgili

- [Şu Anda Desteklenen E-Fatura Standartları](../../currently-supported-e-invoice-standards/)
- [Desteklenen Elektronik Belgeler](./)
