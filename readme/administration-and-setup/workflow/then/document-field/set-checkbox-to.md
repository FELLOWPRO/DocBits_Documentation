# Set Checkbox to

<figure><img src="../../../../.gitbook/assets/image (279).png" alt="" width="563"><figcaption></figcaption></figure>

## **Amaç:**

Bu iş akışı kartı, **"Where"** ve **"And"** bölümlerinde tanımlanan koşullara göre bir onay kutusu alanını belirtilen bir değere (true veya false) ayarlamak için tasarlanmıştır. Belirli ölçütler karşılandığında onay kutusu güncellemelerini otomatikleştirmek için basit ama etkili bir yol sunar ve kolaylaştırılmış belge işlemeyi sağlar.

## **Kartın Bileşenleri:**

1. **Alan Adı (Field Name):**
   * **Açıklama**: Onay kutusunun ayarlanacağı alanı belirtir.
   * **Ayrıntı**: Güncellenecek onay kutusu alanı, alan adıyla tanımlanır.
2. **Boolean**
   * **Açıklama**: **Where** ve **And Bölümleri**ndeki koşulların her ikisi de doğru olduğunda onay kutusu alanının ayarlanacağı değeri tanımlar.
   * **Seçenekler**:
     * **True**: Koşullar karşılanırsa onay kutusu **true** olarak ayarlanır.
     * **False**: Koşullar karşılanırsa onay kutusu **false** olarak ayarlanır.

## **İşlevsellik:**

* **Koşul Değerlendirmesi**: Sistem, hem **"Where"** hem de **"And"** bölümlerindeki koşulları değerlendirir&#x20;
* **Eylem Yürütme**: Hem **"Where"** hem de **"And Bölümleri"** doğru olarak değerlendirilirse, onay kutusu alanı belirtilen değere (true veya false) güncellenir. Koşullardan biri yanlışsa, hiçbir eylem gerçekleştirilmez ve onay kutusu olduğu gibi kalır.

## **Kurulum ve Yapılandırma:**

Bu kartı yapılandırmak için, kullanıcıların şunları yapması gerekir:

1. Koşullar karşılandığında true veya false olarak ayarlanacak **hedef onay kutusu alanını belirtin**.
2. Koşul değerlendirmesi üzerine onay kutusunun ayarlanacağı **değeri (true veya false) seçin**.
3. Kart, eylemini yalnızca **"Where"** ve **"And Bölümleri"**ndeki her iki koşul da doğru olarak değerlendirilirse yürütür.

## **Sonuç:**

**"Set Checkbox"** iş akışı kartı, belirli koşullara göre onay kutusu alanlarını güncellemek için basit ve etkili bir otomasyon aracıdır. Hem **"Where"** hem de **"And Bölümleri"**nin karşılanmasını sağlayarak, kullanıcıların süreçleri otomatikleştirmesine ve manuel müdahaleyi azaltmasına olanak tanır, daha sorunsuz ve verimli belge işlemeyi sağlar.
