<figure><img src="../../../../.gitbook/assets/docbits_assigned_user_cond.png" alt="DocBits Assigned Usuario Cond" width="552"><figcaption></figcaption></figure>

**Amaç**

Bu iş akışı kartı, bir görevin veya belgenin belirli bir kullanıcıya veya kullanıcı kümesine atanıp atanmadığına bağlı olarak işlemlerin yürütülmesini yönetir. Belirli eylemleri tetiklemek veya önlemek için koşullu mantık kullanır; bu da onu kullanıcıya özel işleme gerektiren iş akışları için ideal hale getirir.

**Kartın Bileşenleri**

1. **Operatör**
   * **Açıklama**: Kullanıcı atamasına uygulanacak mantıksal koşulu tanımlar.
   * **Seçenekler**:
     * **DIR (IS)**: Belgenin veya görevin atanan kullanıcısı belirtilen listedeki herhangi bir kullanıcıyla eşleşirse işlemi tetikler.
     * **DEĞİLDİR (IS NOT)**: Belgenin veya görevin atanan kullanıcısı belirtilen listedeki herhangi bir kullanıcıyla eşleşmezse işlemi tetikler.
2. **Kullanıcı Listesi**
   * **Açıklama**: Atanan kullanıcıyla karşılaştırılacak kullanıcıların bir listesi veya seçimi.
   * **Detay**: Bu liste bir veya birden fazla kullanıcıyı içerebilir, bu da kartın hem tekil hem de çoklu kullanıcı koşullarını etkili bir şekilde işlemesini sağlar. Seçim, onay kutuları, çoklu seçim açılır menüsü veya benzeri kullanıcı arabirimi öğeleri aracılığıyla yapılabilir.

**İşlevsellik**

* **Kullanıcı Ataması Tanımlama**: ERP sistemi içindeki belirli bir göreve veya belgeye atanan kullanıcıyı veya kullanıcıları otomatik olarak tanımlar.
* **Koşul Değerlendirmesi**:
  * **DIR** operatörünü kullanarak kart, atanan kullanıcının Kullanıcı Listesinde listelenenler arasında olup olmadığını kontrol eder.
  * **DEĞİLDİR** operatörünü kullanarak kart, atanan kullanıcının listelenenler arasında olmamasını sağlar.
* **Eylem Yürütme**:
  * **Doğru Koşul**: Kullanıcı ataması koşulu karşılıyorsa (DIR veya DEĞİLDİR), bildirimler, görev başlatmaları, onaylar veya diğer iş akışı adımları gibi ilgili eylemler tetiklenir.
  * **Yanlış Koşul**: Koşul karşılanmazsa iş akışı devam etmez.

**Kullanıcı Etkileşimleri**

* **Kurulum ve Yapılandırma**: Kullanıcılar bir operatör seçerek ve Kullanıcı Listesinden ilgili kullanıcıları belirterek kartı yapılandırır. Kurulum, potansiyel olarak büyük kullanıcı tabanlarından seçim yapılmasına olanak tanıyacak şekilde kullanıcı dostu ve sezgisel olmalıdır.
* **İzleme ve Raporlama**: ERP sistemi, bu kart tarafından tetiklenen işlemleri izlemek ve raporlamak için işlevsellik sağlamalı, atama doğruluğu ve süreç verimliliği hakkında bilgiler sunmalıdır.
* **Hata İşleme ve Bildirimler**: Kullanıcılar, atanmamış görevler veya kullanıcı seçimindeki hatalar gibi atamalarla ilgili sorunlar olduğunda uyarı veya bildirim alma seçeneklerine sahip olmalıdır.

#### Sonuç

"Atanan Kullanıcı Koşulu" iş akışı kartı, kullanıcı atamalarına bağlı belge ve görev iş akışlarını yönetmek için kritik bir araçtır. Bir görevin veya belgenin belirli kullanıcılara atanıp atanmadığına bağlı koşullara izin vererek, iş akışlarının yalnızca uygun kullanıcı etkileşimleri tarafından tetiklenmesini sağlar, ekipler içinde hem hesap verebilirliği hem de görev uyumunu artırır. Bu kartın açıkça belgelenmesi, kullanıcıların önemini anlamalarına ve iş akışlarına etkili bir şekilde entegre etmelerine yardımcı olacak, kullanıcı rollerine ve sorumluluklarına göre uyarlanmış sorunsuz ve verimli işlemler sağlayacaktır.
