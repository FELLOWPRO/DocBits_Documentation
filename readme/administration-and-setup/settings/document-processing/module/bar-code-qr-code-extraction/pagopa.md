# PagoPA

## Genel Bakış

**PagoPA**, İtalyan kamu yönetiminin ödeme QR standardıdır. Bir İtalyan PA kuruluşu (belediyeler, üniversiteler, sağlık, vergi makamları) tarafından düzenlenen her fatura bir PagoPA QR kodu taşır. DocBits payload'u çözer ve dört zorunlu ödeme alanını belge API yanıtında döndürür.

### Özellik Özeti

PagoPA payload'ları kompakt ve katı yapılandırılmıştır: tek bir satırda tam olarak **beş boru ile ayrılmış alan**. Tutarlar **cent** cinsinden (tam sayı) kodlanır ve çıkarıcı tarafından otomatik olarak euro ondalığına dönüştürülür. `codice_avviso`'nun (18 haneli ödeme bildirimi) öndeki sıfırları korunur — sabit genişlikli bir tanımlayıcı olduğu için asla tam sayı olarak ayrıştırılmamalıdır.

#### Temel Avantajlar

* **İtalyan PA faturaları için zorunlu kapsam**: `codice_avviso` ve alacaklı mali kodu adlandırılmış alanlara çıkarılır.
* **Güvenli sayısal işleme**: 18 haneli `codice_avviso` öndeki sıfırları korur; cent cinsinden tutar aynı zamanda euro float olarak sunulur.

***

### Tanıma

- Sihirli önek: `PAGOPA|002|`
- Önekten sonra tam olarak **5 boru ile ayrılmış alan**: `PAGOPA|002|<codice_avviso>|<fiscal_code_creditor>|<amount_cents>|<auth>`
- **Yalnızca EUR** — spesifikasyon altında başka hiçbir para birimi geçerli değildir

### Çıkarılan Alanlar

Tüm alanlar `pagopa_` önekini kullanır:

| Alan | Açıklama |
|------|----------|
| `pagopa_codice_avviso` | 18 haneli ödeme bildirimi — öndeki sıfırlar korunur (dize) |
| `pagopa_fiscal_code_creditor` | 11 haneli alacaklı mali kodu (dize) |
| `pagopa_amount_cents` | Cent cinsinden tutar (tam sayı) |
| `pagopa_amount` | Euro cinsinden tutar (ondalık, `pagopa_amount_cents`'den türetilir) |
| `pagopa_auth` | Payload'dan isteğe bağlı auth/sürüm göstergesi |

### Örnek API Yanıtı

```json
{
  "pagopa_codice_avviso": "301234567890123456",
  "pagopa_fiscal_code_creditor": "80012345678",
  "pagopa_amount_cents": 12050,
  "pagopa_amount": 120.50
}
```

***

### Özelliği Etkinleştirme

PagoPA ayrıştırması genel **Barkod / QR Kodu Çıkarımı** anahtarı tarafından kapsanır — standarda özel bir yapılandırma gerekmez.

1. **Ayarları Açın**:
   * Panodan **Ayarlar**'a gidin.
   * **Belge İşleme**'yi ve ardından **Modül**'ü seçin.
2. **Özelliği Etkinleştirin**:
   * **Barkod / QR Kodu Çıkarımı** seçeneğine kaydırın.
   * Kaydırıcıyı etkinleştirmek için açın.

Ödeme QR Kodu standartlarının tam listesi için [Genel Bakış](./README.md) sayfasına bakın.
