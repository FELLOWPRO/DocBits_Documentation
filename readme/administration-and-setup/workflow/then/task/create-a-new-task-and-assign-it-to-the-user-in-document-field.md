# Create a New Task and assign it to the User in Document Field

<figure><img src="../../../../.gitbook/assets/image (290).png" alt="" width="563"><figcaption></figcaption></figure>

## **Amaç:**

**"Create Field-Based Task or Notification"** iş akışı kartı, belirli belge alanları içinde tanımlanan kullanıcılara dinamik olarak atanan görevler veya bildirimler oluşturmak için kullanılır. Bu kart, belge alanı geçerli bir kullanıcı belirtmediğinde bile sorunsuz iş akışı yürütmesini sağlamak için isteğe bağlı bir yedek mekanizması sunar.

## **Kartın Bileşenleri:**&#x20;

1. **Başlık (Title)**
   * **Açıklama**: Görevin veya bildirimin başlığını belirtir.
   * **Ayrıntı**: Oluşturulan görevi veya bildirimi adlandırmak ve tanımlamak için kullanılır.
2. **Açıklama (Description)**
   * **Açıklama**: Görev veya bildirim hakkında ek ayrıntılar sağlar.
   * **Ayrıntı**: Alıcının görevin veya bildirimin amacını ve bağlamını anlamasını sağlar.
3. **Öncelik (Priority)**
   * **Açıklama**: Görevin veya bildirimin aciliyetini tanımlar.
   * **Seçenekler**:
     * **High**: Acil dikkat gerektirir.
     * **Medium**: Önemli ama daha az acil.
     * **Low**: Daha sonra ele alınabilir.
4. **Alan Adı (Field Name)**
   * **Açıklama**: Görevi veya bildirimi atamak için kullanılacak belge alanını belirtir.
   * **Ayrıntı**: Seçilen alan, görevin veya bildirimin atanacağı kullanıcıyı dinamik olarak belirler. Alan boş veya geçersizse, görev veya bildirim açılır listeden seçilen yedek kullanıcıya atanır.
5. **E-posta Bildirimi (Email Notification)**
   * **Açıklama**: Atanan kullanıcının e-posta yoluyla bilgilendirilip bilgilendirilmeyeceğini yapılandırır.
   * **Seçenekler**:
     * **True**: Atanan kullanıcıya bir e-posta bildirimi gönderir.
     * **False**: E-posta bildirimi gönderilmez.
6. **Yedek Kullanıcı (Fallback User)**
   * **Açıklama**: Belge alanında geçerli bir kullanıcı bulunmadığında görevi veya bildirimi atamak için açılır listeden bir kullanıcı seçilmesine olanak tanır.
   * **Ayrıntı**: Belge alanı boş veya geçersiz olsa bile görevin veya bildirimin atanmasını sağlar.

## **Sürüm 3'teki Ek Bileşenler:**

1. **Bildirim Türü (Notification Type)**&#x20;
   * **Açıklama**: Kartın bir görev mi yoksa bir bildirim mi oluşturacağını belirtir.
   * **Seçenekler**:
     * **Task**: Belirtilen kullanıcıya atanan bir görev oluşturur.
     * **Notification**: Görev oluşturmak yerine bir bildirim gönderir.

## **İşlevsellik:**

* **Koşul Değerlendirmesi**:\
  Kart, eylemini yalnızca hem **"Where"** hem de **"And Bölümleri"** doğru olarak değerlendirilirse yürütür.
* **Görev veya Bildirim Oluşturma**:
  * Görevi veya bildirimi belge alanında tanımlanan kullanıcıya atar.
  * Sürüm 3'te, bir görev veya bir bildirim oluşturmaya olanak tanır.
* **Yedek Mekanizması**:\
  Belge alanı geçerli bir kullanıcı tanımlamazsa, kart görevi veya bildirimi açılır listeden seçilen yedek kullanıcıya atar.
* **E-posta Bildirimi**:\
  Bunun için yapılandırılmışsa atanan kullanıcıya bir e-posta bildirimi gönderir.

## **Kurulum ve Yapılandırma:**

1. **Görev veya Bildirim Ayrıntılarını Tanımla**: Başlığı, açıklamayı ve önceliği girin.
2. **Belge Alanını Seç**: Görev veya bildirim ataması için kullanıcıyı belirten alanı seçin.
3. **E-posta Bildirimini Etkinleştir**: Atanan kullanıcıya bir e-posta bildirimi gönderilip gönderilmeyeceğini belirtin.
4. **Yedek Kullanıcı Seç**: Belge alanı geçerli bir kullanıcı tanımlamazsa atama için açılır listeden bir yedek kullanıcı seçin.
5. **Bildirim Türünü Belirt (Sürüm 3)**: Kartın bir görev mi yoksa bildirim mi oluşturacağını belirtin.

## **Sonuç:**

**"Create Field-Based Task or Notification"** iş akışı kartı, sorumlulukları belge alanlarına göre dinamik olarak atayarak görev ve bildirim yönetimini kolaylaştırır. Yedek kullanıcı mekanizması ve Sürüm 3'teki gelişmiş seçenekler esneklik sağlar ve belge verisi eksik olsa bile görevlerin veya bildirimlerin her zaman atanmasını garanti eder.
