# Compare Field with tolerances

<figure><img src="../../../../.gitbook/assets/image (15) (1) (1).png" alt="" width="563"><figcaption></figcaption></figure>

## **Amaç:**

Bu iş akışı kartı, bir alanın değerini belirtilen bir referans değerle, toleranslara izin vererek karşılaştırmak için tasarlanmıştır. Küçük sapmaların kabul edilebilir olduğu iş akışlarında hassas koşullu işlemeyi sağlar, bu da onu kalite güvencesi, finansal analiz veya eşik tabanlı eylemler gibi senaryolar için ideal kılar.

## **Kartın Bileşenleri:**

1. **Alan Adı (Field Name)**
   * **Açıklama:** Karşılaştırmada değerlendirilecek alan.
   * **Ayrıntı:** Bu, belge içindeki ilk alanın tam tanımlayıcısıyla eşleşmelidir.
2. **Karşılaştırma Operatörü**
   * **Açıklama:** Seçilen alan değerinin referans değeriyle nasıl karşılaştırılacağını belirtir.
   * **Seçenekler:**
     * **Eşittir (=):** Alan değerinin referans değeriyle tam olarak eşleşip eşleşmediğini doğrular.
     * **Eşit Değildir (≠):** Alan değerinin referans değeriyle eşleşmediğini doğrular.
     * **Büyüktür (>):** Alan değerinin referans değerinden büyük olup olmadığını kontrol eder.
     * **Büyük veya Eşittir (≥):** Alan değerinin referans değerine eşit veya ondan büyük olup olmadığını kontrol eder.
     * **Küçüktür (<):** Alan değerinin referans değerinden küçük olup olmadığını kontrol eder.
     * **Küçük veya Eşittir (≤):** Alan değerinin referans değerine eşit veya ondan küçük olup olmadığını kontrol eder.
3. **Referans Değer**
   * **Açıklama:** Alanın karşılaştırıldığı değer.
   * **Ayrıntı:** Bu değer, karşılaştırmanın bağlamına bağlı olarak sayısal, metin veya tarih tabanlı olabilir.
4. **Tolerans Miktarı**
   * **Açıklama:** Karşılaştırma için kabul edilebilir hata payını tanımlar.
   * **Ayrıntı:** Tolerans miktarı, karşılaştırmanın doğru kabul edilmesi için iki alan değeri arasındaki izin verilen maksimum farkı gösteren sayısal bir değerdir.
5. **Tolerans Türü**
   * **Açıklama:** Tolerans miktarı için ölçü birimini belirtir.
   * **Seçenekler:**
     * **Değer (Value):** Tolerans mutlak bir değerdir, yani iki alan belirtilen tolerans miktarı kadar farklılaşabilir.
     * **Yüzde (Percent):** Tolerans, ikinci alan değerinin bir yüzdesi olarak hesaplanır ve göreceli bir hata payına olanak tanır.

## **İşlevsellik:**

* **Koşul Değerlendirmesi:** Sistem, seçilen karşılaştırma operatörünü kullanarak alanın değerini referans değerine karşı değerlendirir. Bir tolerans yapılandırılmışsa, sistem alan değeri tanımlanan tolerans aralığına düşerse karşılaştırmayı başarılı sayar.
* **Eylem Yürütme:**
  * **Tolerans İçinde:** Alan değeri belirtilen tolerans içinde koşulu karşılarsa, iş akışı devam eder ve ilişkili eylemleri tetikler.
  * **Tolerans Dışında:** Alan değeri koşulu karşılamazsa veya tolerans aralığının dışına düşerse, günlüğe kaydetme, uyarı gönderme veya iş akışını durdurma gibi alternatif eylemler yürütülebilir.

## **Kurulum ve Yapılandırma:**

* Kullanıcılar, kullanılabilir alanlar listesinden değerlendirilecek alanı seçerek ve açılır listeden karşılaştırma operatörünü (örn. eşittir, büyüktür) seçerek kartı yapılandırır. Ardından, karşılaştırılacak referans değerini belirtir ve tolerans miktarını tanımlar, sonra tolerans türünü (örn. yüzde veya değer) seçerler.&#x20;

## **Sonuç:**

"Field Comparison with Tolerances" kartı, esnek değerlendirmeler gerektiren iş akışları için çok yönlü bir araçtır. Toleranslarla karşılaştırmalar yapılmasına olanak tanıyarak, iş akışlarının verimli ve uyarlanabilir kalmasını sağlar ve doğruluktan ödün vermeden gerçek dünya değişimlerini karşılar.
