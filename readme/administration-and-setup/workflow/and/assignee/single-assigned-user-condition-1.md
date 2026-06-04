# Single Assigned User Condition

<figure><img src="../../../../.gitbook/assets/image (16) (2).png" alt="" width="563"><figcaption></figcaption></figure>

**Amaç:**\
Bu iş akışı kartı, bir görevin veya belgenin belirli bir gruba atanıp atanmadığına göre işlemler yürütür. Grup atamasına göre eylemleri tetiklemek veya engellemek için basit bir koşul kullanır.

**Kartın Bileşenleri:**

1. **Operatör**
   * **Açıklama:** Grup atamasına uygulanacak mantıksal koşulu tanımlar.
   * **Seçenekler:**
     * **IS:** Belgenin veya görevin atanan grubu belirtilen grupla eşleşiyorsa işlemi tetikler.
     * **IS NOT:** Belgenin veya görevin atanan grubu belirtilen grupla eşleşmiyorsa işlemi tetikler.
2. **Grup**
   * **Açıklama:** Atanan grupla karşılaştırılacak grubu belirtir.
   * **Ayrıntı:** Bu alan, atamayı karşılaştırmak için tek bir grup seçmenize olanak tanır.

**İşlevsellik:**

* **Grup Atama Tanımlama:** Belirli bir göreve veya belgeye atanan grubu otomatik olarak tanımlar.
* **Koşul Değerlendirmesi:**
  * **IS** operatörünü kullanarak, kart atanan grubun belirtilen grupla eşleşip eşleşmediğini kontrol eder.
  * **IS NOT** operatörünü kullanarak, kart atanan grubun belirtilen grupla eşleşmediğini garanti eder.
* **Eylem Yürütme:**
  * **Doğru Koşul:** Grup ataması koşulu karşılarsa (**IS** veya **IS NOT**), bildirimler, görev başlatmaları, onaylar veya diğer iş akışı adımları gibi ilgili eylemler tetiklenir.
  * **Yanlış Koşul:** Koşul karşılanmazsa, belge veya görev farklı bir yönlendirmeden geçebilir ya da alternatif eylemler belirtilebilir.

**Kullanıcı Etkileşimleri:**

* **Kurulum ve Yapılandırma:**\
  Kullanıcılar bir operatör seçerek ve ilgili grubu belirterek kartı yapılandırır. Kurulum basit ve sezgisel olmalıdır.
* **İzleme ve Raporlama:**\
  Sistem, bu kart tarafından tetiklenen işlemleri izleme ve raporlama işlevselliği sağlamalı, atama doğruluğu ve süreç verimliliği hakkında öngörüler sunmalıdır.
* **Hata Yönetimi ve Bildirimler:**\
  Kullanıcılar, atanmamış görevler veya grup seçiminde hatalar gibi atamalarla ilgili sorunlar olduğunda uyarı veya bildirim alma seçeneklerine sahip olmalıdır.

**Sonuç:**\
"Assigned Group Condition" iş akışı kartı, grup atamalarına dayalı belge ve görev iş akışlarını yönetmek için gereklidir. Bir görevin veya belgenin belirli bir gruba atanıp atanmadığına dayalı koşullara izin vererek, iş akışlarının yalnızca uygun grup etkileşimleriyle tetiklenmesini sağlar ve görev yönetimi ile iş akışı verimliliğini artırır.
