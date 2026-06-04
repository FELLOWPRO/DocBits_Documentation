# Calculate Columns with

<figure><img src="../../../../.gitbook/assets/image (294).png" alt="" width="563"><figcaption></figcaption></figure>

## **Amaç:**

**"Calculate Columns in Table"** iş akışı kartı, seçilen bir tablodaki sütunlar arasında hesaplamalar gerçekleştirmek için kullanılır. Kullanıcıların sütunları seçmesine, matematiksel bir işlem uygulamasına ve sonucu belirtilen bir sonuç sütununda depolamasına olanak tanır.

## **Kartın Bileşenleri:**

1. **Tablo Adı (Table Name)**
   * **Açıklama:** Sütunların hesaplanacağı **tabloyu** belirtir.
   * **Ayrıntı:** Seçim için tüm kullanılabilir **tabloların** bir açılır listesi sağlanır.
2. **Sütun Adı (1. Sütun)**
   * **Açıklama:** Hesaplamaya dahil olacak **ilk sütunu** belirtir.
   * **Ayrıntı:** Seçim için tüm kullanılabilir **sütunların** bir listesi sağlanır.
3. **İşlem (Operation)**
   * **Açıklama:** Seçilen sütunlar arasında uygulanacak matematiksel işlemi tanımlar.
   * **Seçenekler:**
     * **Topla (+):** İkinci sütunun değerini ilk sütunun değerine ekler.
     * **Çıkar (-):** İkinci sütunun değerini ilk sütunun değerinden çıkarır.
     * **Çarp (\*):** İlk sütundaki değeri ikinci sütundaki değerle çarpar.
     * **Böl (/):** İlk sütundaki değeri ikinci sütundaki değere böler.
4. **Sütun Adı (2. Sütun)**
   * **Açıklama:** Hesaplamaya dahil olacak **ikinci sütunu** belirtir.
   * **Ayrıntı:** Seçim için kullanılabilir **sütunların** bir listesi sağlanır.
5. **Sonuç Sütunu (Result Column)**
   * **Açıklama:** Hesaplamanın sonucunun depolanacağı **sütunu** belirtir.
   * **Ayrıntı:** Hesaplanan değerin kaydedileceği kullanılabilir **sütunların** bir listesi sağlanır.

## **İşlevsellik:**

* **Koşul Değerlendirmesi:**\
  Kart, eylemini yalnızca hem **"Where"** hem de **"And Bölümleri"** doğru olarak değerlendirilirse yürütür.
* **Sütun Hesaplaması:**\
  Kart, seçilen iki sütun arasında seçilen matematiksel işlemi gerçekleştirir.
* **Sonuç Depolama:**\
  Hesaplamanın sonucu seçilen **sonuç sütununda** depolanır.

## **Kurulum ve Yapılandırma:**

* **Tablo Seç:**\
  Sütunların hesaplanacağı **tabloyu** seçin.
* **Sütunları Seç:**\
  Hesaplamada kullanılacak **ilk sütunu** ve **ikinci sütunu** seçin.
* **İşlem Seç:**\
  Sütunlar arasında uygulanacak matematiksel işlemi (**Topla (+)**, **Çıkar (-)**, **Çarp (\*)**, **Böl (/)**) seçin.
* **Sonuç Sütunu Seç:**\
  Hesaplamanın depolanacağı **sonuç sütununu** seçin.

## **Sonuç:**

**"Calculate Columns in Table"** iş akışı kartı, kullanıcıların bir tablodaki sütunlar arasında dinamik hesaplamalar gerçekleştirmesine ve sonuçları belirlenen bir sütunda depolamasına olanak tanır. Kart, farklı matematiksel işlemler uygulama esnekliği sunar ve sonucun belirtilen sütunda depolanmasını sağlar.
