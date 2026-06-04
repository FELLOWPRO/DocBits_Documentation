# Calculate in



<figure><img src="../../../../.gitbook/assets/image (295).png" alt="" width="563"><figcaption></figcaption></figure>

## **Amaç:**

**"Calculate with Regex Dependency"** iş akışı kartı, kullanıcıların seçilen bir tablodaki sütunlar arasında hesaplamalar gerçekleştirmesine olanak tanır; bir bağımlılık sütununa uygulanan düzenli ifade (regex) kalıbına dayalı eklenen bir koşulla birlikte. Kalıp eşleşirse, hesaplama gerçekleştirilir ve sonuç belirtilen sonuç sütununda depolanır.

## **Kartın Bileşenleri:**

1. **Tablo Adı (Table Name)**
   * **Açıklama:** Sütunların hesaplanacağı **tabloyu** belirtir.
   * **Ayrıntı:** Seçim için tüm kullanılabilir **tabloların** bir açılır listesi sağlanır.
2. **Sütun Adı (1. Sütun)**
   * **Açıklama:** Hesaplamaya dahil olan **ilk sütunu** belirtir.
   * **Ayrıntı:** Seçim için tüm kullanılabilir **sütunların** bir listesi sağlanır.
3. **İşlem (Operation)**
   * **Açıklama:** Seçilen sütunlar arasında uygulanacak matematiksel işlemi tanımlar.
   * **Seçenekler:**
     * **Topla (+):** İkinci sütunun değerini ilk sütunun değerine ekler.
     * **Çıkar (-):** İkinci sütunun değerini ilk sütundan çıkarır.
     * **Çarp (\*):** İlk sütunun değerini ikinci sütundaki değerle çarpar.
     * **Böl (/):** İlk sütunun değerini ikinci sütuna böler.
4. **Sütun Adı (2. Sütun)**
   * **Açıklama:** Hesaplamaya dahil olan **ikinci sütunu** belirtir.
   * **Ayrıntı:** Seçim için tüm kullanılabilir **sütunların** bir listesi sağlanır.
5. **Sütun Adı (Bağımlılık)**
   * **Açıklama:** Regex kalıbının uygulanacağı **bağımlılık sütununu** belirtir.
   * **Ayrıntı:** Kalıp eşleştirme için tüm kullanılabilir **sütunların** bir listesi sağlanır.
6. **Regex Kalıbı**
   * **Açıklama:** Bağımlılık sütununa karşı eşleştirme için kullanılacak **regex kalıbını** tanımlar.
   * **Ayrıntı:** Bağımlılık sütunundaki değer regex kalıbıyla eşleşirse, hesaplama gerçekleştirilir.
7. **Sonuç Sütunu (Result Column)**
   * **Açıklama:** Hesaplama sonucunun depolanacağı **sonuç sütununu** belirtir.
   * **Ayrıntı:** Bu, hesaplanan değerin depolanacağı yeni veya mevcut bir sütun olabilir.

## **İşlevsellik:**

* **Koşul Değerlendirmesi:**
  * Kart, eylemini yalnızca hem **"Where"** hem de **"And Bölümleri"** doğru olarak değerlendirilirse yürütür.
  * Kart, eylemini yalnızca bağımlılık sütunundaki değer sağlanan **regex kalıbıyla** eşleşirse yürütür.
* **Sütun Hesaplaması:**\
  Regex kalıbı eşleşirse, kart seçilen iki sütun arasında seçilen matematiksel işlemi gerçekleştirir.
* **Sonuç Depolama:**\
  Hesaplamanın sonucu seçilen **sonuç sütununda** depolanır.

## **Kurulum ve Yapılandırma:**

* **Tablo Seç:**\
  Sütunların hesaplanacağı **tabloyu** seçin.
* **Sütunları Seç:**\
  Hesaplamada kullanılacak **ilk sütunu** ve **ikinci sütunu** seçin.
* **İşlem Seç:**\
  Sütunlar arasında uygulanacak matematiksel işlemi (**Topla (+)**, **Çıkar (-)**, **Çarp (\*)**, **Böl (/)**) seçin.
* **Bağımlılık Sütunu Seç:**\
  Regex kalıbının uygulanacağı **bağımlılık sütununu** seçin.
* **Regex Kalıbı Tanımla:**\
  Bağımlılık sütununun eşleşmesi gereken **regex kalıbını** girin.
* **Sonuç Sütunu Seç:**\
  Hesaplanan değerin depolanacağı **sonuç sütununu** seçin.

## **Sonuç:**

**"Calculate with Regex Dependency"** iş akışı kartı, bir regex kalıbına dayalı koşullu mantıkla hesaplamalar gerçekleştirmek için güçlü bir yol sunar. Bu, yalnızca bağımlılık sütununun belirtilen kalıpla eşleştiği satırların belirtilen hesaplamaya tabi tutulmasını ve sonucun seçilen sonuç sütununda depolanmasını sağlar.
