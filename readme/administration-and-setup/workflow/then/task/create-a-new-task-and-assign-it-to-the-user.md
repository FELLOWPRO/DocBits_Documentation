# Create a New Task and assign it to the User

<figure><img src="../../../../.gitbook/assets/image (287).png" alt="" width="563"><figcaption></figcaption></figure>

## **Amaç**

**"Create Task or Notification"** iş akışı kartı, iş akışları içinde görev yönetimini ve bildirimleri kolaylaştırır. Sürüme bağlı olarak, kart görevler oluşturabilir, bildirimler gönderebilir ve dinamik işleme için karar ağaçları gibi ek işlevsellikten yararlanabilir.

## **Kartın Bileşenleri**

1. **Başlık (Title)**
   * **Açıklama**: Oluşturulan görevin veya bildirimin başlığını tanımlar.
   * **Ayrıntı**: Başlık, görev veya bildirim için açık ve kısa bir tanımlayıcı sağlar.
2. **Açıklama (Description)**
   * **Açıklama**: Görev veya bildirim hakkında ayrıntılar sağlar.
   * **Ayrıntı**: Atanan kullanıcı için görevin veya bildirimin amacına veya bağlamına açıklık getirmeye yardımcı olur.
3. **Öncelik (Priority)**
   * **Açıklama**: Görev için aciliyet düzeyini ayarlar.
   * **Seçenekler**:
     * **High**: Acil dikkat gerektirir.
     * **Medium**: Önemli ama acil değil.
     * **Low**: Daha sonra ele alınabilir.
4. **Atanan Kullanıcı (Assigned User)**
   1. **Açıklama**: Görevin atandığı kullanıcıyı belirtir.
   2. **Ayrıntı**: Kullanıcılar, kullanılabilir personelin açılır listesinden seçilir.
5. **E-posta Bildirimi (Email Notification)**
   * **Açıklama**: Atanan kullanıcının bir e-posta bildirimi alıp almayacağını belirler.
   * **Seçenekler**:
     * **True**: Kullanıcıya bir e-posta bildirimi gönderir.
     * **False**: E-posta bildirimi gönderilmez.

## Sürüm 3 ve Sürüm 4'teki Ek Bileşenler

1. **Karar Ağacı (Yalnızca Sürüm 3)**
   * **Açıklama**: Dinamik görev oluşturma için bir karar ağacının kullanımını etkinleştirir.
   * **Seçenekler**:
     * **True**: Karar ağacı işlemesini etkinleştirir.
     * **False**: Karar ağacı işlemesini devre dışı bırakır.
2. **Görev veya Bildirim (Yalnızca Sürüm 4)**
   * **Açıklama**: Bir görev veya bir bildirim oluşturma arasında seçim yapmaya olanak tanır.
   * **Seçenekler**:
     * **Task**: Bir görev oluşturur.
     * **Notification**: Görev yerine bir bildirim oluşturur.

## **İşlevsellik:**

* **Koşul Değerlendirmesi**:\
  Bu kart yalnızca **"Where"** ve **"And Bölümleri"**ndeki koşullar karşılanırsa tetiklenir.
* **Görev veya Bildirim Oluşturma**:
  * Sürüm 2 ve 3: Belirtilen başlık, açıklama, öncelik ve atanan kullanıcıyla bir görev oluşturulur.
  * Sürüm 4: Bir görev veya bir bildirim oluşturmaya olanak tanır.
* **Dinamik Atama**:
  * Sürüm 3'te, karar ağacı iş akışı parametrelerine göre göreve atanacak kullanıcıyı dinamik olarak belirler.
* **E-posta Bildirimi**:\
  Bildirim seçeneği etkinse atanan kullanıcıya bir e-posta gönderir.

## **Kurulum ve Yapılandırma:**

1. **Sürüm Seç**: Gereken işlevselliğe göre kartın sürümünü seçin:
   * Sürüm 2: Manuel kullanıcı ataması ve e-posta bildirimleriyle temel görev oluşturma.
   * Sürüm 3: Dinamik kullanıcı ataması için karar ağacı işlevselliği içerir.
   * Sürüm 4: Görev yerine bir bildirim oluşturma yeteneğini ekler.
2. **Görev Ayrıntılarını Gir**: Görevin veya bildirimin başlığını, açıklamasını ve önceliğini belirtin.
3. **Kullanıcı Ata**:
   * Sürüm 2 ve 4 için, açılır listeden manuel olarak bir kullanıcı seçin.
   * Sürüm 3 için, atanan kullanıcıyı dinamik olarak belirlemek için karar ağacını etkinleştirin.
4. **E-posta Bildirimini Etkinleştir**: Atanan kullanıcının bir e-posta bildirimi alıp almayacağını belirtin.
5. (Sürüm 4 için) **Görev veya Bildirim Seç**: Bir görev mi yoksa bildirim mi oluşturulacağını belirtin.

## **Sonuç:**

**"Create Task or Notification"** iş akışı kartı, görevleri ve bildirimleri yönetmek için çok yönlü bir araçtır. Karar ağaçları aracılığıyla dinamik kullanıcı atamasını destekleyerek ve görev veya bildirim oluşturma için seçenekler sunarak, iş akışı uyarlanabilirliğini ve işbirliği verimliliğini artırır.
