# Assign document to

<figure><img src="../../../../.gitbook/assets/image (306).png" alt="" width="563"><figcaption></figcaption></figure>

## Amaç:

**"Assign document to \[User/group] based on decision table"** iş akışı kartı, bir **karar tablosunun** sonucuna göre belgeleri dinamik olarak kullanıcılara veya gruplara atar. Bu özellik, belge atamasının önceden tanımlanmış koşullara göre verimli ve tutarlı bir şekilde ele alınmasını sağlar.

## Kartın Bileşenleri:

1. **Kullanıcı/Grup (User/Group)**
   * **Açıklama:** Belgenin atanacağı **kullanıcıyı** veya **grubu** belirtir.
   * **Ayrıntı:** **Karar tablosunun** sonucuna göre seçilir.
2. **Karar Tablosu (Decision Table)**
   * **Açıklama:** Belge ataması için uygun **kullanıcıyı** veya **grubu** belirlemek için bir **karar tablosu** kullanılır.
   * **Ayrıntı:** **"and"** bölümünde tanımlanan karar tablosunu kullanır.

## İşlevsellik:

* **Koşul Değerlendirmesi:** Kart, eylemini yalnızca hem **"Where"** hem de **"And Bölümleri"** doğru olarak değerlendirilirse yürütür.
* **Dinamik Belge Ataması:** Belge, **karar tablosu** tarafından belirlenen **kullanıcıya** veya **gruba** atanır.

## Kurulum ve Yapılandırma:

* **Karar Tablosunu Tanımla:** Hedef **kullanıcıyı** veya **grubu** belirleme koşullarını içerecek şekilde **karar tablosunu** ayarlayın.
* **Belgeyi Kullanıcıya/Gruba Ata:** Belge, karar tablosunun sonucuna göre dinamik olarak atanacaktır.

## Sonuç:

**"Assign document to \[User/group] based on decision table"** iş akışı kartı, karar mantığına dayalı dinamik belge atama yetenekleri sunar. Bu, belgeleri otomatik olarak uygun **kullanıcıya** veya **gruba** yönlendirerek doğru ve verimli işlemeyi sağlar ve iş akışı otomasyonunu artırır.
