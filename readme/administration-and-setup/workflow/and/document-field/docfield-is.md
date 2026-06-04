# Docfield is

<figure><img src="../../../../.gitbook/assets/image (8) (1) (1) (1) (1) (2).png" alt="" width="563"><figcaption></figcaption></figure>

## **Amaç:**

Bu iş akışı kartı, belirtilen bir belge alanının değerini bir referans değer veya koşulla karşılaştırarak eylemleri otomatikleştirmek için tasarlanmıştır. Belge verisi doğrulamasına dayalı olarak iş akışlarında dinamik ve doğru karar vermeyi sağlar.

## **Kartın Bileşenleri:**

1. **Alan Adı (Field Name)**
   * **Açıklama:** Değerlendirilecek belge alanının adını belirtir.
   * **Ayrıntı:** Bu, belge içindeki alanın tam tanımlayıcısıyla eşleşmelidir.
2. **Operatörler**
   * **Açıklama:** Alan değeri ile referans değeri arasında gerçekleştirilecek karşılaştırma türünü tanımlar.
   * **Seçenekler:**
     * **Eşittir (=):** Alan değerinin referans değeriyle eşleşip eşleşmediğini kontrol eder.
     * **Eşit Değildir (≠):** Alan değerinin referans değerinden farklı olduğunu garanti eder.
     * **Büyüktür (>):** Alan değerinin referans değerinden büyük olduğunu doğrular.
     * **Büyük veya Eşittir (≥):** Alan değerinin referans değerine eşit veya ondan büyük olduğunu doğrular.
     * **Küçüktür (<):** Alan değerinin referans değerinden küçük olup olmadığını kontrol eder.
     * **Küçük veya Eşittir (≤):** Alan değerinin referans değerine eşit veya ondan küçük olduğunu garanti eder.

## **İşlevsellik:**

* **Koşul Değerlendirmesi:** Sistem, belge alanının değerinin, ilişkili sütununa göre, operatör ve referans değeri tarafından belirtilen karşılaştırma koşulunu karşılayıp karşılamadığını kontrol eder.
* **Eylem Yürütme:**
  * **Doğru Koşul:**\
    Belge alanının değeri belirtilen koşulu karşılarsa (örn. referans değerine eşitse), sistem ilişkili eylemleri tetikler. Bunlar, kayıtları güncelleme, iş akışını ilerletme veya bildirimler oluşturmayı içerebilir.
  * **Yanlış Koşul:**\
    Belge alanının değeri belirtilen koşulu karşılamazsa, iş akışı yapılandırmasına bağlı olarak alternatif eylemler veya hiçbir eylem yürütülür.

## **Kurulum ve Yapılandırma:**

* Kullanıcı, ilgili belgenin alan adını seçer ve açılır menüden operatörü seçer. Ardından kullanıcı, yapılandırmayı tamamlamak için referans alan değerini belirtir.

## **Sonuç:**

"DocField Comparison Validation" iş akışı kartı, dinamik belge işleme için sağlam bir araçtır. Alan karşılaştırmalarına dayalı eylemleri otomatikleştirerek, bu kart iş akışlarını kolaylaştırır, doğruluğu artırır ve veri odaklı karar vermeyi destekler.
