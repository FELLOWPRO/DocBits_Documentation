# Document Type

<figure><img src="../../../../.gitbook/assets/image (16) (1).png" alt="" width="563"><figcaption></figcaption></figure>

## Amaç:

Bu iş akışı kartı, bir belgenin belirli bir türle eşleşip eşleşmediğini değerlendirmek için tasarlanmıştır. Belgenin verilen türe karşılık gelip gelmediğini kontrol ederek, iş akışları bu koşula göre devam edebilir veya alternatif eylemler gerçekleştirebilir. Bu, belge türünün iş akışındaki sonraki adımları belirlediği süreçleri otomatikleştirmeye yardımcı olur.

## Kartın Bileşenleri:

1. **Operatör**
   * **Açıklama**: Belgenin belirtilen türde olup olmaması gerektiğini tanımlar.
   * **Seçenekler**:
     * **Is**: Koşulun doğru olması için belge belirtilen türle eşleşmelidir.
     * **Is Not**: Koşulun doğru olması için belge belirtilen türle eşleşmemelidir.
2. **Tür**
   * **Açıklama**: Karşılaştırılacak belge türünü belirtir.
   * **Ayrıntı**: Bu, koşulun (is/is not) değerlendirileceği "Invoice", "Purchase Order" vb. gibi çeşitli belge türlerini içerir.

## İşlevsellik:

* **Koşul Değerlendirmesi**: Sistem, belirtilen alandaki belge türünün operatör tarafından tanımlanan koşulla eşleşip eşleşmediğini değerlendirir. Alan değerini sağlanan belge türüyle karşılaştırır.
* **Eylem Yürütme**:
  * **Doğru Koşul**: Belge türü belirtilen türle eşleşirse (veya operatöre bağlı olarak eşleşmezse), iş akışı doğru koşulla devam eder. Bu, belgenin daha fazla işlenmesi, onaya gönderilmesi veya belge türüne göre belirli kuralların uygulanması gibi eylemleri tetikleyebilir.
  * **Yanlış Koşul**: Belge türü belirtilen türle eşleşmezse, iş akışı yanlış koşulla devam eder. Bu, belgeyi farklı bir sürece yönlendirme veya daha fazla eylemi durdurma gibi alternatif eylemleri tetikleyebilir.

## Kurulum ve Yapılandırma:

* Kullanıcılar, kullanılabilir alanlar listesinden belge türünü içeren belge alanını seçerek kartı yapılandırır. Ardından, belgenin belirtilen türde olması gerekip gerekmediğini tanımlamak için operatör seçilir. Son olarak, kullanıcılar belge türüne göre sonraki eylemi belirleyen devam koşulunu (doğru veya yanlış) ayarlar.

## Sonuç:

"Document Type Comparison" iş akışı kartı, iş akışlarının işlenmekte olan belge türüne göre ilerlemesini sağlamak için gereklidir. Belge türünü karşılaştırarak, kuruluşların belge yönlendirme ve işleme görevlerini otomatikleştirmesine yardımcı olur ve belgelerin türlerine göre uygun şekilde ele alınmasını sağlar.
