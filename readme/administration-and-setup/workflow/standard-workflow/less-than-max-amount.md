# Less than Max Amount

<figure><img src="../../../.gitbook/assets/Bildschirmfoto 2024-05-03 um 14.48.55 (1).png" alt=""><figcaption></figcaption></figure>

Bu başlık, kurulan kuralın veya koşulun, toplam tutarın belirtilen bir maksimum tutardan az veya ona eşit olduğu faturaları işlemek üzere tasarlandığını gösterir.

#### Kural Yapılandırması:

1. **When…**
   * **Document Type is Invoice**: Bu koşul, işlenen belgenin bir fatura olup olmadığını kontrol eder. Bu, kuralın yalnızca faturalara uygulanmasını ve diğer belge türlerine uygulanmamasını sağlamak için çok önemlidir.
2. **And…**
   * **Document Status is Pending Approval**: Bu, faturanın "Pending Approval" durumunda olması gerektiğini belirtir. Bu durum kontrolü, kuralın yalnızca onay bekleyen faturalara uygulanmasını sağlar.
   * **Compare two fields: Total Amount Less Or Equals Approver Max Amount**: Bu koşul, faturanın toplam tutarını bir onaylayıcının maksimum yetkili tutarıyla karşılaştırır. Faturanın toplam tutarı bu maksimum tutardan az veya ona eşitse, kural bir sonraki adıma devam eder. Bu, büyük olasılıkla belirtilen sınırlar içinde küçük sapmalara izin veren bir tolerans düzeyi içerir.

#### Eylem (Then…):

* **Assign user from field Approver Name, use user User as fallback**: Belirtilen koşullar karşılanırsa, fatura adı bir alanda belirtilen bir onaylayıcıya otomatik olarak atanır. Bu alan boşsa veya kullanılamıyorsa, onayı işlemek için bir varsayılan kullanıcı (büyük olasılıkla bir yönetici veya başka bir görevli personel) yedek olarak atanır.

#### Arayüz Öğeleri:

* **Add Card**: Bu düğme, büyük olasılıkla kullanıcıların kurala daha fazla koşul veya eylem eklemesine olanak tanıyarak iş akışının esnekliğini ve özgülüğünü artırır.
* **Save**: Yapılandırılan kuralı sisteme kaydeder.

#### Bu Kuralın Amacı:

Bu kurulum, faturaları tutara göre uygun onaylayıcıya otomatik olarak yönlendirerek ve yalnızca belirli bir eşik içindekilerin bu otomatik şekilde işlenmesini sağlayarak faturaların onay sürecini kolaylaştırmak için tasarlanmıştır. Finansal kontrollerin yönetilmesine yardımcı olur ve her fatura için manuel kontrolleri azaltarak iş akışını hızlandırır.

\\
