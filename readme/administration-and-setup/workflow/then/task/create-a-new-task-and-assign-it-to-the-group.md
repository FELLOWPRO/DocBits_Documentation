# Create a New Task and assign it to the group

<figure><img src="../../../../.gitbook/assets/image (289).png" alt="" width="563"><figcaption></figcaption></figure>

## **Amaç:**

**"Create Group Task or Notification"** iş akışı kartı, belirtilen gruplar için görev veya bildirim oluşturmayı kolaylaştırır ve verimli iletişim ile görev yönetimi sağlar. Sonraki sürümlerde karar ağacı işlevselliğiyle geliştirilen kart, atanan grubu veya yöntemi dinamik olarak belirler ve operasyonları kolaylaştırır.

## **Kartın Bileşenleri:**

1. **Başlık (Title)**
   * **Açıklama**: Görevin veya bildirimin başlığını belirtir.
   * **Ayrıntı**: Oluşturulan görev veya bildirim için tanımlayıcı olarak işlev görür.
2. **Açıklama (Description)**
   * **Açıklama**: Görevin veya bildirimin bağlamını veya ayrıntılarını açıklar.
   * **Ayrıntı**: Amacına açıklık sağlar.
3. **Öncelik (Priority)**
   * **Açıklama**: Görevin önem düzeyini ayarlar.
   * **Seçenekler**:
     * **High**: Acil eylem gerektirir.
     * **Medium**: Önemli ama daha az acil.
     * **Low**: Daha sonra ele alınabilir.
4. **Atanan Grup (Assigned Group)**
   * **Açıklama**: Görevden veya bildirimden sorumlu grubu belirtir.
   * **Ayrıntı**: Kullanılabilir grupların açılır listesinden seçilir.
5. **E-posta Bildirimi (Email Notification)**
   * **Açıklama**: Atanan grubu bilgilendirmek için bir e-posta gönderilmesini etkinleştirir.
   * **Seçenekler**:
     * **True**: Bir e-posta bildirimi gönderir.
     * **False**: E-posta bildirimi gönderilmez.

## **Sürüm 3 ve Sürüm 4'teki Ek Bileşenler**

1. **Karar Ağacı (Yalnızca Sürüm 3)**
   * **Açıklama**: Dinamik görev oluşturma için bir karar ağacının kullanımını etkinleştirir.
   * **Seçenekler**:
     * **True**: Karar ağacı işlemesini etkinleştirir.
     * **False**: Karar ağacı işlemesini devre dışı bırakır.
2. **Görev/Bildirim Seçeneği (Yalnızca Sürüm 4)**
   * **Açıklama**: Bir görev veya bir bildirim oluşturmaya olanak tanır.
   * **Seçenekler**:
     * **Task**: Seçilen grup için bir görev oluşturur.
     * **Notification**: Görev oluşturmak yerine bir bildirim gönderir.

## **İşlevsellik:**

* **Koşul Değerlendirmesi**:\
  Kart eylemini yalnızca **"Where"** ve **"And Bölümleri"** doğruysa yürütür.
* **Görev veya Bildirim Oluşturma**:
  * Belirtilen başlık, açıklama ve öncelikle seçilen grup için bir görev oluşturulur.
  * Sürüm 4'te, kart bir görev yerine bir bildirim oluşturabilir.
* **Dinamik Atama (Yalnızca Sürüm 3)**:\
  Etkinleştirilirse, karar ağacı hedef grubu dinamik olarak belirler.
* **E-posta Bildirimi**:\
  E-posta seçeneği true olarak ayarlanırsa gruba bir e-posta bildirimi gönderir.

## **Kurulum ve Yapılandırma:**

1. **Görev veya Bildirim Ayrıntılarını Tanımla**: Başlığı, açıklamayı ve önceliği girin.
2. **Bir Gruba Ata**: Görev veya bildirim ataması için açılır listeden bir grup seçin.
3. **E-posta Bildirimini Etkinleştir**: Grubun e-posta yoluyla bilgilendirilip bilgilendirilmeyeceğini belirtin.
4. **Karar Ağacı Kullan (Yalnızca Sürüm 3)**: Grubu dinamik olarak atamak için karar ağacını etkinleştirin.
5. **Çıktı Türünü Seç (Yalnızca Sürüm 4)**: Kartın bir görev mi yoksa bir bildirim mi oluşturacağını seçin.

## **Sonuç:**

**"Create Group Task or Notification"** iş akışı kartı, grupları doğrudan hedefleyerek görev ve bildirim yönetimini basitleştirir. Karar ağacıyla etkinleştirilen dinamik atama özelliği esnekliği artırırken, e-posta bildirimleri zamanında iletişimi sağlar. Sürüm 3 ve 4 gelişmiş işlevsellik ekler, bu da onu verimli iş akışı yürütmesi için çok yönlü bir araç haline getirir.
