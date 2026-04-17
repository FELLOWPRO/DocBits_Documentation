---
description: DocBits'te Finlandiya TEAPPSXML elektronik belge desteği
---

# 🇫🇮 Finlandiya TEAPPSXML

| Özellik | Değer |
|----------|-------|
| **Ülke / Bölge** | Finlandiya |
| **Belge Türleri** | Fatura, Alacak Notu |
| **Biçim** | XML |
| **Standart** | TEAPPSXML 3.0 (Tieto / Fin Bankacılık Sektörü) |
| **Yerel Ayar** | `fi_FI` |

TEAPPSXML (Tietotekniikan ja viestinnän toimiala), ağırlıklı olarak bankacılık ve finans sektöründe kullanılan bir Fin elektronik fatura standardıdır. Kök element, `urn:TEAPPSXML:3.0` ad alanıyla `<TEAPPSXML>`'dir. DocBits, kök öğede `xmlns="urn:TEAPPSXML:"` varlığıyla TEAPPSXML belgelerini algılar.

TEAPPSXML biçimi, büyük harfli öğe adları ve ayrı `<SENDER>`, `<RECEIVER>`, `<INVOICE>` ve `<PAYMENTINFO>` bölümleriyle düz bir yapı kullanır. Fin işletme kimliği (Y-tunnus) biçimi `1234567-8`'dir ve KDV numaraları `FI` önekini kullanır (örn. `FI12345678`).

## Destek Durumu

| Bileşen | Durum |
|-----------|--------|
| Önizleme | ✅ Destekleniyor |
| Alan Çıkarma | ✅ Destekleniyor |
| Dönüşüm | ✅ Destekleniyor |

## Varsayılan Önizleme

<figure><img src="finland-teappsxml-preview.png" alt="DocBits'te Finlandiya TEAPPSXML fatura önizlemesi"><figcaption><p>Finlandiya TEAPPSXML faturası için DocBits varsayılan önizlemesi</p></figcaption></figure>

## Alan Eşleştirmesi

### Başlık Alanları

| DocBits Alanı | Kaynak XML Öğesi | Notlar |
|---|---|---|
| `invoice_id` | `INVOICE/INVOICENUMBER` | Fatura numarası |
| `invoice_date` | `INVOICE/INVOICEDATE` | Düzenleme tarihi (YYYY-AA-GG) |
| `due_date` | `INVOICE/DUEDATE` | Ödeme vadesi (YYYY-AA-GG) |
| `invoice_type` | `INVOICE/INVOICE_TYPE` | İleti türü (INVOICE) |
| `currency` | `INVOICE/CURRENCY` | Para birimi kodu (genellikle `EUR`) |
| `purchase_order` | `INVOICE/REFERENCENUMBER` | Ödeme referans numarası |
| `payment_reference` | `INVOICE/REFERENCENUMBER` | Fin ödeme referansı (viitenumero) |
| `net_amount` | `INVOICE/TOTALVATEXCLUDED` | KDV hariç net tutar |
| `tax_amount` | `INVOICE/TOTALVAT` | Toplam KDV tutarı |
| `total_amount` | `INVOICE/TOTALAMOUNT` | KDV dahil toplam tutar |
| `payment_terms` | `INVOICE/PAYMENT_TERMS` | Ödeme yöntemi (örn. `BANKTRANSFER`) |
| `supplier_name` | `SENDER/NAME` | Gönderen şirket adı |
| `supplier_id` | `SENDER/ID` | Fin işletme kimliği (Y-tunnus, örn. `1234567-8`) |
| `supplier_tax_id` | `SENDER/VATNUMBER` | KDV numarası (örn. `FI12345678`) |
| `supplier_address` | `SENDER/ADDRESS/STREET` | Gönderen adresi |
| `supplier_city` | `SENDER/ADDRESS/CITY` | Gönderen şehri |
| `supplier_postal_code` | `SENDER/ADDRESS/POSTCODE` | Gönderen posta kodu |
| `supplier_country` | `SENDER/ADDRESS/COUNTRY` | ISO ülke kodu (`FI`) |
| `supplier_bic` | `SENDER/BANK/BIC` | Gönderen bankası BIC kodu |
| `buyer_name` | `INVOICE/BUYER/NAME` | Alıcı şirket adı |
| `buyer_id` | `INVOICE/BUYER/ID` | Alıcının Fin işletme kimliği |
| `buyer_address` | `INVOICE/BUYER/ADDRESS_LINE_1` | Alıcı adresi |
| `buyer_city` | `INVOICE/BUYER/CITY` | Alıcı şehri |
| `buyer_postal_code` | `INVOICE/BUYER/POSTAL_CODE` | Alıcı posta kodu |
| `buyer_country` | `INVOICE/BUYER/COUNTRY` | ISO ülke kodu (`FI`) |
| `iban` | `PAYMENTINFO/BENEFICIARYACCOUNT/IBAN` | Alacaklı IBAN |
| `bic` | `PAYMENTINFO/BENEFICIARYACCOUNT/BIC` | Alacaklı BIC kodu |

### Kalem Tablosu (`INVOICE_TABLE`)

Satır yolu: `INVOICE/LINES/LINE`

| Sütun | Kaynak XML Öğesi | Notlar |
|---|---|---|
| `POSITION` | `LINENUMBER` | Satır sıra numarası |
| `DESCRIPTION` | `ARTICLENAME` | Makale adı / açıklaması |
| `QUANTITY` | `QUANTITY` | Faturalandırılan miktar |
| `UNIT` | `UNIT` | Ölçü birimi (örn. `KPL` = adet) |
| `UNIT_PRICE` | `UNITPRICE` | KDV hariç birim fiyat |
| `VAT_RATE` | `VATRATE` | % cinsinden KDV oranı (standart %25,5) |
| `VAT` | Hesaplanmış | Satır başına KDV tutarı |
| `NET_AMOUNT` | `LINEAMOUNT` | KDV hariç satır toplamı |

## Sınıflandırma Kuralı

DocBits, TEAPPSXML belgelerini kök `<TEAPPSXML>` öğesindeki `xmlns` özniteliğiyle eşleştirerek algılar:

| Elektronik Belge Türü | Desen |
|--------------------------|---------|
| TEAPPSXML | `xmlns` içeriği `urn:TEAPPSXML:` |

## İlgili

- [Şu Anda Desteklenen E-Fatura Standartları](../../currently-supported-e-invoice-standards/)
- [Finlandiya Finvoice](./finland-finvoice.md)
- [Desteklenen Elektronik Belgeler](./)
