# Assigned User Condition

<figure><img src="../../../../.gitbook/assets/userlmn_5e16e9b23626ec1211c753fec5333513 (1).png" alt="" width="552"><figcaption></figcaption></figure>

**Amaç**

Bu iş akışı kartı, bir görevin veya belgenin belirli bir kullanıcıya ya da kullanıcı kümesine atanıp atanmadığına göre işlemlerin yürütülmesini yönetir. Belirli eylemleri ya tetiklemek ya da engellemek için koşullu mantık kullanır, bu da onu kullanıcıya özgü işleme gerektiren iş akışları için ideal kılar.

**Kartın Bileşenleri**

1. **Operatör**
   * **Açıklama**: Kullanıcı atamasına uygulanacak mantıksal koşulu tanımlar.
   * **Seçenekler**:
     * **IS**: Belgenin veya görevin atanan kullanıcısı belirtilen listedeki herhangi bir kullanıcıyla eşleşiyorsa işlemi tetikler.
     * **IS NOT**: Belgenin veya görevin atanan kullanıcısı belirtilen listedeki herhangi bir kullanıcıyla eşleşmiyorsa işlemi tetikler.
2. **Kullanıcı Listesi**
   * **Açıklama**: Atanan kullanıcıyla karşılaştırılacak kullanıcıların bir listesi veya seçimi.
   * **Ayrıntı**: Bu liste bir veya birden fazla kullanıcı içerebilir, böylece kartın hem tekli hem de çoklu kullanıcı koşullarını etkili bir şekilde ele almasına olanak tanır. Seçim, onay kutuları, çoklu seçim açılır menüsü veya benzer arayüz öğeleri aracılığıyla yapılabilir.

**İşlevsellik**

* **Kullanıcı Atama Tanımlama**: ERP sistemi içinde belirli bir göreve veya belgeye atanan kullanıcıyı ya da kullanıcıları otomatik olarak tanımlar.
* **Koşul Değerlendirmesi**:
  * **IS** operatörünü kullanarak, kart atanan kullanıcının Kullanıcı Listesinde listelenenler arasında olup olmadığını kontrol eder.
  * **IS NOT** operatörünü kullanarak, kart atanan kullanıcının listelenenler arasında olmadığını garanti eder.
* **Eylem Yürütme**:
  * **Doğru Koşul**: Kullanıcı ataması koşulu karşılarsa (IS veya IS NOT), bildirimler, görev başlatmaları, onaylar veya diğer iş akışı adımları gibi ilgili eylemler tetiklenir.
  * **Yanlış Koşul**: Koşul karşılanmazsa, iş akışı devam etmez.

**Kullanıcı Etkileşimleri**

* **Kurulum ve Yapılandırma**: Kullanıcılar bir operatör seçerek ve Kullanıcı Listesinden ilgili kullanıcıları belirterek kartı yapılandırır. Kurulum, potansiyel olarak büyük kullanıcı tabanlarından seçimleri karşılayacak şekilde kullanıcı dostu ve sezgisel olmalıdır.
* **İzleme ve Raporlama**: ERP sistemi, bu kart tarafından tetiklenen işlemleri izleme ve raporlama işlevselliği sağlamalı, atama doğruluğu ve süreç verimliliği hakkında öngörüler sunmalıdır.
* **Hata Yönetimi ve Bildirimler**: Kullanıcılar, atanmamış görevler veya kullanıcı seçiminde hatalar gibi atamalarla ilgili sorunlar olduğunda uyarı veya bildirim alma seçeneklerine sahip olmalıdır.

#### Sonuç

"Assigned User Condition" iş akışı kartı, kullanıcı atamalarına bağlı belge ve görev iş akışlarını yönetmek için kritik bir araçtır. Bir görevin veya belgenin belirli kullanıcılara atanıp atanmadığına dayalı koşullara izin vererek, iş akışlarının yalnızca uygun kullanıcı etkileşimleriyle tetiklenmesini sağlar ve ekipler içinde hem hesap verebilirliği hem de görev hizalamasını artırır. Bu kartı net bir şekilde belgelemek, kullanıcıların önemini anlamasına ve iş akışlarına etkili bir şekilde entegre etmesine yardımcı olur, kullanıcı rollerine ve sorumluluklarına göre uyarlanmış sorunsuz ve verimli operasyonlar sağlar.
