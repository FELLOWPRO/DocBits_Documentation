# Compare two Fields

<figure><img src="../../../../.gitbook/assets/image (11) (1) (1) (1) (1).png" alt="" width="563"><figcaption></figcaption></figure>

## **Amaç:**

Bu iş akışı kartı, belirtilen iki belge alanının değerlerini karşılaştırarak eylemleri otomatikleştirmek için tasarlanmıştır. Alan verilerine dayalı dinamik karar vermeyi sağlar ve iş akışlarının farklı belge değerleri arasındaki karşılaştırmalara göre yürütülmesini sağlar.

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
   * **Ayrıntı:** Bu, belge içindeki ikinci alanın tam tanımlayıcısıyla eşleşmelidir.

## **İşlevsellik:**

**Koşul Değerlendirmesi:** Sistem, belirtilen iki alandaki değerlerin operatör tarafından tanımlanan karşılaştırma koşulunu karşılayıp karşılamadığını değerlendirir.

**Eylem Yürütme:**

* **Doğru Koşul:**\
  İki alanın değerleri karşılaştırma koşuluyla eşleşirse, sistem ilişkili eylemleri tetikler. Bu eylemler, kayıtları güncellemeyi veya uyarıları tetiklemeyi içerebilir.
* **Yanlış Koşul:**\
  İki alanın değerleri belirtilen koşulla eşleşmezse, iş akışlarının yapılandırmasına bağlı olarak alternatif eylemler veya hiçbir eylem yürütülebilir.

## **Kurulum ve Yapılandırma:**&#x20;

* Kullanıcılar, sistemdeki kullanılabilir alanlar listesinden karşılaştırılacak iki alanı seçerek kartı yapılandırır. Operatör, kullanılabilir karşılaştırma seçeneklerinin açılır listesinden seçilir.

## **Sonuç:**

"Compare Two Fields" iş akışı kartı, belgeler içindeki alanlar arasında veri karşılaştırmak için temel bir araçtır. Alan karşılaştırmalarına dayalı eylemleri otomatikleştirerek, bu kart karar vermeyi optimize etmeye yardımcı olur, veri doğrulamayı destekler ve iş akışı otomasyonunu artırır.
