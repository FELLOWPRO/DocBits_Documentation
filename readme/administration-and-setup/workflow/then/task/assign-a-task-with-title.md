# Assign a Task with Title

<figure><img src="../../../../.gitbook/assets/image (291).png" alt="" width="563"><figcaption></figcaption></figure>

## **Amaç:**

"Assign Task / Notification from Decision Table" iş akışı kartı, bir karar tablosunun sonuçlarına göre görevleri veya bildirimleri dinamik olarak atamak için tasarlanmıştır. Bu kart, görevlerin veya bildirimlerin karar tablosunda tanımlanan mantığa göre doğru kullanıcıya veya gruba atanmasını sağlar; alıcıya gönderilen isteğe bağlı bir e-posta bildirimiyle birlikte.

## **Kartın Bileşenleri:**

1. **Başlık (Title)**
   * **Açıklama**: Oluşturulan görevin veya bildirimin başlığını belirtir.
   * **Ayrıntı**: Başlık bağlam sağlamalı ve görevin veya bildirimin amacını açıklamalıdır.
2. **Açıklama (Description)**
   * **Açıklama**: Görevin veya bildirimin içeriğini veya amacını tanımlar.
   * **Ayrıntı**: Görev veya bildirim hakkında ek bilgi sağlar, bağlamı veya gerekli eylemi açıklar.
3. **Öncelik (Priority)**
   * **Açıklama**: Görevin veya bildirimin aciliyet düzeyini tanımlar.
   * **Seçenekler**:
     * **High**: Acil dikkat gerektiren görevler veya bildirimler.
     * **Medium**: Hemen ele alınması gereken önemli görevler.
     * **Low**: Daha sonra ele alınabilecek görevler.
4. **Atanan Türü (Assignee Type)**
   * **Açıklama**: Karar tablosunun çıktısına göre göreve veya bildirime atanan kullanıcıyı veya grubu belirtir.
   * **Ayrıntı**: Karar tablosu, koşulları dinamik olarak değerlendirir ve atama için uygun kullanıcıyı veya grubu döndürür.
5. **E-posta Bildirimi (Email Notification)**
   * **Açıklama**: Atanan kullanıcıya veya gruba bir e-posta bildirimi gönderilip gönderilmeyeceğini yapılandırır.
   * **Seçenekler**:
     * **True**: Alıcıya bir e-posta bildirimi gönderir.
     * **False**: E-posta bildirimi gönderilmez.

#### **Sürüm 3'teki Ek Bileşenler**

1. **Bildirim Türü (Notification Type)**
   * **Açıklama**: Kartın bir görev mi yoksa bir bildirim mi oluşturacağını belirtir.
   * **Seçenekler**:
     * **Task**: Karar tablosundan kullanıcıya veya gruba atanan bir görev oluşturur.
     * **Notification**: Karar tablosundan kullanıcıya veya gruba bir bildirim gönderir.

## **İşlevsellik:**

* **Koşul Değerlendirmesi:**\
  Kart, eylemini yalnızca hem **"Where"** hem de **"And Bölümleri"** doğru olarak değerlendirilirse yürütür.
* **Görev / Bildirim Ataması**\
  Kart, görevi veya bildirimi karar tablosu tarafından tanımlanan kullanıcıya veya gruba atar. Karar tablosu, önceden tanımlanmış koşulları dinamik olarak değerlendirir ve karşılık gelen alıcıyı döndürür.
* **E-posta Bildirimi**\
  Bunun için yapılandırılmışsa, atanan kullanıcıya veya gruba bir e-posta bildirimi gönderilir.
* **Sürüm 3 İşlevselliği**\
  Sürüm 3'te, kart bir Görev veya bir Bildirim oluşturulmasına olanak tanır ve görev yönetimi ile iletişim için daha fazla esneklik sağlar.

## **Kurulum ve Yapılandırma:**

1. **Görev veya Bildirim Ayrıntılarını Tanımla**:\
   Görev veya bildirim için başlığı, açıklamayı ve önceliği girin.
2. **Karar Tablosunu Yapılandır**:\
   Hangi kullanıcının veya grubun göreve veya bildirime atanması gerektiğini dinamik olarak belirlemek için karar tablosunu ayarlayın.
3. **E-posta Bildirimini Etkinleştir**:\
   Atanan kullanıcıya veya gruba bir e-posta bildirimi gönderilip gönderilmeyeceğini belirtin.
4. **Bildirim Türünü Belirt (Sürüm 3)**:\
   Kartın bir görev mi oluşturacağını yoksa bir bildirim mi göndereceğini seçin.

## **Sonuç:**

**"Assign Task / Notification from Decision Table"** iş akışı kartı, bir karar tablosunda tanımlanan dinamik koşullara göre görevlerin veya bildirimlerin atanmasını otomatikleştirir. Sürüm 3, kullanıcıların bir görev veya bildirim oluşturma arasında seçim yapmasına olanak tanıyarak işlevselliğini geliştirir ve her zaman doğru alıcının atanmasını sağlar. E-posta bildirim özelliği, kullanıcıları bilgilendirir, iletişimi ve görev yönetimini kolaylaştırır.
