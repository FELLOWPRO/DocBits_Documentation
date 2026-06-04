# Assign to group

<figure><img src="../../../../.gitbook/assets/image (304).png" alt="" width="563"><figcaption></figcaption></figure>

## Amaç:

**"Assign to Group"** iş akışı kartı, belgelerin sistem içindeki belirli bir **gruba** atanmasını kolaylaştırır. Bu, belgenin uygun ekip tarafından işlenmesini sağlar ve iş akışını kolaylaştırır. Sonraki sürümlerde geliştirilen kart, dinamik grup ataması için karar ağacı işlevselliği sunar.

## Kartın Bileşenleri:

1. **Gruplar (Groups)**
   * **Açıklama:** Belgenin atanacağı **grubu** belirtir.
   * **Ayrıntı:** Kullanılabilir **gruplar** açılır listesinden seçilir.



## **Sürüm 3'teki Ek Bileşenler**

1. **Karar Ağacı (Yalnızca Sürüm 3)**
   * **Açıklama:** Belgenin atanacağı **grubu** dinamik olarak belirlemek için bir karar ağacının kullanılmasına olanak tanır.
   * **Seçenekler:**
     * **True:** Karar ağacı işlemesini etkinleştirir.
     * **False:** Karar ağacı işlemesini devre dışı bırakır.

## İşlevsellik:

* **Koşul Değerlendirmesi:** Kart, eylemini yalnızca hem **"Where"** hem de **"And Bölümleri"** doğru olarak değerlendirilirse yürütür.
* **Belge Ataması:** Belgeyi seçilen **gruba** atar. **Sürüm 3**'te, etkinleştirilirse **karar ağacı** hedef grubu dinamik olarak belirler.

## Kurulum ve Yapılandırma:

* **Grup Seç:** Belgeyi atamak için **grubu** açılır listeden seçin.
* **Karar Ağacı Kullan (Yalnızca Sürüm 3):** Dinamik atama için **karar ağacı** kullanılması gerekiyorsa bu seçeneği etkinleştirin.

## Sonuç:

**"Assign to Group"** iş akışı kartı, belge atamasını önceden tanımlanmış **gruplara** otomatikleştirir ve ekip koordinasyonunu artırır. **Sürüm 3**, karar ağacı mantığına dayalı olarak grupları dinamik olarak atama yeteneğini sunar.
