# İsviçre QR Faturası

## Genel Bakış

**İsviçre QR Faturası**, 30 Haziran 2020'den itibaren turuncu ve kırmızı İsviçre ödeme fişlerinin yerini alan ulusal ödeme fişi standardıdır. İsviçre'deki her yerel fatura — kamu hizmetleri, sigorta şirketleri veya iş ortaklarından gelen — bugün bir İsviçre QR Faturası QR kodu taşır. DocBits bu kodları otomatik olarak çözer ve her ödeme alanını API yanıtı üzerinden sunar.

### Özellik Özeti

İsviçre QR Faturaları **ISO 20022** ödeme standardını takip eder ve iki sürümde yayınlanır: **v1.0** (erken yayılma) ve **v2.0** (mevcut). DocBits çıkarıcısı her ikisini de destekler. Tanınan payload'lar tam bir alan kümesine çözülür — alacaklı, borçlu, IBAN / QR-IBAN, tutar, para birimi, referans türü (QRR, SCOR veya NON), yapılandırılmış ve serbest mesajlar ve alternatif ödeme şemaları.

<figure><img src="../../../../../../.gitbook/assets/module_swiss_qr.png" alt=""><figcaption></figcaption></figure>

#### Temel Avantajlar

* **İsviçre faturaları için sıfır manuel giriş**: IBAN, tutar, referans ve alacaklı doğrudan belgeye akar.
* **Her iki sürüm kapsanır**: v1.0 ve v2.0 otomatik olarak algılanır.
* **Referans türleri korunur**: QRR, SCOR ve NON tam olarak basıldığı gibi korunur; bu da downstream mutabakatı çalışır durumda tutar.

***

### Tanıma

- Sihirli önek: `SPC\n0100` (v1.0) veya `SPC\n0200` (v2.0)
- ISO 20022 uyumlu
- Ayrıştırıcı, varsa `alt-schemes`'i de (alternatif ödeme prosedürleri) sunar

### Çıkarılan Alanlar

Tüm alanlar `swissqr_` önekini kullanır:

| Alan | Açıklama |
|------|----------|
| `swissqr_account` | Alacaklının IBAN veya QR-IBAN'ı |
| `swissqr_creditor_name` | Alacaklı adı |
| `swissqr_creditor_street` | Alacaklı adres satırı |
| `swissqr_creditor_city` | Alacaklı şehri |
| `swissqr_creditor_postal_code` | Alacaklı posta kodu |
| `swissqr_creditor_country` | Alacaklı ülkesi (ISO 3166 alpha-2) |
| `swissqr_debtor_name` | Borçlu adı (basılıysa) |
| `swissqr_debtor_street`, `swissqr_debtor_city`, `swissqr_debtor_postal_code`, `swissqr_debtor_country` | Borçlu adresi |
| `swissqr_amount` | Tutar (ondalık) |
| `swissqr_currency` | Para birimi (ISO 4217) — genellikle `CHF` veya `EUR` |
| `swissqr_reference` | Yapılandırılmış referans (QRR veya SCOR) |
| `swissqr_reference_type` | `QRR`, `SCOR` veya `NON` |
| `swissqr_unstructured_message` | Serbest metin mesajı |
| `swissqr_bill_information` | Yapılandırılmış fatura bilgileri (S1 / Swico) |
| `swissqr_alt_schemes` | Alternatif prosedürler (varsa) |

### Örnek API Yanıtı

```json
{
  "swissqr_account": "CH4431999123000889012",
  "swissqr_creditor_name": "Robert Schneider AG",
  "swissqr_creditor_street": "Rue du Lac 1268",
  "swissqr_creditor_city": "Biel",
  "swissqr_creditor_postal_code": "2501",
  "swissqr_creditor_country": "CH",
  "swissqr_amount": 1949.75,
  "swissqr_currency": "CHF",
  "swissqr_reference": "210000000003139471430009017",
  "swissqr_reference_type": "QRR",
  "swissqr_unstructured_message": "Bill No. 3139 for services 2026"
}
```

***

### Özelliği Etkinleştirme

İsviçre QR Faturası ayrıştırması genel **Barkod / QR Kodu Çıkarımı** anahtarı tarafından kapsanır — standarda özel bir yapılandırma gerekmez.

1. **Ayarları Açın**:
   * Panodan **Ayarlar**'a gidin.
   * **Belge İşleme**'yi ve ardından **Modül**'ü seçin.
2. **Özelliği Etkinleştirin**:
   * **Barkod / QR Kodu Çıkarımı** seçeneğine kaydırın.
   * Kaydırıcıyı etkinleştirmek için açın.

Ödeme QR Kodu standartlarının tam listesi için [Genel Bakış](./README.md) sayfasına bakın.
