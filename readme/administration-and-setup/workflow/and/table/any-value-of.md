# Any Value of

<figure><img src="../../../../.gitbook/assets/image (46).png" alt="" width="563"><figcaption></figcaption></figure>

## **Amaç:**

Bu DocBits kartı, bir tablonun belirli bir sütunundaki herhangi bir değerin sağlanan bir regex kalıbıyla eşleşip eşleşmediğini doğrulamak için kullanılır. Sütundaki herhangi bir tek giriş kalıpla eşleşirse, iş akışı devam eder, bu da tek bir eşleşmenin bile tanımlanmasının süreçteki sonraki adımları tetiklediği kullanım durumları için ideal kılar.

## **İşlevsellik:**

* **Regex Kalıbı Doğrulaması:** Bu kart, bir tablonun belirli bir sütunundaki herhangi bir değerin sağlanan düzenli ifade kalıbıyla eşleşip eşleşmediğini kontrol eder. Sütundaki en az bir giriş koşulu karşılarsa, kart tetiklenir ve iş akışının devam etmesine izin verir.
* **Operatör:** Kullanıcılar sütunu tanımlar ve regex kalıbını belirtir. Kullanılabilir koşul şunları içerir:
  * **Regex Kalıbıyla Eşleşir:** Belirtilen sütundaki en az bir değerin regex kalıbıyla eşleştiğini doğrular.
* **Tablo ve Sütun Seçimi:** Kullanıcılar, regex kalıbı eşleşmeleri için kontrol etmek istedikleri tabloyu ve sütunu belirtir.

## **Kullanım:**

Bu kart, özellikle bir tablonun e-posta adreslerini, fatura numaralarını veya ürün kimliklerini doğrulama gibi belirli eşleşmeler gerektirebilecek veriler içerdiği senaryolar için yararlıdır. Her girişi kontrol etmeye gerek kalmadan, herhangi bir ilgili giriş tanımlanan kalıpla eşleştiğinde iş akışlarının ilerlemesini sağlar.

## **Örnek Senaryo:**

* Bir kullanıcı, geçerli e-posta biçimleri için bir regex kalıbı kullanarak "Customers" tablosunun "Email Address" sütunundaki girişleri kontrol edecek şekilde kartı ayarlar. Sütundaki en az bir e-posta adresi kalıpla eşleşirse, kart bir sonraki iş akışı adımını tetikler ve sistemin geçerli girişi işlemesini sağlar.

"Regex Pattern Matching" kartını kullanarak kuruluşlar, dinamik, kalıp tabanlı doğrulamalara dayalı iş akışlarını otomatikleştirebilir, süreçleri kolaylaştırabilir ve yalnızca ilgili girişlerin başka eylemleri tetiklemesini sağlayabilir.
