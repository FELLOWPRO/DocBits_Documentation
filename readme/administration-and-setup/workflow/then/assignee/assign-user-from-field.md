# Assign user from field

<figure><img src="../../../../.gitbook/assets/image (299).png" alt="" width="563"><figcaption></figcaption></figure>

## **Amaç:**

**"Assign User from Field with Fallback"** iş akışı kartı, belirtilen bir belge alanında bulunan değere göre bir kullanıcıyı dinamik olarak atar. Alan geçerli bir kullanıcı içermiyorsa, görevin veya eylemin düzgün şekilde atanmasını sağlamak için önceden tanımlanmış bir kullanılabilir kullanıcı listesinden bir yedek kullanıcı seçilir.

## **Kartın Bileşenleri:**

1. **Alan Adı (Field Name)**
   * **Açıklama:** Atanacak kullanıcı bilgisini içeren **belge alanını** belirtir.
   * **Ayrıntı:** Bu alan, hangi kullanıcının atanması gerektiğini belirlemek için değerlendirilir. Alan geçerli bir kullanıcı içeriyorsa, o kullanıcıya görev atanır. Alan boş veya geçersizse, yedek kullanıcı atanır.
2. **Kullanıcı (Yedek)**
   * **Açıklama:** Belge alanı geçerli bir kullanıcı içermiyorsa atanacak **yedek kullanıcıyı** belirtir.
   * **Ayrıntı:** Seçim için tüm kullanılabilir kullanıcıların bir açılır listesi sağlanır. Belge alanı boşsa veya geçerli bir kullanıcı içermiyorsa bu kullanıcı atanır.

## **İşlevsellik:**

* **Koşul Değerlendirmesi:**\
  Kart, eylemini yalnızca hem **"Where"** hem de **"And Bölümleri"** doğru olarak değerlendirilirse yürütür.
* **Alan Tabanlı Kullanıcı Ataması:**\
  Kart önce görevi veya eylemi **Alan Adı**'nda tanımlanan kullanıcıya atamaya çalışır.
* **Yedek Kullanıcı Ataması:**\
  Alan geçerli bir kullanıcı içermiyorsa (veya boşsa), kart görevi **Kullanıcı (Yedek)** açılır listesinden seçilen yedek kullanıcıya atar.

## **Kurulum ve Yapılandırma:**

* **Alan Adı Seç:**\
  Atama için kullanıcıyı belirten **belge alanını** seçin.
* **Yedek Kullanıcı Seç:**\
  **Yedek kullanıcıyı** açılır listeden seçin. Belge alanı geçerli bir kullanıcı içermiyorsa görev bu kullanıcıya atanır.

## **Sonuç:**

**"Assign User from Field with Fallback"** iş akışı kartı, bir görevin veya eylemin her zaman geçerli bir kullanıcıya atanmasını sağlar. Belge alanındaki kullanıcı kullanılamıyorsa, yedek kullanıcı otomatik olarak atanır, esneklik sağlar ve görevin tamamlanmasını garanti eder.
