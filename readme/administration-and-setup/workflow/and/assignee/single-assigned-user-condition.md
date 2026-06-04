# Single Assigned User Condition

<figure><img src="../../../../.gitbook/assets/userlmn_77e991cee96598023f9a3ac7ad230e50 (1).png" alt="" width="552"><figcaption></figcaption></figure>

**Amaç**

Bu iş akışı kartı, bir görevin veya belgenin tek, belirli bir kullanıcıya atanmasına göre işlemleri kolaylaştırır. Doğrudan koşullu mantık yaklaşımı kullanarak, hedefli kullanıcı katılımı gerektiren iş akışlarını yönetir ve kullanıcı tabanlı görev işlemede hassasiyet sağlar.

**Kartın Bileşenleri**

1. **Operatör**
   * **Açıklama**: Kullanıcı atamasına uygulanacak mantığı belirtir.
   * **Seçenekler**:
     * **IS**: Belgenin veya görevin atanan kullanıcısı belirtilen kullanıcıyla eşleşiyorsa işlemi tetikler.
     * **IS NOT**: Atanan kullanıcı belirtilen kullanıcıyla eşleşmiyorsa işlemi tetikler.
2. **Kullanıcı**
   * **Açıklama**: Atanan kullanıcının karşılaştırılacağı tek bir kullanıcının seçimine olanak tanır.
   * **Ayrıntı**: Bu, aynı anda bir kullanıcının seçilebileceği basit bir açılır menü veya otomatik tamamlama alanını içerir.

**İşlevsellik**

* **Kullanıcı Atama Tanımlama**: Belirli bir göreve veya belgeye şu anda atanan kullanıcıyı tanımlar.
* **Koşul Değerlendirmesi**:
  * **IS** operatörü için, kart atanan kullanıcının seçilen kullanıcıyla aynı olup olmadığını kontrol eder.
  * **IS NOT** operatörü için, atanan kullanıcının seçilen kullanıcıdan farklı olduğunu doğrular.
* **Eylem Yürütme**:
  * **Doğru Koşul**: Atama ayarlanan koşulu karşılarsa (IS veya IS NOT), önaylarla devam etme, başka görevler başlatma, bildirim gönderme veya diğer ilgili iş akışlarını içerebilecek önceden tanımlanmış eylemleri tetikler.
  * **Yanlış Koşul**: Koşul karşılanmazsa, iş akışı devam etmez.

**Kullanıcı Etkileşimleri**

* **Kurulum ve Yapılandırma**: Kullanıcılar bir operatör seçerek ve kullanıcı alanından bir kullanıcı seçerek kartı kurar. Bu kurulum, kolay kullanıcı seçimi ve yapılandırması sağlayacak şekilde basit olmalıdır.
* **İzleme ve Raporlama**: Belirli kullanıcı atamalarıyla hangi görevlerin tetiklendiğini ve bu tetiklemelerin sonuçlarını izleme gibi kartın performansını izlemek için araçlar sunar.
* **Hata Yönetimi ve Bildirimler**: Görevler yanlış atanırsa veya atama sorunları nedeniyle operasyonel hatalar oluşursa kullanıcıları uyarmak için mekanizmalar sağlar.

#### Sonuç

"Single Assigned User Condition" iş akışı kartı, bir ERP sistemi içinde hassas, kullanıcıya özgü belge ve görev yönetimi için gereklidir. Bireysel kullanıcı atamalarına odaklanarak iş akışlarını basitleştirir, böylece eylemlerin yalnızca uygun olduğunda, kullanıcının rolüne ve sorumluluklarına göre yürütülmesini sağlar. Bu kartı net bir şekilde belgelemek, kullanıcıların uygulamasını anlamasına yardımcı olur ve günlük operasyonları içinde etkili bir şekilde uygulamasına ve yönetmesine olanak tanır. Bu belgeleme, tüm potansiyel kullanıcıların kartın amacını kolayca kavramasını ve iş akışlarına sorunsuz bir şekilde entegre etmesini sağlar.
