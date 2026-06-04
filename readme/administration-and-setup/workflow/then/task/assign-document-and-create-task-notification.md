# Assign Document and Create Task/Notification

<figure><img src="../../../../.gitbook/assets/image (14) (1) (2).png" alt="" width="563"><figcaption></figcaption></figure>

## **Amaç**

"**Assign Document and Create Task/Notification Based on Decision Table**" iş akışı kartı, bir belgeyi atar ve yapılandırılabilir ayrıntılarla bir görev veya bildirim oluşturur. Atanan, bir karar tablosunun dönüşüyle belirlenir ve kart öncelikler ayarlamaya ve e-posta bildirimleri göndermeye olanak tanır.

## **Kartın Bileşenleri**

1. **Atanan Türü (Assignee Type)**
   * **Açıklama:** Karar tablosunun dönüşünün belgeyi ve görevi/bildirimi bir kullanıcıya mı yoksa gruba mı atadığını belirtir.
   * **Ayrıntı:** Karar tablosu çıktısına göre atanan türünü "User" veya "Group" olarak yapılandırmak için bir alan.
2. **Görev/Bildirim (Task/Notification)**
   * **Açıklama:** Atanan için oluşturulacak eylem türünü belirtir.
   * **Ayrıntı:** İş akışı ihtiyaçlarına göre "Task" veya "Notification" seçmek için bir açılır menü.
3. **Başlık (Title)**
   * **Açıklama:** Görevin veya bildirimin başlığı.
   * **Ayrıntı:** Görevi veya bildirimi tanımlayan kısa bir başlık sağlamak için bir alan.
4. **Açıklama (Description)**
   * **Açıklama:** Görev veya bildirim hakkında ek ayrıntılar.
   * **Ayrıntı:** Görevin veya bildirimin amacını ve bağlamını açıklamak için bir alan.
5. **Öncelik (Priority)**
   * **Açıklama:** Görevin veya bildirimin aciliyet düzeyini tanımlar.
   * **Seçenekler:**
     * **High:** Acil dikkat gerektirir.
     * **Medium:** Önemli ama acil değil.
     * **Low:** Daha sonra ele alınabilir.
6. **Atanan Türü (Assignee Type)**
   * **Açıklama:** Bu alan, belgenin ve görevin/bildirimin atanacağı atanan türünü (User veya Group) belirler.
   * **Ayrıntı:** Görevin/bildirimin karar tablosunun çıktısına göre bir kullanıcıya mı yoksa bir gruba mı atanacağını seçmek için bir açılır menü.
7. **Posta Gönder (Send Mail)**
   * **Açıklama:** Atanana bir e-posta bildirimi gönderilip gönderilmeyeceğini yapılandırır.
   * **Seçenekler:**
     * **True:** Bir e-posta bildirimi gönderir.
     * **False:** E-posta bildirimi gönderilmez.
8. **Değer (Value)**
   * **Açıklama:** Belge ataması için sayısal önceliği ayarlar.
   * **Ayrıntı:** Daha düşük sayıların daha yüksek önceliği gösterdiği sayısal bir değer girmek için bir alan.

## **İşlevsellik**

* **Koşul Değerlendirmesi:**\
  Kart, eylemlerini yalnızca iş akışı koşulları karşılanırsa yürütür.
* **Karar Tablosu Değerlendirmesi:**\
  Karar tablosu, belgenin ve görevin/bildirimin bir kullanıcıya mı yoksa gruba mı atanacağını belirler.
* **Belge Ataması ve Görev/Bildirim Oluşturma:**\
  Belge, karar tablosunun sonucuna atanır. Belirtilen başlık, açıklama ve öncelik düzeyiyle bir görev veya bildirim oluşturulur.
* **E-posta Bildirimi:**\
  "Send Mail" True olarak ayarlanırsa, atanana bir e-posta bildirimi gönderilir.

## **Kurulum ve Yapılandırma**

1. **Atanan Türünü Tanımla:**
   * Atanan Türü alanını karar tablosunun çıktısına göre "User" veya "Group" olarak yapılandırın.
2. **Görev/Bildirim Seç:**
   * Görev/Bildirim açılır menüsünden "Task" veya "Notification" seçin.
3. **Görev/Bildirim Ayrıntılarını Ayarla:**
   * Görev veya bildirim için Başlık ve Açıklama girin.
   * Açılır menüden Önceliği (High, Medium veya Low) seçin.
4. **E-posta Bildirimini Etkinleştir:**
   * Bir e-posta bildirimi gönderilip gönderilmeyeceğine bağlı olarak Send Mail seçeneğini True veya False olarak ayarlayın.
5. **Sayısal Önceliği Ayarla:**
   * Atama önceliğini belirlemek için Değer alanına sayısal bir değer girin; daha düşük sayılar önce işlenir.
6. Kart yapılandırmasını kaydedin ve iş akışını etkinleştirin.

## **Sonuç**

"Assign Document and Create Task/Notification Based on Decision Table" iş akışı kartı, görevlerin veya bildirimlerin karar tablosu sonuçlarına göre uygun kullanıcıya veya gruba dinamik olarak atanmasını sağlar. Bu kart, verimli görev devri, özelleştirilebilir öncelikler ve iş akışı yanıt verebilirliğini artırmak için isteğe bağlı e-posta bildirimleri sağlar.
