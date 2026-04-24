# Barkod / QR Kodu Çıkarımı

Bu bölüm, **DocBits**'in belgelerden barkodları ve QR kodlarını nasıl tanıdığı ve çıkardığı ile ilgili ayarları içerir. Bu özellik, fatura işleme, envanter takibi ve belge sınıflandırma gibi çeşitli otomasyon senaryoları için kullanışlıdır.

## Mevcut Seçenekler

* [**Barkod Çıkarımları**](bar-code-extractions.md): Standart barkod formatlarının (örneğin Code 128, EAN) çıkarılmasını yapılandırın.
* [**İsviçre QR Faturası**](swiss-qr-code.md): İsviçre ödeme standartlarına (QR-fatura) uygun QR kodlarının işlenmesi için özel ayarlar.

## Ödeme QR Kodu Standartları

Genel QR kod çözmenin ötesinde, DocBits **yedi farklı Ödeme QR Kodu standardını** tanır ve ödeme alanlarını otomatik olarak belge API yanıtına çıkarır. Müşterilerin bu QR dizelerini artık manuel olarak çözmesi gerekmez — her standart, değerlerin doğrudan eşleştirme, doğrulama ve dışa aktarma süreçlerine akması için kendi alan önekini (örn. `swissqr_*`, `girocode_*`) sağlar.

| # | Standart | Bölge | Alan öneki | Tipik kullanım |
|---|----------|-------|------------|----------------|
| 1 | [İsviçre QR Faturası](swiss-qr-code.md) | İsviçre | `swissqr_*` | 2020'den bu yana her İsviçre faturası |
| 2 | [GiroCode (EPC069-12)](girocode.md) | DE, AT, NL, BE, FI | `girocode_*` | SEPA ödemeleri |
| 3 | [SPAYD / SPD](spayd.md) | CZ, kısmen SK | `spayd_*` | Çek Bankalar Birliği standardı |
| 4 | [PagoPA](pagopa.md) | IT (kamu yönetimi) | `pagopa_*` | İtalyan PA faturalarında zorunlu |
| 5 | [Kripto Ödeme URI'leri](crypto-uris.md) | Küresel (kripto) | `crypto_*` | Bitcoin, Lightning, Ethereum, Zcash, Litecoin |
| 6 | [EMVCo MPM](emvco-mpm.md) | BR, IN, SG, TH, MY, ID, PH, VN, HK vb. | `emvmpm_*` | Pix, UPI, PayNow, PromptPay, QRIS, QR Ph, VietQR, FPS |
| 7 | [ZATCA Fatoora](zatca-fatoora.md) | Suudi Arabistan | `zatca_*` | Her KSA faturasında zorunlu |

**Tanıma otomatiktir.** Çözülen her QR dizesi sihirli öneki (örn. İsviçre QR Faturası v2.0 için `SPC\n0200` veya PagoPA için `PAGOPA|002|`) için incelenir; yalnızca tanınan standartlar yapılandırılmış alanlara ayrıştırılır.
