# Standard Workflow

<figure><img src="../../../.gitbook/assets/DocBits-APWorkflow-Gronbach.drawio (1) (1).svg" alt=""><figcaption></figcaption></figure>

#### İş Akışı Bileşenlerine Genel Bakış:

* **AP Invoice Email**: Süreç büyük olasılıkla e-posta yoluyla alınan bir faturayla başlar.
* **DocBits**: Bu araç, faturaların yakalanması ve dijitalleştirilmesi gibi ilk belge yönetimi görevleri için kullanılabilir.
* **Finance Review**: Faturalar, geçerlilikleri ve doğrulukları hakkında kararların verildiği bir finans incelemesinden geçer.

#### İş Akışındaki Adımlar:

1. **İlk İnceleme**:
   * Faturalar alınır ve başlangıçta DocBits kullanılarak işlenir.
   * Ardından finans ekibi tarafından incelenir; eksiksizlerse iş akışından çıkarılmaları, aksi takdirde daha fazla işlem için ileriye taşınmaları sağlanır.
2. **PO ve PO Olmayan Faturalar**:
   * İş akışı, PO ile ilgili faturalar ile PO olmayan faturaları birbirinden ayırt eder.
   * PO olmayan faturalar, tedarikçi kimliği, miktar, birim fiyat ve kalem numarası gibi önceden tanımlanmış ölçütlere göre daha fazla onay veya reddetme için yönlendirilir.
3. **Eşleşme ve Uyuşmazlık**:
   * Faturalar, ayrıntıların eşleştiğinden (tedarikçi kimliği ve miktar gibi) emin olmak için mal kabulleriyle karşılaştırılır.
   * Uyuşmazlıklar oluşursa, fatura daha fazla incelemeye ve muhtemelen reddedilmeye tabidir.
4. **Finans ve Alıcı İncelemesi**:
   * PO ile ilgili faturalar için, bir alıcı incelemesini içeren ayrıntılı bir eşleştirme süreci yürütülür.
   * Satın alma siparişlerinde veya mal kabullerinde düzeltmeler gerekebilir.
5. **Nihai Kararlar**:
   * Tüm kontrolleri geçen faturalar onaylanır ve kayıt tutma amacıyla finansal sistemlere entegre edilir.
   * Reddedilen faturalar bildirimleri tetikler ve alıcı tarafından yeni bir fatura talep edilebilir.
6. **Infor IDM & LN+M3 ile Entegrasyon**:
   * Onaylanan faturalar büyük olasılıkla belge yönetimi için Infor'un IDM'sine ve defter kaydı için LN'ye gönderilir.
   * Bu entegrasyon, tüm finansal kayıtların güncel olmasını ve iş akışının daha geniş ERP sistemine sorunsuz bir şekilde beslenmesini sağlar.

#### Karar Noktaları:

* İş akışı boyunca, bir faturanın onaylanabileceği, reddedilebileceği veya ek bilgi için geri gönderilebileceği çeşitli karar noktaları vardır. Gecikmelerden sonra bildirimler gönderilerek zamanında işlem yapılması sağlanır.

Bu iş akışları Standard Workflow'a dahil edilecektir
