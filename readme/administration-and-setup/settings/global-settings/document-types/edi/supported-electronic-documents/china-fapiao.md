---
description: DocBits'te Çin Fapiao (FAPIAO, E-FAPIAO, Genel KDV Faturası, Özel KDV Faturası) elektronik belge desteği
---

# 🇨🇳 China Fapiao

| Özellik | Değer |
|----------|-------|
| **Ülke / Bölge** | China |
| **Belge Türleri** | Genel KDV Faturası (普通发票), Özel KDV Faturası (专用发票), E-Fapiao |
| **Format** | XML |
| **Standart** | Fapiao (发票), State Taxation Administration |
| **Yerel Ayar** | `zh_CN` |

Fapiao (发票), Devlet Vergi İdaresi'nin (STA / 国家税务总局) yetkisi altında düzenlenen Çin vergi faturası standardıdır. Tüm Fapiao belgeleri `urn:china:tax:fapiao:1.0` ad alanını paylaşır. DocBits, `fapiao_type` öğesi aracılığıyla Fapiao türünü otomatik olarak algılar ve uygun çıkarma kurallarına yönlendirir:

| fapiao_type değeri | Belge Türü |
|-------------------|--------------|
| 普通发票 | Genel KDV Faturası (FAPIAO / GENERAL VAT INVOICE) |
| 专用发票 | Özel KDV Faturası (SPECIAL VAT INVOICE) |
| 电子发票 | E-Fapiao (E-FAPIAO) |

## Destek Durumu

| Bileşen | Durum |
|-----------|--------|
| Önizleme | ✅ Supported |
| Alan Çıkarma | ✅ Supported |
| Dönüşüm | ✅ Supported |

## Varsayılan Önizleme

<figure><img src="china-fapiao-preview.png" alt="DocBits'te Çin Fapiao Genel KDV Faturası önizlemesi"><figcaption><p>Çin Fapiao Genel KDV Faturası için DocBits varsayılan önizlemesi (普通发票)</p></figcaption></figure>

## Alan Eşleme

### Başlık Alanları

| DocBits Alanı | Kaynak XML Öğesi | Notlar |
|---|---|---|
| `invoice_id` | `fapiao_head/fapiao_number` | Fapiao numarası — 8 basamak (发票号码) |
| `invoice_date` | `fapiao_head/issue_date` | Düzenleme tarihi (ISO 8601) |
| `currency` | Sabit: `CNY` | Her zaman Çin Yuanı Renminbi |
| `total_amount` | `total/total_with_tax` | KDV dahil toplam tutar (价税合计) |
| `net_amount` | `total/total_amount` | KDV hariç net vergilendirilebilir tutar (金额) |
| `tax_amount` | `total/total_tax` | Toplam KDV tutarı (税额) |
| `supplier_name` | `seller/name` | Satıcı şirket adı (销售方名称) |
| `supplier_id` | `seller/taxpayer_id` | Satıcı vergi kimlik numarası — 18 karakter (纳税人识别号) |
| `supplier_address` | `seller/address` | Satıcı adresi |
| `supplier_country` | Sabit: `CN` | Her zaman Çin |
| `iban` | `seller/bank_account` | Satıcı banka hesap numarası |
| `buyer_name` | `buyer/name` | Alıcı şirket adı (购买方名称) |
| `buyer_id` | `buyer/taxpayer_id` | Alıcı vergi kimlik numarası (纳税人识别号) |
| `buyer_address` | `buyer/address` | Alıcı adresi |
| `buyer_country` | Sabit: `CN` | Her zaman Çin |

### Satır Kalemi Tablosu (`INVOICE_TABLE`)

Satır yolu: `items/item`

| Sütun | Kaynak XML Öğesi | Notlar |
|---|---|---|
| `POSITION` | `seq` | Satır sıra numarası |
| `DESCRIPTION` | `name` + `spec` | Ürün adı ve özelliği (birleştirilmiş) |
| `QUANTITY` | `quantity` | Miktar |
| `UNIT` | `unit` | Ölçü birimi (örn. 箱, 台, 项) |
| `UNIT_PRICE` | `unit_price` | KDV hariç birim fiyat |
| `VAT_RATE` | `tax_rate` | KDV oranı % cinsinden (genellikle %6, %9 veya %13) |
| `VAT` | `tax_amount` | Satır başına KDV tutarı |
| `NET_AMOUNT` | `amount` | KDV hariç satır toplamı |

## Sınıflandırma Kuralları

DocBits, XML ad alanını ve `fapiao_type` değerini eşleştirerek China Fapiao belgelerini algılar:

| Elektronik Belge Türü | Desen |
|--------------------------|---------|
| CHINA GENERAL VAT INVOICE | `urn:china:tax:fapiao:1.0` + `<fapiao_type>普通发票</fapiao_type>` |
| CHINA SPECIAL VAT INVOICE | `urn:china:tax:fapiao:1.0` + `<fapiao_type>专用发票</fapiao_type>` |
| CHINA E-FAPIAO | `urn:china:tax:fapiao:1.0` + `<fapiao_type>电子发票</fapiao_type>` |

Kök öğe, `urn:china:tax:fapiao:1.0` ad alanıyla `<fapiao>`'dur. Sınıflandırma, **first-match-wins** ilkesini kullanır ve desen uzunluğuna göre sıralanır (en uzun önce).

## İlgili

- [Şu Anda Desteklenen E-Fatura Standartları](../../currently-supported-e-invoice-standards/)
- [Desteklenen Elektronik Belgeler](./)
