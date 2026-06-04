# Create a New Task and assign it to the Recipient

<figure><img src="../../../../.gitbook/assets/image (288).png" alt="" width="563"><figcaption></figcaption></figure>

## **Amaç:**

**"Create Task with Fallback"** iş akışı kartı, görevleri belirli rollere — disponent veya purchaser — atayarak verimli görev devrini sağlarken, görev atama hatalarını önlemek için bir yedek mekanizması içerir. Bu kart, dinamik senaryolarda iş akışı güvenilirliğini ve uyarlanabilirliğini iyileştirir.

## **Kartın Bileşenleri:**

1. **Başlık (Title)**
   * **Açıklama**: Oluşturulan görevin başlığını belirtir.
   * **Ayrıntı**: Görev için kısa bir tanımlayıcı sağlar.
2. **Açıklama (Description)**
   * **Açıklama**: Görevin amacını veya bağlamını açıklar.
   * **Ayrıntı**: Görevin ayrıntılarına açıklık getirir.
3. **Öncelik (Priority)**
   * **Açıklama**: Görev için aciliyet düzeyini ayarlar.
   * **Seçenekler**:
     * **High**: Acil dikkat gerektirir.
     * **Medium**: Önemli ama acil değil.
     * **Low**: Daha sonra ele alınabilir.
4. **Atanan Rol (Assigned Role)**
   * **Açıklama**: Görevin atandığı birincil rolü belirtir.
   * **Seçenekler**:
     * **Disponent**: Görevi disponent'e atar.
     * **Purchaser**: Görevi purchaser'a atar.
5. **E-posta Bildirimi (Email Notification)**
   * **Açıklama**: Atanan kullanıcıyı e-posta yoluyla bilgilendirmeyi etkinleştirir.
   * **Seçenekler**:
     * **True**: Kullanıcıya bir e-posta bildirimi gönderir.
     * **False**: E-posta bildirimi gönderilmez.
6. **Yedek Kullanıcı (Fallback User)**
   * **Açıklama**: Alıcı rolü bulunmazsa görev ataması için bir yedek seçenek sağlar.
   * **Ayrıntı**: Görev devrini sağlamak için açılır listeden bir kullanıcı seçilmesine olanak tanır.

## **İşlevsellik:**

* **Koşul Değerlendirmesi**:\
  Kart yalnızca **"Where"** ve **"And Bölümleri"**ndeki koşullar karşılanırsa yürütülür.
* **Görev Ataması**:
  * Görev, seçilen role (disponent veya purchaser) atanır.
  * Belirtilen rol bulunmazsa, görev yedek açılır listesinden bir kullanıcıya atanır.
* **E-posta Bildirimi**:\
  E-posta bildirimi etkinse atanan kullanıcıya bir e-posta gönderir.

## **Kurulum ve Yapılandırma:**

1. **Görev Ayrıntılarını Belirt**: Görevin başlığını, açıklamasını ve önceliğini girin.
2. **Birincil Rolü Seç**: Görevin atanacağı rolü (disponent veya purchaser) seçin.
3. **Yedek Kullanıcıyı Yapılandır**: Birincil rol bulunmazsa görev atamasını sağlamak için açılır listeden bir yedek kullanıcı seçin.
4. **E-posta Bildirimini Etkinleştir**: Atanan kullanıcının bir e-posta bildirimi alıp almayacağını belirtin.

## **Sonuç:**

**"Create Task with Fallback"** iş akışı kartı, bir yedek mekanizması entegre ederek sorunsuz görev devrini sağlar. Görevleri rollere göre atayarak ve alternatif bir kullanıcı seçeneği sağlayarak, görev yönetimi süreçlerinde güvenilirliği ve esnekliği artırır.
