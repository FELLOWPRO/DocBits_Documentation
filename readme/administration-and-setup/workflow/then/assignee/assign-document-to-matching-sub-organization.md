# Assign document to matching sub organization

<figure><img src="../../../../.gitbook/assets/image (303).png" alt="" width="563"><figcaption></figcaption></figure>

## **Amaç:**

**"Assign Document to Matching Sub-Organization Based on Field"** iş akışı kartı, belgedeki belirtilen bir alana göre bir belgeyi dinamik olarak bir alt kuruluşa atar. Eşleşen bir alt kuruluş bulunmazsa, kart önceden tanımlanmış bir yedek alt kuruluş kullanır.

## **Kartın Bileşenleri:**

1. **Alan Adı (Field Name)**
   * **Açıklama:** Eşleşen alt kuruluşu belirlemek için kullanılacak belge alanını belirtir.
   * **Ayrıntı:** Kart, kullanılabilir bir alt kuruluşla eşleştirmek için belirtilen alanda bir değer arar.
2. **Alt Kuruluş (Yedek)**
   * **Açıklama:** Belirtilen alanda eşleşme bulunmazsa kullanılacak yedek alt kuruluşu tanımlar.
   * **Ayrıntı:** Alan değeri herhangi bir alt kuruluşla eşleşmezse, belge seçilen yedek alt kuruluşa atanır.

## **İşlevsellik:**

* **Koşul Değerlendirmesi:**\
  Kart, eylemini yalnızca hem **"Where"** hem de **"And Bölümleri"** doğru olarak değerlendirilirse yürütür.
* **Dinamik Atama:**\
  Kart, belirtilen alanın değerini kontrol eder ve belgeyi bu değerle eşleşen alt kuruluşa atar.
* **Yedek Mekanizması:**\
  Eşleşen bir alt kuruluş bulunmazsa, belge yedek alt kuruluşa atanır.

## **Kurulum ve Yapılandırma:**

* **Alan Adı Seç:**\
  Belgeden, bir alt kuruluşla eşleştirilecek değeri içeren alanı seçin.
* **Yedek Alt Kuruluş Seç:**\
  Belge alanında eşleşme bulunmazsa kullanılacak alt kuruluşu seçin.

## **Sonuç:**

**"Assign Document to Matching Sub-Organization Based on Field"** iş akışı kartı, belgeleri uygun alt kuruluşa dinamik olarak yönlendirerek esneklik sunar; hiçbir belgenin atanmamış kalmamasını sağlamak için eklenen bir yedek seçeneğiyle birlikte.
