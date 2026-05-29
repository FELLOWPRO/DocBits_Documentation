# Hibrit PDF XML Çıkarımını Atla

### Genel Bakış

**Hibrit PDF XML Çıkarımını Atla** (Skip Hybrid PDF XML Extraction) ayarı, DocBits'in **hibrit PDF'leri** — gömülü yapılandırılmış bir e-fatura (ZUGFeRD / Factur-X) içeren PDF faturaları — nasıl işlediğini denetler. **PDF içindeki yapılandırılmış XML'in** otomatik işleme için öncü belge mi olduğuna, yoksa **PDF'in kendisinin** OCR ile birincil belge olarak mı işleneceğine karar verir.

Bu ayar özellikle **ABD'deki müşteriler** için önemlidir. AB/Almanya'nın aksine, ABD'de genel bir B2B e-fatura zorunluluğu yoktur; bu nedenle ABD'deki kuruluşlar, karşı taraf gömülü XML içeren bir ZUGFeRD/Factur-X dosyası gönderdiğinde bile genellikle PDF'in birincil, insan tarafından okunabilir fatura olarak ele alınmasını ister.

### Ne işe yarar?

Bir ZUGFeRD/Factur-X dosyası, makine tarafından okunabilir bir XML fatura da içeren tek bir PDF'tir. Varsayılan olarak DocBits, bu gömülü XML'i algılar ve çıkarım için öncü kaynak olarak kullanır (yapılandırılmış elektronik yol).

* **Devre dışı (varsayılan)** — DocBits gömülü e-fatura XML'ini algılar ve belgeyi **yapılandırılmış elektronik yolda** işler. XML, öncü faturadır. Bu, yapılandırılmış e-faturanın ilgili fatura olduğu ve PDF'in yalnızca bir görselleştirme / okuma kopyası olduğu AB/Almanya için hukuken doğru davranıştır.
* **Etkin** — DocBits **gömülü XML'i yok sayar** ve belgeyi **PDF işlemcisine (OCR)** yönlendirir. PDF, birincil işleme belgesi olur. Bu, PDF öncelikli işleme isteyen **ABD kuruluşları** için tipik seçimdir.

{% hint style="info" %}
Bu ayar yalnızca **hibrit PDF'leri** etkiler (ZUGFeRD / Factur-X = gömülü XML içeren bir `.pdf`). `.xml` olarak yüklenen saf bir XRechnung/EDI dosyası her zaman yapılandırılmış elektronik yolda işlenir — birincil belge olabilecek bir PDF yoktur.
{% endhint %}

### Denetim ve uyumluluk — orijinal her zaman korunur

Bu ayarı etkinleştirmek e-faturayı **atmaz**. Orijinal belge her zaman korunur:

* Orijinal ZUGFeRD/Factur-X **PDF — gömülü XML'i dahil — depolanmış** ve indirilebilir durumda kalır. Belgenin saklanan kopyasından hiçbir şey silinmez.
* İşleme yalnızca **çıkarımı hangi içeriğin yönlendirdiğini** (PDF/OCR ile gömülü XML arasında) değiştirir, arşivlenen şeyi değil.

Böylece bir ABD kuruluşu, yapılandırılmış e-fatura denetim için kullanılabilir kalırken PDF'i birincil olarak işleyebilir.

{% hint style="warning" %}
AB/Almanya kuruluşları için bu ayarı **devre dışı** bırakın. 2025 e-fatura kurallarına göre yapılandırılmış bir e-fatura (ZUGFeRD/Factur-X, XRechnung) hukuken ilgili faturadır; düz bir PDF yalnızca bir okuma kopyasıdır. Geçerli bir e-fatura mevcutken yapılandırılmış veriler yerine PDF'i birincil olarak işlemek uygun değildir.
{% endhint %}

### Nasıl kullanılır

1. **Ayarı açın**:
   * **Ayarlar**'a gidin.
   * **Belge İşleme**'yi seçin.
   * **Modül**'ü seçin.
   * **Belge Türü** bölümünü açın.
   * **Hibrit PDF XML Çıkarımını Atla** seçeneğini bulun ve anahtarı değiştirin.
2. **Modu seçin**:
   * **ABD / PDF öncelikli kuruluşlar** → ZUGFeRD/Factur-X PDF'lerinin OCR ile birincil belge olarak işlenmesi için anahtarı etkinleştirin.
   * **AB/Almanya kuruluşları** → yapılandırılmış e-faturanın öncü belge olarak kalması için anahtarı devre dışı bırakın.
3. **Doğrulayın**:
   * Bir ZUGFeRD/Factur-X PDF'i yükleyin ve işleme sonucunu kontrol edin — anahtar etkinken normal bir PDF (OCR) olarak işlenir; devre dışıyken gömülü e-fatura verileri çıkarılır.

### Bu özellik ne zaman kullanılır

* **ABD müşterileri / e-fatura zorunluluğu yok**: Gömülü e-fatura arşivlenmiş kalırken bilinen PDF'in birincil işleme belgesi olması için etkinleştirin.
* **Karma / PDF öncelikli iş akışları**: Sonraki süreçler, doğrulama veya inceleme XML yerine PDF düzenine dayandığında etkinleştirin.
* **AB/Almanya uyumluluğu**: Gerektiği gibi yapılandırılmış e-fatura verilerinin işlemeyi yönlendirmesi için devre dışı bırakın.
