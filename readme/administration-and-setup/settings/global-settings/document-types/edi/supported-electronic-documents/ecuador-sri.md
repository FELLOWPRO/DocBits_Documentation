---
description: DocBits'te Ecuador SRI (Factura Electrónica, SRI 1.0.0 – 2.1.0) elektronik belge desteği
---

# 🇪🇨 Ecuador SRI

| Özellik | Değer |
|---------|-------|
| **Ülke / Bölge** | Ekvador |
| **Belge Türleri** | Factura (Fatura), Nota de Crédito, Nota de Débito, Guía de Remisión, Comprobante de Retención |
| **Format** | XML |
| **Standart** | SRI (Servicio de Rentas Internas) |
| **Yerel Ayar** | `es_EC` |

Ecuador SRI elektronik fatura standardı, Ekvador'un vergi otoritesi olan Servicio de Rentas Internas (SRI) yetkisi altında yayımlanmaktadır. Belgeler, `<factura id="comprobante" version="X.X.X">` kök öğesiyle özel bir XML formatı kullanır. DocBits, sürümü `version` özniteliğinden ve belge türünü `codDoc` alanından otomatik olarak algılar:

| version özniteliği | Belge Türü |
|-------------------|-----------|
| `1.0.0` | SRI 1.0.0 |
| `1.1.0` | SRI 1.1.0 |
| `2.0.0` | SRI 2.0.0 |
| `2.1.0` | SRI 2.1.0 / FACTURA ELECTRONICA |

Fatura numarası üç alanın birleşiminden oluşur: `estab-ptoEmi-secuencial` (örn. `001-001-000000001`). `claveAcceso`, SRI tarafından belge doğrulaması için verilen 49 haneli bir erişim anahtarıdır. Ekvador, resmi para birimi olarak **ABD Doları (USD)** kullanmaktadır.

## Destek Durumu

| Bileşen | Durum |
|---------|-------|
| Önizleme | ✅ Destekleniyor |
| Alan Çıkarma | ✅ Destekleniyor |
| Dönüştürme | ✅ Destekleniyor |

## Varsayılan Önizleme

<figure><img src="ecuador-sri-preview.png" alt="DocBits'te Ecuador SRI Factura önizlemesi"><figcaption><p>Bir Ecuador SRI Factura Electrónica (sürüm 2.1.0) için DocBits varsayılan önizlemesi</p></figcaption></figure>

## Alan Eşleştirmesi

### Başlık Alanları

| DocBits Alanı | Kaynak XML Öğesi | Notlar |
|---|---|---|
| `invoice_id` | `estab` + `ptoEmi` + `secuencial` | Birleşik: `001-001-000000001` |
| `invoice_date` | `infoFactura/fechaEmision` | Tarih formatı `DD/MM/YYYY` |
| `due_date` | `infoFactura/pagos/pago/plazo` + `unidadTiempo` | Ödeme vadesi (örn. `30 dias`) |
| `currency` | Sabit: `USD` | Her zaman ABD Doları (Ekvador'un resmi para birimi) |
| `invoice_type` | Sabit: `Factura` | Belge türü etiketi |
| `net_amount` | `infoFactura/totalSinImpuestos` | KDV hariç net toplam |
| `tax_amount` | `infoFactura/totalConImpuestos/totalImpuesto/valor` | KDV tutarı (IVA) |
| `total_amount` | `infoFactura/importeTotal` | KDV dahil toplam tutar |
| `supplier_name` | `infoTributaria/razonSocial` | Düzenleyici şirket adı |
| `supplier_id` | `infoTributaria/ruc` | RUC — 13 haneli vergi kimlik numarası |
| `supplier_tax_id` | `infoTributaria/ruc` | RUC (supplier_id ile aynı) |
| `supplier_address` | `infoTributaria/dirMatriz` | Düzenleyicinin genel merkez adresi |
| `payment_terms` | `infoFactura/pagos/pago/formaPago` | SRI ödeme yöntemi kodu |
| `buyer_name` | `infoFactura/razonSocialComprador` | Alıcı şirket adı |
| `buyer_id` | `infoFactura/identificacionComprador` | Alıcının RUC veya CI'si |

### Satır Öğesi Tablosu (`INVOICE_TABLE`)

Satır yolu: `detalles/detalle`

| Sütun | Kaynak XML Öğesi | Notlar |
|---|---|---|
| `POSITION` | Sıralı indeks | 1 tabanlı satır numarası |
| `DESCRIPTION` | `descripcion` | Ürün açıklaması |
| `QUANTITY` | `cantidad` | Miktar |
| `UNIT_PRICE` | `precioUnitario` | KDV hariç birim fiyat |
| `VAT_RATE` | `impuestos/impuesto/tarifa` | % cinsinden KDV oranı (örn. %15) |
| `VAT` | `impuestos/impuesto/valor` | Satır başına KDV tutarı |
| `NET_AMOUNT` | `precioTotalSinImpuesto` | KDV hariç satır toplamı |

## Sınıflandırma Kuralları

DocBits, kök öğeyi ve version özniteliğini eşleştirerek Ecuador SRI belgelerini tespit eder:

| Elektronik Belge Türü | Desen |
|----------------------|-------|
| ECUADOR SRI / FACTURA ELECTRONICA | `<factura id="comprobante"` (herhangi bir sürüm) |
| ECUADOR SRI 1.0.0 | `<factura id="comprobante" version="1.0.0">` |
| ECUADOR SRI 1.1.0 | `<factura id="comprobante" version="1.1.0">` |
| ECUADOR SRI 2.0.0 | `<factura id="comprobante" version="2.0.0">` |
| ECUADOR SRI 2.1.0 | `<factura id="comprobante" version="2.1.0">` |

Kök öğe `id="comprobante"` ile `<factura>`'dır. `version` özniteliği belirli SRI sürümünü belirler. Sınıflandırma, desen uzunluğuna göre sıralanmış (en uzun/en özel önce) **ilk eşleşme kazanır** ilkesini kullanır.

## İlgili

- [Şu Anda Desteklenen E-Fatura Standartları](../../currently-supported-e-invoice-standards/)
- [Desteklenen Elektronik Belgeler](./)
