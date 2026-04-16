---
description: DocBits'te CHILE DTE elektronik belge desteği
---

# 🇨🇱 CHILE DTE

| Özellik | Değer |
|----------|-------|
| **Ülke / Bölge** | Şili |
| **Belge Türleri** | Fatura (Factura), Kredi Notu, Borç Notu, Sevk İrsaliyesi |
| **Biçim** | XML |
| **Standart** | DTE (Documento Tributario Electrónico), SII |
| **Yerel Ayar** | `es_CL` |

DTE (Documento Tributario Electrónico), Servicio de Impuestos Internos (SII) tarafından düzenlenen Şili elektronik vergi belgesi standardıdır. Tüm DTE belgeleri `http://www.sii.cl/SiiDte` ad alanını paylaşır. DocBits, DTE tür kodunu (`TipoDTE`) otomatik olarak algılar ve uygun çıkarma kurallarına yönlendirir:

| Tür Kodu | Belge Türü |
|-----------|--------------|
| 33 | Factura Electrónica (Invoice) |
| 34 | Factura No Afecta o Exenta (Tax-exempt invoice) |
| 52 | Guía de Despacho (Dispatch Guide) |
| 56 | Nota de Débito (Debit Note) |
| 61 | Nota de Crédito (Credit Note) |

## Destek Durumu

| Bileşen | Durum |
|-----------|--------|
| Önizleme | ✅ Destekleniyor |
| Alan Çıkarma | ✅ Destekleniyor |
| Dönüşüm | ✅ Destekleniyor |

## Varsayılan Önizleme

<figure><img src="chile-dte-preview.png" alt="DocBits'te Chile DTE Factura önizlemesi"><figcaption><p>CHILE DTE FACTURA (tür 33) için varsayılan DocBits önizlemesi</p></figcaption></figure>

## Alan Eşlemesi

### Başlık Alanları

| DocBits Alanı | Kaynak XML Öğesi | Notlar |
|---|---|---|
| `invoice_id` | `Folio` | Belge folio numarası |
| `invoice_date` | `FchEmis` | ISO 8601 düzenleme tarihi |
| `due_date` | `FchVenc` | Ödeme son tarihi |
| `currency` | Sabit: `CLP` | Her zaman Şili Pesosu |
| `total_amount` | `MntTotal` | KDV dahil toplam tutar |
| `net_amount` | `MntNeto` | Net vergiye tabi tutar |
| `tax_amount` | `IVA` | KDV tutarı (standart oran %19) |
| `supplier_name` | `RznSoc` (Emisor) | Düzenleyici firma adı |
| `supplier_id` | `RUTEmisor` | Düzenleyici RUT (örn. `76123456-7`) |
| `supplier_address` | `DirOrigen` | Düzenleyici sokak adresi |
| `supplier_city` | `CiudadOrigen` | Düzenleyici şehri |
| `supplier_country` | Sabit: `CL` | Her zaman Şili |
| `buyer_name` | `RznSocRecep` | Alıcı firma adı |
| `buyer_id` | `RUTRecep` | Alıcı RUT |
| `buyer_address` | `DirRecep` | Alıcı sokak adresi |
| `buyer_city` | `CiudadRecep` | Alıcı şehri |
| `buyer_country` | Sabit: `CL` | Her zaman Şili |

### Satır Kalemi Tablosu (`INVOICE_TABLE`)

Satır yolu: `Detalle`

| Sütun | Kaynak XML Öğesi | Notlar |
|---|---|---|
| `POSITION` | `NroLinDet` | Satır sıra numarası |
| `DESCRIPTION` | `NmbItem` | Kalem adı |
| `QUANTITY` | `QtyItem` | Miktar |
| `UNIT` | `UnmdItem` | Ölçü birimi |
| `UNIT_PRICE` | `PrcItem` | KDV hariç birim fiyat |
| `VAT_RATE` | `TasaIVA` (başlıktan) | % olarak KDV oranı (genellikle %19) |
| `VAT` | Hesaplanmış | Satır başına KDV |
| `NET_AMOUNT` | `MontoItem` | Satır toplamı |

## Sınıflandırma Kuralları

DocBits, XML ad alanını ve `TipoDTE`'yi eşleştirerek Chile DTE belgelerini algılar:

| Elektronik Belge Türü | Desen |
|--------------------------|---------|
| CHILE DTE FACTURA | `http://www.sii.cl/SiiDte` + `<TipoDTE>33</TipoDTE>` |
| CHILE DTE FACTURA ELECTRONICA | `http://www.sii.cl/SiiDte` + `<TipoDTE>34</TipoDTE>` |
| CHILE DTE GUIA DESPACHO | `http://www.sii.cl/SiiDte` + `<TipoDTE>52</TipoDTE>` |
| CHILE DTE NOTA CREDITO | `http://www.sii.cl/SiiDte` + `<TipoDTE>61</TipoDTE>` |

Zarf öğesi `<EnvioDTE>`'dir ve her DTE `<DTE><Documento>` içinde sarmalanmıştır.

## İlgili

- [Şu Anda Desteklenen E-Fatura Standartları](../../currently-supported-e-invoice-standards/)
- [Desteklenen Elektronik Belgeler](./)
