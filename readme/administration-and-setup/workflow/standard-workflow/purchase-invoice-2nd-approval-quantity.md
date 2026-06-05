# Purchase Invoice - 2nd Approval Quantity

<figure><img src="../../../.gitbook/assets/Bildschirmfoto 2024-05-03 um 14.56.54 (1).png" alt=""><figcaption></figcaption></figure>

Bu başlık, kuralın özellikle ikincil bir onay aşamasında satın alma faturalarının işlenmesiyle ilgili olduğunu ve listelenen miktarların doğruluğunu doğrulamaya odaklandığını gösterir.

#### Kural Yapılandırması:

1. **When…**
   * **Document Type is Invoice**: Bu koşul, kuralın yalnızca fatura olarak sınıflandırılan belgeler için etkinleştirilmesini sağlar. Bu, iş akışında özgülüğün ve uygunluğun korunması için gereklidir.
2. **And…**
   * **Document Status is Pending Second Approval**: Bu, faturanın şu anda ikinci bir onayı beklediğini belirtir. Bu aşama, genellikle faturayı sonuçlandırmadan önce ek denetim sağlamayı amaçlar.
   * **Document Field Invoice Sub Type is Equals Purchase Invoice**: Bu koşul, kuralı yalnızca "Purchase Invoices" olarak tanımlanan faturalara uygulanacak şekilde daha da daraltır. Bu sınıflandırma, onları diğer fatura türlerinden ayırt etmeye yardımcı olur.
   * **Logic Quantity in order confirmation Not Equals purchase order**: Bu kritik koşul, sipariş onayında belirtilen miktarın orijinal satın alma siparişindeki miktarla eşleşip eşleşmediğini kontrol eder. Bir tutarsızlık varsa, çözülmesi gereken olası bir hata veya soruna işaret eden eylem tetiklenir.

#### Eylem (Then…):

* **Assign user from field Buyer Name, use user User as fallback**: Kuralın koşulları karşılanırsa (yani miktarlarda bir tutarsızlık varsa), fatura daha fazla inceleme için 'Buyer Name' alanında listelenen kişiye otomatik olarak atanır. Bu alan boşsa veya belirtilen kişi kullanılamıyorsa, zamanında inceleme ve çözüm sağlamak için bir varsayılan kullanıcı (büyük olasılıkla bir yönetici veya başka bir görevli personel) devreye girer.

#### Bu Kuralın Amacı:

* **Doğruluk ve Uyumluluk**: Bu kural, faturalandırma sürecinin doğru olmasını ve satın alma siparişinde üzerinde anlaşılan koşullarla uyumlu olmasını sağlamak için hayati önem taşır. Finansal tutarsızlıkları ve olası envanter hatalarını önlemeye yardımcı olur.
* **Kolaylaştırılmış Onaylar**: Belirli tutarsızlıklar için inceleme sürecinin otomatikleştirilmesi, onayların kolaylaştırılmasına yardımcı olur ve sorunların uygun personel tarafından hızla ele alınmasını sağlar.
* **Geliştirilmiş Finansal Denetim**: Miktar doğrulamaları için ikincil bir onay gerektirmek, organizasyon içindeki finansal kontrolleri ve hesap verebilirliği güçlendirir.

Bu kurulum, özellikle bir şirket içindeki karmaşık satın alma süreçlerini yönetirken, iş akışı otomasyonunun operasyonel verimliliği artırmak ve finansal bütünlüğü sağlamak için nasıl kullanılabileceğini örnekler.
