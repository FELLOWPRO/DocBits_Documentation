---
description: DocBits'te Finlandiya Finvoice (1.3, 2.0, 2.01, 3.0) elektronik belge desteği
---

# 🇫🇮 Finlandiya Finvoice

| Özellik | Değer |
|----------|-------|
| **Ülke / Bölge** | Finlandiya |
| **Belge Türleri** | Fatura (Lasku), Alacak Notu (Hyvityslasku) |
| **Biçim** | XML |
| **Standart** | Finvoice 1.3 / 2.0 / 2.01 / 3.0 (Finance Finland / Finanssiala) |
| **Yerel Ayar** | `fi_FI` |

Finvoice, Finance Finland (Finanssiala ry) tarafından geliştirilen ve sürdürülen Finlandiya bankacılık sektörünün e-fatura standardıdır. Hem B2B hem de B2G faturalandırma için kullanılır ve Finlandiya bankacılık altyapısı üzerinden iletilir. Kök element, sürümlü bir ad alanı URL'si ile `<Finvoice>`'dır. DocBits sürümü `xmlns` özniteliği aracılığıyla algılar:

| Sürüm | Ad Alanı URL'si |
|---------|--------------|
| Finvoice 1.3 | `http://www.finvoice.fi/schema/finvoice13` |
| Finvoice 2.0 | `http://www.finvoice.fi/schema/finvoice20` |
| Finvoice 2.01 | `http://www.finvoice.fi/schema/finvoice201` |
| Finvoice 3.0 | `http://www.finvoice.fi/schema/finvoice30` |

Fin işletme kimliği (Y-tunnus) biçimi, taraf tanımlayıcı olarak kullanılan `1234567-8` (7 rakam + kontrol rakamı) şeklindedir. KDV numarası `FI` öneki ve ardından 8 rakamdan oluşur (örn. `FI12345678`). Tarihler `CCYYMMDD` biçiminde kodlanır.

## Destek Durumu

| Bileşen | Durum |
|-----------|--------|
| Önizleme | ✅ Destekleniyor |
| Alan Çıkarma | ✅ Destekleniyor |
| Dönüşüm | ✅ Destekleniyor |

## Varsayılan Önizleme

<figure><img src="finland-finvoice-preview.png" alt="DocBits'te Finlandiya Finvoice 3.0 fatura önizlemesi"><figcaption><p>Finlandiya Finvoice 3.0 faturası (Lasku) için DocBits varsayılan önizlemesi</p></figcaption></figure>

## Alan Eşleştirmesi

### Başlık Alanları

| DocBits Alanı | Kaynak XML Öğesi | Notlar |
|---|---|---|
| `invoice_id` | `InvoiceDetails/InvoiceNumber` | Fatura numarası |
| `invoice_date` | `InvoiceDetails/InvoiceDate` | `CCYYMMDD` biçiminde tarih, ISO 8601'e dönüştürülür |
| `due_date` | `InvoiceDetails/PaymentTermsDetails/InvoiceDueDate` | Ödeme vadesi (`CCYYMMDD`) |
| `invoice_type` | `InvoiceDetails/InvoiceTypeCode` | INV01=Fatura, CRE01=Alacak Notu |
| `currency` | `InvoiceDetails/InvoiceTotalVatExcludedAmount/@AmountCurrencyIdentifier` | Para birimi kodu (genellikle `EUR`) |
| `net_amount` | `InvoiceDetails/InvoiceTotalVatExcludedAmount` | KDV hariç net tutar |
| `tax_amount` | `InvoiceDetails/InvoiceTotalVatAmount` | Toplam KDV tutarı |
| `total_amount` | `InvoiceDetails/InvoiceTotalVatIncludedAmount` | KDV dahil toplam tutar |
| `tax_rate` | `InvoiceDetails/VatSpecificationDetails/VatRatePercent` | % cinsinden KDV oranı (standart %25,5) |
| `supplier_name` | `SellerPartyDetails/SellerOrganisationName` | Tedarikçi şirket adı |
| `supplier_id` | `SellerPartyDetails/SellerPartyIdentifier` | Fin işletme kimliği (Y-tunnus, örn. `1234567-8`) |
| `supplier_vat` | `SellerPartyDetails/SellerOrganisationTaxCode` | KDV numarası (örn. `FI12345678`) |
| `supplier_address` | `SellerPartyDetails/SellerPostalAddressDetails/SellerStreetName` | Tedarikçi adresi |
| `supplier_city` | `SellerPartyDetails/SellerPostalAddressDetails/SellerTownName` | Tedarikçi şehri |
| `supplier_postal_code` | `SellerPartyDetails/SellerPostalAddressDetails/SellerPostCodeIdentifier` | Tedarikçi posta kodu |
| `supplier_country` | `SellerPartyDetails/SellerPostalAddressDetails/CountryCode` | ISO ülke kodu (`FI`) |
| `buyer_name` | `BuyerPartyDetails/BuyerOrganisationName` | Alıcı şirket adı |
| `buyer_id` | `BuyerPartyDetails/BuyerPartyIdentifier` | Fin işletme kimliği (Y-tunnus) |
| `buyer_address` | `BuyerPartyDetails/BuyerPostalAddressDetails/BuyerStreetName` | Alıcı adresi |
| `buyer_city` | `BuyerPartyDetails/BuyerPostalAddressDetails/BuyerTownName` | Alıcı şehri |
| `buyer_postal_code` | `BuyerPartyDetails/BuyerPostalAddressDetails/BuyerPostCodeIdentifier` | Alıcı posta kodu |
| `buyer_country` | `BuyerPartyDetails/BuyerPostalAddressDetails/CountryCode` | ISO ülke kodu (`FI`) |
| `iban` | `EpiDetails/EpiBfiPartyDetails/EpiBfiIdentifier` | Alacaklı IBAN (EPI ödeme ayrıntıları) |
| `bic` | `EpiDetails/EpiPaymentInstructionId` | BIC/SWIFT kodu |
| `payment_terms` | `InvoiceDetails/PaymentTermsDetails/PaymentTermsFreeText` | Serbest metin ödeme koşulları |

### Kalem Tablosu (`INVOICE_TABLE`)

Satır yolu: `InvoiceRow`

| Sütun | Kaynak XML Öğesi | Notlar |
|---|---|---|
| `POSITION` | `InvoiceRow/ArticleIdentifier` | Makale / ürün kodu |
| `DESCRIPTION` | `InvoiceRow/ArticleName` | Makale adı / açıklaması |
| `QUANTITY` | `InvoiceRow/DeliveredQuantity` | Teslim edilen miktar |
| `UNIT` | `InvoiceRow/DeliveredQuantity/@QuantityUnitCode` | Birim kodu (örn. `KPL` = adet) |
| `UNIT_PRICE` | `InvoiceRow/UnitPriceAmount` | KDV hariç birim fiyat |
| `VAT_RATE` | `InvoiceRow/RowVatRatePercent` | Satır başına % KDV oranı |
| `VAT` | `InvoiceRow/RowVatAmount` | Satır başına KDV tutarı |
| `NET_AMOUNT` | `InvoiceRow/RowAmount` | KDV hariç satır toplamı |

## Sınıflandırma Kuralları

DocBits, Finvoice belgelerini kök `<Finvoice>` öğesindeki `xmlns` özniteliğiyle eşleştirerek algılar:

| Elektronik Belge Türü | Desen |
|--------------------------|---------|
| FINVOICE 1.3 | `xmlns` içeriği `http://www.finvoice.fi/schema/finvoice13` |
| FINVOICE 2.0 | `xmlns` içeriği `http://www.finvoice.fi/schema/finvoice20` (2.01 değil) |
| FINVOICE 2.01 | `xmlns` içeriği `http://www.finvoice.fi/schema/finvoice201` |
| FINVOICE 3.0 | `xmlns` içeriği `http://www.finvoice.fi/schema/finvoice30` |

Sınıflandırma, daha spesifik desenlerin (2.01) genel 2.0'dan önce değerlendirildiği **ilk eşleşme kazanır** ilkesini kullanır.

## İlgili

- [Şu Anda Desteklenen E-Fatura Standartları](../../currently-supported-e-invoice-standards/)
- [Finlandiya TEAPPSXML](./finland-teappsxml.md)
- [Desteklenen Elektronik Belgeler](./)
