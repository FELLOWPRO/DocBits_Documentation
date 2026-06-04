# Compare two Fields with Tolerance

<figure><img src="../../../../.gitbook/assets/image (12) (1) (1) (1) (1).png" alt="" width="563"><figcaption></figcaption></figure>

## **Amaç:**

Bu iş akışı kartı, belirtilen iki belge alanının değerlerini karşılaştırarak ve bir tolerans değeri uygulama özelliğini ekleyerek eylemleri otomatikleştirmek için tasarlanmıştır. Bu özellik, sistemin alan değerlerini karşılaştırırken bir hata payını (tolerans) dikkate almasına olanak tanır ve iş akışları içinde daha esnek karar verme sağlar.

## **Kartın Bileşenleri:**

1. **Alan Adı (1) (Field Name)**
   * **Açıklama:** Karşılaştırılacak ilk belge alanını belirtir.
   * **Ayrıntı:** Bu, belge içindeki ilk alanın tam tanımlayıcısıyla eşleşmelidir.
2. **Operatör**
   * **Açıklama:** İki alan arasında gerçekleştirilecek karşılaştırma türünü tanımlar.
   * **Seçenekler:**
     * **Eşittir (=):** İki alanın değerlerinin eşit olup olmadığını kontrol eder.
     * **Eşit Değildir (≠):** İki alanın değerlerinin farklı olduğunu garanti eder.
     * **Büyüktür (>):** İlk alanın değerinin ikinci alandan büyük olduğunu doğrular.
     * **Büyük veya Eşittir (≥):** İlk alanın değerinin ikinci alana eşit veya ondan büyük olduğunu doğrular.
     * **Küçüktür (<):** İlk alanın değerinin ikinci alandan küçük olup olmadığını kontrol eder.
     * **Küçük veya Eşittir (≤):** İlk alanın değerinin ikinci alana eşit veya ondan küçük olduğunu garanti eder.
3. **Alan Adı (2) (Field Name)**
   * **Açıklama:** İlk alana karşı karşılaştırılacak ikinci belge alanını belirtir.
   * **Ayrıntı:** Bu, belge içindeki ikinci alanın tam tanımlayıcısıyla eşleşmelidir.&#x20;
4. **Tolerans Miktarı**
   * **Açıklama:** Karşılaştırma için kabul edilebilir hata payını tanımlar.
   * **Ayrıntı:** Tolerans miktarı, karşılaştırmanın doğru kabul edilmesi için iki alan değeri arasındaki izin verilen maksimum farkı gösteren sayısal bir değerdir.
5. **Tolerans Türü**
   * **Açıklama:** Tolerans miktarı için ölçü birimini belirtir.
   * **Seçenekler:**
     * **Değer (Value):** Tolerans mutlak bir değerdir, yani iki alan belirtilen tolerans miktarı kadar farklılaşabilir.
     * **Yüzde (Percent):** Tolerans, ikinci alan değerinin bir yüzdesi olarak hesaplanır ve göreceli bir hata payına olanak tanır.

## **İşlevsellik:**

* **Koşul Değerlendirmesi:** Sistem, tanımlanan toleransı dikkate alarak belirtilen iki alandaki değerlerin karşılaştırma koşulunu karşılayıp karşılamadığını değerlendirir. İki alan arasındaki mutlak veya göreceli fark tolerans içine düşerse, koşul doğru kabul edilir.
* **Eylem Yürütme:**
  * **Doğru Koşul:**\
    İki alanın değerleri, tolerans dikkate alındıktan sonra, karşılaştırma koşuluyla eşleşirse, sistem ilişkili eylemleri tetikler. Bu eylemler, iş akışını ilerletme, kayıtları güncelleme, uyarıları tetikleme veya belirli işlemleri etkinleştirmeyi içerebilir.
  * **Yanlış Koşul:**\
    İki alanın değerleri, tolerans dikkate alındıktan sonra, belirtilen koşulla eşleşmezse, iş akışının yapılandırmasına bağlı olarak alternatif eylemler veya hiçbir eylem yürütülebilir.

## **Kurulum ve Yapılandırma:**

* Kullanıcılar, sistemdeki kullanılabilir alanlar listesinden karşılaştırılacak iki alanı seçerek kartı yapılandırır. Operatör, kullanılabilir karşılaştırma seçeneklerinin açılır listesinden seçilir. Kullanıcılar tolerans miktarını girer ve tolerans türünü (değer veya yüzde) seçer.&#x20;

## **Sonuç:**

"Compare Two Fields with Tolerance" iş akışı kartı, verilerdeki izin verilen sapmaları hesaba katarak belge alanlarını karşılaştırmak için güçlü bir araçtır. Alan karşılaştırmalarına tolerans uygulayarak, bu kart iş akışına esneklik katar ve gerçek dünya veri değişimlerini ele almasını sağlar. Karar vermeyi iyileştirir, veri doğrulamayı destekler ve genel iş akışı otomasyonunu artırır.
