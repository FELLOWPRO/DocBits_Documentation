# Yapay Zeka Modeli

## Genel Bakış

**Yapay Zeka Modeli** ayarı, belge işleme sırasında **alan çıkarma** ve **tablo çıkarma** için varsayılan olarak hangi yapay zeka modelinin kullanılacağını tanımlamanıza olanak tanır.
Bu bölümde, her model için belirteç maliyetini inceleyebilir ve her tedarikçiye şu anda hangi modelin atandığını görebilirsiniz.

## Nasıl Erişilir

1.  **Ayarlar** → **Belge İşleme** → **Sınıflandırma ve Çıkarma** yoluna gidin

    <figure><img src="../../../../.gitbook/assets/settings_classification_and_extraction.png" alt=""><figcaption></figcaption></figure>
2.  **Tablo Çıkarma** bölümüne gidin

    <figure><img src="../../../../.gitbook/assets/ai_model_1.png" alt=""><figcaption></figcaption></figure>

## Yapay Zeka Modeli Seçenekleri

DocBits, alan ve tablo çıkarımı için üç yapay zeka modeli seçeneği sunar. **Çıkarım doğruluğu**, **işleme hızı** ve **belge başına belirteç maliyeti** arasındaki dengede farklılık gösterirler — böylece seçeneği işlediğiniz belge türüne göre ayarlayabilirsiniz. Şu anda seçili seçeneğin belirteç maliyetini görmek için ayarın yanındaki bilgi simgesinin üzerine gelin.

* **Full** – En kapsamlı seçenek, en yüksek çıkarım doğruluğuna sahiptir. Karmaşık düzenler, düşük kaliteli taramalar veya doğruluğun en önemli olduğu belgeler için idealdir. En güçlü seçenek olduğu için aynı zamanda en yavaşıdır, **belge başına 2 belirteç**.
* **Fast** – Yüksek doğruluğu daha hızlı işleme ve daha düşük maliyetle birleştiren dengeli bir seçenek. Çoğu günlük belge için önerilen varsayılan seçenektir, **belge başına 1 belirteç**.
* **Turbo** – En hızlı ve en ekonomik seçenek. Hızın ve düşük maliyetin azami doğruluktan daha önemli olduğu çok sayıda basit, temiz ve iyi yapılandırılmış belge için en uygunudur, **belge başına 1 belirteç**.

| Seçenek | İdeal kullanım | Doğruluk | Hız | Belirteç maliyeti |
|---------|----------------|----------|-----|-------------------|
| **Full** | Karmaşık düzenler, kötü taramalar, yüksek hassasiyet | En yüksek | En yavaş | 2 / belge |
| **Fast** | Günlük belgeler (önerilen varsayılan) | Yüksek | Hızlı | 1 / belge |
| **Turbo** | Çok sayıda basit, temiz belge | İyi | En hızlı | 1 / belge |

<figure><img src="../../../../.gitbook/assets/ai_model_2.png" alt=""><figcaption></figcaption></figure>

## Yapay Zeka Modeli Atama Tablosu

Ayrıca tedarikçiye özel **Yapay Zeka modellerini** doğrudan **Doğrulama ekranında** yapılandırabilir, böylece bireysel tedarikçiler için çıkarma doğruluğunu ince ayar yapabilirsiniz.


Daha fazla bilgi için lütfen ilgili dokümantasyona [buradan](../../../../end-user-and-partner-section/end-user-section/validation-screen/supplier-specific-ai-model-for-field-and-table-extraction.md) bakın.

Atama tablosu, her tedarikçi için yapay zeka modeli ayarlarını görüntüler ve aşağıdaki ayrıntıları içerir:

* **Tedarikçi Kimliği** – Tedarikçinin benzersiz tanımlayıcısı
* **Yapay Zeka Modeli** – Tedarikçiye şu anda atanan yapay zeka modeli
* **E-Metin**: E-Metin özelliğinin etkin olup olmadığını belirtir
* **Eylem** – Girdiyi silme seçeneğini içerir

<figure><img src="../../../../.gitbook/assets/ai_model_3.png" alt=""><figcaption></figcaption></figure>

### Girdiyi Sil – Tedarikçiye Özel Ayarları Sıfırla

Bir tedarikçinin yapay zeka modeli ayarını varsayılana sıfırlamak için:

1.  Tedarikçi girişinin yanındaki **Eylem** sütunundaki çöp kutusu simgesine tıklayın.

    <figure><img src="../../../../.gitbook/assets/ai_model_4.png" alt=""><figcaption></figcaption></figure>
2.  Bir onay iletişim kutusu görünecektir—girdiyi silmek istediğinizi onaylayın.

    <figure><img src="../../../../.gitbook/assets/ai_model_5.png" alt=""><figcaption></figcaption></figure>

Silindikten sonra, tedarikçi **alan çıkarma** ve **tablo çıkarma** için varsayılan **Yapay Zeka modelini** kullanmaya geri dönecektir.
