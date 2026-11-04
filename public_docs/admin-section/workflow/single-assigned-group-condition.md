<figure><img src="../../../../.gitbook/assets/image (16) (2).png" alt="" width="563"><figcaption></figcaption></figure>

**Amaç:**
Bu iş akışı kartı, bir görevin veya belgenin belirli bir gruba atanıp atanmadığına bağlı olarak işlemleri yürütür. Grup atamasına bağlı olarak eylemleri tetiklemek veya önlemek için doğrudan bir koşul kullanır.

**Kartın Bileşenleri:**

1. **Operatör**
   * **Açıklama:** Grup atamasına uygulanacak mantıksal koşulu tanımlar.
   * **Seçenekler:**
     * **DIR (IS):** Belgenin veya görevin atanan grubu belirtilen grupla eşleşirse işlemi tetikler.
     * **DEĞİLDİR (IS NOT):** Belgenin veya görevin atanan grubu belirtilen grupla eşleşmezse işlemi tetikler.
2. **Grup**
   * **Açıklama:** Atanan grupla karşılaştırılacak grubu belirtir.
   * **Detay:** Bu alan, atamayı karşılaştırmak için tek bir grup seçmenize olanak tanır.

**İşlevsellik:**

* **Grup Ataması Tanımlama:** Belirli bir göreve veya belgeye atanan grubu otomatik olarak tanımlar.
* **Koşul Değerlendirmesi:**
  * **DIR** operatörünü kullanarak kart, atanan grubun belirtilen grupla eşleşip eşleşmediğini kontrol eder.
  * **DEĞİLDİR** operatörünü kullanarak kart, atanan grubun belirtilen grupla eşleşmemesini sağlar.
* **Eylem Yürütme:**
  * **Doğru Koşul:** Grup ataması koşulu karşılıyorsa (**DIR** veya **DEĞİLDİR**), bildirimler, görev başlatmaları, onaylar veya diğer iş akışı adımları gibi ilgili eylemler tetiklenir.
  * **Yanlış Koşul:** Koşul karşılanmazsa, belge veya görev farklı bir yönlendirmeden geçebilir veya alternatif eylemler belirlenebilir.

**Kullanıcı Etkileşimleri:**

* **Kurulum ve Yapılandırma:**
  Kullanıcılar bir operatör seçerek ve ilgili grubu belirterek kartı yapılandırır. Kurulum basit ve sezgisel olmalıdır.
* **İzleme ve Raporlama:**
  Sistem, bu kart tarafından tetiklenen işlemleri izlemek ve raporlamak için işlevsellik sağlamalı, atama doğruluğu ve süreç verimliliği hakkında bilgiler sunmalıdır.
* **Hata İşleme ve Bildirimler:**
  Kullanıcılar, atanmamış görevler veya grup seçimindeki hatalar gibi atamalarla ilgili sorunlar olduğunda uyarı veya bildirim alma seçeneklerine sahip olmalıdır.

**Sonuç:**
"Atanan Grup Koşulu" iş akışı kartı, grup atamalarına dayalı belge ve görev iş akışlarını yönetmek için gereklidir. Bir görevin veya belgenin belirli bir gruba atanıp atanmadığına bağlı koşullara izin vererek, iş akışlarının yalnızca uygun grup etkileşimleri tarafından tetiklenmesini sağlar, görev yönetimini ve iş akışı verimliliğini artırır.
