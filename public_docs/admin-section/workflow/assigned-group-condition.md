<figure><img src="../../../../.gitbook/assets/image (15) (1) (2).png" alt="" width="563"><figcaption></figcaption></figure>

**Amaç:**

Bu iş akışı kartı, bir görevin veya belgenin belirli bir gruba veya grup kümesine atanıp atanmadığına bağlı olarak işlemleri yürütür. Grup atamasına bağlı olarak belirli eylemleri tetiklemek veya önlemek için koşullu mantık kullanır; bu da onu gruba özel işleme gerektiren iş akışları için ideal hale getirir.

**Kartın Bileşenleri:**

1. **Operatör**
   * **Açıklama:** Grup atamasına uygulanacak mantıksal koşulu tanımlar.
   * **Seçenekler:**
     * **DIR (IS):** Belgenin veya görevin atanan grubu belirtilen listedeki gruplardan biriyle eşleşirse işlemi tetikler.
     * **DEĞİLDİR (IS NOT):** Belgenin veya görevin atanan grubu belirtilen listedeki gruplardan hiçbiriyle eşleşmezse işlemi tetikler.
2. **Grup Listesi**
   * **Açıklama:** Atanan grupla karşılaştırılacak grupların bir listesi veya seçimi.
   * **Detay:** Bu liste bir veya birden fazla grubu içerebilir, bu da kartın hem tekil hem de çoklu grup koşullarını etkili bir şekilde işlemesini sağlar.

**İşlevsellik:**

* **Grup Ataması Tanımlama:** Sistem içindeki belirli bir göreve veya belgeye atanan grubu veya grupları otomatik olarak tanımlar.
* **Koşul Değerlendirmesi:**
  * **DIR** operatörünü kullanarak kart, atanan grubun Grup Listesinde listelenen gruplardan biri olup olmadığını kontrol eder.
  * **DEĞİLDİR** operatörünü kullanarak kart, atanan grubun listelenen grupların bir parçası olmamasını sağlar.
* **Eylem Yürütme:**
  * **Doğru Koşul:** Grup ataması koşulu karşılıyorsa (**DIR** veya **DEĞİLDİR**), bildirimler, görev başlatmaları, onaylar veya diğer iş akışı adımları gibi ilgili eylemler tetiklenir.
  * **Yanlış Koşul:** Koşul karşılanmazsa iş akışı devam etmez.

**Kullanıcı Etkileşimleri:**

* **Kurulum ve Yapılandırma:** Kullanıcılar bir operatör seçerek ve Grup Listesinden ilgili grupları belirterek kartı yapılandırır. Kurulum, potansiyel olarak büyük grup tabanlarından seçim yapılmasına olanak tanıyacak şekilde kullanıcı dostu ve sezgisel olmalıdır.
* **İzleme ve Raporlama:**
  Sistem, bu kart tarafından tetiklenen işlemleri izlemek ve raporlamak için işlevsellik sağlamalı, atama doğruluğu ve süreç verimliliği hakkında bilgiler sunmalıdır.
* **Hata İşleme ve Bildirimler:**
  Kullanıcılar, atanmamış görevler veya grup seçimindeki hatalar gibi atamalarla ilgili sorunlar olduğunda uyarı veya bildirim alma seçeneklerine sahip olmalıdır.

**Sonuç:**
"Atanan Grup Koşulu" iş akışı kartı, grup atamalarına bağlı belge ve görev iş akışlarını yönetmek için gereklidir. Bir görevin veya belgenin belirli gruplara atanıp atanmadığına bağlı koşullara izin vererek, iş akışlarının yalnızca uygun grup etkileşimleri tarafından tetiklenmesini sağlar, ekipler arasında hesap verebilirliği ve görev yönetimini geliştirir.
