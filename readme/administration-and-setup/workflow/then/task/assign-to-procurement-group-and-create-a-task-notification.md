# Assign to Procurement Group and Create a Task/Notification

<figure><img src="../../../../.gitbook/assets/image (2) (1) (1) (2).png" alt="" width="563"><figcaption></figcaption></figure>

## **Amaç**

"**Assign Document to Procurement Group and Create Task/Notification**" iş akışı kartı, bir belgeyi belirtilen bir satınalma grubuna atar, tanımlanmış ayrıntılarla bir görev veya bildirim oluşturur ve isteğe bağlı olarak grubu e-posta yoluyla bilgilendirir. Yapılandırılabilir bir sayısal öncelik değerine göre görev yürütmesini önceliklendirir.

## **Kartın Bileşenleri**

1. **Grup Adı (Group Name)**
   * **Açıklama:** Belgeyi ele almaktan sorumlu satınalma grubunu belirtir.
   * **Ayrıntı:** Kullanıcının satınalma grubunun adını manuel olarak girebileceği bir alan.
2. **Görev/Bildirim (Task/Notification)**
   * **Açıklama:** Grup için bir görev mi yoksa bildirim mi oluşturulacağını tanımlar.
   * **Ayrıntı:** Kullanıcının bir görev veya bildirim oluşturma arasında seçim yapabileceği bir alan
3. **Başlık (Title)**
   * **Açıklama:** Grup için oluşturulan görevin veya bildirimin başlığı.
   * **Ayrıntı:** Görev veya bildirim için kısa ve tanımlanabilir bir başlık sağlamak için bir alan.
4. **Açıklama (Description)**
   * **Açıklama:** Görev veya bildirim hakkında ek ayrıntılar.
   * **Ayrıntı:** Görevin amacını açıklamak ve bağlam veya talimatlar sağlamak için bir alan.
5. **Öncelik (Priority)**
   * **Açıklama:** Görevin veya bildirimin aciliyet düzeyini tanımlar.
   * **Seçenekler:**
     * **High:** Görev acil dikkat gerektirir.
     * **Medium:** Görev önemli ama acil değil.
     * **Low:** Görev daha sonra ele alınabilir.
6. **Posta Gönder (Send Mail)**
   * **Açıklama:** Gruba bir e-posta bildirimi gönderilip gönderilmeyeceğini yapılandırır.
   * **Seçenekler:**
     * **True:** Satınalma grubuna bir e-posta bildirimi gönderir.
     * **False:** E-posta bildirimi gönderilmez.
7. **Değer (Value)**
   * **Açıklama:** Görev yürütmesi için sayısal önceliği ayarlar.
   * **Ayrıntı:** Daha düşük bir sayının daha yüksek önceliği temsil ettiği sayısal bir değer girmek için bir alan.

## **İşlevsellik**

* **Koşul Değerlendirmesi:**\
  Kart, eylemlerini yalnızca tanımlanan iş akışı koşulları karşılanırsa gerçekleştirir.
* **Grup Ataması ve Görev/Bildirim Oluşturma:**\
  Belge, belirtilen satınalma grubuna atanır. Sağlanan başlık, açıklama ve öncelikle bir görev veya bildirim oluşturulur.
* **E-posta Bildirimi:**\
  "Send Mail" True olarak ayarlanırsa, grup görev veya bildirim hakkında bir e-posta alır.

## **Kurulum ve Yapılandırma**

1. **Grup Adını Tanımla:**
   * Group Name alanına satınalma grubunun adını girin.
2. **Görev/Bildirim Ayrıntılarını Yapılandır:**
   * Görev veya bildirim için Başlık ve Açıklama belirtin.
   * Açılır menüden Önceliği (High, Medium veya Low) seçin.
3. **E-posta Bildirimini Etkinleştir:**
   * Grubun bir e-posta alıp almamasına bağlı olarak "Send Mail"i True veya False olarak ayarlayın.
4. **Sayısal Önceliği Ayarla:**
   * Görevin önceliğini belirlemek için Değer alanına sayısal bir değer girin; daha düşük değerler önce işlenir.
5. Kart yapılandırmasını kaydedin ve iş akışını etkinleştirin.

## **Sonuç**

"Assign Document to Procurement Group and Create Task/Notification" iş akışı kartı, belgelerin açık görev talimatları ve öncelik düzeyleriyle uygun gruba yönlendirilmesini sağlar. İsteğe bağlı e-posta bildirimlerini mümkün kılarak, bu kart görev görünürlüğünü artırır ve sorunsuz iş akışı yürütmesini sağlar.
