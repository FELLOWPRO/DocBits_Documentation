# Order Type of Purchase Order

<figure><img src="../../../../.gitbook/assets/image (277).png" alt="" width="563"><figcaption></figcaption></figure>

## **Amaç:**

Bu iş akışı kartı, bir satınalma siparişinin sipariş türünü belirtilen bir değere karşı karşılaştırmak için tasarlanmıştır. Kart, satınalma siparişinin doğru şekilde sınıflandırıldığından emin olmak için satınalma siparişinin sipariş türünün belirtilen koşulu karşılayıp karşılamadığını (örn. eşit mi, eşit değil mi, büyük mü veya başka bir koşulu karşılıyor mu) kontrol eder. Bu karşılaştırma, tutarsızlıklar bulunursa siparişi daha fazla inceleme veya onay için yönlendirme gibi belirli koşullara dayalı eylemleri tetikleyebilir.

## **Kartın Bileşenleri:**

1. **Any/All:**
   * **Açıklama**: Koşulun iş akışında değerlendirilen herhangi bir veya tüm satınalma siparişlerine uygulanıp uygulanmayacağını tanımlar.
   * **Seçenekler**:
     * **Any**: Satınalma siparişlerinden herhangi biri belirtilen koşulu karşılarsa koşul karşılanır.
     * **All**: Yalnızca satınalma siparişlerinin tümü belirtilen koşulu karşılarsa koşul karşılanır.
2. **Operatör:**
   * **Açıklama**: Sipariş türünü belirtilen bir değere karşı karşılaştırmak için uygulanacak koşulu tanımlar.
   * **Seçenekler**:
     * **Eşittir (=)**: Sipariş türünün belirtilen değerle eşleşip eşleşmediğini kontrol eder.
     * **Eşit Değildir (≠)**: Sipariş türünün belirtilen değerden farklı olduğunu garanti eder.
3. **Sipariş Türü (Order Type):**
   * **Açıklama**: Satınalma siparişinin sipariş türünün karşılaştırılacağı değeri belirtir.
   * **Ayrıntı**: Değer, sistemdeki sipariş türüyle veya sınıflandırmayla eşleşmelidir.

## **İşlevsellik:**

* **Koşul Değerlendirmesi:** Sistem, seçilen operatörü kullanarak satınalma siparişinin sipariş türünü belirtilen koşula karşı değerlendirir. Sipariş türü belirtilen değerle eşleşirse (veya eşleşmezse), iş akışı buna göre ilerler.
* **Eylem Yürütme:**
  * **Doğru Koşul**: Koşul doğru olarak değerlendirilirse (örn. sipariş türü belirtilen değerle eşleşirse), iş akışı devam eder ve muhtemelen ek eylemler veya işleme adımları tetikler.
  * **Yanlış Koşul**: Koşul yanlış olarak değerlendirilirse (örn. sipariş türü belirtilen değerle eşleşmezse), iş akışı devam etmez.

## **Kurulum ve Yapılandırma:**

* Kullanıcılar, satınalma siparişinin sipariş türü alanını seçerek ve sipariş türünün nasıl karşılaştırılacağını tanımlayan operatörü seçerek kartı yapılandırır. Ardından, belirtilen değeri ayarlar ve koşulu satınalma siparişi satırlarının herhangi birine veya tümüne uygulayıp uygulamayacağına karar verirler.

## **Örnek Senaryo:**

* Bir satınalma siparişinin sipariş türü "Standard"dır. İş akışı, sipariş türünün "Urgent" olup olmadığını kontrol edecek şekilde yapılandırılmıştır. "Eşittir" operatörünü kullanarak, kart sipariş türünü karşılaştırır ve belirtilen değerle eşleşmediğini bulur, bu da iş akışını uyuşmazlık nedeniyle siparişi inceleme için göndermeye tetikler.

## **Sonuç:**

"Order Type of Purchase Order" iş akışı kartı, satınalma siparişlerinin belirtilen sipariş türlerine göre doğru şekilde sınıflandırılmasını sağlar. Sipariş türlerinin karşılaştırmasını otomatikleştirerek, kuruluşlar satınalma siparişlerinin beklenen sınıflandırmalarına göre işlenmesini sağlayabilir, bu da uyumluluğu uygulamaya ve satınalma iş akışlarını kolaylaştırmaya yardımcı olur.
