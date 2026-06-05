# Cost Invoice - Export

<figure><img src="../../../.gitbook/assets/Bildschirmfoto 2024-05-03 um 14.53.28 (1).png" alt=""><figcaption></figcaption></figure>

Bu başlık, kuralın özellikle maliyet faturalarını yönetmek için yapılandırıldığını ve muhtemelen raporlama, daha fazla işleme veya diğer sistemlerle entegrasyon için bir dışa aktarma eylemi içerdiğini gösterir.

#### Kural Yapılandırması:

1. **When…**
   * **Document Type is Invoice**: Bu koşul, kuralın yalnızca fatura olarak sınıflandırılan belgeler için tetiklenmesini sağlayarak iş akışının fatura yönetimine özgülüğünü korur.
2. **And…**
   * **Document Field Invoice Sub Type is Equals Cost Invoice**: Bu, kuralın yalnızca belge içindeki belirli bir alanda açıkça "Cost Invoices" olarak işaretlenmiş faturalara uygulandığını belirtir. Bu, onları diğer fatura türlerinden ayırt etmeye yardımcı olur.
   * **Document Status is Pending Second Approval**: Faturanın "Pending Second Approval" durumunda olması gerekir. Bu, faturanın daha önce bir ilk onaydan geçtiğini ve ikinci, muhtemelen nihai bir incelemeyi beklediğini gösterir.

#### Eylem (Then…):

* **Start Export**: Fatura belirtilen koşulları karşıladığında (bir maliyet faturası olması ve ikinci onayı bekliyor olması), "Start Export" eylemi yürütülür. Bu, fatura verilerinin finansal analiz, raporlama veya uyumluluk amaçları için başka bir sisteme gönderilmesini içerebilir.

#### Bu Kuralın Amacı:

* **İş Akışı Verimliliği**: Bu kural, maliyet faturalarının manuel müdahale olmadan gerekli onay aşamalarından geçirilmesini sağlayarak işlenmesini otomatikleştirmeye yardımcı olur ve finansal işlemlerin hızını ve doğruluğunu artırır.
* **Kontrol ve Uyumluluk**: Sistem, ikinci bir onay gerektirerek maliyet faturalarının kapsamlı bir şekilde incelenmesini sağlayan bir kontrol mekanizması uygular ve finansal denetimi güçlendirir.
* **Entegrasyon ve Raporlama**: Dışa aktarma eylemi, faturalar tamamen onaylandıktan sonra finansal raporlama ve denetimler için kritik olan daha fazla işleme veya analiz için diğer sistemlere entegre edilebileceklerini gösterir.

Bu tür bir kural, çeşitli fatura türleriyle ilgilenen ve her türün belirli protokollere göre işlendiğinden emin olması gereken organizasyonlar için hayati önem taşır. Hata riskini azaltır ve dahili kontroller ile harici düzenlemelere uyumu sağlar.
