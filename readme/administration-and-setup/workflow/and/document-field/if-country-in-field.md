# If Country in Field

<figure><img src="../../../../.gitbook/assets/image (13) (1) (1) (1) (1).png" alt="" width="563"><figcaption></figcaption></figure>

## **Amaç:**

Bu iş akışı kartı, belirlenmiş bir alanda bulunan belirtilen bir ülkenin belirli bir ticaret veya siyasi alanın (Avrupa Birliği, Schengen Bölgesi veya NAFTA) parçası olup olmadığını değerlendirmek için tasarlanmıştır. Bu değerlendirmeye dayanarak, iş akışı doğru veya yanlış koşulla devam edebilir ve sistem içinde başka eylemlere olanak tanır. Özellikle bölgeye özgü iş kurallarını otomatikleştirmek, uyumluluğu sağlamak veya coğrafi bağlantılara dayalı belirli iş akışlarını tetiklemek için yararlıdır.

## **Kartın Bileşenleri:**

1. **Alan Adı (Field Name)**
   * **Açıklama:** Ülke adının veya kodunun depolandığı belge alanını belirtir.
   * **Ayrıntı:** Bu, belge içindeki ülke verisinin tam alan tanımlayıcısıyla eşleşmelidir.&#x20;
2. **Operatör**
   * **Açıklama:** Seçilen alandaki ülkenin seçilen bölge veya anlaşmayla eşleşmesi mi yoksa eşleşmemesi mi gerektiğini belirtir.
   * **Seçenekler:**
     * **Is:** Koşulun doğru olması için ülke seçilen anlaşmanın (EU, Schengen veya NAFTA) parçası olmalıdır.
     * **Is Not:** Koşulun doğru olması için ülke seçilen anlaşmanın parçası olmamalıdır.
3. **Ülke Karşılaştırması**
   * **Açıklama:** Alandaki ülkenin belirli bir siyasi veya ticari anlaşmaya karşı kontrol edilip edilmeyeceğini tanımlar.
   * **Seçenekler:**
     * **Avrupa Birliği:** Kart, ülkenin Avrupa Birliği üyesi olup olmadığını kontrol eder.
     * **Schengen Bölgesi:** Kart, ülkenin Schengen Bölgesinin parçası olup olmadığını kontrol eder.
     * **NAFTA:** Kart, ülkenin NAFTA anlaşmasının üyesi olup olmadığını kontrol eder.
4. **Boolean**
   * **Açıklama:** Karşılaştırmanın sonucunu tanımlar. Ülke koşulu karşılarsa, iş akışı belirtilen Boolean değeriyle devam eder.
   * **Seçenekler:**
     * **True:** Koşul eşleşirse iş akışı devam eder.
     * **False:** Koşul eşleşmezse iş akışı devam eder.

## **İşlevsellik:**

* **Koşul Değerlendirmesi:**
  * Sistem, seçilen operatöre dayanarak alanda belirtilen ülkenin seçilen bölge veya anlaşmanın (EU, Schengen Bölgesi veya NAFTA) parçası olup olmadığını değerlendirir. Bu değerlendirme, ülke adını veya kodunu her ilgili gruba ait önceden tanımlanmış ülke listesine karşı kontrol eder.
* **Eylem Yürütme:**
  * **Doğru Koşul:** Alandaki ülke seçilen bölgeyle eşleşirse (operatöre göre), iş akışı belirtilen doğru koşulla devam eder. Bu, belgeleri yönlendirme, özel işleme kuralları uygulama veya bölgeye özgü özellikleri etkinleştirme gibi başka eylemleri tetikleyebilir.
  * **Yanlış Koşul:** Ülke seçilen bölgeyle eşleşmezse (operatöre göre), iş akışı belirtilen yanlış koşulla devam eder ve sistem kurulumuna bağlı olarak alternatif eylemlerin yürütülmesine veya iş akışının sonlandırılmasına olanak tanır.

## **Kurulum ve Yapılandırma:**&#x20;

* Kullanıcılar, ülkeyi içeren belge alanını seçerek ve bölgeyi (Avrupa Birliği, Schengen Bölgesi veya NAFTA) belirterek kartı yapılandırır. Ardından, ülkenin seçilen bölgenin parçası olması ya da olmaması gerektiğini tanımlamak için operatör bir açılır listeden seçilir. Son olarak, kullanıcılar iş akışındaki sonraki adımı belirleyen devam koşulunu (doğru veya yanlış) ayarlar.

## **Sonuç:**

"Country in Field Comparison" iş akışı kartı, ticaret anlaşmalarına uyumluluk veya siyasi bağlantılar gibi coğrafi kurallara bağlı süreçleri otomatikleştirmek için temel bir araçtır. Ülke verilerini Avrupa Birliği, Schengen Bölgesi veya NAFTA gibi belirli bölgelerle karşılaştırarak, bu kart sistemin doğru işleme mantığını uygulamasını sağlar, verimliliği artırır ve coğrafi koşullara dayalı doğru iş akışı yürütmesini sağlar.
