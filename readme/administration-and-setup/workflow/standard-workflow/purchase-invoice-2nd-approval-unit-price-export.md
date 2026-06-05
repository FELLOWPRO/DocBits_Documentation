# Purchase Invoice - 2nd Approval Unit Price Export

<figure><img src="../../../.gitbook/assets/Bildschirmfoto 2024-05-03 um 14.59.02 (1).png" alt=""><figcaption></figcaption></figure>

Bu başlık, kuralın satın alma faturalarının ikinci onay aşamasını birim fiyata odaklanarak yönetmek üzere kurulduğunu ve birim fiyatın üzerinde anlaşılan koşullarla eşleştiğinden emin olduğunu gösterir.

#### Kural Yapılandırması:

1. **When…**
   * **Document Type is Invoice**: Bu koşul, kuralın yalnızca fatura olarak tanımlanan belgeler için etkinleştirilmesini sağlar; bu da iş akışının doğru yönlendirilmesi için çok önemlidir.
2. **And…**
   * **Document Status is Pending Second Approval**: Bu, faturanın ikinci bir onayı beklediğini belirtir. Bu aşama, genellikle işlem sonuçlandırılmadan önce doğruluğu sağlamak için ek denetim sağlar.
   * **Document Field Invoice Sub Type is Equals Purchase Invoice**: Bu koşul, kuralın yalnızca özellikle "Purchase Invoices" olarak sınıflandırılan faturalara uygulandığını ve onları diğer fatura türlerinden ayırt ettiğini daha da belirtir.
   * **Logic Unit Price in order confirmation Equals purchase order**: Bu koşul, sipariş onayında listelenen birim fiyatın satın alma siparişindeki birim fiyatla eşleşip eşleşmediğini kontrol eder. Fatura işlemenin yalnızca fiyatlandırmada tutarlılık olması durumunda ilerlemesini sağlar; bu da bütçeleme ve finansal raporlama için kritik öneme sahiptir.

#### Eylem (Then…):

* **Start Export**: Fatura belirtilen koşulları karşıladığında (yani birim fiyatlar sipariş onayı ile satın alma siparişi arasında eşleştiğinde), "Start Export" eylemi tetiklenir. Bu, büyük olasılıkla fatura verilerinin daha fazla işlenmesi için, muhtemelen başka bir finansal sisteme veya raporlama amaçları için dışa aktarılmasını içerir.

#### Bu Kuralın Amacı:

* **Doğruluk ve Tutarlılığı Sağlama**: Sistem, birim fiyatların sipariş onayı ile satın alma siparişi arasında eşleştiğini doğrulayarak finansal doğruluğu korumaya yardımcı olur ve fazla veya eksik ücretlendirmeyi önler.
* **Finansal İşlemeyi Kolaylaştırma**: Fiyatlar onaylandıktan sonra veri dışa aktarımının otomatikleştirilmesi, manuel işlemeyi azaltır ve finansal işleme döngüsünü hızlandırır.
* **Uyumluluk ve Denetimi Güçlendirme**: Fiyat doğrulaması için ikinci bir onay gerektirmek, finansal politikalara ve kontrollere uyum için kritik olan ek bir denetim katmanı ekler.

Bu kural, özellikle titiz doğrulama gerektiren büyük hacimli işlemler bağlamında, iş akışı otomasyonunun bir organizasyon içinde finansal belgelerin kesin ve verimli bir şekilde işlenmesini sağlamak için nasıl etkili bir şekilde kullanılabileceğine bir örnektir.
