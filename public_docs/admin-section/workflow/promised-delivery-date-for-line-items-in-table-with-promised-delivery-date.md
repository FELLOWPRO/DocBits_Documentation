# Vaat Edilen Teslimat Tarihi Tablosundaki Kalemler İçin Vaat Edilen Teslimat Tarihi

<figure><img src="../../../../../../.gitbook/assets/image.png" alt="" width="375"><figcaption></figcaption></figure>

## Amaç:

Bu iş akışı kartı, karşılaştırma operatörlerini ve yapılandırılabilir tolerans kurallarını kullanarak **kalemlerin vaat edilen teslimat tarihini**, **satın alma siparişindeki vaat edilen teslimat tarihine** göre doğrulamak için tasarlanmıştır. İş akışlarının uyumlu, erken veya geç teslimat tarihlerini otomatik olarak algılamasını ve buna göre tepki vermesini sağlar.

## Kartın Bileşenleri:

1. **Operatör**
   * **Açıklama:**
     Kalem vaat edilen teslimat tarihinin satın alma siparişi vaat edilen teslimat tarihiyle nasıl karşılaştırılacağını tanımlar.
   * **Seçenekler:**
     * **Eşittir (=):** Kalem tarihi tolerans penceresi içine düşmelidir.
     * **Eşit Değildir (≠):** Kalem tarihi tolerans penceresinin dışına düşmelidir.
     * **Büyüktür (>):** Kalem tarihi tolerans penceresinden sonra olmalıdır.
     * **Büyük veya Eşittir (≥):** Kalem tarihi tolerans penceresinin başlangıcında veya sonrasında olmalıdır.
     * **Küçüktür (<):** Kalem tarihi tolerans penceresinden önce olmalıdır.
     * **Küçük veya Eşittir (≤):** Kalem tarihi tolerans penceresinin sonunda veya öncesinde olmalıdır.<br>
2. **Tolerans Günleri**
   * **Açıklama:**
     Satın alma siparişi vaat edilen teslimat tarihi etrafındaki kabul edilebilir tolerans penceresini hesaplamak için kullanılan gün sayısını belirtir.
   * **Detay:**
     Bu değer bir tam sayıdır ve doğrulama sırasında satın alma siparişi tarihinden kaç gün öncesinin ve sonrasının dikkate alınacağını tanımlar.<br>
3. **İzin Verilen Tolerans Günleri**
   * **Açıklama:**
     Tolerans günleri hesaplanırken hangi haftanın günlerinin sayılacağını tanımlar.
   * **Detay:**
     Kullanıcılar belirli haftanın günlerini seçebilir (örneğin, Pazartesi'den Cuma'ya). Tolerans penceresi hesaplanırken yalnızca seçilen günler dahil edilir.

### İşlevsellik:

* **Koşul Değerlendirmesi:** Sistem, yapılandırılan **Tolerans Günleri** ve **İzin Verilen Tolerans Günleri**ne göre satın alma siparişi vaat edilen teslimat tarihi etrafında bir tolerans penceresi hesaplar.
  Her bir kalemin vaat edilen teslimat tarihi daha sonra seçilen operatör kullanılarak bu pencereyle karşılaştırılır.
* Eylem Yürütme:
  * **Doğru Koşul:** Teslimat tarihi farkı tolerans aralığı içindeyse ve operatör tarafından belirlenen koşulla eşleşiyorsa iş akışı devam eder.
  * **Yanlış Koşul:** Koşul karşılanmazsa iş akışı devam etmez.

### Kurulum ve Yapılandırma:

* Uygun karşılaştırma operatörünü seçin.
* Tolerans gün sayısını girin.
* Hangi haftanın günlerinin tolerans günü olarak sayılması gerektiğini seçin.

### Sonuç:

**Satın Alma Siparişi ile Karşılaştır – Kalemler İçin Vaat Edilen Teslimat Tarihi** iş akışı kartı, teslimat tarihi kurallarını zorunlu kılmak için esnek bir yol sunar. Operatörleri haftanın günü duyarlı tolerans işleme ile birleştirerek, manuel kontrolleri ve istisnaları azaltırken teslimat taahhütlerinin hassas bir şekilde doğrulanmasını sağlar.
