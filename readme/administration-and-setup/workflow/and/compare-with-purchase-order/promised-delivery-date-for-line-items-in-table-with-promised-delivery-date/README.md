# Promised delivery date for line items in table with promised delivery date

<figure><img src="../../../../../.gitbook/assets/image (3).png" alt="" width="375"><figcaption></figcaption></figure>

## Amaç:

Bu iş akışı kartı, **satır öğelerinin vaat edilen teslimat tarihini**, karşılaştırma operatörleri ve yapılandırılabilir tolerans kuralları kullanarak **satınalma siparişindeki vaat edilen teslimat tarihine** karşı doğrulamak için tasarlanmıştır. İş akışlarının uyumlu, erken veya geç teslimat tarihlerini otomatik olarak algılamasına ve buna göre tepki vermesine olanak tanır.

## Kartın Bileşenleri:

1. **Operatör**
   * **Açıklama:**\
     Satır öğesi vaat edilen teslimat tarihinin satınalma siparişi vaat edilen teslimat tarihiyle nasıl karşılaştırılacağını tanımlar.
   * **Seçenekler:**
     * **Eşittir (=):** Satır öğesi tarihi tolerans penceresi içine düşmelidir.
     * **Eşit Değildir (≠):** Satır öğesi tarihi tolerans penceresinin dışına düşmelidir.
     * **Büyüktür (>):** Satır öğesi tarihi tolerans penceresinden sonra olmalıdır.
     * **Büyük veya Eşittir (≥):** Satır öğesi tarihi tolerans penceresinin başlangıcında veya sonrasında olmalıdır.
     * **Küçüktür (<):** Satır öğesi tarihi tolerans penceresinden önce olmalıdır.
     * **Küçük veya Eşittir (≤):** Satır öğesi tarihi tolerans penceresinin sonunda veya öncesinde olmalıdır.<br>
2. **Tolerans Günleri**
   * **Açıklama:**\
     Satınalma siparişi vaat edilen teslimat tarihi etrafındaki kabul edilebilir tolerans penceresini hesaplamak için kullanılan gün sayısını belirtir.
   * **Ayrıntı:**\
     Bu değer bir tam sayıdır ve doğrulama sırasında satınalma siparişi tarihinden önce ve sonra kaç günün dikkate alınacağını tanımlar.<br>
3. **İzin Verilen Tolerans Günleri**
   * **Açıklama:**\
     Tolerans günleri hesaplanırken hangi hafta içi günlerin sayılacağını tanımlar.
   * **Ayrıntı:**\
     Kullanıcılar belirli hafta içi günleri (örneğin Pazartesiden Cumaya) seçebilir. Tolerans penceresi hesaplanırken yalnızca seçilen günler dahil edilir.

### İşlevsellik:

* **Koşul Değerlendirmesi:** Sistem, yapılandırılan **Tolerans Günleri** ve **İzin Verilen Tolerans Günleri**'ne dayanarak satınalma siparişi vaat edilen teslimat tarihi etrafında bir tolerans penceresi hesaplar.\
  Ardından her satır öğesinin vaat edilen teslimat tarihi seçilen operatör kullanılarak bu pencereyle karşılaştırılır.
* Eylem Yürütme:
  * **Doğru Koşul:** Teslimat tarihi farkı tolerans aralığında ise ve operatör tarafından ayarlanan koşulla eşleşiyorsa, iş akışı ilerler.
  * **Yanlış Koşul:** Koşul karşılanmazsa, iş akışı devam etmez.

### Kurulum ve Yapılandırma:

* Uygun karşılaştırma operatörünü seçin.
* Tolerans günlerinin sayısını girin.
* Hangi hafta içi günlerin tolerans günleri olarak sayılacağını seçin.

### Sonuç:

**Compare with Purchase Order – Promised Delivery Date for Line Items** iş akışı kartı, teslimat tarihi kurallarını uygulamak için esnek bir yol sunar. Operatörleri hafta içi farkındalıklı tolerans işlemesiyle birleştirerek, manuel kontrolleri ve istisnaları azaltırken teslimat taahhütlerinin hassas doğrulanmasını mümkün kılar.
