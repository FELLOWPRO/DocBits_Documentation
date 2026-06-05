# Purchase Invoice - 2nd Approval Unit Price

<figure><img src="../../../.gitbook/assets/Bildschirmfoto 2024-05-03 um 14.55.09 (1).png" alt=""><figcaption></figcaption></figure>

Bu başlık, kuralın bir satın alma faturasının ikinci onay aşamasını yönetmek üzere kurulduğunu ve özellikle birim fiyatın doğrulanmasına odaklandığını gösterir.

#### Kural Yapılandırması:

1. **When…**
   * **Document Type is Invoice**: Bu koşul, kuralın yalnızca fatura olarak tanımlanan belgeler için tetiklenmesini sağlar; diğer belge türlerini filtreler ve iş akışının uygunluğunu korur.
2. **And…**
   * **Document Status is Pending Second Approval**: Bu, faturanın ikinci bir onayı beklediği aşamada olduğunu belirtir. Bu, genellikle nihai işlemden önce ek denetim sağlamak için tasarlanmış bir adımdır.
   * **Document Field Invoice Sub Type is Equals Purchase Invoice**: Bu, kuralın uygulanmasını yalnızca "Purchase Invoices" olarak sınıflandırılan faturalarla daraltır ve onları diğer fatura alt türlerinden ayırt eder.
   * **Logic Unit Price in order confirmation Not Equals purchase order**: Bu mantıksal kontrol, sipariş onayında listelenen birim fiyatı orijinal satın alma siparişindeki birim fiyatla karşılaştırdığı için çok önemlidir. Bu değerler eşleşmezse eylem tetiklenir; bu da çözülmesi gereken bir tutarsızlığa işaret edebilir.

#### Eylem (Then…):

* **Assign user from field Buyer Name, use user User as fallback**: Belirtilen koşullar karşılanırsa (yani birim fiyatlarda bir uyuşmazlık varsa), fatura daha fazla inceleme için bir alıcıya ('Buyer Name' alanında belirtilen ad) otomatik olarak atanır. 'Buyer Name' alanı boşsa veya belirtilmemişse, onayı işlemek için bir varsayılan kullanıcı (büyük olasılıkla bir yönetici veya başka bir görevli personel) yedek olarak atanır.

#### Bu Kuralın Amacı:

* **Doğruluk ve Uyumluluğu Sağlama**: Bu kural, faturalandırma sürecinin doğru olmasını ve üzerinde anlaşılan koşullara uymasını sağlamada kritik öneme sahiptir. Birim fiyatlarda bir tutarsızlık olduğunda bir incelemeyi tetikleyerek sistem, finansal hataların veya olası dolandırıcılığın önlenmesine yardımcı olur.
* **Onayları Kolaylaştırma**: Belirli tutarsızlıklara göre inceleme için atamanın otomatikleştirilmesi, onay sürecini kolaylaştırmaya yardımcı olur ve sorunların uygun personel tarafından hızla ele alınmasını sağlar.
* **Finansal Denetim**: Özellikle fiyat eşleştirmesine dayalı olarak ikinci bir onay gerektirmek, organizasyon içindeki finansal kontrolleri ve hesap verebilirliği güçlendirir.
