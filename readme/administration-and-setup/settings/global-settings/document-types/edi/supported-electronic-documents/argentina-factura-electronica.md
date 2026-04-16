---
description: DocBits'te ARGENTINA FACTURA ELECTRONICA elektronik belge desteği
---

# 🇦🇷 ARGENTINA FACTURA ELECTRONICA

| Özellik | Değer |
|---------|-------|
| **Ülke / Bölge** | Arjantin |
| **Belge Türleri** | Fatura |
| **Format** | XML |
| **Standart** | Argentina Factura Electrónica (Factura A'nın ötesindeki AFIP comprobante türleri) |
| **Dil** | `es_AR` |

ARGENTINA FACTURA ELECTRONICA, Factura A'nın (tip 001) ötesindeki daha geniş Arjantin AFIP elektronik belgelerini kapsar. Buna Factura B (tip 006), Factura C (tip 011), Nota de Crédito (tip 003) ve diğer varyantlar dahildir.

## Destek Durumu

| Bileşen | Durum |
|---------|-------|
| Önizleme | ✅ Destekleniyor |
| Alan Çıkarımı | ✅ Destekleniyor |
| Dönüşüm | ✅ Destekleniyor |

## Varsayılan Önizleme

<figure><img src="argentina-factura-electronica-preview.png" alt="DocBits'te Argentina Factura Electronica önizlemesi"><figcaption><p>ARGENTINA FACTURA ELECTRONICA belgesi için varsayılan DocBits önizlemesi</p></figcaption></figure>

## Alan Eşleştirme

### Başlık Alanları

| DocBits Alanı | Kaynak XML Öğeleri | Notlar |
|---|---|---|
| `invoice_id` | `//NumeroFactura`, `//cbte_nro`, `//CbteNro`, `//InvoiceNumber` | Birden fazla XPath yedek yolu |
| `invoice_date` | `//FechaEmision`, `//cbte_fch`, `//CbteFch`, `//IssueDate` | |
| `currency` | `//Moneda`, `//mon_id`, `//MonId`, yedek: `ARS` | |
| `total_amount` | `//MontoTotal`, `//imp_total`, `//ImpTotal`, `//TotalAmount` | |
| `net_amount` | `//MontoNeto`, `//imp_neto`, `//ImpNeto`, `//NetAmount` | |
| `tax_amount` | `//MontoIVA`, `//imp_iva`, `//ImpIVA`, `//TaxAmount` | |
| `supplier_name` | `//NombreProveedor`, `//razon_social`, `//RazonSocial`, `//SellerName` | |
| `buyer_name` | `//NombreComprador`, `//nombre_cliente`, `//NombreCliente`, `//BuyerName` | |

### Kalem Tablosu (`INVOICE_TABLE`)

Satır yolu: `<items>/<item>`, `<Items>/<Item>` veya `<Detalle>/<Linea>`

| Sütun | Kaynak | Notlar |
|---|---|---|
| `POSITION` | `@numero`, `<numero>` veya `position()` | |
| `DESCRIPTION` | `<descripcion>`, `<Descripcion>` | |
| `QUANTITY` | `<cantidad>`, `<Cantidad>` | |
| `UNIT_PRICE` | `<precioUnitario>`, `<PrecioUnitario>` | |
| `VAT_RATE` | `<alicuotaIVA>`, `<AlicuotaIVA>` | |
| `NET_AMOUNT` | `<subtotal>`, `<Subtotal>`, `<importe>` | |

## Sınıflandırma Kuralı

`001` dışındaki `<tipoComprobante>` değerlerine sahip belgeler bu standarda yönlendirilir.

## İlgili

- [ARGENTINA AFIP](argentina-afip.md)
- [Desteklenen Elektronik Belgeler](./)
