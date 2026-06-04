# Single Document Status Condition

<figure><img src="../../../../.gitbook/assets/userlmn_928e514bc0e2aa775894e4ec5f992bd9 (1).png" alt="" width="528"><figcaption></figcaption></figure>

**Amaç**

Bu iş akışı kartı, tek, belirtilen bir belge durumuna göre belgeler üzerindeki işlemleri yönetmek için uyarlanmıştır. Koşulu tek bir duruma basitleştirerek, kart çok belirli iş akışı tetikleyicilerine odaklanır, bu da onu bir ERP sistemi içindeki hedefli belge işleme etkinlikleri için ideal kılar.

**Kartın Bileşenleri**

1. **Operatör**
   * **Açıklama**: Belgenin durumunu seçilen koşula karşı değerlendirme yöntemini belirtir.
   * **Seçenekler**:
     * **is**: Belgenin mevcut durumu seçilen durumla eşleşirse işlemi tetikler.
     * **is not**: Belgenin mevcut durumu seçilen durumla eşleşmezse işlemi tetikler.
2. **Durum**
   * **Açıklama**: Koşulu ayarlamak için tek bir belge durumunun seçilmesine olanak tanır.
   * **Durum Örnekleri**: "Error", "Export Error", "Ready in Validation", "Ready in Review", "Pending Approval", "Pending Second Approval".
   * **Ayrıntı**: Kullanıcılar bir açılır menüden veya bir dizi radyo düğmesinden bir durum seçer. Bu durum daha sonra kartın işlemi için ölçüt olarak hizmet eder.

**İşlevsellik**

* **Belge Durumu Tanımlama**: ERP sistemi aracılığıyla işlenirken bir belgenin mevcut durumunu tanımlar.
* **Koşul Değerlendirmesi**:
  * Seçilen operatöre (`is` veya `is not`) dayanarak, kart belgenin mevcut durumunun seçilen durum ölçütüyle uyumlu olup olmadığını kontrol eder.
* **Eylem Yürütme**:
  * **Doğru Koşul**: Durum eşleşirse (veya operatöre bağlı olarak eşleşmezse), karşılık gelen eylem başlatılır. Bu, daha fazla işleme için yönlendirme, bildirim oluşturma veya diğer önceden tanımlanmış iş akışları olabilir.
  * **Yanlış Koşul**: Koşul karşılanmazsa, hiçbir eylem gerçekleştirilmez veya alternatif bir yol tetiklenir.
* **Diğer İş Akışlarıyla Entegrasyon**: Tek durum değerlendirmesi için tasarlanmış olsa da, bu kart hassas belge işlemeyi sağlamak için daha geniş iş akışı dizilerine etkili bir şekilde entegre edilebilir.

**Kullanıcı Etkileşimleri**

* **Kurulum ve Yapılandırma**: Kullanıcılar, bir operatör seçerek ve ardından kullanılabilir seçenekler arasından bir durum seçerek kartı kurar. Bu seçim süreci basittir ve kafa karışıklığını önlemek için tasarlanmıştır.
* **İzleme ve Raporlama**: Belgelerin durumlarına göre işlenmesini izleyen sistem tarafından oluşturulan raporlar veya gösterge panelleri aracılığıyla izlemeyi mümkün kılar ve uygulanan iş akışlarının etkinliğini denetlemeye yardımcı olur.
* **Hata Yönetimi ve Bildirimler**: Herhangi bir işleme anomalisi konusunda kullanıcıları uyarmak veya ayarlanan koşulları karşılamayan belgeleri işaretlemek için yapılandırılabilir, böylece hızlı ilgi ve çözüm sağlanır.

#### Sonuç

"Single Document Status Condition" iş akışı kartı, bireysel durum koşullarına odaklanarak belge yönetimini basitleştirir. Bu özellik, özellikle sıkı işleme ölçütlerine sahip ortamlarda, belge akışları üzerinde hassas kontrolün gerekli olduğu durumlarda yardımcı olur. Kartın bu sürümünü net bir şekilde belgelemek, kullanıcıların uygulamasını tam olarak anlamasını ve günlük operasyonlarına etkili bir şekilde entegre etmesini sağlar, belge işlemede hem uyumluluğu hem de verimliliği artırır.
