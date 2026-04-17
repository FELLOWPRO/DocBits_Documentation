---
description: Hindistan GST E-Fatura elektronik belge desteği DocBits'te
---

# 🇮🇳 India GST E-Invoice

| Özellik | Değer |
|----------|-------|
| **Ülke / Bölge** | Hindistan |
| **Belge Türleri** | Fatura (INV), Alacak Notu (CRN), Borç Notu (DBN) |
| **Biçim** | XML (`<SignedInvoice>`) |
| **Standart** | GST E-Invoice (GSTN Invoice Registration Portal) |
| **Locale** | `en_IN` |

Hindistan GST E-Faturası, GSTN (GST Network) tarafından işletilen Hindistan'ın Mal ve Hizmet Vergisi (GST) rejimi kapsamındaki zorunlu elektronik faturalama standardıdır. Belirlenen ciro eşiğini aşan işletmeler, faturayı imzalayıp **IRN** (Invoice Reference Number — 64 karakterli SHA-256 hash) ve QR kodu döndüren IRP (Invoice Registration Portal) üzerinden e-fatura oluşturmak zorundadır.

DocBits, GST E-Invoice belgelerini kök eleman olarak `<SignedInvoice>` varlığıyla tespit eder. Biçim üç GST vergi bileşeni içerir:

| Vergi Bileşeni | Açıklama |
|--------------|-------------|
| IGST | Entegre GST — eyaletler arası işlemlere uygulanır |
| CGST | Merkezi GST — eyalet içi işlemlere uygulanır (merkezi bileşen) |
| SGST | Eyalet GST — eyalet içi işlemlere uygulanır (eyalet bileşeni) |

Mükellef tanımlayıcısı, `29AABCU9603R1ZM` formatında (2 haneli eyalet kodu + 10 haneli PAN + kuruluş numarası + kontrol hanesi) 15 karakterli alfasayısal bir kod olan **GSTIN** (Goods and Services Tax Identification Number)'dir. Tarihler `GG/AA/YYYY` formatını kullanır.

## Destek Durumu

| Bileşen | Durum |
|-----------|--------|
| Önizleme | ✅ Destekleniyor |
| Alan Çıkarımı | ✅ Destekleniyor |
| Dönüşüm | ✅ Destekleniyor |

## Varsayılan Önizleme

<figure><img src="india-gst-e-invoice-preview.png" alt="India GST E-Invoice preview in DocBits"><figcaption><p>Hindistan GST E-Faturası için DocBits varsayılan önizlemesi</p></figcaption></figure>

## Alan Eşleştirmesi

### Başlık Alanları

| DocBits Alanı | Kaynak XML Elemanı | Notlar |
|---|---|---|
| `invoice_id` | `Invoice/DocDtls/No` | Fatura numarası |
| `invoice_date` | `Invoice/DocDtls/Dt` | Düzenleme tarihi (`GG/AA/YYYY`) |
| `invoice_type` | `Invoice/DocDtls/Typ` | INV=Fatura, CRN=Alacak Notu, DBN=Borç Notu |
| `currency` | Sabit: `INR` | Her zaman Hindistan Rupisi |
| `net_amount` | `Invoice/ValDtls/AssVal` | Vergiye tabi / değerlendirilebilir değer |
| `tax_amount` | `Invoice/ValDtls/IgstVal` + `CgstVal` + `SgstVal` | Toplam GST tutarı |
| `total_amount` | `Invoice/ValDtls/TotInvVal` | GST dahil toplam fatura değeri |
| `igst_amount` | `Invoice/ValDtls/IgstVal` | Entegre GST tutarı |
| `cgst_amount` | `Invoice/ValDtls/CgstVal` | Merkezi GST tutarı |
| `sgst_amount` | `Invoice/ValDtls/SgstVal` | Eyalet GST tutarı |
| `cess_amount` | `Invoice/ValDtls/CesVal` | Cess tutarı (varsa) |
| `supplier_name` | `Invoice/SellerDtls/LglNm` | Satıcının yasal adı |
| `supplier_id` | `Invoice/SellerDtls/Gstin` | Satıcı GSTIN (15 karakter, örn. `29AABCU9603R1ZM`) |
| `supplier_trade_name` | `Invoice/SellerDtls/TrdNm` | Satıcının ticari adı |
| `supplier_address` | `Invoice/SellerDtls/Addr1` | Satıcı adresi satır 1 |
| `supplier_city` | `Invoice/SellerDtls/Loc` | Satıcı şehri / konumu |
| `supplier_postal_code` | `Invoice/SellerDtls/Pin` | Satıcı PIN kodu |
| `supplier_state_code` | `Invoice/SellerDtls/Stcd` | Satıcı eyalet kodu (2 hane) |
| `buyer_name` | `Invoice/BuyerDtls/LglNm` | Alıcının yasal adı |
| `buyer_id` | `Invoice/BuyerDtls/Gstin` | Alıcı GSTIN |
| `buyer_trade_name` | `Invoice/BuyerDtls/TrdNm` | Alıcının ticari adı |
| `buyer_address` | `Invoice/BuyerDtls/Addr1` | Alıcı adresi satır 1 |
| `buyer_city` | `Invoice/BuyerDtls/Loc` | Alıcı şehri / konumu |
| `buyer_postal_code` | `Invoice/BuyerDtls/Pin` | Alıcı PIN kodu |
| `buyer_state_code` | `Invoice/BuyerDtls/Stcd` | Alıcı eyalet kodu |
| `irn` | `Irn` | Fatura Referans Numarası (64 karakterli SHA-256 hash) |
| `ack_number` | `AckNo` | IRP onay numarası |
| `ack_date` | `AckDt` | IRP onay tarihi |

### Kalem Tablosu (`INVOICE_TABLE`)

Satır yolu: `Invoice/ItemList/Item`

| Sütun | Kaynak XML Elemanı | Notlar |
|---|---|---|
| `POSITION` | `SlNo` | Satır sıra numarası |
| `DESCRIPTION` | `PrdDesc` | Ürün / hizmet açıklaması |
| `QUANTITY` | `Qty` | Faturalanan miktar |
| `UNIT` | `Unit` | Ölçü birimi (örn. `OTH`, `NOS`, `KGS`) |
| `UNIT_PRICE` | `UnitPrice` | Birim fiyat |
| `VAT_RATE` | `GstRt` | GST oranı % (örn. %18) |
| `VAT` | `IgstAmt` (veya `CgstAmt` + `SgstAmt`) | Satır başına GST tutarı |
| `NET_AMOUNT` | `AssAmt` | Satır başına vergiye tabi tutar |

## Sınıflandırma Kuralı

DocBits, India GST E-Invoice belgelerini kök elemanı eşleştirerek tespit eder:

| Elektronik Belge Türü | Desen |
|--------------------------|---------|
| INDIA GST E-INVOICE | Kök eleman `<SignedInvoice` içerir |

## İlgili

- [Şu Anda Desteklenen E-Fatura Standartları](../../currently-supported-e-invoice-standards/)
- [Desteklenen Elektronik Belgeler](./)
