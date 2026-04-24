# GiroCode (EPC069-12)

## Genel Bakış

**GiroCode**, European Payments Council tarafından **EPC069-12** spesifikasyonunda tanımlanan SEPA ödeme QR kodudur. Alman ve Avusturyalı bankaların faturalarında (Sparkasse, VR-Banken, Deutsche Bank, Commerzbank, PSA Austria) fiili standarttır ve Hollanda, Belçika ve Finlandiya'da da verilir. DocBits her iki revizyonu da (**v001** ve **v002**) çözer ve tam SEPA ödeme payload'unu belge API yanıtında döndürür.

### Özellik Özeti

Bir GiroCode, SEPA kredi transferini başlatmak için gereken her şeyi içerir: alıcının BIC ve IBAN'ı, alıcı adı, tutar, amaç ve yapılandırılmış bir alacaklı referansı veya serbest metin mesajı. DocBits, payload'u normalleştirir; böylece **ondalık ayırıcı olarak `.` veya `,` kullanan tutarlar** — Alman jeneratörlerinin spesifikasyondan yaygın sapması — hatasız kabul edilir.

#### Temel Avantajlar

* **Geniş DE / AT kapsamı**: her büyük perakende bankası müşteri faturalarına GiroCode basar.
* **Her iki revizyon desteklenir**: v001 (BIC zorunlu) ve v002 (EEA için BIC isteğe bağlı).
* **Ondalık ayırıcı toleranslı**: `227.01` ve `227,01` birbirinin yerine kabul edilir.

***

### Tanıma

- Sihirli önek: `BCD\n001` (v001) veya `BCD\n002` (v002)
- EPC069-12 spesifikasyonuna uygun satır bazlı yapılandırılmış payload
- **v002**, IBAN Tek Euro Ödeme Alanı içindeyse BIC'i isteğe bağlı yapar

### Çıkarılan Alanlar

Tüm alanlar `girocode_` önekini kullanır:

| Alan | Açıklama |
|------|----------|
| `girocode_bic` | Alıcının BIC'i (v001'de zorunlu, v002'de EEA için isteğe bağlı) |
| `girocode_creditor_name` | Alıcı adı |
| `girocode_iban` | Alıcı IBAN'ı |
| `girocode_amount` | Tutar (ondalık) — `.` ve `,` kabul edilir |
| `girocode_currency` | Para birimi (genellikle `EUR`) |
| `girocode_purpose` | SEPA amaç kodu |
| `girocode_structured_reference` | Yapılandırılmış alacaklı referansı (ISO 11649 RF) |
| `girocode_unstructured_remittance` | Serbest metin mesajı |
| `girocode_version` | `001` veya `002` |

### Örnek API Yanıtı

Gerçek örnek (Dr. Meindl u. Partner faturası):

```json
{
  "girocode_bic": "DAAEDEDDXXX",
  "girocode_creditor_name": "Dr. Meindl u. Partner",
  "girocode_iban": "DE69300606010006343686",
  "girocode_amount": 227.01,
  "girocode_currency": "EUR",
  "girocode_unstructured_remittance": "38710498001705 - QR",
  "girocode_version": "002"
}
```

***

### Özelliği Etkinleştirme

GiroCode ayrıştırması genel **Barkod / QR Kodu Çıkarımı** anahtarı tarafından kapsanır — standarda özel bir yapılandırma gerekmez.

1. **Ayarları Açın**:
   * Panodan **Ayarlar**'a gidin.
   * **Belge İşleme**'yi ve ardından **Modül**'ü seçin.
2. **Özelliği Etkinleştirin**:
   * **Barkod / QR Kodu Çıkarımı** seçeneğine kaydırın.
   * Kaydırıcıyı etkinleştirmek için açın.

Ödeme QR Kodu standartlarının tam listesi için [Genel Bakış](./README.md) sayfasına bakın.
