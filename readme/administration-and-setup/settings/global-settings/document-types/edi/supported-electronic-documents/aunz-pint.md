---
description: DocBits'te AUNZ PINT elektronik belge desteği
---

# 🇦🇺 AUNZ PINT

| Özellik | Değer |
|----------|-------|
| **Ülke / Bölge** | Avustralya / Yeni Zelanda |
| **Belge Türleri** | Fatura, Kredi Notu |
| **Format** | UBL 2.1 XML |
| **Standard** | PINT A-NZ (Peppol International Model for Australia-New Zealand) |
| **Locale** | `en_AU` |

AUNZ PINT, Peppol International (PINT) fatura modelinin Avustralya/Yeni Zelanda uygulamasıdır. ABN/NZBN kimliklendirmesi, GST işleme ve A-NZ Peppol Authority spesifikasyonlarına uyum dahil olmak üzere A-NZ mevzuat gereksinimlerine uyarlanmış UBL 2.1 tabanlı bir fatura formatı tanımlar. DocBits, `PINT A-NZ` elektronik belge türü altında standart Fatura ve Kredi Notu belge türlerinin yanı sıra Self-Billing varyantını da destekler.

## Destek Durumu

| Bileşen | Durum |
|-----------|--------|
| Önizleme | ✅ Destekleniyor |
| Alan Çıkarımı | ✅ Destekleniyor |
| Dönüşüm | ✅ Destekleniyor |

## Varsayılan Önizleme

<figure><img src="aunz-pint-preview.png" alt="DocBits'te AUNZ PINT fatura önizlemesi"><figcaption><p>AUNZ PINT faturası için varsayılan DocBits önizlemesi</p></figcaption></figure>

## Alan Eşlemesi

### Başlık Alanları

| DocBits Alanı | Kaynak XPath (UBL 2.1) | Notlar |
|---|---|---|
| `invoice_id` | `cbc:ID` | Fatura numarası |
| `invoice_date` | `cbc:IssueDate` | ISO 8601 tarihi |
| `due_date` | `cbc:DueDate` | Vade tarihi |
| `currency` | `cbc:DocumentCurrencyCode` | Tipik olarak `AUD` veya `NZD` |
| `total_amount` | `cbc:PayableAmount` (`cac:LegalMonetaryTotal` içinde) | GST dahil toplam |
| `net_amount` | `cbc:TaxExclusiveAmount` (`cac:LegalMonetaryTotal` içinde) | GST hariç alttoplam |
| `tax_amount` | `cbc:TaxAmount` (`cac:TaxTotal` içinde) | GST tutarı |
| `purchase_order` | `cbc:BuyerReference` | Alıcının satınalma referansı |
| `payment_terms` | `cbc:Note` (`cac:PaymentTerms` içinde) | Serbest metin ödeme koşulları |
| `supplier_name` | `cac:AccountingSupplierParty/cac:Party/cac:PartyName/cbc:Name` | Tedarikçi şirket adı |
| `supplier_id` | `cac:AccountingSupplierParty/cac:Party/cbc:EndpointID` | ABN (schemeID 0151) |
| `supplier_tax_id` | `cac:AccountingSupplierParty/cac:Party/cac:PartyTaxScheme/cbc:CompanyID` | ABN veya GST numarası |
| `supplier_street` | `cac:AccountingSupplierParty/cac:Party/cac:PostalAddress/cbc:StreetName` | Tedarikçi sokak |
| `supplier_city` | `cac:AccountingSupplierParty/cac:Party/cac:PostalAddress/cbc:CityName` | Tedarikçi şehir |
| `supplier_postal_code` | `cac:AccountingSupplierParty/cac:Party/cac:PostalAddress/cbc:PostalZone` | Tedarikçi posta kodu |
| `supplier_country` | `cac:AccountingSupplierParty/cac:Party/cac:PostalAddress/cac:Country/cbc:IdentificationCode` | ISO ülke kodu (`AU` veya `NZ`) |
| `buyer_name` | `cac:AccountingCustomerParty/cac:Party/cac:PartyName/cbc:Name` | Alıcı şirket adı |
| `buyer_id` | `cac:AccountingCustomerParty/cac:Party/cbc:EndpointID` | ABN/NZBN (schemeID 0151) |
| `buyer_street` | `cac:AccountingCustomerParty/cac:Party/cac:PostalAddress/cbc:StreetName` | Alıcı sokak |
| `buyer_city` | `cac:AccountingCustomerParty/cac:Party/cac:PostalAddress/cbc:CityName` | Alıcı şehir |
| `buyer_postal_code` | `cac:AccountingCustomerParty/cac:Party/cac:PostalAddress/cbc:PostalZone` | Alıcı posta kodu |
| `buyer_country` | `cac:AccountingCustomerParty/cac:Party/cac:PostalAddress/cac:Country/cbc:IdentificationCode` | ISO ülke kodu |
| `iban` | `cac:PaymentMeans/cac:PayeeFinancialAccount/cbc:ID` | Ödeme hesabı kimliği |

### Satır Tablosu (`INVOICE_TABLE`)

Satır yolu: `cac:InvoiceLine`

| Sütun | Kaynak XPath (UBL 2.1) | Notlar |
|---|---|---|
| `POSITION` | `cbc:ID` | Satır numarası |
| `DESCRIPTION` | `cac:Item/cbc:Description` | Ürün/hizmet açıklaması |
| `QUANTITY` | `cbc:InvoicedQuantity` | Miktar (`@unitCode` içinde birim kodu) |
| `UNIT` | `cbc:InvoicedQuantity/@unitCode` | Birim kodu (ör. `C62` = adet, `EA` = her bir) |
| `UNIT_PRICE` | `cac:Price/cbc:PriceAmount` | GST hariç birim fiyat |
| `VAT_RATE` | `cac:Item/cac:ClassifiedTaxCategory/cbc:Percent` | GST oranı % |
| `VAT` | *(vergi tutarından hesaplanır)* | Satır başına GST tutarı |
| `NET_AMOUNT` | `cbc:LineExtensionAmount` | GST hariç satır toplamı |

## Sınıflandırma Kuralları

DocBits, `CustomizationID` öğesini eşleştirerek PINT A-NZ belgelerini algılar:

| Örüntü | Kural Türü | Elektronik Belge Türü |
|---------|-----------|--------------------------|
| `urn:peppol.org:pint:billing-1@aunz` | STRING_CONTAINS | PINT A-NZ (Fatura) |
| `urn:peppol.org:pint:selfbilling-1@aunz` | STRING_CONTAINS | PINT A-NZ (Self-Billing Faturası) |

Her iki örüntü de `PINT A-NZ` elektronik belge türü altında sınıflandırılır. Kök öğe standart faturalar için `<Invoice>`, kredi notları için `<CreditNote>` şeklindedir.

### A-NZ'ye Özgü Özellikler

- **ABN/NZBN tanımlayıcıları**: Avustralya İş Numaraları ve Yeni Zelanda İş Numaraları için `schemeID="0151"` kullanır
- **GST vergisi**: GST vergi düzeniyle `S` (standart oranlı) vergi kategorisini kullanır
- **CustomizationID**: PINT A-NZ olarak sınıflandırılmak için `@aunz` sonekini içermelidir (vs. global PINT)

## Ayrıca bakınız

- [AUNZ PINT Self-Billing](aunz-pint-self-billing.md)
- [PINT A-NZ](pint-a-nz.md)
- [Desteklenen elektronik belgeler](./)
