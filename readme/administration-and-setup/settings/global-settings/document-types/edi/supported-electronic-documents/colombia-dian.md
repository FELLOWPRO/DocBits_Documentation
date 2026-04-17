---
description: DocBits'te Kolombiya DIAN elektronik belge desteği (Factura Electrónica, Documento Soporte)
---

# 🇨🇴 Kolombiya DIAN

| Özellik | Değer |
|----------|-------|
| **Ülke / Bölge** | Colombia |
| **Belge Türleri** | Fatura (Factura Electrónica), Alacak Dekontu (Nota de Crédito), Documento Soporte |
| **Biçim** | XML (UBL 2.1) |
| **Standart** | DIAN 2.1 (Dirección de Impuestos y Aduanas Nacionales) |
| **Yerel Ayar** | `es_CO` |

Kolombiya elektronik faturalama standardı, **DIAN** (Dirección de Impuestos y Aduanas Nacionales) tarafından düzenlenmektedir. DIAN'a özgü uzantılarla (`sts:DianExtensions`) UBL 2.1 tabanlıdır. DocBits, Kolombiya DIAN belgelerini DIAN ad alanı üzerinden tespit eder ve `CustomizationID`'ye göre yönlendirir:

| CustomizationID | Belge Türü |
|-----------------|--------------|
| 10 | Factura Electrónica de Venta (FACTURA ELECTRONICA) |
| 20 | Nota de Crédito (Alacak Dekontu) |
| 91 | Nota de Crédito por devolución |
| 92 | Nota de Débito |
| DS | Documento Soporte (DOCUMENTO SOPORTE) |

DIAN tanımlayıcısı (**NIT** — Número de Identificación Tributaria), UBL `CompanyID` öğesinde `schemeID="31"` kullanır.

## Destek Durumu

| Bileşen | Durum |
|-----------|--------|
| Önizleme | ✅ Destekleniyor |
| Alan Çıkarma | ✅ Destekleniyor |
| Dönüşüm | ✅ Destekleniyor |

## Varsayılan Önizleme

<figure><img src="colombia-dian-preview.png" alt="DocBits'te Kolombiya DIAN Factura Electrónica önizlemesi"><figcaption><p>COLOMBIA FACTURA ELECTRONICA için varsayılan DocBits önizlemesi (CustomizationID 10)</p></figcaption></figure>

## Alan Eşlemesi

### Başlık Alanları

| DocBits Alanı | Kaynak XML Öğesi | Notlar |
|---|---|---|
| `invoice_id` | `cbc:ID` | Önekli fatura numarası (örn. `SETP990000001`) |
| `invoice_date` | `cbc:IssueDate` | Düzenleme tarihi (ISO 8601) |
| `due_date` | `cbc:DueDate` | Ödeme vade tarihi |
| `currency` | `cbc:DocumentCurrencyCode` | Her zaman `COP` (Kolombiya Pesosu) |
| `total_amount` | `cac:LegalMonetaryTotal/cbc:PayableAmount` | KDV dahil toplam ödenecek tutar |
| `net_amount` | `cac:LegalMonetaryTotal/cbc:TaxExclusiveAmount` | KDV hariç net tutar |
| `tax_amount` | `cac:TaxTotal/cbc:TaxAmount` | Toplam KDV tutarı (standart oran %19) |
| `supplier_name` | `cac:AccountingSupplierParty//cbc:RegistrationName` | Tedarikçinin yasal adı |
| `supplier_id` | `cac:AccountingSupplierParty//cbc:CompanyID` | Tedarikçi NIT'i (schemeID=31) |
| `buyer_name` | `cac:AccountingCustomerParty//cbc:RegistrationName` | Alıcının yasal adı |
| `buyer_id` | `cac:AccountingCustomerParty//cbc:CompanyID` | Alıcı NIT'i (schemeID=31) |

### Satır Öğesi Tablosu (`INVOICE_TABLE`)

Satır yolu: `cac:InvoiceLine` (veya `cac:CreditNoteLine`)

| Sütun | Kaynak XML Öğesi | Notlar |
|---|---|---|
| `POSITION` | `cbc:ID` | Satır numarası |
| `DESCRIPTION` | `cac:Item/cbc:Description` | Ürün veya hizmet açıklaması |
| `QUANTITY` | `cbc:InvoicedQuantity` | Birim kodu özniteliğiyle miktar |
| `UNIT_PRICE` | `cac:Price/cbc:PriceAmount` | KDV hariç birim fiyat |
| `NET_AMOUNT` | `cbc:LineExtensionAmount` | KDV hariç satır toplamı |

## Sınıflandırma Kuralları

DocBits, Kolombiya DIAN belgelerini DIAN ad alanı dizesiyle tespit eder:

| Elektronik Belge Türü | Desen |
|--------------------------|---------|
| COLOMBIA FACTURA ELECTRONICA | `http://www.dian.gov.co/contratos/facturaelectronica/v1/Structures` + `DianExtensions` |
| COLOMBIA DOCUMENTO SOPORTE | `http://www.dian.gov.co/contratos/facturaelectronica/v1/Structures` + `CustomizationID=DS` |

Faturalar için kök öğe `<Invoice>` (UBL 2.1), alacak dekontları için `<CreditNote>`'tur. Tüm belgeler, DIAN yetkilendirme verilerini (`InvoiceAuthorization`, `CUFE`/`CUDE` UUID, QR kodu) içeren bir `<sts:DianExtensions>` bloğu barındırır.

## İlgili

- [Şu Anda Desteklenen E-Fatura Standartları](../../currently-supported-e-invoice-standards/)
- [Desteklenen Elektronik Belgeler](./)
