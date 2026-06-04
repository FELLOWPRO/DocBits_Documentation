# Document Operator for Sub-Organizations

<figure><img src="../../../../.gitbook/assets/image (42).png" alt="" width="563"><figcaption></figcaption></figure>

## Amaç:

Bu iş akışı kartı, bir belgenin belirli bir alt kuruluşun parçası olup olmadığını değerlendirir. Bu değerlendirmeye dayanarak, iş akışı, belgenin belirtilen alt kuruluşla ilişkili olup olmamasına bağlı olarak devam edebilir veya farklı eylemler tetikleyebilir.

## Kartın Bileşenleri:

1. **Operatör**
   * **Açıklama:** Belgenin belirtilen alt kuruluşun parçası olup olmaması gerektiğini tanımlar.
   * **Seçenekler:**
     * **Is:** Koşulun doğru olması için belge belirtilen alt kuruluşun parçası olmalıdır.
     * **Is Not:** Koşulun doğru olması için belge belirtilen alt kuruluşun parçası olmamalıdır.
2. **Alt kuruluş (Sub-org)**
   * **Açıklama:** Belgenin karşılaştırılacağı alt kuruluşu belirtir.
   * **Ayrıntı:** Bu, alt kuruluş tanımlayıcısıyla eşleşmelidir. Karşılaştırma, belgenin belirtilen alt kuruluşa ait olup olmadığını kontrol eder.

## İşlevsellik:

* **Koşul Değerlendirmesi:** Sistem, belgenin belirtilen alt kuruluşun parçası olup olmadığını değerlendirir. Bu değerlendirme, belgenin alt kuruluşunu kullanıcı tarafından sağlanana karşı kontrol eder.
* **Eylem Yürütme:**
  * **Doğru Koşul:**\
    Belge belirtilen alt kuruluşun parçasıysa, iş akışı doğru koşulla devam eder. Bu, belgeyi belirli bir departmana yönlendirme, alt kuruluşa özgü kuralları uygulama veya o alt kuruluşa uyarlanmış özellikleri etkinleştirme gibi başka eylemleri tetikleyebilir.
  * **Yanlış Koşul:**\
    Belge belirtilen alt kuruluşun parçası değilse, iş akışı yanlış koşulla devam eder. Bu, bildirim gönderme, iş akışını durdurma veya alt kuruluşun kapsamı dışındaki genel kuralları uygulama gibi alternatif eylemlerin yürütülmesine olanak tanır.

## Kurulum ve Yapılandırma:

* Kullanıcılar, belgeyi içeren belge alanını seçerek ve karşılaştırılacak alt kuruluşu belirterek kartı yapılandırır. Ardından, belgenin belirtilen alt kuruluşun parçası olması ya da olmaması gerektiğini tanımlamak için operatör bir açılır listeden seçilir. Son olarak, kullanıcılar iş akışındaki sonraki adımı belirleyen devam koşulunu (doğru veya yanlış) ayarlar.

## Sonuç:

"Document in Sub-organization" iş akışı kartı, bir belgenin belirli bir alt kuruluşa ait olup olmadığına göre eylemleri otomatikleştirmek için yararlı bir araçtır. Belgelerin alt kuruluşa özgü kurallara göre işlenmesini sağlayarak, bu kart iş akışı verimliliğini artırır ve eylemlerin doğru kurumsal bağlam içinde yürütülmesini sağlar.
