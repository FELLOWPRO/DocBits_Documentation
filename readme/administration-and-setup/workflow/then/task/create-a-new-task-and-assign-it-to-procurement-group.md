# Create a New Task and assign it to Procurement Group

<figure><img src="../../../../.gitbook/assets/image (292).png" alt="" width="563"><figcaption></figcaption></figure>

## **Amaç:**

**"Create Task for Procurement Group"** iş akışı kartı, yapılandırmada belirtilen satınalma grubuna dinamik olarak atanan yeni bir görev oluşturur. Bu görev farklı öncelik düzeyleriyle atanabilir ve grubu görev hakkında bilgilendirmek için isteğe bağlı bir e-posta bildirimi gönderilebilir. Bu kart, iş akışı koşullarına göre doğru ekibin uyarılmasını sağlar.

## **Kartın Bileşenleri:**

1. **Başlık (Title)**
   * **Açıklama:** Görevin başlığını belirtir.
   * **Ayrıntı:** Bu alan, oluşturulan görevi tanımlar ve kolay tanımlama için kısa bir başlık sağlar.
2. **Açıklama (Description)**
   * **Açıklama:** Görev hakkında daha fazla ayrıntı sağlar.
   * **Ayrıntı:** Bu alan, görevin amacını ve gerekli bağlam veya talimatları açıklamak için kullanılır.
3. **Öncelik (Priority)**
   * **Açıklama:** Görevin aciliyetini tanımlar.
   * **Seçenekler:**
     * **High:** Görev acil dikkat gerektirir.
     * **Medium:** Görev önemli ama acil değil.
     * **Low:** Görev daha sonra ele alınabilir.
4. **Grup Adı (Group Name)**
   * **Açıklama:** Görevin atanacağı satınalma grubunu belirtir.
   * **Ayrıntı:** Bu alan, görevden sorumlu satınalma grubunu belirler. Görevin doğru ekibe yönlendirilmesini sağlar.
5. **E-posta Bildirimi (Email Notification)**
   * **Açıklama:** Atanan satınalma grubuna bir e-posta bildirimi gönderilip gönderilmeyeceğini yapılandırır.
   * **Seçenekler:**
     * **True:** Satınalma grubuna bir e-posta bildirimi gönderir.
     * **False:** E-posta bildirimi gönderilmez.

## **İşlevsellik:**

* **Koşul Değerlendirmesi:**\
  Kart, eylemini yalnızca hem **"Where"** hem de **"And Bölümleri"** doğru olarak değerlendirilirse yürütür.
* **Görev Oluşturma:**\
  Kart, "Group Name" alanında tanımlanan satınalma grubuna atayarak yeni bir görev oluşturur. Bu görev, belirtilen başlık, açıklama ve öncelik düzeyini içerecektir.
* **E-posta Bildirimi:**\
  E-posta bildirim seçeneği true olarak ayarlanırsa, satınalma grubuna görev hakkında bilgilendiren bir e-posta gönderilir.

## **Kurulum ve Yapılandırma:**

* **Görev Ayrıntılarını Tanımla:**\
  Görevin başlığını, açıklamasını ve öncelik düzeyini girin.
* **Satınalma Grubu Seç:**\
  Görevden sorumlu olacak satınalma grubunu seçin.
* **E-posta Bildirimini Etkinleştir:**\
  Görev oluşturma üzerine gruba bir e-posta bildirimi gönderilip gönderilmeyeceğini belirtin.

## **Sonuç:**

"Create Task for Procurement Group" iş akışı kartı, görevlerin tanımlanmış önceliklerle uygun satınalma grubuna otomatik olarak atanmasını sağlar. Bu kart ayrıca görevlerin hemen ele alınmasını sağlamak için grubu e-posta yoluyla bilgilendirebilir, iş akışı verimliliğini ve görev yönetimini iyileştirir.
