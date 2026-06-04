# Assign document to User

<figure><img src="../../../../.gitbook/assets/image (300).png" alt="" width="563"><figcaption></figcaption></figure>

## **Amaç:**

**"Assign Document to User"** iş akışı kartı, kullanıcıların bir belgeyi belirli bir kullanıcıya atamasına olanak tanır ve belgeleri uygun kişiye yönlendirerek sorunsuz iş akışı yönetimi sağlar. Sürüm 3, mevcut koşullara göre kullanıcı atamasını dinamik olarak belirlemek için bir karar ağacı kullanma yeteneğini ekler.

## **Kartın Bileşenleri:**

1. **Kullanıcı (User)**
   * **Açıklama:** Belgenin atanacağı kullanıcıyı belirtir.
   * **Ayrıntı:** Seçim için tüm kullanılabilir kullanıcıların bir açılır listesi sağlanır. Seçilen kullanıcıya, daha fazla işlem için belge atanır.

## **Sürüm 3'teki Ek Bileşenler:**

1. **Karar Ağacı Kullan (Use Decision Tree)**
   * **Açıklama:** Etkinleştirilirse, kart kullanıcı atamasını dinamik olarak belirlemek için bir karar ağacı kullanır.
   * **Seçenekler:**
     * **True:** Dinamik kullanıcı ataması için karar ağacını kullanır.
     * **False:** Belgeyi karar ağacını kullanmadan seçilen kullanıcıya atar.

## **İşlevsellik:**

* **Koşul Değerlendirmesi:**\
  Kart, eylemini yalnızca hem **"Where"** hem de **"And Bölümleri"** doğru olarak değerlendirilirse yürütür.
* **Belge Ataması:**\
  Kart, belgeyi seçilen kullanıcıya atar ve görevin eylem için uygun kişiye yönlendirilmesini sağlar. Bu, hesap verebilirliğe ve etkili belge yönetimine yardımcı olur.
* **Karar Ağacı (Sürüm 3):**\
  Karar ağacı etkinleştirilirse, kart belge ataması için kullanıcıyı dinamik olarak seçmek üzere ağaç içinde tanımlanan koşulları değerlendirir.

## **Kurulum ve Yapılandırma:**

* **Kullanıcı Seç:**\
  Belgenin atanacağı **kullanıcıyı** açılır listeden seçin.
* **Karar Ağacı Kullan (Sürüm 3):**\
  Kullanıcıyı dinamik olarak seçmek için karar ağacının kullanımını etkinleştirin veya devre dışı bırakın.

## **Sonuç:**

**"Assign Document to User"** iş akışı kartı, belgeyi seçilen kullanıcıya atayarak verimli belge yönlendirmesini kolaylaştırır; Sürüm 3'te bir karar ağacı kullanarak kullanıcıyı dinamik olarak belirleme ek esnekliğiyle birlikte. Bu, daha uyarlanabilir ve verimli bir iş akışı süreci sağlar.
