# Satın Alma Siparişinin Sipariş Türü

<figure><img src="../../../../.gitbook/assets/image (277).png" alt="" width="563"><figcaption></figcaption></figure>

## **Amaç:**

Bu iş akışı kartı, bir satın alma siparişinin sipariş türünü belirtilen bir değerle karşılaştırmak için tasarlanmıştır. Kart, satın alma siparişinin sipariş türünün belirtilen koşulu (örneğin, eşit olup olmadığı, eşit olmadığı, daha büyük olup olmadığı veya başka bir koşulu karşılayıp karşılamadığı) karşılayıp karşılamadığını kontrol ederek satın alma siparişinin doğru sınıflandırılmasını sağlar. Bu karşılaştırma, tutarsızlıklar bulunursa siparişin daha fazla inceleme veya onay için yönlendirilmesi gibi belirli koşullara dayalı eylemleri tetikleyebilir.

## **Kartın Bileşenleri:**

1. **Herhangi biri/Tümü (Any/All):**
   * **Açıklama**: Koşulun iş akışında değerlendirilen herhangi bir satın alma siparişi için mi yoksa tümü için mi geçerli olduğunu tanımlar.
   * **Seçenekler**:
     * **Herhangi biri (Any)**: Satın alma siparişlerinden herhangi biri belirtilen koşulla eşleşirse koşul karşılanır.
     * **Tümü (All)**: Koşul yalnızca tüm satın alma siparişleri belirtilen koşulu karşılıyorsa karşılanır.
2. **Operatör:**
   * **Açıklama**: Sipariş türünü belirtilen bir değerle karşılaştırmak için uygulanacak koşulu tanımlar.
   * **Seçenekler**:
     * **Eşittir (=)**: Sipariş türünün belirtilen değerle eşleşip eşleşmediğini kontrol eder.
     * **Eşit Değildir (≠)**: Sipariş türünün belirtilen değerden farklı olmasını sağlar.
3. **Sipariş Türü:**
   * **Açıklama**: Satın alma siparişinin sipariş türünün karşılaştırılacağı değeri belirtir.
   * **Detay**: Değer, sistemdeki sipariş türü veya sınıflandırmasıyla eşleşmelidir.

## **İşlevsellik:**

* **Koşul Değerlendirmesi:** Sistem, seçilen operatörü kullanarak satın alma siparişinin sipariş türünü belirtilen koşula göre değerlendirir. Sipariş türü belirtilen değerle eşleşirse (veya eşleşmezse), iş akışı buna göre devam eder.
* **Eylem Yürütme:**
  * **Doğru Koşul**: Koşul doğru olarak değerlendirilirse (örneğin, sipariş türü belirtilen değerle eşleşirse), iş akışı muhtemelen ek eylemleri veya işleme adımlarını tetikleyerek devam edecektir.
  * **Yanlış Koşul**: Koşul yanlış olarak değerlendirilirse (örneğin, sipariş türü belirtilen değerle eşleşmiyorsa), iş akışı devam etmeyecektir.

## **Kurulum ve Yapılandırma:**

* Kullanıcılar, satın alma siparişinin sipariş türü alanını seçerek ve sipariş türünün nasıl karşılaştırılacağını tanımlayan operatörü seçerek kartı yapılandırır. Ardından, belirtilen değeri ayarlarlar ve koşulun satın alma siparişi satırlarının herhangi birine mi yoksa tümüne mi uygulanacağına karar verirler.

## **Örnek Senaryo:**

* Bir satın alma siparişinin sipariş türü "Standart"tır. İş akışı, sipariş türünün "Acil" olup olmadığını kontrol edecek şekilde yapılandırılmıştır. "Eşittir" operatörünü kullanan kart, sipariş türünü karşılaştırır ve belirtilen değerle eşleşmediğini bulur; bu da uyuşmazlık nedeniyle siparişin inceleme için gönderilmesi için iş akışını tetikler.

## **Sonuç:**

"Satın Alma Siparişinin Sipariş Türü" iş akışı kartı, satın alma siparişlerinin belirtilen sipariş türlerine göre doğru şekilde sınıflandırılmasını sağlar. Sipariş türlerinin karşılaştırılmasını otomatikleştirerek kuruluşlar, satın alma siparişlerinin beklenen sınıflandırmalarına göre işlenmesini sağlayabilir ve bu da uyumluluğu zorunlu kılmaya ve satın alma iş akışlarını kolaylaştırmaya yardımcı olur.
