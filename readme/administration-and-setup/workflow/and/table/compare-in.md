# Compare In

<figure><img src="../../../../.gitbook/assets/image (43).png" alt="" width="563"><figcaption></figcaption></figure>

## **Amaç:**

Bu DocBits kartı, belirtilen bir tablodaki iki sütun arasında bir karşılaştırma gerçekleştirir ve kullanıcıların her sütundaki değerlere göre koşullar ayarlamasına olanak tanır. Ayrıca, bu kart, karşılaştırmanın yalnızca üçüncü bir sütundaki değer belirtilen bir Python regex kalıbıyla eşleşirse gerçekleşeceği bir bağımlılık özelliği içerir. Bu kurulum, bir veri kümesi içindeki birden fazla veri noktasına bağlı koşullu kontroller için yararlıdır.

## **İşlevsellik:**

* **Bağımlılıkla Sütun Karşılaştırması:** Bu kart, yalnızca üçüncü bir "bağımlılık" sütunundaki değer tanımlanan bir Python regex kalıbıyla eşleşirse uygulanan ayarlanmış bir koşula dayanarak belirtilen iki sütundaki değerleri karşılaştırır.
* **Operatörler:** Kullanıcılar sütun karşılaştırması için aşağıdaki operatörleri seçebilir:
  * **Eşittir (=):** İki sütundaki değerlerin tam olarak eşit olup olmadığını kontrol eder.
  * **Eşit Değildir (≠):** İki sütundaki değerlerin eşit olmadığını garanti eder.
  * **Büyüktür (>):** İlk sütundaki değerlerin ikinci sütundakilerden büyük olduğunu doğrular.
  * **Büyük veya Eşittir (≥):** İlk sütundaki değerlerin ikinci sütundakilere eşit veya onlardan büyük olduğunu garanti eder.
  * **Küçüktür (<):** İlk sütundaki değerlerin ikinci sütundakilerden küçük olup olmadığını kontrol eder.
  * **Küçük veya Eşittir (≤):** İlk sütundaki değerlerin ikinci sütundakilere eşit veya onlardan küçük olduğunu garanti eder.
* **Regex Bağımlılığı:** Bu kart, kullanıcıların üçüncü bir sütun için bir regex kalıbı tanımlamasına olanak tanıyan bir bağımlılık özelliği içerir. Karşılaştırma koşulu yalnızca bağımlılık sütunundaki en az bir değer regex kalıbıyla eşleşirse uygulanır.

## **Kullanım:**

Bu kart, özellikle veri noktaları arasındaki ilişkilere bağlı kalite kontrolleri gibi, veri biçimlendirmesine veya belirli kalıplara dayalı ek koşullarla karmaşık koşullu mantığın gerektiği senaryolarda yararlıdır.

***

## **Örnek Senaryo:**

* Bir kullanıcı, bir "Stock" tablosundaki "Quantity" ve "Threshold" sütunlarını **Quantity ≥ Threshold** koşuluyla karşılaştırmak için kartı yapılandırır. Bu karşılaştırma yalnızca "Item Code" sütunu, **^A\d{3}$** (örneğin "A" ile başlayıp ardından üç rakam gelen bir öğe kodunu gösterir) gibi belirli kod biçimlerine yönelik regex kalıbıyla eşleşirse gerçekleşir.

"Conditional Column Comparison" kartını kullanarak kuruluşlar, veri kümeleri içinde gelişmiş, kalıba bağlı karşılaştırmalar oluşturabilir, ince ayarlı veri işlemeyi mümkün kılabilir ve koşullu iş akışlarında doğruluğu artırabilir.
