---
description: İspanya Facturae (3.2, 3.2.1, 3.2.2) – DocBits'te elektronik belge desteği
---

# 🇪🇸 İspanya Facturae

| Özellik | Değer |
|---------|-------|
| **Ülke / Bölge** | İspanya |
| **Belge Türleri** | Fatura (Factura), Alacak Notu |
| **Format** | XML |
| **Standart** | Facturae 3.2 / 3.2.1 / 3.2.2 (Agencia Tributaria / AEAT) |
| **Yerel Ayar** | `es_ES` |

Facturae, Agencia Estatal de Administración Tributaria (AEAT) ve Maliye Bakanlığı tarafından yönetilen İspanya'nın zorunlu e-fatura standardıdır. İspanya kamu sektörü kuruluşlarına yönelik faturalar için zorunlu olup B2B işlemlerinde de yaygın olarak kullanılmaktadır. Kök eleman, sürümlü bir ad alanı URL'sine sahip `<fe:Facturae>`'dır. DocBits, sürümü resmi şema URL'lerinden birine başvuran `xsi:schemaLocation` özniteliği aracılığıyla algılar:

| Sürüm | Şema URL'si |
|-------|------------|
| Facturae 3.2 | `http://www.facturae.gob.es/formato/Versiones/Facturaev3_2.xml` |
| Facturae 3.2.1 | `http://www.facturae.gob.es/formato/Versiones/Facturaev3_2_1.xml` |
| Facturae 3.2.2 | `http://www.facturae.gob.es/formato/Versiones/Facturaev3_2_2.xml` |

## Destek Durumu

| Bileşen | Durum |
|---------|-------|
| Önizleme | ✅ Destekleniyor |
| Alan Çıkarma | ✅ Destekleniyor |
| Dönüşüm | ✅ Destekleniyor |

## Varsayılan Önizleme

<figure><img src="spain-facturae-preview.png" alt="DocBits'te İspanya Facturae fatura önizlemesi"><figcaption><p>İspanya Facturae 3.2.2 faturası için DocBits varsayılan önizlemesi</p></figcaption></figure>

## Alan Eşleştirmesi

### Başlık Alanları

| DocBits Alanı | Kaynak XML Elemanı | Notlar |
|---|---|---|
| `invoice_id` | `Invoices/Invoice/InvoiceHeader/InvoiceNumber` | Fatura numarası |
| `invoice_date` | `Invoices/Invoice/InvoiceIssueData/IssueDate` | Düzenleme tarihi (YYYY-AA-GG) |
| `due_date` | `PaymentDetails/Installment/InstallmentDueDate` | Ödeme son tarihi |
| `invoice_type` | `Invoices/Invoice/InvoiceHeader/InvoiceDocumentType` | FC=Fatura, NC=Alacak Notu |
| `currency` | `Invoices/Invoice/InvoiceIssueData/InvoiceCurrencyCode` | Her zaman `EUR` |
| `purchase_order` | `Invoices/Invoice/InvoiceHeader/ReceiverContractReference` | Alıcı sipariş / sözleşme referansı |
| `net_amount` | `Invoices/Invoice/InvoiceTotals/TotalGrossAmountBeforeTaxes` | KDV hariç net tutar |
| `tax_amount` | `Invoices/Invoice/InvoiceTotals/TotalTaxOutputs` | Toplam KDV tutarı |
| `total_amount` | `Invoices/Invoice/InvoiceTotals/InvoiceTotal` | KDV dahil toplam tutar |
| `tax_rate` | `TaxesOutputs/Tax/TaxRate` | KDV oranı % (standart %21) |
| `payment_terms` | `PaymentDetails/Installment/PaymentMeans` | Ödeme aracı kodu |
| `supplier_name` | `Parties/SellerParty/LegalEntity/CorporateName` | Tedarikçi şirket adı |
| `supplier_id` | `Parties/SellerParty/TaxIdentification/TaxIdentificationNumber` | NIF/CIF (ör. `ES12345678A`) |
| `supplier_tax_id` | `Parties/SellerParty/TaxIdentification/TaxIdentificationNumber` | İspanyol NIF veya CIF vergi kimliği |
| `supplier_address` | `Parties/SellerParty/LegalEntity/AddressInSpain/Address` | Tedarikçi adresi |
| `supplier_city` | `Parties/SellerParty/LegalEntity/AddressInSpain/Town` | Tedarikçi şehri |
| `supplier_postal_code` | `Parties/SellerParty/LegalEntity/AddressInSpain/PostCode` | Tedarikçi posta kodu |
| `supplier_country` | `Parties/SellerParty/LegalEntity/AddressInSpain/CountryCode` | ISO ülke kodu (`ESP`) |
| `buyer_name` | `Parties/BuyerParty/LegalEntity/CorporateName` | Alıcı şirket adı |
| `buyer_id` | `Parties/BuyerParty/TaxIdentification/TaxIdentificationNumber` | Alıcı NIF/CIF |
| `buyer_address` | `Parties/BuyerParty/LegalEntity/AddressInSpain/Address` | Alıcı adresi |
| `buyer_city` | `Parties/BuyerParty/LegalEntity/AddressInSpain/Town` | Alıcı şehri |
| `buyer_postal_code` | `Parties/BuyerParty/LegalEntity/AddressInSpain/PostCode` | Alıcı posta kodu |
| `buyer_country` | `Parties/BuyerParty/LegalEntity/AddressInSpain/CountryCode` | ISO ülke kodu (`ESP`) |
| `iban` | `PaymentDetails/Installment/AccountToBeCredited/IBAN` | Alacaklı IBAN'ı |

### Kalem Tablosu (`INVOICE_TABLE`)

Satır yolu: `Invoices/Invoice/Items/InvoiceLine`

| Sütun | Kaynak XML Elemanı | Notlar |
|---|---|---|
| `POSITION` | `ItemDescription` | Sıra / tanımlayıcı olarak kullanılan açıklama |
| `DESCRIPTION` | `ItemDescription` | Ürün açıklaması |
| `QUANTITY` | `Quantity` | Faturalandırılan miktar |
| `UNIT` | `UnitOfMeasure` | Ölçü birimi (ör. `units`) |
| `UNIT_PRICE` | `UnitPriceWithoutTax` | KDV hariç birim fiyat |
| `VAT_RATE` | `TaxesOutputs/Tax/TaxRate` | KDV oranı % (genellikle %21) |
| `VAT` | `TaxesOutputs/Tax/TaxAmount/TotalAmount` | Satır başına KDV tutarı |
| `NET_AMOUNT` | `TotalCost` | KDV hariç satır toplamı |

## Sınıflandırma Kuralları

DocBits, `<fe:Facturae>` kök elemanındaki `xsi:schemaLocation` özniteliğini eşleştirerek Facturae belgelerini algılar:

| Elektronik Belge Türü | Desen |
|----------------------|-------|
| FACTURAE 3.2 | `xsi:schemaLocation` içerir `Facturaev3_2.xml` (3_2_1 veya 3_2_2 değil) |
| FACTURAE 3.2.1 | `xsi:schemaLocation` içerir `Facturaev3_2_1.xml` |
| FACTURAE 3.2.2 | `xsi:schemaLocation` içerir `Facturaev3_2_2.xml` |

Kök eleman, `http://www.facturae.es/Facturae/2014/v3.2.2/Facturae` ad alanıyla `<fe:Facturae>`'dır (sürüme özgü). Sınıflandırma, daha spesifik desenlerin (3.2.2, 3.2.1) genel 3.2'den önce değerlendirildiği **ilk eşleşme kazanır** ilkesini kullanır.

## İlgili

- [Şu Anda Desteklenen E-Fatura Standartları](../../currently-supported-e-invoice-standards/)
- [Desteklenen Elektronik Belgeler](./)
