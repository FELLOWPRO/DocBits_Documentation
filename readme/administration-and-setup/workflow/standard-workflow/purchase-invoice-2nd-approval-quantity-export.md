# Purchase Invoice - 2nd Approval Quantity Export

<figure><img src="../../../.gitbook/assets/Bildschirmfoto 2024-05-03 um 15.00.53 (1).png" alt=""><figcaption></figcaption></figure>

Bu başlık, kuralın satın alma faturaları için ikinci onay aşamasını miktar ayrıntılarına vurgu yaparak yönetmek üzere kurulduğunu ve faturadaki miktarların orijinal satın alma siparişindekilerle eşleştiğinden emin olduğunu gösterir.

#### Kural Yapılandırması:

1. **When…**
   * **Document Type is Invoice**: Bu koşul, kuralın yalnızca fatura olarak tanımlanan belgeler için etkinleştirilmesini sağlar; bu da iş akışının doğru yönlendirilmesi için çok önemlidir.
2. **And…**
   * **Document Status is Pending Second Approval**: Bu, faturanın şu anda ikinci bir onayı beklediğini belirtir. Bu aşama, genellikle işlem sonuçlandırılmadan önce doğruluğu sağlamak için ek denetim sağlar.
   * **Document Field Invoice Sub Type is Equals Purchase Invoice**: Bu koşul, kuralın yalnızca özellikle "Purchase Invoices" olarak sınıflandırılan faturalara uygulandığını ve onları diğer fatura türlerinden ayırt ettiğini daha da belirtir.
   * **Logic Quantity in order confirmation Equals purchase order**: Bu koşul, sipariş onayında listelenen miktarın satın alma siparişindeki miktarla eşleşip eşleşmediğini kontrol eder. Fatura işlemenin yalnızca miktarlar tutarlıysa ilerlemesini sağlar; bu da envanter yönetimi ve finansal doğruluk için kritik öneme sahiptir.

#### Eylem (Then…):

* **Start Export**: Fatura belirtilen koşulları karşıladığında (yani miktarlar sipariş onayı ile satın alma siparişi arasında eşleştiğinde), "Start Export" eylemi tetiklenir. Bu, büyük olasılıkla fatura verilerinin daha fazla işlenmesi için, muhtemelen başka bir finansal sisteme veya raporlama amaçları için dışa aktarılmasını içerir.

#### Bu Kuralın Amacı:

* **Doğruluk ve Tutarlılığı Sağlama**: Sistem, miktarların sipariş onayı ile satın alma siparişi arasında eşleştiğini doğrulayarak envanter doğruluğunu korumaya yardımcı olur ve finansal raporlamayı veya stok yönetimini etkileyebilecek tutarsızlıkları önler.
* **Finansal İşlemeyi Kolaylaştırma**: Miktarlar onaylandıktan sonra veri dışa aktarımının otomatikleştirilmesi, manuel işlemeyi azaltır ve finansal işleme döngüsünü hızlandırır.
* **Uyumluluk ve Denetimi Güçlendirme**: Miktar doğrulaması için ikinci bir onay gerektirmek, finansal politikalara ve kontrollere uyum için kritik olan ek bir denetim katmanı ekler.

Bu kural, özellikle titiz doğrulama gerektiren büyük hacimli işlemlerin yer aldığı satın alma süreçleri bağlamında, iş akışı otomasyonunun bir organizasyon içinde finansal belgelerin kesin ve verimli bir şekilde işlenmesini sağlamak için nasıl etkili bir şekilde kullanılabileceğinin açık bir örneğidir.
