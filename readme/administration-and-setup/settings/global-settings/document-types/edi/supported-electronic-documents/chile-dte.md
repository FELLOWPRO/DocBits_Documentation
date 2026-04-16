---
description: DocBits'te CHILE DTE elektronik belge desteği
---

# 🇨🇱 CHILE DTE

| Özellik | Değer |
|----------|-------|
| **Ülke / Bölge** | Şili |
| **Belge türleri** | Fatura, Alacak dekontu, Borç dekontu, İrsaliye |
| **Format** | XML |
| **Standart** | DTE (Documento Tributario Electrónico), SII |
| **Locale** | `es_CL` |

DTE (Documento Tributario Electrónico), Servicio de Impuestos Internos (SII) tarafından düzenlenen Şili elektronik mali belge standardıdır. Tüm DTE belgeleri `http://www.sii.cl/SiiDte` ad alanını paylaşır. DocBits, DTE tür kodunu (`TipoDTE`) otomatik olarak algılar ve uygun çıkarma kurallarına yönlendirir:

| Tür kodu | Belge türü |
|-----------|--------------|
| 33 | Factura Electrónica (Fatura) |
| 34 | Factura No Afecta o Exenta (Muaf fatura) |
| 52 | Guía de Despacho (İrsaliye) |
| 56 | Nota de Débito (Borç dekontu) |
| 61 | Nota de Crédito (Alacak dekontu) |

## Destek durumu

| Bileşen | Durum |
|-----------|--------|
| Önizleme | ✅ Destekleniyor |
| Alan çıkarımı | ✅ Destekleniyor |
| Dönüştürme | ✅ Destekleniyor |

## Varsayılan önizleme

<figure><img src="chile-dte-preview.png" alt="DocBits'te Chile DTE fatura önizlemesi"><figcaption><p>CHILE DTE FACTURA (tür 33) için varsayılan DocBits önizlemesi</p></figcaption></figure>

## Alan eşleştirmesi

### Başlık alanları

| DocBits alanı | Kaynak XML öğesi | Notlar |
|---|---|---|
| `invoice_id` | `Folio` | Belge folio numarası |
| `invoice_date` | `FchEmis` | ISO 8601 düzenleme tarihi |
| `due_date` | `FchVenc` | Vade tarihi |
| `currency` | Sabit: `CLP` | Her zaman Şili pesosu |
| `total_amount` | `MntTotal` | KDV dahil toplam tutar |
| `net_amount` | `MntNeto` | Vergiye tabi net tutar |
| `tax_amount` | `IVA` | KDV tutarı (standart oran %19) |
| `supplier_name` | `RznSoc` (Emisor) | Düzenleyen şirket adı |
| `supplier_id` | `RUTEmisor` | Düzenleyen RUT (ör. `76123456-7`) |
| `supplier_address` | `DirOrigen` | Düzenleyen adresi |
| `supplier_city` | `CiudadOrigen` | Düzenleyen şehri |
| `supplier_country` | Sabit: `CL` | Her zaman Şili |
| `buyer_name` | `RznSocRecep` | Alıcı şirket adı |
| `buyer_id` | `RUTRecep` | Alıcı RUT |
| `buyer_address` | `DirRecep` | Alıcı adresi |
| `buyer_city` | `CiudadRecep` | Alıcı şehri |
| `buyer_country` | Sabit: `CL` | Her zaman Şili |

### Satır tablosu (`INVOICE_TABLE`)

Satır yolu: `Detalle`

| Sütun | Kaynak XML öğesi | Notlar |
|---|---|---|
| `POSITION` | `NroLinDet` | Satır numarası |
| `DESCRIPTION` | `NmbItem` | Kalemin açıklaması |
| `QUANTITY` | `QtyItem` | Miktar |
| `UNIT` | `UnmdItem` | Ölçü birimi |
| `UNIT_PRICE` | `PrcItem` | KDV hariç birim fiyat |
| `VAT_RATE` | `TasaIVA` (başlıktan) | KDV oranı % (tipik %19) |
| `VAT` | Hesaplanan | Satır başına KDV |
| `NET_AMOUNT` | `MontoItem` | Satır toplamı |

## Sınıflandırma kuralları

DocBits, XML ad alanını ve `TipoDTE` öğesini eşleştirerek Chile DTE belgelerini algılar:

| Elektronik belge türü | Örüntü |
|--------------------------|---------|
| CHILE DTE FACTURA | `http://www.sii.cl/SiiDte` + `<TipoDTE>33</TipoDTE>` |
| CHILE DTE FACTURA ELECTRONICA | `http://www.sii.cl/SiiDte` + `<TipoDTE>34</TipoDTE>` |
| CHILE DTE GUIA DESPACHO | `http://www.sii.cl/SiiDte` + `<TipoDTE>52</TipoDTE>` |
| CHILE DTE NOTA CREDITO | `http://www.sii.cl/SiiDte` + `<TipoDTE>61</TipoDTE>` |

Zarf öğesi `<EnvioDTE>` ve her DTE `<DTE><Documento>` içine sarılır.

## Ayrıca bakınız

- [Şu anda desteklenen e-fatura standartları](../../currently-supported-e-invoice-standards/)
- [Desteklenen elektronik belgeler](./)
