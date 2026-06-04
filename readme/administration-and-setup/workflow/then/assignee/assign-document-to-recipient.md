# Assign document to recipient

<figure><img src="../../../../.gitbook/assets/image (301).png" alt="" width="563"><figcaption></figcaption></figure>

## **Amaç:**

**"Assign Document to Disponent / Purchaser"** iş akışı kartı, bir belgeyi bir **Disponent** veya **Purchaser**'a atar. Geçerli bir kullanıcı bulunmazsa, belgenin her zaman birine atanmasını sağlamak için bir yedek kullanıcı seçilir.

## **Kartın Bileşenleri:**

1. **Disponent / Purchaser**
   * **Açıklama:** Belgenin bir Disponent'e mi yoksa Purchaser'a mı atanacağını belirtir.
   * **Seçenekler:**
     * **Disponent:** Belgeyi Disponent'e atar.
     * **Purchaser:** Belgeyi Purchaser'a atar.
2. **Yedek Kullanıcı (Fallback User)**
   * **Açıklama:** Belge seçilen Disponent veya Purchaser'a atanamazsa atanacak bir yedek kullanıcıyı belirtir.
   * **Ayrıntı:** Kullanılabilir kullanıcıların açılır listesi, birincil kullanıcı belirlenemese bile belgenin atanmasını sağlamak için bir yedek kullanıcı seçmenize olanak tanır.

## **İşlevsellik:**

* **Koşul Değerlendirmesi:**\
  Kart, eylemini yalnızca hem **"Where"** hem de **"And Bölümleri"** doğru olarak değerlendirilirse yürütür.
* **Belge Ataması:**\
  Kart, belgeyi seçildiği gibi **Disponent** veya **Purchaser**'a atar. Seçilen kişi kullanılamaz veya geçerli değilse, belge yedek kullanıcıya atanır.

## **Kurulum ve Yapılandırma:**

* **Disponent / Purchaser Seç:**\
  Belgenin **Disponent**'e mi yoksa **Purchaser**'a mı atanacağını seçin.
* **Yedek Kullanıcı Seç:**\
  Birincil atama mümkün değilse belgeyi alacak yedek kullanıcıyı açılır listeden seçin.

## **Sonuç:**

**"Assign Document to Disponent / Purchaser"** iş akışı kartı, belgenin her zaman atanmasını sağlar; ya seçilen Disponent/Purchaser'a ya da gerekirse yedek kullanıcıya. Bu, iş akışı kesintilerini en aza indirir ve belge işlemenin sorunsuz devam etmesini sağlar.
