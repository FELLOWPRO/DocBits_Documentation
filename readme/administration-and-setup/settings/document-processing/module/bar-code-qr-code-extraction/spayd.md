# SPAYD / Short Payment Descriptor (Çek)

## Genel Bakış

**SPAYD** (Short Payment Descriptor), diğer adıyla **SPD**, Çek Bankalar Birliği tarafından tanımlanan standart ödeme QR kodudur. Neredeyse her Çek ticari faturasında basılıdır ve kısmen Slovakya'da da kullanılır. DocBits, SPAYD payload'larını çözer ve ödeme talimatını tamamen — Çekçe'ye özgü sembollerle (variable, specific, constant) birlikte — belge API yanıtında döndürür.

### Özellik Özeti

SPAYD payload'u, yıldız işareti ile ayrılmış anahtar:değer çiftlerinin bir listesidir. Değerler yüzde kodludur, böylece UTF-8 alıcı adları ve mesajlar korunur. DocBits, yaygın `ACC` varyantını (IBAN artı isteğe bağlı BIC, artı işaretiyle ayrılmış), `ALT-ACC`'yi (alternatif IBAN'lar, virgülle ayrılmış) destekler ve bilinmeyen satıcıya özgü anahtarları özel bir alanda (`spayd_raw_pairs`) korur; böylece downstream tüketiciler hiçbir zaman veri kaybetmez.

#### Temel Avantajlar

* **Çek ödemeleri için tam kapsam**: IBAN/BIC ile birlikte VS/SS/KS sembolleri adlandırılmış alanlara çıkarılır.
* **Unicode güvenli**: yüzde kodlu UTF-8 alıcı adları ve mesajlar sorunsuz aktarılır.
* **İleriye uyumlu**: bilinmeyen anahtarlar `spayd_raw_pairs`'te korunur.

***

### Tanıma

- Sihirli önek: `SPD*1.0*`
- Payload, `*` ile ayrılmış `KEY:value` çiftleri listesidir, örn. `SPD*1.0*ACC:CZ5508000000001234567899*AM:480.55*CC:CZK`
- Değerler **yüzde kodludur** (RFC 3986)
- `ACC`, `IBAN+BIC` taşıyabilir (artı ile ayrılmış); `ALT-ACC`, virgülle ayrılmış alternatif IBAN'ları taşır

### Çıkarılan Alanlar

Tüm alanlar `spayd_` önekini kullanır:

| Alan | Açıklama |
|------|----------|
| `spayd_iban` | Ana IBAN (`ACC`'den) |
| `spayd_bic` | BIC (`ACC`'den, varsa) |
| `spayd_alt_ibans` | Alternatif IBAN'lar listesi (`ALT-ACC`'den) |
| `spayd_amount` | Tutar (ondalık, `AM`'den) |
| `spayd_currency` | Para birimi (`CC`'den, genellikle `CZK`) |
| `spayd_variable_symbol` | Değişken sembol (`VS`) — fatura/referans numarası |
| `spayd_specific_symbol` | Özel sembol (`SS`) |
| `spayd_constant_symbol` | Sabit sembol (`KS`) |
| `spayd_recipient_name` | Alıcı adı (`RN`'den) |
| `spayd_due_date` | Vade tarihi (`DT`'den, `YYYYMMDD`) |
| `spayd_message` | Serbest mesaj (`MSG`'den) |
| `spayd_raw_pairs` | Bilinmeyen veya satıcıya özgü `KEY:value` çiftleri, değişmeden korunur |

### Örnek API Yanıtı

```json
{
  "spayd_iban": "CZ5508000000001234567899",
  "spayd_amount": 480.55,
  "spayd_currency": "CZK",
  "spayd_variable_symbol": "2026041720",
  "spayd_constant_symbol": "0308",
  "spayd_recipient_name": "Moje firma, s.r.o.",
  "spayd_due_date": "20260507",
  "spayd_message": "Platba za fakturu 2026041720"
}
```

***

### Özelliği Etkinleştirme

SPAYD ayrıştırması genel **Barkod / QR Kodu Çıkarımı** anahtarı tarafından kapsanır — standarda özel bir yapılandırma gerekmez.

1. **Ayarları Açın**:
   * Panodan **Ayarlar**'a gidin.
   * **Belge İşleme**'yi ve ardından **Modül**'ü seçin.
2. **Özelliği Etkinleştirin**:
   * **Barkod / QR Kodu Çıkarımı** seçeneğine kaydırın.
   * Kaydırıcıyı etkinleştirmek için açın.

Ödeme QR Kodu standartlarının tam listesi için [Genel Bakış](./README.md) sayfasına bakın.
