# Assign Document and Create Task/Notification for User

<figure><img src="../../../../.gitbook/assets/image (13) (1) (2).png" alt="" width="563"><figcaption></figcaption></figure>

## **Amaç**

"**Assign Document and Create Task/Notification for User**" iş akışı kartı, bir belgeyi belirtilen bir kullanıcıya atar, yapılandırılabilir ayrıntılarla bir görev veya bildirim oluşturur ve isteğe bağlı olarak kullanıcıya bir e-posta bildirimi gönderir. Bu kart ayrıca yürütme sırasını belirlemek için sayısal bir öncelik değeri ayarlamayı mümkün kılar.

## **Kartın Bileşenleri**

1. **Kullanıcı (User)**
   * **Açıklama:** Görevi veya bildirimi alacak kullanıcıyı belirtir.
   * **Ayrıntı:** Belgenin ve görevin/bildirimin atanacağı kullanıcıyı seçmek için bir açılır menü.
2. **Görev/Bildirim (Task/Notification)**
   * **Açıklama:** Kullanıcı için oluşturulacak eylem türünü belirtir.
   * **Ayrıntı:** Amaçlanan eyleme göre "Task" veya "Notification" seçmek için bir açılır menü.
3. **Başlık (Title)**
   * **Açıklama:** Görevin veya bildirimin başlığı.
   * **Ayrıntı:** Görev veya bildirim için kısa, açıklayıcı bir başlık sağlamak için bir alan.
4. **Açıklama (Description)**
   * **Açıklama:** Görev veya bildirim hakkında ek ayrıntılar.
   * **Ayrıntı:** Görevin amacını açıklamak veya bildirim için bağlam sağlamak için bir alan.
5. **Öncelik (Priority)**
   * **Açıklama:** Görevin veya bildirimin aciliyet düzeyini tanımlar.
   * **Seçenekler:**
     * **High:** Acil dikkat gerektirir.
     * **Medium:** Önemli ama acil değil.
     * **Low:** Daha sonra ele alınabilir.
6. **Posta Gönder (Send Mail)**
   * **Açıklama:** Kullanıcıya bir e-posta bildirimi gönderilip gönderilmeyeceğini yapılandırır.
   * **Seçenekler:**
     * **True:** Kullanıcıya bir e-posta bildirimi gönderir.
     * **False:** E-posta bildirimi gönderilmez.
7. **Değer (Value)**
   * **Açıklama:** Belge ataması için sayısal önceliği ayarlar.
   * **Ayrıntı:** Daha düşük sayıların daha yüksek önceliği gösterdiği sayısal bir değer girmek için bir alan.

## **İşlevsellik**

* **Koşul Değerlendirmesi:**\
  Kart, eylemlerini yalnızca yapılandırılmış iş akışı koşulları karşılanırsa yürütür.
* **Belge Ataması ve Görev/Bildirim Oluşturma:**\
  Belge, "User" alanında belirtilen kullanıcıya atanır. Sağlanan başlık, açıklama ve öncelik düzeyiyle bir görev veya bildirim oluşturulur.
* **E-posta Bildirimi:**\
  "Send Mail" True olarak ayarlanırsa, kullanıcıya görev veya bildirim hakkında bilgilendiren bir e-posta gönderilir.

## **Kurulum ve Yapılandırma**

1. **Kullanıcı Seç:**
   * Kullanıcı açılır menüsünden kullanıcıyı seçin.
2. **Görev/Bildirim Ayrıntılarını Yapılandır:**
   * Görev/Bildirim açılır menüsünden "Task" veya "Notification" seçin.
   * Görev veya bildirim için Başlık ve Açıklama girin.
   * Açılır menüden High, Medium veya Low seçerek Önceliği ayarlayın.
3. **E-posta Bildirimini Etkinleştir:**
   * Bir e-posta bildirimi gönderilip gönderilmeyeceğine bağlı olarak Send Mail seçeneğini True veya False olarak yapılandırın.
4. **Sayısal Önceliği Ayarla:**
   * Atamanın önceliğini belirlemek için Değer alanına sayısal bir değer girin; daha düşük değerler önce işlenir.
5. Kart yapılandırmasını kaydedin ve iş akışını etkinleştirin.

## **Sonuç**

"Assign Document and Create Task/Notification for User" iş akışı kartı, belgelerin uygun kullanıcıya atanmasını sağlarken tanımlanmış önceliklerle ve isteğe bağlı e-posta bildirimleriyle görevler veya bildirimler oluşturur. Bu kart, görev devrini kolaylaştırmaya yardımcı olur ve iş akışı verimliliğini artırır.
