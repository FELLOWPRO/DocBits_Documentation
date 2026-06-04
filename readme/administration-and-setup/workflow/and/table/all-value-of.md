# All Value of

<figure><img src="../../../../.gitbook/assets/image (45).png" alt="" width="563"><figcaption></figcaption></figure>

## **Amaç:**

Bu DocBits kartı, bir tablonun belirli bir sütunundaki **tüm değerlerin** sağlanan bir regex kalıbıyla eşleşip eşleşmediğini doğrulamak için kullanılır. İş akışının devam etmesi için, sütundaki her girişin koşulu karşılaması gerekir, bu da bu kartı tüm girişler arasında tutarlılık ve veri bütünlüğü sağlamak için ideal kılar.

## **İşlevsellik:**

* **Regex Kalıbı Doğrulaması:** Bu kart, bir tablonun belirtilen bir sütunundaki **tüm değerlerin** sağlanan düzenli ifade kalıbıyla eşleştiğini kontrol eder. İş akışı yalnızca sütundaki her giriş koşulu karşılarsa ilerler.
* **Operatör:** Kullanıcılar sütunu tanımlar ve regex kalıbını belirtir. Kullanılabilir koşul şunları içerir:
  * **Regex Kalıbıyla Eşleşir:** Belirtilen sütundaki her değerin regex kalıbıyla eşleştiğini doğrular.
* **Tablo ve Sütun Seçimi:** Kullanıcılar, eksiksiz regex kalıbı eşleşmeleri için kontrol etmek istedikleri tabloyu ve sütunu belirtir.

## **Kullanım:**

Bu kart, tüm telefon numaralarının, ürün kimliklerinin veya diğer alan girişlerinin belirli bir biçime uymasını sağlama gibi veri tekdüzeliğinin gerektiği durumlar için idealdir. İş akışlarının yalnızca her ilgili giriş kalıpla tutarlı olduğunda ilerlemesini sağlar.

## **Örnek Senaryo:**

* Bir kullanıcı, telefon numarası biçimlerini doğrulamak için bir regex kalıbı kullanarak "Contacts" tablosundaki "Phone Number" sütununu kontrol edecek şekilde kartı ayarlar. Sütundaki her telefon numarası girişi kalıpla eşleşirse, kart iş akışındaki bir sonraki adımı tetikler ve tekdüze veri biçimlendirmesini onaylar.

"All Values Regex Pattern Matching" kartını kullanarak kuruluşlar, sıkı veri standartlarını uygulayabilir ve iş akışı doğruluğunu artırabilir, böylece belirtilen bir sütundaki her girişin devam etmeden önce gerekli biçimi karşılamasını sağlar.
