# Vade Tarihi Hesaplama

<figure><img src="../../../.gitbook/assets/due_date_calc_overview.png" alt="Vade tarihi hesaplama ayarları"><figcaption><p>Vade tarihi hesaplama ayarları</p></figcaption></figure>

**Vade Tarihi Hesaplama** sayfası (**Belge İşleme → Vade Tarihi Hesaplama**), DocBits'in fatura vade tarihlerini, iskonto (Skonto) vade tarihlerini ve ödeme koşullarını faturalarda bulunan ödeme koşulu kodlarından nasıl hesapladığını denetler.

## Hesaplanan Alanları Göster

Otomatik olarak hesaplanan fatura alanlarının — vade tarihi, iskonto vade tarihi, ödeme koşulları ve AP atama kodu — Alan Ayarları'nda ve Hızlı Arama ile e-posta şablonlarında değişken olarak görünmesi için **Hesaplanan Alanları Göster**'i etkinleştirin. Özel belge türleri asla etkilenmez.

## Fatura Vade Tarihi Hesaplama

### Hafta Sonu İşlemesi

<figure><img src="../../../.gitbook/assets/due_date_calc_weekend_options.png" alt="Hafta sonu kuralı seçenekleri"><figcaption><p>Hafta sonu kuralı seçenekleri</p></figcaption></figure>

Cumartesi veya pazara denk gelen bir vade tarihinin nasıl ayarlanacağını seçin. Bu, **hem** fatura vade tarihi **hem de** iskonto (Skonto) vade tarihi için geçerlidir.

| Kural | Etki |
|-------|------|
| **Yok** | Takvim tarihini koru (ayarlama yok). |
| **Sonraki** | Cmt/Paz'ı sonraki Pazartesiye taşı. |
| **Önceki** | Cmt/Paz'ı önceki Cumaya taşı. |
| **En yakın** | Cumartesi → Cuma, Pazar → Pazartesi. |
| **Değiştirilmiş Sonraki** | Sonraki Pazartesi; ancak sonraki aya geçerse, önceki Cuma. |

### AP Atama Kodu

**AP Atama Kodu Alanı**'nı seçerek tedarikçi ödeme koşullarını otomatik fatura yönlendirmesi için AP atama kodlarıyla eşleştirin.

## İskonto Koşulu Geçersiz Kılmaları

<figure><img src="../../../.gitbook/assets/due_date_calc_mappings.png" alt="İskonto koşulu geçersiz kılmaları"><figcaption><p>İskonto koşulu geçersiz kılmaları</p></figcaption></figure>

Belirli bir öneki bir iskonto yüzdesine ve gün sayısına eşlemek için **İskonto Koşulu Geçersiz Kılmaları**'nı kullanın. **Önek**, **Yüzde** ve **Gün** içeren bir satır eklemek için **+ Eşleme Ekle**'ye tıklayın.

## Desteklenen Biçimler

<figure><img src="../../../.gitbook/assets/due_date_calc_formats.png" alt="Desteklenen ödeme koşulu ve iskonto biçimleri"><figcaption><p>Desteklenen ödeme koşulu ve iskonto biçimleri</p></figcaption></figure>

DocBits aşağıdaki ödeme koşulu ve iskonto kodlarını tanır.

**Desteklenen Ödeme Koşulu Biçimleri**

| Biçim | Örnek | Anlamı |
|-------|-------|--------|
| Infor M3 | `N90`, `N30` | Net 90 / 30 gün |
| Infor M3 | `NET` | Teslimde ödenir |
| Infor M3 | `M20` | Sonraki ayın 20'si |
| Infor M3 | `E15` | Ay sonu + 15 gün |
| Infor LN | `030`, `30` | Net 30 gün |
| Reversed | `14N`, `30N` | Net 14 / 30 gün |
| Metin Kodları | `REC`, `DUE`, `COD` | Teslimde ödenir |

**İskonto Koşulu Biçimi** — iskonto koşulları erken ödeme iskontolarını 3 haneli kodlar olarak kodlar: ilk hane iskonto yüzdesi, son iki hane ise ödeme yapılması gereken gün sayısıdır.

| Kod | Anlamı |
|-----|--------|
| `210` | 10 gün içinde ödenirse %2 iskonto |
| `130` | 30 gün içinde ödenirse %1 iskonto |
| `545` | 45 gün içinde ödenirse %5 iskonto |
| `0` | İskonto yok |
