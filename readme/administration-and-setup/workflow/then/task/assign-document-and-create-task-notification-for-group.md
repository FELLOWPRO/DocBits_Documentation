# Assign Document and Create Task/Notification for Group

<figure><img src="../../../../.gitbook/assets/image (12) (1) (2).png" alt="" width="563"><figcaption></figcaption></figure>

## **Amaç**

"**Assign Document and Create Task/Notification for Group**" iş akışı kartı, bir belgeyi belirtilen bir gruba atar, özelleştirilebilir ayrıntılarla bir görev veya bildirim oluşturur ve isteğe bağlı olarak gruba bir e-posta bildirimi gönderir. Bu kart ayrıca yürütme sırasını belirlemek için sayısal bir öncelik değeri atamayı destekler.

## **Kartın Bileşenleri**

1. **Grup Adı (Group Name)**
   * **Açıklama:** Görevi veya bildirimi alacak grubu belirtir.
   * **Ayrıntı:** Belgenin ve görevin/bildirimin atanacağı grubun adını seçmek için bir açılır menü.
2. **Görev/Bildirim (Task/Notification)**
   * **Açıklama:** Grup için oluşturulacak eylem türünü belirtir.
   * **Ayrıntı:** İstenen eyleme göre "Task" veya "Notification" seçmek için bir açılır menü.
3. **Başlık (Title)**
   * **Açıklama:** Görevin veya bildirimin başlığını sağlar.
   * **Ayrıntı:** Görev veya bildirim için kısa, açıklayıcı bir başlık eklemek için bir alan.
4. **Açıklama (Description)**
   * **Açıklama:** Görevi veya bildirimi daha ayrıntılı açıklar.
   * **Ayrıntı:** Görevin amacı veya bildirimin içeriği hakkında ek ayrıntılar sağlamak için bir alan.
5. **Öncelik (Priority)**
   * **Açıklama:** Görevin veya bildirimin aciliyet düzeyini tanımlar.
   * **Seçenekler:**
     * **High:** Acil dikkat gerektirir.
     * **Medium:** Önemli ama acil değil.
     * **Low:** Daha sonra ele alınabilir.
6. **Posta Gönder (Send Mail)**
   * **Açıklama:** Gruba bir e-posta bildirimi gönderilip gönderilmeyeceğini yapılandırır.
   * **Seçenekler:**
     * **True:** Bir e-posta bildirimi gönderir.
     * **False:** E-posta göndermez.
7. **Değer (Value)**
   * **Açıklama:** Belge ataması için sayısal önceliği ayarlar.
   * **Ayrıntı:** Daha düşük bir sayının daha yüksek önceliği gösterdiği sayısal bir değer girmek için bir alan.

## **İşlevsellik**

* **Koşul Değerlendirmesi:**\
  Kart, eylemlerini yalnızca yapılandırılmış iş akışı koşulları karşılanırsa yürütür.
* **Belge Ataması ve Görev/Bildirim Oluşturma:**\
  Belge, "Group Name" alanında belirtilen gruba atanır. Yapılandırılmış başlık, açıklama ve öncelik düzeyiyle bir görev veya bildirim oluşturulur.
* **E-posta Bildirimi:**\
  "Send Mail" True olarak ayarlanırsa, görev veya bildirim hakkında bilgilendirmek için gruba bir e-posta bildirimi gönderilir.

## **Kurulum ve Yapılandırma**

1. **Grup Adını Tanımla:**
   * Group Name alanına grubun adını girin.
2. **Görev/Bildirim Seç:**
   * Görev/Bildirim açılır menüsünden "Task" veya "Notification" seçin.
3. **Görev/Bildirim Ayrıntılarını Ayarla:**
   * Görev veya bildirim için Başlık ve Açıklama girin.
   * Açılır menüden Önceliği (High, Medium veya Low) seçin.
4. **E-posta Bildirimini Etkinleştir:**
   * Bir e-posta bildirimi gönderilip gönderilmeyeceğine bağlı olarak Send Mail seçeneğini True veya False olarak yapılandırın.
5. **Sayısal Öncelik Ata:**
   * Atamanın önceliğini belirlemek için Değer alanına sayısal bir değer girin; daha düşük değerler önceliklidir.
6. Kart yapılandırmasını kaydedin ve iş akışını etkinleştirin.

## **Sonuç**

"Assign Document and Create Task/Notification for Group" iş akışı kartı, belgelerin uygun gruba atanmasını sağlarken özelleştirilebilir öncelik ve e-posta bildirim seçenekleriyle görevler veya bildirimler oluşturur. Bu, belge yönetimini kolaylaştırır ve iş akışı verimliliğini artırır.
