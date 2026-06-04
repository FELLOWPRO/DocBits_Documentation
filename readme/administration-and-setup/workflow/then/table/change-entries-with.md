# Change Entries with

<figure><img src="../../../../.gitbook/assets/image (293).png" alt="" width="563"><figcaption></figcaption></figure>

## **Amaç:**

**"Change Entries in Table"** iş akışı kartı, belirtilen bir veritabanı tablosundaki girişleri güncellemek için kullanılır. Bir **tablo** ve **sütun** seçmenize, ardından belirtilen bir değer kullanarak o sütundaki değerler üzerinde matematiksel işlemler (toplama, çıkarma, çarpma veya bölme) gerçekleştirmenize olanak tanır.

## **Kartın Bileşenleri:**

1. **Tablo Adı (Table Name)**
   * **Açıklama:** Girişlerin güncelleneceği **tabloyu** belirtir.
   * **Ayrıntı:** Girişleri güncellemek için hedef tabloyu seçmenize olanak tanıyan, kullanılabilir **tabloların** bir açılır listesi sağlanır.
2. **Sütun Adı (Column Name)**
   * **Açıklama:** Seçilen tablo içinde güncellenecek **sütunu** belirtir.
   * **Ayrıntı:** Seçim için tüm kullanılabilir **sütunların** bir listesi sağlanır.
3. **İşlem (Operation)**
   * **Açıklama:** **Sütun** değerleri üzerinde gerçekleştirilecek matematiksel işlemi tanımlar.
   * **Seçenekler:**
     * **Topla (+):** Seçilen sütundaki mevcut değere belirtilen bir **değer** ekler.
     * **Çıkar (-):** Seçilen sütundaki mevcut değerden belirtilen bir **değer** çıkarır.
     * **Çarp (\*):** Seçilen sütundaki mevcut değeri belirtilen bir **değerle** çarpar.
     * **Böl (/):** Seçilen sütundaki mevcut değeri belirtilen bir **değere** böler.
4. **Değer (Value)**
   * **Açıklama:** Seçilen işlemde kullanılacak **değeri** belirtir.
   * **Ayrıntı:** Bu, seçilen sütundaki girişlerle toplanacak, çıkarılacak, çarpılacak veya bölünecek sayıdır.

## **İşlevsellik:**

* **Koşul Değerlendirmesi:**\
  Kart, eylemini yalnızca hem **"Where"** hem de **"And Bölümleri"** doğru olarak değerlendirilirse yürütür.
* **Tablo Girişi Güncelleme:**\
  Kart, belirtilen **değeri** kullanarak seçilen **tablonun** seçilen **sütunundaki** değerler üzerinde seçilen işlemi (**+**, **-**, **\*** veya **/**) gerçekleştirir.

## **Kurulum ve Yapılandırma:**

* **Tablo Seç:**\
  Değişikliklerin uygulanacağı **tabloyu** seçin.
* **Sütun Seç:**\
  Tablo içinde güncellemek istediğiniz **sütunu** seçin.
* **İşlem Seç:**\
  Seçilen sütunun değerlerine uygulanacak matematiksel işlemi (**+**, **-**, **\***, **/**) seçin.
* **Değer Gir:**\
  Seçilen işlemde kullanılacak **değeri** sağlayın.

## **Sonuç:**

**"Change Entries in Table"** iş akışı kartı, bir **tablo**, **sütun** ve istenen **matematiksel işlem** seçerek veritabanı girişlerine otomatik güncellemeler yapılmasını mümkün kılar. Bu kart, veritabanınız içinde toplu veri değişiklikleri veya hesaplamalar gerçekleştirmek için gereklidir.
