# Kripto Ödeme URI'leri (BIP21 / BIP321)

## Genel Bakış

Kripto Ödeme URI'leri, kripto para ödeme taleplerini QR kodlarına kodlamak için gayri resmi ancak geniş çapta benimsenmiş standarttır. DocBits, hem **BIP21**'i (orijinal Bitcoin ödeme URI'si) hem de **BIP321**'i (2024'ün modernize edilmiş uzantısı) en yaygın beş blok zincirinde tanır: **Bitcoin**, **Lightning Network**, **Zcash**, **Ethereum** ve **Litecoin**.

### Özellik Özeti

Bir kripto QR payload'u, bir şema (`bitcoin:`, `lightning:`, `zcash:`, `ethereum:`, `litecoin:`), alıcı adresi ve URL tarzı parametrelerden oluşan bir URI'dir. DocBits tüm standart BIP21 parametrelerini (`amount`, `label`, `message`) ve daha yeni BIP321 uzantılarını (`lightning=` ödeme yedeği, `pj=` / `pjos=` payjoin uç noktaları) çıkarır. BIP21 spesifikasyonuna göre `req-` önekli parametreler desteklenmiyorsa tüketiciler tarafından reddedilebilir — bu nedenle DocBits bunları ayrı bir alanda (`crypto_required_params`) tutar, böylece istemciler nasıl işleneceğine karar verebilir.

#### Temel Avantajlar

* **Çoklu zincir desteği**: Bitcoin, Lightning, Zcash, Ethereum ve Litecoin tek bir çıkarıcıda.
* **BIP21 + BIP321**: her iki sürüm de tanınır; sürüm çıktıda sunulur.
* **Şema büyük/küçük harf duyarsız**: `BITCOIN:` ve `bitcoin:` aynı şekilde işlenir.

***

### Tanıma

- Şema tabanlı tanıma (büyük/küçük harf duyarsız): `bitcoin:`, `lightning:`, `zcash:`, `ethereum:`, `litecoin:`
- Standart URI biçimi: `<scheme>:<address>?<param>=<value>&<param>=<value>`

### Desteklenen Parametreler

**BIP21 temel parametreleri:**
- `amount` — yerel birimde istenen tutar
- `label` — alıcının okunabilir etiketi
- `message` — serbest metin

**BIP321 uzantıları:**
- `lightning=<BOLT11>` — yedek olarak Lightning faturası
- `pj=<endpoint>` / `pjos=<endpoint>` — payjoin uç noktaları
- `req-*` — zorunlu parametreler (`crypto_required_params`'te korunur)

### Çıkarılan Alanlar

Tüm alanlar `crypto_` önekini kullanır:

| Alan | Açıklama |
|------|----------|
| `crypto_scheme` | `bitcoin`, `lightning`, `zcash`, `ethereum` veya `litecoin` |
| `crypto_address` | Alıcı adresi |
| `crypto_amount` | İstenen tutar (ondalık) |
| `crypto_currency` | Yerel para birimi sembolü (`BTC`, `ETH`, `LTC`, `ZEC`) |
| `crypto_label` | Alıcı etiketi (ayarlanmışsa) |
| `crypto_message` | Serbest metin (ayarlanmışsa) |
| `crypto_lightning_fallback` | BOLT11 Lightning faturası (BIP321 `lightning=` dan) |
| `crypto_payjoin_endpoint` | Payjoin uç noktası (`pj=` / `pjos=` dan) |
| `crypto_required_params` | Tüm `req-*` parametreleri, istemci kararı için korunur |
| `crypto_uri_version` | `bip21` veya `bip321` |

### Örnek API Yanıtı

```json
{
  "crypto_scheme": "bitcoin",
  "crypto_address": "bc1q9h6mksxrsfnd4ymr8mu2w2v3v0sylgkfghxwzm",
  "crypto_amount": 0.00254,
  "crypto_currency": "BTC",
  "crypto_label": "Acme Invoice 2026-042",
  "crypto_message": "Payment for invoice 2026-042",
  "crypto_uri_version": "bip21"
}
```

***

### Özelliği Etkinleştirme

Kripto URI ayrıştırması genel **Barkod / QR Kodu Çıkarımı** anahtarı tarafından kapsanır — standarda özel bir yapılandırma gerekmez.

1. **Ayarları Açın**:
   * Panodan **Ayarlar**'a gidin.
   * **Belge İşleme**'yi ve ardından **Modül**'ü seçin.
2. **Özelliği Etkinleştirin**:
   * **Barkod / QR Kodu Çıkarımı** seçeneğine kaydırın.
   * Kaydırıcıyı etkinleştirmek için açın.

Ödeme QR Kodu standartlarının tam listesi için [Genel Bakış](./README.md) sayfasına bakın.
