# Assigned Group Condition

<figure><img src="../../../../.gitbook/assets/image (15) (1) (2).png" alt="" width="563"><figcaption></figcaption></figure>

**Amaç:**

Bu iş akışı kartı, bir görevin veya belgenin belirli bir gruba ya da grup kümesine atanıp atanmadığına göre işlemler yürütür. Grup atamasına bağlı olarak belirli eylemleri ya tetiklemek ya da engellemek için koşullu mantık kullanır, bu da onu gruba özgü işleme gerektiren iş akışları için ideal kılar.

**Kartın Bileşenleri:**

1. **Operatör**
   * **Açıklama:** Grup atamasına uygulanacak mantıksal koşulu tanımlar.
   * **Seçenekler:**
     * **IS:** Belgenin veya görevin atanan grubu belirtilen listedeki gruplardan biriyle eşleşiyorsa işlemi tetikler.
     * **IS NOT:** Belgenin veya görevin atanan grubu belirtilen listedeki gruplardan hiçbiriyle eşleşmiyorsa işlemi tetikler.
2. **Gruplar Listesi**
   * **Açıklama:** Atanan grupla karşılaştırılacak grupların bir listesi veya seçimi.
   * **Ayrıntı:** Bu liste bir veya birden fazla grup içerebilir, böylece kartın hem tekli hem de çoklu grup koşullarını etkili bir şekilde ele almasına olanak tanır.

**İşlevsellik:**

* **Grup Atama Tanımlama:** Sistem içinde belirli bir göreve veya belgeye atanan grubu ya da grupları otomatik olarak tanımlar.
* **Koşul Değerlendirmesi:**
  * **IS** operatörünü kullanarak, kart atanan grubun Gruplar Listesinde listelenen gruplardan biri olup olmadığını kontrol eder.
  * **IS NOT** operatörünü kullanarak, kart atanan grubun listelenen grupların parçası olmadığını garanti eder.
* **Eylem Yürütme:**
  * **Doğru Koşul:** Grup ataması koşulu karşılarsa (**IS** veya **IS NOT**), bildirimler, görev başlatmaları, onaylar veya diğer iş akışı adımları gibi ilgili eylemler tetiklenir.
  * **Yanlış Koşul:** Koşul karşılanmazsa, iş akışı devam etmez.

**Kullanıcı Etkileşimleri:**

* **Kurulum ve Yapılandırma:** Kullanıcılar bir operatör seçerek ve Gruplar Listesinden ilgili grupları belirterek kartı yapılandırır. Kurulum, potansiyel olarak büyük grup tabanlarından seçimleri karşılayacak şekilde kullanıcı dostu ve sezgisel olmalıdır.
* **İzleme ve Raporlama:**\
  Sistem, bu kart tarafından tetiklenen işlemleri izleme ve raporlama işlevselliği sağlamalı, atama doğruluğu ve süreç verimliliği hakkında öngörüler sunmalıdır.
* **Hata Yönetimi ve Bildirimler:**\
  Kullanıcılar, atanmamış görevler veya grup seçiminde hatalar gibi atamalarla ilgili sorunlar olduğunda uyarı veya bildirim alma seçeneklerine sahip olmalıdır.

**Sonuç:**\
"Assigned Group Condition" iş akışı kartı, grup atamalarına bağlı belge ve görev iş akışlarını yönetmek için gereklidir. Bir görevin veya belgenin belirli gruplara atanıp atanmadığına dayalı koşullara izin vererek, iş akışlarının yalnızca uygun grup etkileşimleriyle tetiklenmesini sağlar ve ekipler arasında hesap verebilirliği ve görev yönetimini iyileştirir.
