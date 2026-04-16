---
description: DocBits'te ARGENTINA AFIP elektronik belge desteği
---

# 🇦🇷 ARGENTINA AFIP

| Özellik | Değer |
|---------|-------|
| **Ülke / Bölge** | Arjantin |
| **Belge Türleri** | Fatura |
| **Format** | XML |
| **Standart** | AFIP Comprobante Electrónico (Administración Federal de Ingresos Públicos) |
| **Dil** | `es_AR` |

ARGENTINA AFIP standardı, Arjantin federal vergi otoritesinin (AFIP) elektronik fatura formatıdır. Belgeler `<tipoComprobante>` ile tanımlanır — örneğin tip `001` = Factura A. Her fatura, AFIP doğrulaması için bir CAE numarası (Código de Autorización Electrónica) ve barkod içerir.

## Destek Durumu

| Bileşen | Durum |
|---------|-------|
| Önizleme | ✅ Destekleniyor |
| Alan Çıkarımı | ✅ Destekleniyor |
| Dönüşüm | ✅ Destekleniyor |

## Varsayılan Önizleme

<figure><img src="argentina-afip-preview.png" alt="DocBits'te ARGENTINA AFIP fatura önizlemesi"><figcaption><p>ARGENTINA AFIP Factura A faturası için varsayılan DocBits önizlemesi</p></figcaption></figure>

## Alan Eşleştirme

### Başlık Alanları

| DocBits Alanı | Kaynak XML Öğesi | Notlar |
|---|---|---|
| `invoice_id` | `<puntoVenta>` + `<numeroComprobante>` | Format: `PPPP-NNNNNNNN` |
| `invoice_date` | `<cabecera>/<fechaEmision>` | |
| `due_date` | `<cabecera>/<fechaVencimiento>` | |
| `currency` | Sabit: `ARS` | Her zaman Arjantin Pesosu |
| `total_amount` | `<totales>/<total>` | |
| `net_amount` | `<totales>/<netoGravado>` veya `<subtotal>` | |
| `tax_amount` | `<totales>/<totalIVA>` | |
| `supplier_name` | `<emisor>/<razonSocial>` | |
| `supplier_id` | `<emisor>/<CUIT>` veya `<cabecera>/<CUIT>` | CUIT = Arjantin vergi kimlik numarası |
| `supplier_address` | `<emisor>/<domicilioComercial>/<calle>` + `<numero>` | |
| `supplier_postal_code` | `<emisor>/<domicilioComercial>/<codigoPostal>` | |
| `supplier_city` | `<emisor>/<domicilioComercial>/<localidad>` | |
| `supplier_country` | Sabit: `AR` | |
| `buyer_name` | `<receptor>/<razonSocial>` | |
| `buyer_id` | `<receptor>/<CUIT>` | |
| `buyer_address` | `<receptor>/<domicilio>/<calle>` + `<numero>` | |
| `buyer_postal_code` | `<receptor>/<domicilio>/<codigoPostal>` | |
| `buyer_city` | `<receptor>/<domicilio>/<localidad>` | |
| `buyer_country` | Sabit: `AR` | |
| `iban` | `<PAYMENT/IBAN>` | Genellikle boş |
| `bic` | `<PAYMENT/BIC>` | Genellikle boş |
| `payment_terms` | `<PAYMENT_TERMS>` | Genellikle boş |
| `purchase_order` | `<PURCHASE_ORDER>` | Genellikle boş |

### Kalem Tablosu (`INVOICE_TABLE`)

Satır yolu: `<items>/<item>`

| Sütun | Kaynak Öznitelik / Öğe | Notlar |
|---|---|---|
| `POSITION` | `@numero` özniteliği | Pozisyon numarası |
| `DESCRIPTION` | `<descripcion>` | |
| `QUANTITY` | `<cantidad>` | |
| `UNIT` | `<unidadMedida>` | AFIP birim kodu (örn. `7` = birim) |
| `UNIT_PRICE` | `<precioUnitario>` | |
| `VAT_RATE` | `<alicuotaIVA>` | örn. standart Arjantin KDV için `21.00` |
| `VAT` | `<importeIVA>` | |
| `NET_AMOUNT` | `<subtotal>` | Vergi öncesi satır toplamı |

## Sınıflandırma Kuralı

DocBits, ARGENTINA AFIP belgelerini regex deseniyle tespit eder:

```
<tipoComprobante>001\s*</tipoComprobante>
```

## İlgili

- [ARGENTINA FACTURA ELECTRONICA](argentina-factura-electronica.md)
- [Desteklenen Elektronik Belgeler](./)
