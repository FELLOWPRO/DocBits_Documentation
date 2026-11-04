<figure><img src="../../../../.gitbook/assets/docbits_single_assigned_user.png" alt="DocBits Single Assigned Usuario" width="552"><figcaption></figcaption></figure>

**Amaç**

Bu iş akışı kartı, bir görevin veya belgenin tek bir belirli kullanıcıya atanmasına bağlı olarak işlemleri kolaylaştırır. Doğrudan koşullu mantık yaklaşımını kullanarak, hedeflenen kullanıcı katılımını gerektiren iş akışlarını yönetir ve kullanıcı tabanlı görev işlemede hassasiyet sağlar.

**Kartın Bileşenleri**

1. **Operatör**
   * **Açıklama**: Kullanıcı atamasına uygulanacak mantığı belirtir.
   * **Seçenekler**:
     * **DIR (IS)**: Belgenin veya görevin atanan kullanıcısı belirtilen kullanıcıyla eşleşirse işlemi tetikler.
     * **DEĞİLDİR (IS NOT)**: Atanan kullanıcı belirtilen kullanıcıyla eşleşmezse işlemi tetikler.
2. **Kullanıcı**
   * **Açıklama**: Atanan kullanıcının karşılaştırılacağı tek bir kullanıcının seçilmesine olanak tanır.
   * **Detay**: Bu, bir seferde bir kullanıcının seçilebildiği basit bir açılır menü veya otomatik tamamlama alanını içerir.

**İşlevsellik**

* **Kullanıcı Ataması Tanımlama**: Şu anda belirli bir göreve veya belgeye atanmış olan kullanıcıyı tanımlar.
* **Koşul Değerlendirmesi**:
  * **DIR** operatörü için kart, atanan kullanıcının seçilen kullanıcıyla aynı olup olmadığını kontrol eder.
  * **DEĞİLDİR** operatörü için, atanan kullanıcının seçilen kullanıcıdan farklı olduğunu doğrular.
* **Eylem Yürütme**:
  * **Doğru Koşul**: Atama belirlenen koşulu karşılıyorsa (DIR veya DEĞİLDİR), onaylarla ilerlemek, daha ileri görevleri başlatmak, bildirimler göndermek veya diğer ilgili iş akışları gibi önceden tanımlanmış eylemleri tetikler.
  * **Yanlış Koşul**: Koşul karşılanmazsa iş akışı devam etmez.

**Kullanıcı Etkileşimleri**

* **Kurulum ve Yapılandırma**: Kullanıcılar bir operatör seçerek ve kullanıcı alanından bir kullanıcı belirleyerek kartı kurar. Bu kurulum basit olmalı, kolay kullanıcı seçimi ve yapılandırması sağlamalıdır.
* **İzleme ve Raporlama**: Belirli kullanıcı atamaları tarafından hangi görevlerin tetiklendiği ve bu tetiklemelerin sonuçları gibi kartın performansını izlemek için araçlar sunar.
* **Hata İşleme ve Bildirimler**: Görevler yanlış atanmışsa veya atama sorunları nedeniyle operasyonel hatalar oluşursa kullanıcıları uyarmak için mekanizmalar sağlar.

#### Sonuç

"Tek Atanan Kullanıcı Koşulu" iş akışı kartı, bir ERP sistemi içinde hassas, kullanıcıya özel belge ve görev yönetimi için gereklidir. Bireysel kullanıcı atamalarına odaklanarak iş akışlarını basitleştirir, böylece eylemlerin yalnızca kullanıcının rolü ve sorumluluklarına göre uygun olduğunda yürütülmesini sağlar. Bu kartın açıkça belgelenmesi, kullanıcıların uygulamasını anlamalarına yardımcı olacak ve günlük operasyonlarında etkili bir şekilde uygulamalarına ve yönetmelerine olanak tanıyacaktır. Bu belgelendirme, tüm potansiyel kullanıcıların kartın amacını kolayca kavrayabilmesini ve iş akışlarına sorunsuz bir şekilde entegre edebilmesini sağlar.
