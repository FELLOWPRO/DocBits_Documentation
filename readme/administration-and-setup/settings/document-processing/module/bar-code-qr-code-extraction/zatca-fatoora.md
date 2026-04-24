# ZATCA Fatoora (Suudi Arabistan)

## Genel Bakış

**ZATCA Fatoora**, Suudi Arabistan Zekat, Vergi ve Gümrük Otoritesi tarafından zorunlu kılınan e-fatura QR kodudur. **Aralık 2021'den (Aşama 1) itibaren** Krallık'ta düzenlenen her B2C faturası beş temel fatura alanını içeren bir Fatoora QR taşımalıdır; ve **Ocak 2023'ten (Aşama 2) itibaren** QR ayrıca bir kriptografik imza zarfı taşır. DocBits her iki aşamayı da çözer ve her Aşama 1 ödeme alanını belge API yanıtında adlandırılmış özellik olarak döndürür.

### Özellik Özeti

ZATCA Fatoora, **Base64** içinde paketlenmiş bir **ikili TLV** biçimi (1 bayt etiket kimliği, 1 bayt uzunluk, değer) kullanır. Tüm metin UTF-8'dir, bu nedenle Arapça satıcı adları temiz bir şekilde çözülür. Çıkarıcı Aşama 1 etiketlerini 1–5'i yapılandırılmış alanlar olarak ve — mevcutsa — Aşama 2 etiketlerini 6–9'u downstream uyum araçları için Base64 dizeleri olarak sunar. **İmza ve karma doğrulaması kasıtlı olarak kapsam dışındadır**; bu, özel e-fatura uyum yığınlarına aittir.

#### Temel Avantajlar

* **Zorunlu uyum kapsamı**: her Suudi B2C faturası ayrıştırılır.
* **Arapça desteği**: UTF-8 satıcı adları yeniden kodlamadan geçer.
* **Aşama 1 ve Aşama 2**: her iki aşama da algılanır; aşama çıktıda sunulur.
* **Aşama 2 zarfı korunur**: karma, imza, genel anahtar ve sertifika imzası uyum araçları için Base64 dizeleri olarak tutulur.

***

### Tanıma

- Base64 ile sarılmış ikili TLV (etiketler 1–9, 1 bayt etiket kimliği + 1 bayt uzunluk + değer)
- Aşama tespiti: yalnızca etiketler 1–5 mevcutsa `zatca_phase = 1`; etiketler 6–9 da mevcutsa `zatca_phase = 2`

### TLV Etiket Yerleşimi

| Etiket | Aşama | İçerik |
|--------|-------|--------|
| 1 | 1 | Satıcı adı (UTF-8, Arapça destekler) |
| 2 | 1 | KDV kayıt numarası |
| 3 | 1 | Fatura zaman damgası (ISO 8601) |
| 4 | 1 | Fatura toplamı |
| 5 | 1 | KDV toplamı |
| 6 | 2 | XML fatura karması (Base64) |
| 7 | 2 | Dijital imza (Base64) |
| 8 | 2 | Genel anahtar (Base64) |
| 9 | 2 | Sertifika imzası (Base64) |

### Çıkarılan Alanlar

Tüm alanlar `zatca_` önekini kullanır:

| Alan | Açıklama |
|------|----------|
| `zatca_seller_name` | Satıcı adı (UTF-8) |
| `zatca_vat_number` | KDV kayıt numarası |
| `zatca_invoice_timestamp` | Fatura tarihi/saati |
| `zatca_invoice_total` | Fatura toplamı (ondalık) |
| `zatca_vat_total` | KDV toplamı (ondalık) |
| `zatca_phase` | `1` (Aşama 1) veya `2` (Aşama 2) |
| `zatca_invoice_hash` | XML fatura karması — yalnızca Aşama 2, Base64 |
| `zatca_signature` | Dijital imza — yalnızca Aşama 2, Base64 |
| `zatca_public_key` | Genel anahtar — yalnızca Aşama 2, Base64 |
| `zatca_certificate_signature` | Sertifika imzası — yalnızca Aşama 2, Base64 |

{% hint style="info" %}
**Kapsam dışı**: DocBits kriptografik imzayı, karma veya sertifika zincirini doğrulamaz. Bu doğrulama ayrı bir uyum meselesidir ve ZATCA sertifikalı bir e-fatura yığını tarafından yönetilmelidir.
{% endhint %}

### Örnek API Yanıtı (Aşama 1)

```json
{
  "zatca_seller_name": "شركة أكمي التجارية",
  "zatca_vat_number": "300123456700003",
  "zatca_invoice_timestamp": "2026-04-24T10:00:00",
  "zatca_invoice_total": 115.00,
  "zatca_vat_total": 15.00,
  "zatca_phase": 1
}
```

***

### Özelliği Etkinleştirme

ZATCA Fatoora ayrıştırması genel **Barkod / QR Kodu Çıkarımı** anahtarı tarafından kapsanır — standarda özel bir yapılandırma gerekmez.

1. **Ayarları Açın**:
   * Panodan **Ayarlar**'a gidin.
   * **Belge İşleme**'yi ve ardından **Modül**'ü seçin.
2. **Özelliği Etkinleştirin**:
   * **Barkod / QR Kodu Çıkarımı** seçeneğine kaydırın.
   * Kaydırıcıyı etkinleştirmek için açın.

Ödeme QR Kodu standartlarının tam listesi için [Genel Bakış](./README.md) sayfasına bakın.
