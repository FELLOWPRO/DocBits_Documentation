# Items Have Shelf Life

<figure><img src="../../../../.gitbook/assets/image (44).png" alt="" width="563"><figcaption></figcaption></figure>

## **Amaç:**

Bu DocBits kartı, bir veri kümesindeki öğelerin raf ömürlerine göre belirtilen koşulları karşılayıp karşılamadığını doğrular. Kart, kullanıcıların doğrulama için "herhangi bir" veya "tüm" öğeler arasından seçim yapmasına olanak tanır ve çeşitli karşılaştırma operatörlerini destekler. Bu, kalite kontrolü, envanter yönetimi veya uyumluluk kontrolleri gibi iş akışı kararlarının öğelerin raf ömrüne bağlı olduğu senaryolar için idealdir.

## **İşlevsellik:**

* **Raf Ömrü Doğrulaması:** Bu kart, öğelerin raf ömrünü belirtilen bir koşula karşı kontrol eder. Kullanıcılar, veri kümesindeki **herhangi bir** öğeyi veya **tüm** öğeleri doğrulamayı seçebilir ve koşulu tanımlamak için çeşitli karşılaştırma operatörleri uygulayabilir.
* **Öğe Seçimi:** Kullanıcılar şunlar arasından seçim yapabilir:
  * **Herhangi Bir Öğe:** En az bir öğe belirtilen raf ömrü koşulunu karşılarsa kart tetiklenir.
  * **Tüm Öğeler:** Yalnızca tüm öğeler belirtilen raf ömrü koşulunu karşılarsa kart tetiklenir.
* **Operatörler:** Raf ömrü koşulunu ayarlamak için aşağıdaki operatörler kullanılabilir:
  * **Eşittir (=):** Raf ömrünün belirtilen değere tam olarak eşit olup olmadığını kontrol eder.
  * **Eşit Değildir (≠):** Raf ömrünün belirtilen değere eşit olmadığını garanti eder.
  * **Büyüktür (>):** Raf ömrünün belirtilen değerden büyük olduğunu doğrular.
  * **Büyük veya Eşittir (≥):** Raf ömrünün belirtilen değere eşit veya ondan büyük olduğunu garanti eder.
  * **Küçüktür (<):** Raf ömrünün belirtilen değerden küçük olup olmadığını kontrol eder.
  * **Küçük veya Eşittir (≤):** Raf ömrünün belirtilen değere eşit veya ondan küçük olduğunu garanti eder.



## **Kullanım:**

Bu kart, başka eylemler veya iş akışlarıyla devam etmeden önce öğelerin belirli raf ömrü gereksinimlerini karşıladığından emin olması gereken kalite kontrol ekipleri, envanter yöneticileri veya uyumluluk yetkilileri için uygundur.

## **Örnek Senaryo:**

* Bir kullanıcı, **tüm öğelerin** raf ömrünün **30 günden büyük veya eşit** olup olmadığını kontrol etmek için kartı yapılandırır. Her öğe bu koşulu karşılarsa, iş akışı ilerler ve tüm öğelerin satış veya dağıtım için yeterli raf ömrüne sahip olduğunu onaylar.

"Shelf Life Validation" kartını kullanarak kuruluşlar, raf ömrü standartlarını uygulayabilir, ürün kalitesini koruyabilir ve öğe raf ömrü koşullarına dayalı iş akışı doğruluğunu sağlayabilir.
