# EMVCo MPM (Satıcı-Sunumlu QR)

## Genel Bakış

**EMVCo MPM** (Merchant-Presented Mode), çipli kart ve temassız ödeme standartlarının arkasındaki aynı kuruluş olan EMVCo tarafından sürdürülen küresel QR kod spesifikasyonudur. Tek bir TLV (Tag-Length-Value) zarfı bir düzineden fazla ulusal anlık ödeme sistemi arasında paylaşılır, böylece tek bir ayrıştırıcı **Pix** (Brezilya), **UPI** (Hindistan), **PayNow** (Singapur), **PromptPay** (Tayland), **QRIS** (Endonezya), **QR Ph** (Filipinler), **VietQR** (Vietnam), **FPS** (Hong Kong), **DuitNow** (Malezya), **NETS** (Singapur) ve çok daha fazlasının kilidini açar.

### Özellik Özeti

Her EMVCo MPM payload'u aynı zarfı paylaşır: `000201` ile başlar (Payload Format Indicator = 01) ve `6304<CRC>` ile biter; burada `<CRC>` bir 4 hex CRC16-CCITT-FALSE sağlama toplamıdır. İçinde, TLV kodlu 26–51 etiketleri bir **GUI alt-etiketi** ile tanımlanan **Merchant Account Info** şablonlarını taşır — DocBits, QR'nin hangi ulusal şemaya ait olduğunu bu GUI etiketi üzerinden algılar. CRC doğrulanır ve sonuç, satıcıların değiştirilmiş QR kodlarını tespit edebilmesi için boolean olarak sunulur.

#### Temel Avantajlar

* **Tek çıkarıcı, birçok şema**: tek bir genel TLV ayrıştırıcı tüm EMVCo MPM ailesini ele alır.
* **Ulusal şemalar tanımlanır**: çıktı adlandırılmış bir şema içerir (örn. `pix`, `upi`, `paynow`), böylece downstream mantık temiz bir şekilde dallanabilir.
* **CRC geçerliliği sunulur**: `emvmpm_crc16_valid` değiştirilmiş veya bozuk QR kodlarını açığa çıkarır.
* **Para birimi normalleştirme**: ISO 4217 sayısal para birimi kodları otomatik olarak alpha-3'e eşlenir (20+ para birimi; eşleşmemiş sayısal kodlar olduğu gibi geçer).

***

### Tanıma

- Sihirli biçim: `000201` ile başlar ve `6304<4-hex CRC16-CCITT-FALSE>` ile biter
- Genel bir TLV çözücü her etiketi dolaşır
- Ulusal şemalar, Merchant Account Info şablonlarındaki (etiket 26–51) **GUI alt-etiketi** ile tanımlanır

### Tanınan Ulusal Şemalar

| GUI alt-etiketi | Şema | Ülke |
|-----------------|------|------|
| `br.gov.bcb.pix` | **Pix** | Brezilya |
| `UPI` | **UPI** | Hindistan |
| `SG.PAYNOW` | **PayNow / SGQR** | Singapur |
| `SG.COM.NETS` | **NETS** | Singapur |
| `HK.COM.HKICL.FPS` | **FPS** | Hong Kong |
| `ID.CO.QRIS.WWW` | **QRIS** | Endonezya |
| `COM.BDO.QRPH` / `COM.BPI.QRPH` / `PH.PPMI.P2MEMV` | **QR Ph** | Filipinler |
| `COM.QRCODE.TELLUSBANGKOK` + AID `A000000677010111` | **PromptPay** | Tayland |
| `A000000727` | **VietQR** | Vietnam |

Tanınmayan GUI / AID değerleri yine ayrıştırılır — çıkarıcı, genel EMVCo MPM alan kümesine geri döner.

### Çıkarılan Alanlar

Tüm alanlar `emvmpm_` önekini kullanır:

| Alan | Açıklama |
|------|----------|
| `emvmpm_scheme` | Tespit edilen ulusal şema (örn. `pix`, `upi`, `paynow`, `qris`, `promptpay`, `vietqr`, `fps`, `qrph`, `nets`) veya `generic` |
| `emvmpm_merchant_name` | Satıcı adı (etiket 59) |
| `emvmpm_merchant_city` | Satıcı şehri (etiket 60) |
| `emvmpm_country_code` | Ülke kodu ISO 3166 alpha-2 (etiket 58) |
| `emvmpm_amount` | İşlem tutarı (ondalık, etiket 54) |
| `emvmpm_currency` | Para birimi alpha-3 (etiket 53 sayısal kodundan dönüştürülür) |
| `emvmpm_additional_data` | İç içe nesne: fatura numarası, referans etiketi, terminal etiketi, işlem amacı (etiket 62 alt-etiketleri) |
| `emvmpm_crc16_valid` | Boolean — CRC16 sağlama toplamı eşleşirse `true` |

### Örnek API Yanıtı (Pix)

```json
{
  "emvmpm_scheme": "pix",
  "emvmpm_merchant_name": "ACME COMERCIO LTDA",
  "emvmpm_merchant_city": "SAO PAULO",
  "emvmpm_country_code": "BR",
  "emvmpm_amount": 125.00,
  "emvmpm_currency": "BRL",
  "emvmpm_additional_data": {
    "reference_label": "PEDIDO-2026-0427"
  },
  "emvmpm_crc16_valid": true
}
```

***

### Özelliği Etkinleştirme

EMVCo MPM ayrıştırması genel **Barkod / QR Kodu Çıkarımı** anahtarı tarafından kapsanır — standarda özel bir yapılandırma gerekmez.

1. **Ayarları Açın**:
   * Panodan **Ayarlar**'a gidin.
   * **Belge İşleme**'yi ve ardından **Modül**'ü seçin.
2. **Özelliği Etkinleştirin**:
   * **Barkod / QR Kodu Çıkarımı** seçeneğine kaydırın.
   * Kaydırıcıyı etkinleştirmek için açın.

Ödeme QR Kodu standartlarının tam listesi için [Genel Bakış](./README.md) sayfasına bakın.
