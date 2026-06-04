# If Country in Field is One of

<figure><img src="../../../../.gitbook/assets/image (14) (1) (1).png" alt="" width="563"><figcaption></figcaption></figure>

## **Amaç**

Bu iş akışı kartı, belirlenmiş bir alanda bulunan belirtilen bir ülkenin, önceden tanımlanmış bir ülke listesinin parçası olup olmadığını değerlendirmek için tasarlanmıştır. Bu değerlendirmeye dayanarak, iş akışı doğru veya yanlış koşulla devam edebilir. Eylemlerin, ülkenin izin verilen veya kısıtlanmış bir ülke kümesi arasında listelenip listelenmediğine bağlı olduğu süreçleri otomatikleştirmeye yardımcı olur.

## **Kartın Bileşenleri:**

1. **Alan Adı (Field Name)**
   * **Açıklama:** Ülke adının veya kodunun depolandığı belge alanını belirtir.
   * **Ayrıntı:** Bu, belge içindeki ülke verisinin tam alan tanımlayıcısıyla eşleşmelidir.&#x20;
2. **Operatör**
   * **Açıklama:** Alandaki ülkenin önceden tanımlanmış bir ülke listesinin parçası olması gerekip gerekmediğini tanımlar.
   * **Seçenekler:**
     * **Is:** Koşulun doğru olması için ülke belirtilen ülkeler listesine dahil edilmelidir.
     * **Is Not:** Koşulun doğru olması için ülke belirtilen ülkeler listesine dahil edilmemelidir.
3. **Ülkeler (Countries)**
   * **Açıklama:** Seçilen ülkenin karşılaştırılacağı ülkeler listesini belirtir.
   * **Ayrıntı:** Bu, virgülle ayrılmış bir ülke listesidir. Karşılaştırma, alandaki ülkenin bu listeye dahil olup olmadığını kontrol eder.
4. **Devam Koşulu (Continue Condition)**
   * **Açıklama:** Karşılaştırmanın sonucunu tanımlar. Ülke koşulu karşılarsa, iş akışı belirtilen Boolean değeriyle devam eder.
   * **Seçenekler:**
     * **True:** Koşul eşleşirse iş akışı devam eder.
     * **False:** Koşul eşleşmezse iş akışı devam eder.

## **İşlevsellik:**

* **Koşul Değerlendirmesi:** Sistem, alanda belirtilen ülkenin önceden tanımlanmış ülkeler listesinin parçası olup olmadığını değerlendirir. Bu değerlendirme, ülke adını veya kodunu sağlanan listeye karşı kontrol eder.
* **Eylem Yürütme:**
  * **Doğru Koşul:**\
    Alandaki ülke belirtilen ülkeler listesinin parçasıysa, iş akışı doğru koşulla devam eder. Bu, belgeleri uygun departmana yönlendirme, belirli işleme kurallarını uygulama veya bölgeye özgü özellikleri etkinleştirme gibi başka eylemleri tetikleyebilir.
  * **Yanlış Koşul:**\
    Ülke listeyle eşleşmezse, iş akışı yanlış koşulla devam eder. Bu, sistem kurulumuna bağlı olarak alternatif eylemler yürütmeye veya iş akışını durdurmaya olanak tanır.

## **Kurulum ve Yapılandırma:**

* Kullanıcılar, ülkeyi içeren belge alanını seçerek ve karşılaştırılacak ülkeler listesini belirterek kartı yapılandırır. Ardından, ülkenin belirtilen ülkeler listesinin parçası olması ya da olmaması gerektiğini tanımlamak için operatör bir açılır listeden seçilir. Son olarak, kullanıcılar iş akışındaki sonraki adımı belirleyen devam koşulunu (doğru veya yanlış) ayarlar.

## **Sonuç:**

"Country in Field Comparison with List" iş akışı kartı, bir ülkenin önceden tanımlanmış bir grubun parçası olup olmadığına göre eylemleri otomatikleştirmek için değerli bir araçtır. Ülke verilerini izin verilen veya kısıtlanmış ülkeler listesiyle karşılaştırarak, bu kart iş akışı verimliliğini artırır ve sistem süreçlerinin doğru coğrafi kuralları izlemesini sağlar.
