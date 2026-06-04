# Then

## "Then..." Eylem Kartlarına Genel Bakış

### **1. Belge Alanı Eylemleri:**

* **Invert Checkbox:** Bu eylem, bir belgedeki onay kutusu alanının durumunu değiştirir.
* **Set Checkbox:** Bu, bir onay kutusu alanının durumunu true (işaretli) veya false (işaretsiz) olarak ayarlar.
* **Set Field to Text:** Bu eylem, belirtilen bir belge alanını verilen bir metin değerine ayarlar.

<figure><img src="../../../.gitbook/assets/then1 (1).png" alt=""><figcaption></figcaption></figure>

### **2. Belge Eylemleri:**

* **Approve the Document:** Bir belgeyi sistemde onaylanmış olarak işaretler.
* **Reject the Document:** Bir belgeyi reddedilmiş olarak işaretler.

<figure><img src="../../../.gitbook/assets/image (259).png" alt=""><figcaption></figcaption></figure>

### **3. Dışa Aktarma Eylemleri:**

* **Export document with export configuration:** Belirli bir dışa aktarma yapılandırmasıyla dışa aktarma sürecini başlatır.
* **Start Export:** Dışa aktarma sürecini başlatır.

<figure><img src="../../../.gitbook/assets/image (260).png" alt=""><figcaption></figcaption></figure>

### **4. Durum Eylemleri:**

* **Change Status:** Bir belgenin veya görevin durumunu belirtilen yeni bir duruma değiştirir.

<figure><img src="../../../.gitbook/assets/then3 (1).png" alt=""><figcaption></figcaption></figure>

### **5. Görev Eylemleri:**

* Atamalar ve bildirimler:
  * **Assign Task:** Belirli ayrıntılarla bir görev oluşturur ve bir kişiye veya gruba atar, onları e-posta yoluyla bilgilendirme seçenekleri dahil.
  * **Create a New Task:** Atamaya benzer ama sistemde tamamen yeni bir görev kurmaya odaklanmıştır.

<figure><img src="../../../.gitbook/assets/then4 (1).png" alt=""><figcaption></figcaption></figure>

### **6. Tablo Eylemleri:**

* **Calculate in Table:** Belirtilen koşullara göre tablo verileri üzerinde hesaplamalar gerçekleştirir ve sonuçları belirlenen bir sütunda depolar.
* **Change Entries:** Belirtilen koşullara göre bir tablodaki girişleri günceller.

<figure><img src="../../../.gitbook/assets/then5 (1).png" alt=""><figcaption></figcaption></figure>

### **7. Atanan (Assignee) Eylemleri:**

* **Assign User from Field:** Belirli bir alanda depolanan kullanıcı verisine göre bir görevi veya belgeyi bir kullanıcıya atar, birincil kullanıcı kullanılamıyorsa yedek bir kullanıcı seçeneğiyle.
* **Assign Document to User or Group:** Bir belgeyi doğrudan bir kullanıcıya veya gruba atar ve sorumluluğun uygun şekilde belirlenmesini sağlar.

<figure><img src="../../../.gitbook/assets/then6 (1).png" alt=""><figcaption></figcaption></figure>

### **8. Harici Etkileşim Eylemleri:**

* **Call API:** Belirli yöntemler, parametreler ve verilerle özelleştirilebilen, harici bir API'ye istek gönderir.
* **Send HTTPS Request:** API çağrılarına benzer ama özellikle HTTPS protokolleri için biçimlendirilmiştir.

<figure><img src="../../../.gitbook/assets/then7 (1).png" alt=""><figcaption></figcaption></figure>

### **9. Gelişmiş İşleme:**

* **Run Workflow:** Sistemde başka bir iş akışını tetikler ve karmaşık süreç zincirlemesine olanak tanır.

#### Pratik Uygulama

Bu eylem kartları, iş akışı kurulumunun önceki bölümlerinde tanımlanan belirli tetikleyicilere göre yanıtları otomatikleştirmek için kullanılır. Örneğin:

* Bir belge inceleme gerektirir olarak tanımlanırsa, tüm belirtilen koşulları geçtikten sonra "Approve the Document" eylemi otomatik olarak tetiklenebilir.
* Veri yönetimi görevleri için, "Set Checkbox" veya "Set Field to Text" eylemleri belge alanlarının otomatik olarak güncellenmesini sağlar, manuel veri girişini ve hata olasılığını azaltır.
* API etkileşimleri veya durum değişiklikleri gibi karmaşık görevler, yalnızca ERP sistemi içinde değil aynı zamanda harici servisler ve araçlarla da etkileşimleri kolaylaştırır, entegrasyonu ve işlevselliği artırır.

### Sonuç

İş akışı sisteminizdeki "Then..." bölümü, iş akışında koşulların karşılanması sonucunda gerçekleşmesi gereken kesin eylemleri tanımlamak için sağlam araçlar sunar. Bu eylemleri etkili bir şekilde kullanarak, işletmeler rutin süreçleri otomatikleştirebilir, veri doğruluğunu sağlayabilir ve değişen bilgilere ve sistem durumlarına dinamik olarak yanıt verebilir. Bu eylemlerin nasıl yapılandırılacağını ve kullanılacağını anlamak, ERP sisteminizin iş akışı yeteneklerinin verimliliğini ve etkinliğini en üst düzeye çıkarmanın anahtarıdır.
