# Above Max Amount

<figure><img src="../../../.gitbook/assets/Bildschirmfoto 2024-05-03 um 14.51.42 (1).png" alt=""><figcaption></figcaption></figure>

Bu başlık, kuralın fatura toplamının bir onaylayıcının işlemeye yetkili olduğu maksimum tutardan büyük olduğu durumları yönetmek üzere tasarlandığını gösterir.

#### Kural Yapılandırması:

1. **When…**
   * **Document Type is Invoice**: Bu koşul, kuralın yalnızca faturalara uygulanmasını sağlar; bu da iş akışının doğru yönlendirilmesi için gereklidir.
2. **And…**
   * **Document Status is Pending Approval**: Faturanın "Pending Approval" durumunda olması gerekir. Bu durum, kuralın hâlâ işlenmekte olan ve henüz tamamlanmamış faturalara uygulanmasını sağlamak için çok önemlidir.
   * **Compare two fields: Total Amount Greater Than Approver Max Amount**: Bu koşul, faturanın toplam tutarının bir onaylayıcının işlemesine izin verilen maksimum tutarı aşıp aşmadığını kontrol eder. Bu karşılaştırma, önceden tanımlanmış ölçütlere göre küçük varyasyonlara izin veren bir tolerans ayarını da içerebilir.

#### Eylem (Then…):

* **Assign user from field Next Level Approver, use user User as fallback**: Fatura belirtilen maksimum tutarı aşarsa, 'Next Level Approver' alanında belirtilen daha üst düzey bir onaylayıcıya otomatik olarak atanır. Bu alan doldurulmamışsa veya belirtilen kullanıcı kullanılamıyorsa, faturanın gecikmeden incelenmesini sağlamak için bir varsayılan kullanıcı (büyük olasılıkla bir yönetici veya başka bir görevli personel) yedek olarak kullanılır.

#### Arayüz Öğeleri:

* **Add Card**: Bu seçenek, kurala ek koşullar veya eylemler eklenmesine olanak tanıyarak karmaşık senaryoları ele almak için esneklik sağlar.
* **Save**: Bu düğme, kural yapılandırmasını sisteme kaydeder.

#### Bu Kuralın Amacı:

Bu kuralın amacı, belirli finansal eşikleri aşan faturaların uygun yetkilendirme düzeylerine sahip onaylayıcılar tarafından incelenmesini sağlamaktır. Bu, harcamaların gerekli onay sınırlarına sahip personel tarafından incelenmesini sağlayarak finansal kontrolün ve denetimin sürdürülmesine yardımcı olur ve böylece organizasyonu yetkisiz veya uygunsuz harcamalara karşı korur.

Bu kural, öncekiler gibi, iş akışını otomatikleştirerek manuel çabayı azaltmaya ve organizasyonun finansal politikalarına uyumu artırmaya yardımcı olur. İş akışı otomasyonunun bir şirket içindeki karmaşık finansal süreçleri yönetmek için nasıl etkili bir şekilde kullanılabileceğine bir örnektir.
